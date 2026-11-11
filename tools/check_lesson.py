"""Check a lesson: runnable examples, real output, and matching English/Khmer files.

Usage (from the repo root):

    python3 tools/check_lesson.py 01-dart/sections/04-functions
    python3 tools/check_lesson.py 03-swift/sections/01-getting-started
    python3 tools/check_lesson.py 21-c-cpp/sections/01-how-computers-work
    python3 tools/check_lesson.py 22-rust/sections/01-introduction-to-rust

The course folder decides the language: 01-dart is Dart, 03-swift is Swift, 21-c-cpp is C and C++, 22-rust is Rust (see COURSE_LANGUAGE).
Examples run from inside examples/, so they can read data files with relative paths.
Examples that read keyboard input (stdin) get it from examples/<name>.input.

Dart: if examples/ has a pubspec.yaml, the checker runs `dart pub get`; if it has a test/ folder, `dart test`.
Swift: each top-level .swift file in examples/ is a program. It is compiled in the Swift 6 language mode with
warnings as errors, and run three times: Swift prints dictionaries and sets in a different order on every run,
so output that changes is an error. If examples/ has a Package.swift, the checker runs `swift build`, and
`swift test` if there is a Tests/ folder. `swift format lint` must report nothing.
C and C++: each top-level .c or .cpp file in examples/ is a program. It is compiled with Clang (C17 or C++23) with
strict warnings as errors, AddressSanitizer, and UndefinedBehaviorSanitizer, and run three times. Printed memory
addresses change on every run, so they are compared as 0xADDR. A subfolder with a Makefile or a CMakeLists.txt is a
multi-file project: it must build, and `make run` output counts as real output. `clang-format` must report nothing.
A lesson may have no examples at all.
TypeScript: each top-level .ts file in examples/ is a program. examples/ is a small npm package (package.json and
tsconfig.json, strict): the checker installs its packages, type-checks every file with `tsc --noEmit`, runs Prettier,
and runs each program with Node.js, which removes the types itself. A ```typescript block in the book must type-check
and run on its own.
Rust: each top-level .rs file in examples/ is a program. It is compiled with rustc (edition 2024) with warnings as
errors, checked with Clippy (warnings as errors) and rustfmt, and run three times. A subfolder with a Cargo.toml is a
Cargo project: `cargo clippy`, `cargo test`, and `cargo run` must pass, and its output counts as real output.
Kotlin: each top-level .kt file in examples/ is a program, compiled with kotlinc (warnings as errors) and run on the
JVM; ktlint must report nothing. A subfolder with a settings.gradle.kts is a Gradle project: `gradle test` (if it has
src/test) and `gradle run` must pass, and its output counts as real output. If examples/<project>.args exists, the
project runs once for each of its lines, with that line as the command-line arguments. A single-file program can
have examples/<name>.args too.
Web: ```html and ```css blocks are pages and stylesheets. They must pass Prettier; they are not run until browser
checks exist. Terminal output in ```console blocks is copied from real runs by hand.

Errors (exit status 1):
- an example fails the analyzer or compiler, or does not run;
- a Swift example prints different output on different runs;
- a line in a code block is not in any example (blocks under a
  "Common Mistakes" heading are skipped, because they are meant to fail);
- a ```text block is not, line for line, part of some example's real output;
- en/ and km/ slides have different slide IDs or different code/output blocks;
- a script's slide IDs differ from its slides, or the km script's
  Show/Do/Time lines differ from the en script;
- en/ and km/ books (when both exist) have different code/output blocks;
- a book or slide file mentions examples/ or an example file name (learners never
  receive those files; only the teacher's script may name them);
- a code example in book.md is not a complete program, has analyzer issues or warnings, does not run on its own,
  or does not produce the output shown after it (learners type these themselves).

Code blocks: ```dart, ```swift, ```c, ```cpp, ```typescript, or ```rust is a program or part of one. The -library form (```c-library) is
a library file or header shown in full (checked line by line, not run on its own). The -wrong form (```c-wrong)
shows a problem and is not checked.

Warnings (reported, but do not fail):
- VISUAL TODO and SCREENSHOT TODO markers still in the lesson;
- transliterated technical terms in Khmer files (see STYLE-GUIDE.md).
"""
import atexit
import json
import pathlib
import re
import shlex
import zipfile
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
COURSE_LANGUAGE = {"01-dart": "dart", "02-flutter": "flutter", "03-swift": "swift", "04-ios-development": "ios", "05-kotlin": "kotlin", "06-android-development": "android", "07-java-script": "javascript", "08-typescript": "typescript", "09-web-development": "web", "10-react-native": "react-native", "11-ci-cd": "ci-cd", "12-automated-testing": "dart", "13-mobile-architecture": "dart", "14-mobile-security": "dart", "15-observability-monitoring": "dart", "16-performance-profiling": "dart", "17-release-engineering": "dart", "18-data-networking": "dart", "19-accessibility-localization": "dart", "20-developer-workflow": "dart", "21-c-cpp": "c-cpp", "22-rust": "rust", "23-java": "java", "24-spring-boot": "spring-boot"}
FENCES = {"typescript": ("typescript",), "web": ("html", "css"), "ci-cd": ("yaml", "dart"), "react-native": ("tsx",), "javascript": ("javascript",), "kotlin": ("kotlin",), "android": ("kotlin",), "dart": ("dart",), "flutter": ("dart",), "ios": ("swift",), "swift": ("swift",), "c-cpp": ("c", "cpp"), "rust": ("rust",), "java": ("java",), "spring-boot": ("java", "yaml", "json")}  # the code block names of each course
EXTENSIONS = {"typescript": (".ts",), "web": (), "ci-cd": (".dart",), "react-native": (), "javascript": (".js", ".mjs"), "kotlin": (".kt",), "android": (), "dart": (".dart",), "flutter": (), "ios": (".swift",), "swift": (".swift",), "c-cpp": (".c", ".cpp"), "rust": (".rs",), "java": (".java",), "spring-boot": (".java",)}
SOURCE_EXTENSIONS = {"typescript": (".ts", ".json"), "web": (".html", ".css", ".js"), "ci-cd": (".dart", ".yml", ".yaml"), "react-native": (".ts", ".tsx"), "javascript": (".js", ".mjs", ".json"), "kotlin": (".kt", ".kts"), "android": (".kt", ".kts", ".xml"), "dart": (".dart",), "flutter": (".dart",), "ios": (".swift",), "swift": (".swift",), "c-cpp": (".c", ".cpp", ".h", ".hpp"), "rust": (".rs", ".toml"), "java": (".java",), "spring-boot": (".java", ".yaml", ".yml", ".properties", ".xml", ".json")}

lesson = pathlib.Path(sys.argv[1])
LANG = COURSE_LANGUAGE[lesson.resolve().relative_to(ROOT).parts[0]]
EX = (lesson / "examples").resolve()
TOOL_DIRS = {"target", "node_modules", ".dart_tool", ".build", "coverage", "output", "build", "dist", ".gradle", "gradle"}  # generated folders, not sources
# Every hand-written file Prettier can format, not only code: JSON settings (tsconfig.json, package.json) too.
PRETTIER_FILES = {".js", ".mjs", ".cjs", ".ts", ".tsx", ".json", ".html", ".css"}
GENERATED = {"package-lock.json"}  # written by npm, never by hand
examples = sorted(f for f in EX.glob("*") if f.suffix in EXTENSIONS[LANG] and f.name != "Package.swift") if EX.is_dir() else []
# All sources, including test/, lib/, Sources/, and Tests/ in examples that are packages.
all_sources = [f for f in sorted(EX.rglob("*")) if f.suffix in SOURCE_EXTENSIONS[LANG]
               and not TOOL_DIRS & set(f.relative_to(EX).parts)] if EX.is_dir() else []
errors, warnings = [], []
BUILD = pathlib.Path(tempfile.mkdtemp(prefix="check_lesson_"))  # compiled Swift programs
atexit.register(shutil.rmtree, BUILD, ignore_errors=True)


def run(cmd, stdin="", cwd=EX if EX.is_dir() else ROOT, timeout=300):
    return subprocess.run(cmd, cwd=cwd, input=stdin, capture_output=True, text=True, timeout=timeout)


def input_for(f):
    stdin_file = f.with_suffix(".input")
    return stdin_file.read_text() if stdin_file.exists() else ""


# --- language tools ------------------------------------------------------------------

def dart_prepare():
    if (EX / "pubspec.yaml").exists():
        pub = run(["dart", "pub", "get"])
        if pub.returncode != 0:
            errors.append("PUB      dart pub get failed:\n" + pub.stderr.strip()[:400])
    analyze = run(["dart", "analyze", "."])
    if analyze.returncode != 0 or "No issues found" not in analyze.stdout:
        errors.append("ANALYZE  examples/ has analyzer issues:\n" + analyze.stdout.strip())
    if (EX / "test").is_dir():
        tests = run(["dart", "test"])
        if tests.returncode != 0:
            errors.append("TEST     dart test failed:\n" + tests.stdout.strip()[-600:])


def dart_run(f, stdin):
    """Run one program. Returns (stdout lines, error message or None)."""
    done = run(["dart", "run", f.name], stdin)
    return done.stdout.splitlines(), (None if done.returncode == 0 else done.stderr.strip())


def dart_book_example(code, stdin):
    """Run a book example on its own. Returns (stdout lines, problem or None)."""
    if "main(" not in code:
        return [], "example has no main()"
    # Run inside examples/ so that data files and packages resolve, then remove the file.
    with tempfile.NamedTemporaryFile("w", suffix=".dart", dir=EX, prefix="check_", delete=True) as program:
        program.write(code)
        program.flush()
        name = pathlib.Path(program.name).name
        done = run(["dart", "run", name], stdin)
        lint = run(["dart", "analyze", name])
    if "No issues found" not in lint.stdout:
        return [], "example has analyzer issues:\n         " + lint.stdout.strip()[:240]
    if done.returncode != 0:
        return [], "example does not run on its own:\n         " + done.stderr.strip()[:200]
    return done.stdout.splitlines(), None


def swift_packages():
    """Every Swift package in examples/ itself, or one folder down (such as examples/MinaCoffee/)."""
    return [p.parent for p in [EX / "Package.swift", *sorted(EX.glob("*/Package.swift"))] if p.exists()]


def swift_prepare():
    for package in swift_packages():
        name = package.relative_to(EX).as_posix() if package != EX else "examples"
        build = run(["swift", "build", "-Xswiftc", "-warnings-as-errors"], cwd=package, timeout=900)
        if build.returncode != 0:
            errors.append(f"BUILD    swift build failed in {name}:\n" + (build.stdout + build.stderr).strip()[-600:])
            continue
        if (package / "Tests").is_dir():
            tests = run(["swift", "test"], cwd=package, timeout=900)
            if tests.returncode != 0:
                errors.append(f"TEST     swift test failed in {name}:\n" + (tests.stdout + tests.stderr).strip()[-600:])
            else:
                # Test results print a summary line with timing; keep the lines that never change.
                project_output.append([steady(l) for l in (tests.stdout + tests.stderr).splitlines()])
        # Run every executable product. Its output counts as real output, like `make run` for C projects.
        described = run(["swift", "package", "describe", "--type", "json"], cwd=package)
        try:
            products = [p["name"] for p in json.loads(described.stdout).get("products", []) if "executable" in p.get("type", {})]
        except ValueError:
            products = []
        for product in products:
            stdin = (package / f"{product}.input").read_text() if (package / f"{product}.input").exists() else ""
            runs = [run(["swift", "run", "-q", product], stdin, cwd=package, timeout=900) for _ in range(2)]
            if any(r.returncode != 0 for r in runs):
                errors.append(f"RUN      swift run {product} failed in {name}:\n" + runs[0].stderr.strip()[-400:])
            elif runs[0].stdout != runs[1].stdout:
                errors.append(f"RUN      swift run {product} in {name} prints different output on different runs")
            else:
                project_output.append(runs[0].stdout.splitlines())
    sources = [str(f) for f in all_sources]
    if sources:
        config = next((str(d / ".swift-format") for d in EX.parents if (d / ".swift-format").exists()), None)
        lint = run(["swift", "format", "lint", *(["--configuration", config] if config else []), *sources])
        found = (lint.stdout + lint.stderr).strip()
        if found:
            errors.append("FORMAT   swift format lint found problems (run `swift format -i` on the files):\n"
                          + found.replace(str(EX) + "/", "")[:600])


def swift_compile(source, name):
    """Compile one Swift program. Returns (binary, error message or None)."""
    binary = BUILD / name
    done = run(["swiftc", "-swift-version", "6", "-warnings-as-errors", "-o", str(binary), str(source)], timeout=300)
    if done.returncode != 0:
        return None, (done.stdout + done.stderr).strip().replace(str(source.parent) + "/", "")[:600]
    return binary, None


def swift_runs(binary, stdin):
    """Run a program three times. Returns (stdout lines, error message or None)."""
    outputs = []
    for _ in range(3):
        done = run([str(binary)], stdin)
        if done.returncode != 0:
            return done.stdout.splitlines(), done.stderr.strip()[:400] or f"exit status {done.returncode}"
        outputs.append(done.stdout)
    if len(set(outputs)) > 1:
        return outputs[0].splitlines(), "prints different output on different runs (sort dictionary or set output)"
    return outputs[0].splitlines(), None


def swift_run(f, stdin):
    binary, problem = swift_compile(f, f.stem)
    if problem:
        return [], problem
    return swift_runs(binary, stdin)


def swift_book_example(code, stdin):
    with tempfile.TemporaryDirectory(dir=BUILD) as folder:
        source = pathlib.Path(folder) / "main.swift"
        source.write_text(code)
        binary, problem = swift_compile(source, "book_example")
    if problem:
        return [], "example does not compile on its own:\n         " + problem[:300]
    lines, problem = swift_runs(binary, stdin)
    if problem:
        return [], "example does not run correctly on its own:\n         " + problem
    return lines, None


# --- C and C++ -----------------------------------------------------------------------
C_FLAGS = ["-Wall", "-Wextra", "-Wpedantic", "-Werror", "-g", "-fsanitize=address,undefined", "-fno-sanitize-recover=all"]
COMPILERS = {".c": ["clang", "-std=c17"], ".cpp": ["clang++", "-std=c++23"]}
ADDRESS = re.compile(r"0x[0-9a-fA-F]{6,}")
project_output = []  # the `make run` output of multi-file projects


def steady(text):
    """Printed memory addresses change on every run, so they are compared as 0xADDR."""
    return ADDRESS.sub("0xADDR", text) if LANG == "c-cpp" else text


def c_prepare():
    if all_sources:
        lint = run(["clang-format", "--style=file", "--dry-run", "--Werror", *map(str, all_sources)])
        if lint.returncode != 0:
            errors.append("FORMAT   clang-format found problems (run `clang-format -i` on the files):\n"
                          + lint.stderr.replace(str(EX) + "/", "")[:600])
    for folder in sorted(p for p in EX.iterdir() if p.is_dir() and not TOOL_DIRS & {p.name}) if EX.is_dir() else []:
        if (folder / "CMakeLists.txt").exists():
            out = BUILD / ("cmake-" + folder.name)
            for step in (["cmake", "-S", str(folder), "-B", str(out)], ["cmake", "--build", str(out)]):
                done = run(step, timeout=600)
                if done.returncode != 0:
                    errors.append(f"BUILD    {folder.name}: {' '.join(step[:2])} failed:\n" + (done.stdout + done.stderr).strip()[-600:])
                    break
        elif (folder / "Makefile").exists():
            done = run(["make", "-s", "-C", str(folder), "run"], timeout=300)
            if done.returncode != 0:
                errors.append(f"BUILD    {folder.name}: make run failed:\n" + (done.stdout + done.stderr).strip()[-600:])
            project_output.append(steady(done.stdout).splitlines())
            run(["make", "-s", "-C", str(folder), "clean"])


def c_compile(source, name):
    binary = BUILD / name
    extra = ["-lm"] if source.suffix == ".c" else []
    done = run([*COMPILERS[source.suffix], *C_FLAGS, "-o", str(binary), str(source), *extra], timeout=300)
    if done.returncode != 0:
        return None, (done.stdout + done.stderr).strip().replace(str(source.parent) + "/", "")[:600]
    return binary, None


def c_runs(binary, stdin):
    """Run a program three times. Returns (stdout lines, error message or None)."""
    outputs = []
    for _ in range(3):
        done = run([str(binary)], stdin)
        if done.returncode != 0:
            return steady(done.stdout).splitlines(), (done.stderr.strip()[:500] or f"exit status {done.returncode}")
        outputs.append(steady(done.stdout))
    if len(set(outputs)) > 1:
        return outputs[0].splitlines(), "prints different output on different runs"
    return outputs[0].splitlines(), None


def c_run(f, stdin):
    binary, problem = c_compile(f, f.stem + f.suffix.replace(".", "_"))
    if problem:
        return [], problem
    return c_runs(binary, stdin)


def c_book_example(code, stdin, fence="c"):
    if "main(" not in code:
        return [], "example has no main()"
    with tempfile.TemporaryDirectory(dir=BUILD) as folder:
        source = pathlib.Path(folder) / f"example.{fence}"
        source.write_text(code)
        binary, problem = c_compile(source, "book_example")
    if problem:
        return [], "example does not compile on its own:\n         " + problem[:300]
    lines, problem = c_runs(binary, stdin)
    if problem:
        return [], "example does not run correctly on its own:\n         " + problem
    return lines, None


# --- Flutter ----------------------------------------------------------------------
# examples/ is one Flutter project (pubspec.yaml, lib/, test/). Apps have no console output to compare, so their
# behavior is checked with widget tests in test/, and screens are screenshots taken by hand.

def flutter_prepare():
    if not (EX / "pubspec.yaml").exists():
        return
    for step, timeout in ((["flutter", "pub", "get"], 600), (["flutter", "analyze", "--no-pub"], 600), (["flutter", "test", "--no-pub"], 900)):
        if step[1] == "test" and not (EX / "test").is_dir():
            continue
        done = run(step, timeout=timeout)
        if done.returncode != 0:
            errors.append(f"FLUTTER  {' '.join(step)} failed:\n" + (done.stdout + done.stderr).strip()[-700:])
    fmt = run(["dart", "format", "--output=none", "--set-exit-if-changed", "lib", "test"])
    if fmt.returncode != 0:
        errors.append("FORMAT   dart format would change these files (run `dart format lib test`):\n" + fmt.stdout.strip()[:400])


def flutter_book_example(code, stdin, fence):
    """A book example is a whole app (main.dart): it must pass the analyzer inside the examples project."""
    if "main(" not in code:
        return [], "example has no main()"
    with tempfile.NamedTemporaryFile("w", suffix=".dart", dir=EX / "lib", prefix="check_", delete=True) as program:
        program.write(code)
        program.flush()
        lint = run(["flutter", "analyze", "--no-pub", str(pathlib.Path(program.name).relative_to(EX))], timeout=600)
    if lint.returncode != 0 or "No issues found" not in lint.stdout:
        return [], "example has analyzer issues:\n         " + lint.stdout.strip()[-300:]
    return [], None


# --- iOS (SwiftUI) ------------------------------------------------------------------
# Apps run in the simulator, so the checker type-checks them for iOS instead of running them: Swift 6 language mode,
# warnings as errors. A top-level .swift file is a whole app in one file. A subfolder is one app in several files,
# checked together. What a screen shows is captured by hand as a screenshot.
IOS = ["xcrun", "-sdk", "iphonesimulator", "swiftc", "-typecheck", "-swift-version", "6", "-warnings-as-errors",
       "-target", "arm64-apple-ios18.0-simulator", "-parse-as-library"]


def ios_prepare():
    for folder in sorted(p for p in EX.iterdir() if p.is_dir()) if EX.is_dir() else []:
        files = sorted(str(f) for f in folder.rglob("*.swift"))
        if files:
            done = run([*IOS, *files], timeout=600)
            if done.returncode != 0:
                errors.append(f"BUILD    {folder.name}: does not type-check for iOS:\n" + (done.stdout + done.stderr).replace(str(EX) + "/", "").strip()[:700])
    swift_prepare()


def ios_run(f, stdin):
    done = run([*IOS, str(f)], timeout=600)
    return [], (None if done.returncode == 0 else (done.stdout + done.stderr).replace(str(EX) + "/", "").strip()[:600])


def ios_book_example(code, stdin, fence):
    with tempfile.TemporaryDirectory(dir=BUILD) as folder:
        source = pathlib.Path(folder) / "App.swift"
        source.write_text(code)
        done = run([*IOS, str(source)], timeout=600)
    if done.returncode != 0:
        return [], "example does not type-check on its own:\n         " + (done.stdout + done.stderr).strip()[:300]
    return [], None


# --- Kotlin -----------------------------------------------------------------------------
# Each top-level .kt file in examples/ is a program with main(). It is compiled with kotlinc, with warnings as errors,
# into a jar with the Kotlin runtime, and run with java. ktlint must report nothing (rules in the course's .editorconfig).
# A subfolder with a settings.gradle.kts is a Gradle project (see kotlin_prepare).

def kotlin_prepare():
    if all_sources:
        lint = run(["ktlint", *map(str, all_sources)])
        if lint.returncode != 0:
            errors.append("FORMAT   ktlint found problems (run `ktlint -F` on the files):\n" + (lint.stdout + lint.stderr).replace(str(EX) + "/", "").strip()[:600])
    # A subfolder with a settings.gradle.kts is a Gradle project. Its tests must pass (if it has src/test), and its
    # `run` output counts as real output: once for each line of examples/<project>.args (an empty line runs it with no
    # arguments), or once with no arguments if there is no such file.
    for folder in sorted(p for p in EX.iterdir() if p.is_dir() and (p / "settings.gradle.kts").exists()) if EX.is_dir() else []:
        gradle = ["./gradlew"] if (folder / "gradlew").exists() else ["gradle"]
        if (folder / "src/test").is_dir():
            done = run([*gradle, "-q", "--console=plain", "test"], cwd=folder, timeout=1800)
            if done.returncode != 0:
                errors.append(f"TEST     {folder.name}: gradle test failed:\n" + (done.stdout + done.stderr).strip()[-600:])
        args_file = EX / f"{folder.name}.args"
        for args in args_file.read_text().splitlines() if args_file.exists() else [None]:
            done = run([*gradle, "-q", "--console=plain", "run", *([f"--args={args}"] if args else [])], cwd=folder, timeout=1800)
            if done.returncode != 0:
                errors.append(f"RUN      {folder.name}: gradle run {args or ''} failed:\n" + (done.stdout + done.stderr).strip()[-600:])
            project_output.append(done.stdout.splitlines())


# Libraries that single-file examples may import. Learners get them through Gradle (the lesson shows the
# dependency); the checker takes the same version from Gradle's cache, which a lesson's Gradle project fills.
KOTLIN_LIBS = {
    "kotlinx.coroutines": ("org.jetbrains.kotlinx", "kotlinx-coroutines-core-jvm", "1.11.0"),
    "kotlinx.coroutines.test": ("org.jetbrains.kotlinx", "kotlinx-coroutines-test-jvm", "1.11.0"),
    "kotlin.reflect.full": ("org.jetbrains.kotlin", "kotlin-reflect", "2.4.21"),
    "kotlinx.serialization": ("org.jetbrains.kotlinx", "kotlinx-serialization-core-jvm", "1.12.0"),
    "kotlinx.serialization.json": ("org.jetbrains.kotlinx", "kotlinx-serialization-json-jvm", "1.12.0"),
}


def kotlin_plugins(code):
    """Compiler plugins a Kotlin source needs: kotlinx.serialization's ships with kotlinc."""
    if not re.search(r"^import kotlinx\.serialization\.", code, re.M):
        return []
    kotlinc = pathlib.Path(shutil.which("kotlinc")).resolve()
    plugin = next(kotlinc.parent.parent.rglob("lib/kotlinx-serialization-compiler-plugin.jar"), None)
    return [f"-Xplugin={plugin}"] if plugin else []


def kotlin_libs(code):
    """The library jars a Kotlin source needs, from its imports."""
    jars = []
    for package, (group, artifact, version) in KOTLIN_LIBS.items():
        if re.search(rf"^import {re.escape(package)}\.", code, re.M):
            found = sorted(pathlib.Path.home().glob(
                f".gradle/caches/modules-2/files-2.1/{group}/{artifact}/{version}/*/{artifact}-{version}.jar"))
            if not found:
                errors.append(f"LIBRARY  {artifact} {version} is not in Gradle's cache: build a Gradle project that uses it first")
            jars += found[:1]
            if artifact.endswith("-test-jvm"):
                jars += kotlin_libs("import kotlinx.coroutines.x")
    return list(dict.fromkeys(jars))


def kotlin_compile(source, name):
    jar = BUILD / f"{name}.jar"
    libs = kotlin_libs(source.read_text())
    classpath = ["-cp", ":".join(map(str, libs))] if libs else []
    classpath += kotlin_plugins(source.read_text())
    done = run(["kotlinc", str(source), *classpath, "-Werror", "-include-runtime", "-d", str(jar)], timeout=600)
    if done.returncode != 0:
        return None, (done.stdout + done.stderr).strip().replace(str(source.parent) + "/", "")[:600]
    return (jar, libs), None


def kotlin_run_jar(built, stdin, args=()):
    jar, libs = built
    if libs:
        with zipfile.ZipFile(jar) as z:
            manifest = z.read("META-INF/MANIFEST.MF").decode()
        main = re.search(r"^Main-Class: (\S+)", manifest, re.M).group(1)
        command = ["java", "-cp", ":".join(map(str, [jar, *libs])), main, *args]
    else:
        command = ["java", "-jar", str(jar), *args]
    done = run(command, stdin, timeout=120)
    return done.stdout.splitlines(), (None if done.returncode == 0 else done.stderr.strip()[:400] or f"exit status {done.returncode}")


def kotlin_run(f, stdin):
    """Runs the program once, or once for each line of <name>.args, with that line's words as its arguments."""
    jar, problem = kotlin_compile(f, f.stem)
    if problem:
        return [], problem
    args_file = f.with_suffix(".args")
    if not args_file.exists():
        return kotlin_run_jar(jar, stdin)
    lines = []
    for line in args_file.read_text().splitlines():
        out, problem = kotlin_run_jar(jar, stdin, shlex.split(line))
        if problem:
            return lines, problem
        lines += out
    return lines, None


def kotlin_book_example(code, stdin, fence):
    if "main(" not in code:
        return [], "example has no main()"
    with tempfile.TemporaryDirectory(dir=BUILD) as folder:
        source = pathlib.Path(folder) / "Main.kt"
        source.write_text(code)
        jar, problem = kotlin_compile(source, "book_example")
    if problem:
        return [], "example does not compile on its own:\n         " + problem[:300]
    return kotlin_run_jar(jar, stdin)


# --- Android ----------------------------------------------------------------------------
# examples/ is one Android Studio project, built with its Gradle wrapper. The checker compiles the Kotlin code
# (including Compose), runs unit tests in app/src/test if there are any, and runs ktlint. Screens are screenshots.

def android_prepare():
    if not (EX / "gradlew").exists():
        return
    local = EX / "local.properties"
    if not local.exists():
        sdk = pathlib.Path.home() / "Library/Android/sdk"
        local.write_text(f"sdk.dir={sdk}\n")
    tasks = [":app:compileDebugKotlin"] + ([":app:testDebugUnitTest"] if (EX / "app/src/test").is_dir() else [])
    done = run(["./gradlew", "-q", "--console=plain", *tasks], timeout=1800)
    if done.returncode != 0:
        errors.append("GRADLE   " + " ".join(tasks) + " failed:\n" + (done.stdout + done.stderr).strip()[-800:])
    kotlin_files = [f for f in all_sources if f.suffix == ".kt"]
    if kotlin_files:
        lint = run(["ktlint", *map(str, kotlin_files)])
        if lint.returncode != 0:
            errors.append("FORMAT   ktlint found problems (run `ktlint -F` on the files):\n" + (lint.stdout + lint.stderr).replace(str(EX) + "/", "").strip()[:600])


# --- JavaScript -------------------------------------------------------------------------
# Each top-level .js or .mjs file in examples/ is a program, run with Node.js. Prettier must report nothing.

def js_prepare():
    if (EX / "package.json").exists() and not (EX / "node_modules").exists():
        run(["npm", "install", "--silent"], timeout=600)
    files = [str(f) for f in all_sources if f.suffix in PRETTIER_FILES and f.name not in GENERATED]
    if files:
        fmt = run(["npx", "--yes", "prettier@3.3.3", "--check", *files], timeout=300)
        if fmt.returncode != 0:
            errors.append("FORMAT   Prettier would change these files (run `npx prettier --write`):\n" + (fmt.stdout + fmt.stderr).replace(str(EX) + "/", "").strip()[:500])


def js_run(f, stdin):
    done = run(["node", f.name], stdin)
    return done.stdout.splitlines(), (None if done.returncode == 0 else done.stderr.strip()[:500] or f"exit status {done.returncode}")


def js_book_example(code, stdin, fence):
    with tempfile.NamedTemporaryFile("w", suffix=".mjs" if "import " in code or "export " in code else ".js", dir=EX, prefix="check_", delete=True) as program:
        program.write(code)
        program.flush()
        done = run(["node", pathlib.Path(program.name).name], stdin)
    if done.returncode != 0:
        return [], "example does not run on its own:\n         " + done.stderr.strip()[:300]
    return done.stdout.splitlines(), None


# --- TypeScript ----------------------------------------------------------------------------
# examples/ is a small npm package: package.json (typescript and @types/node) and a strict tsconfig.json.
# Programs run with Node.js, which strips the types: so examples use only erasable syntax (no enums or namespaces).

def ts_install():
    if (EX / "package.json").exists() and not (EX / "node_modules").exists():
        done = run(["npm", "install", "--silent", "--no-audit", "--no-fund"], timeout=600)
        if done.returncode != 0:
            errors.append("NPM      npm install failed:\n" + (done.stdout + done.stderr).strip()[-500:])


def ts_check(*files):
    """tsc with the project's tsconfig. With files, only those files (and the same options)."""
    if files:
        return run(["npx", "tsc", "--noEmit", "--strict", "--target", "esnext", "--module", "nodenext", "--erasableSyntaxOnly",
                    "--types", "node", "--skipLibCheck", *files], timeout=600)
    return run(["npx", "tsc", "--noEmit", "-p", "tsconfig.json"], timeout=600)


def ts_prepare():
    if not EX.is_dir():
        return
    ts_install()
    if (EX / "tsconfig.json").exists():
        tsc = ts_check()
        if tsc.returncode != 0:
            errors.append("TYPES    tsc found problems:\n" + (tsc.stdout + tsc.stderr).strip()[:700])
    files = [str(f) for f in all_sources if f.suffix in PRETTIER_FILES and f.name not in GENERATED]
    if files:
        fmt = run(["npx", "--yes", "prettier@3.3.3", "--check", *files], timeout=300)
        if fmt.returncode != 0:
            errors.append("FORMAT   Prettier would change these files (run `npx prettier --write`):\n" + (fmt.stdout + fmt.stderr).replace(str(EX) + "/", "").strip()[:500])


def ts_run(f, stdin):
    done = run(["node", f.name], stdin)
    return done.stdout.splitlines(), (None if done.returncode == 0 else done.stderr.strip()[:500] or f"exit status {done.returncode}")


def ts_book_example(code, stdin, fence):
    with tempfile.NamedTemporaryFile("w", suffix=".ts", dir=EX, prefix="check_", delete=True) as program:
        program.write(code)
        program.flush()
        name = pathlib.Path(program.name).name
        tsc = ts_check(name)
        done = run(["node", name], stdin)
    if tsc.returncode != 0:
        return [], "example does not type-check on its own:\n         " + (tsc.stdout + tsc.stderr).strip()[:300]
    if done.returncode != 0:
        return [], "example does not run on its own:\n         " + done.stderr.strip()[:300]
    return done.stdout.splitlines(), None


# --- Web ---------------------------------------------------------------------------------------
# ```html and ```css blocks must pass Prettier. Pages are not run yet: browser checks come before the first lesson
# that needs them.

def web_prepare():
    files = [str(f) for f in all_sources]
    if files:
        fmt = run(["npx", "--yes", "prettier@3.3.3", "--check", *files], timeout=300)
        if fmt.returncode != 0:
            errors.append("FORMAT   Prettier would change these files (run `npx prettier --write`):\n" + (fmt.stdout + fmt.stderr).replace(str(EX) + "/", "").strip()[:500])


def web_book_example(code, stdin, fence):
    with tempfile.NamedTemporaryFile("w", suffix="." + fence, dir=BUILD, prefix="check_", delete=True) as page:
        page.write(code)
        page.flush()
        fmt = run(["npx", "--yes", "prettier@3.3.3", "--check", page.name], cwd=BUILD, timeout=300)
    if fmt.returncode != 0:
        return [], f"{fence} example is not formatted with Prettier"
    return [], None


# --- React Native ---------------------------------------------------------------------------
# examples/ is one Expo project (package.json, App.tsx, ...). The checker installs its packages if needed, type-checks
# everything with TypeScript, and runs Prettier. A ```tsx block in the book must type-check as a file of the project.
# Screens are screenshots, taken by hand.

def rn_prepare():
    if not (EX / "package.json").exists():
        return
    if not (EX / "node_modules").exists():
        done = run(["npm", "ci", "--silent"], timeout=1200)
        if done.returncode != 0:
            errors.append("NPM      npm ci failed:\n" + (done.stdout + done.stderr).strip()[-500:])
            return
    tsc = run(["npx", "tsc", "--noEmit"], timeout=600)
    if tsc.returncode != 0:
        errors.append("TYPES    tsc found problems:\n" + (tsc.stdout + tsc.stderr).strip()[:700])
    files = [str(f) for f in all_sources]
    if files:
        fmt = run(["npx", "--yes", "prettier@3.3.3", "--check", *files], timeout=300)
        if fmt.returncode != 0:
            errors.append("FORMAT   Prettier would change these files (run `npx prettier --write`):\n" + (fmt.stdout + fmt.stderr).replace(str(EX) + "/", "").strip()[:500])


def rn_book_example(code, stdin, fence):
    with tempfile.NamedTemporaryFile("w", suffix=".tsx", dir=EX, prefix="check_", delete=True) as program:
        program.write(code)
        program.flush()
        tsc = run(["npx", "tsc", "--noEmit"], timeout=600)
    if tsc.returncode != 0:
        return [], "example does not type-check in the project:\n         " + (tsc.stdout + tsc.stderr).strip()[:300]
    return [], None


# --- CI/CD --------------------------------------------------------------------------------
# examples/ is a small Dart package with a GitHub Actions workflow in .github/workflows/. The checker runs the same
# steps as the workflow (dart pub get, analyze, test) and checks every workflow with actionlint. A ```yaml block in the
# book that has jobs: is checked with actionlint too. Top-level .dart files are programs, as in the Dart course.

def cicd_prepare():
    dart_prepare()
    workflows = sorted((EX / ".github/workflows").glob("*.y*ml")) if EX.is_dir() else []
    if workflows:
        lint = run(["actionlint", *map(str, workflows)])
        if lint.returncode != 0:
            errors.append("WORKFLOW actionlint found problems:\n" + (lint.stdout + lint.stderr).replace(str(EX) + "/", "").strip()[:600])


def cicd_book_example(code, stdin, fence):
    if fence == "dart":
        return dart_book_example(code, stdin)
    if "jobs:" not in code:
        return [], None
    with tempfile.TemporaryDirectory(dir=BUILD) as folder:
        flow = pathlib.Path(folder) / ".github/workflows/book.yml"
        flow.parent.mkdir(parents=True)
        flow.write_text(code)
        lint = run(["actionlint", str(flow)], cwd=folder)
    if lint.returncode != 0:
        return [], "workflow fails actionlint:\n         " + lint.stdout.strip()[:300]
    return [], None


# --- Rust ------------------------------------------------------------------------------------
# Each top-level .rs file is a program, compiled with rustc (edition 2024) and checked with Clippy, both with warnings
# as errors. A subfolder with a Cargo.toml is a Cargo project.

RUST_FLAGS = ["--edition", "2024", "-D", "warnings"]


def rust_prepare():
    files = [str(f) for f in all_sources if f.suffix == ".rs"]
    if files:
        fmt = run(["rustfmt", "--color", "never", "--edition", "2024", "--check", *files])
        if fmt.returncode != 0:
            errors.append("FORMAT   rustfmt would change these files (run `rustfmt --edition 2024`):\n"
                          + (fmt.stdout + fmt.stderr).replace(str(EX) + "/", "").strip()[:600])
    for folder in sorted(p for p in EX.iterdir() if p.is_dir() and (p / "Cargo.toml").exists()) if EX.is_dir() else []:
        target = ["--target-dir", str(BUILD / ("cargo-" + folder.name))]
        for step in (["cargo", "clippy", "-q", *target, "--", "-D", "warnings"], ["cargo", "test", "-q", *target]):
            done = run(step, cwd=folder, timeout=900)
            if done.returncode != 0:
                errors.append(f"BUILD    {folder.name}: {' '.join(step[:2])} failed:\n" + (done.stdout + done.stderr).strip()[-600:])
        done = run(["cargo", "run", "-q", *target], cwd=folder, timeout=900)
        if done.returncode != 0:
            errors.append(f"RUN      {folder.name}: cargo run failed:\n" + done.stderr.strip()[-600:])
        project_output.append(done.stdout.splitlines())


def rust_compile(source, name):
    binary = BUILD / name
    done = run(["rustc", *RUST_FLAGS, "-o", str(binary), str(source)], cwd=source.parent, timeout=300)
    if done.returncode != 0:
        return None, (done.stdout + done.stderr).strip().replace(str(source.parent) + "/", "")[:600]
    lint = run(["clippy-driver", *RUST_FLAGS, "-o", str(BUILD / (name + "_clippy")), str(source)], cwd=source.parent, timeout=300)
    if lint.returncode != 0:
        return None, "Clippy: " + (lint.stdout + lint.stderr).strip().replace(str(source.parent) + "/", "")[:600]
    return binary, None


def rust_run(f, stdin):
    binary, problem = rust_compile(f, f.stem + "_rs")
    if problem:
        return [], problem
    return c_runs(binary, stdin)


def rust_book_example(code, stdin, fence):
    if "fn main(" not in code:
        return [], "example has no fn main()"
    with tempfile.TemporaryDirectory(dir=BUILD) as folder:
        source = pathlib.Path(folder) / "main.rs"
        source.write_text(code)
        fmt = run(["rustfmt", "--color", "never", "--edition", "2024", "--check", str(source)])
        binary, problem = rust_compile(source, "book_example_rs")
    if problem:
        return [], "example does not compile on its own:\n         " + problem[:300]
    if fmt.returncode != 0:
        return [], "example is not formatted with rustfmt"
    lines, problem = c_runs(binary, stdin)
    if problem:
        return [], "example does not run correctly on its own:\n         " + problem
    return lines, None


def java_prepare():
    java_files = [str(s) for s in all_sources if s.suffix == ".java"]
    if java_files:
        compile_res = run(["javac", "-d", str(BUILD), *java_files], cwd=EX, timeout=120)
        if compile_res.returncode != 0:
            errors.append("BUILD    javac found problems:\n" + (compile_res.stdout + compile_res.stderr).replace(str(EX) + "/", "").strip()[:600])


def java_run(f, stdin):
    done = run(["java", str(f)], stdin, cwd=EX, timeout=120)
    return done.stdout.splitlines(), (None if done.returncode == 0 else done.stderr.strip()[:400] or f"exit status {done.returncode}")


def java_book_example(code, stdin, fence):
    if "main(" not in code:
        return [], "example has no main()"
    with tempfile.TemporaryDirectory(dir=BUILD) as folder:
        source = pathlib.Path(folder) / "Main.java"
        source.write_text(code)
        done = run(["java", str(source)], stdin, cwd=folder, timeout=120)
    if done.returncode != 0:
        return [], "example does not run on its own:\n         " + (done.stdout + done.stderr).strip()[:300]
    return done.stdout.splitlines(), None


def spring_prepare():
    if not (EX / "pom.xml").exists() and not (EX / "build.gradle").exists() and not (EX / "build.gradle.kts").exists():
        return
    if (EX / "gradlew").exists():
        done = run(["./gradlew", "classes", "--no-daemon"], cwd=EX, timeout=300)
        if done.returncode != 0:
            errors.append("BUILD    Gradle failed:\n" + (done.stdout + done.stderr).strip()[-600:])
    elif (EX / "mvnw").exists():
        done = run(["./mvnw", "compile", "-q"], cwd=EX, timeout=300)
        if done.returncode != 0:
            errors.append("BUILD    Maven failed:\n" + (done.stdout + done.stderr).strip()[-600:])


def spring_book_example(code, stdin, fence):
    return [], None


TOOLS = {
    "ci-cd": (cicd_prepare, dart_run, cicd_book_example),
    "react-native": (rn_prepare, lambda f, stdin: ([], None), rn_book_example),
    "javascript": (js_prepare, js_run, js_book_example),
    "typescript": (ts_prepare, ts_run, ts_book_example),
    "web": (web_prepare, lambda f, stdin: ([], None), web_book_example),
    "android": (android_prepare, lambda f, stdin: ([], None), kotlin_book_example),
    "kotlin": (kotlin_prepare, kotlin_run, kotlin_book_example),
    "ios": (ios_prepare, ios_run, ios_book_example),
    "flutter": (flutter_prepare, lambda f, stdin: ([], None), flutter_book_example),
    "dart": (dart_prepare, dart_run, lambda code, stdin, fence: dart_book_example(code, stdin)),
    "swift": (swift_prepare, swift_run, lambda code, stdin, fence: swift_book_example(code, stdin)),
    "c-cpp": (c_prepare, c_run, c_book_example),
    "rust": (rust_prepare, rust_run, rust_book_example),
    "java": (java_prepare, java_run, java_book_example),
    "spring-boot": (spring_prepare, java_run, java_book_example),
}
prepare, run_example, book_example = TOOLS[LANG]

# --- examples: analyze and run ------------------------------------------------
prepare()
source_lines = {line.strip() for f in all_sources for line in f.read_text().splitlines() if line.strip()}
outputs = []
for f in examples:
    lines, problem = run_example(f, input_for(f))
    if problem:
        errors.append(f"RUN      {f.name} failed:\n{problem}")
    outputs.append(lines)


outputs.extend(project_output)


def in_some_output(block):
    block = [steady(line) for line in block]
    return any(out[i:i + len(block)] == block
               for out in outputs for i in range(len(out) - len(block) + 1))


BLOCK = re.compile(r"^(#+ [^\n]*)$|^```([\w-]+)\n(.*?)^```", re.M | re.S)
MISTAKES = ("common mistakes", "កំហុសដែល")
# The -library form is a library file with no top-level program, shown in full.
CODE_LANGS = tuple(name for fence in FENCES[LANG] for name in (fence, f"{fence}-library"))


def blocks(md):
    """All fenced blocks as (lang, body, in_mistakes_section)."""
    found, in_mistakes = [], False
    for m in BLOCK.finditer(md.read_text()):
        if m.group(1):
            in_mistakes = any(k in m.group(1).lower() for k in MISTAKES)
        else:
            found.append((m.group(2), m.group(3), in_mistakes))
    return found


# --- every Markdown file: code and output are real ----------------------------
for md in sorted(lesson.glob("*/*.md")):
    for lang, body, in_mistakes in blocks(md):
        if in_mistakes:
            continue
        if lang in CODE_LANGS:
            for line in body.splitlines():
                if line.strip() and line.strip() not in source_lines:
                    errors.append(f"CODE     {md}: not in examples/: {line.strip()}")
        elif lang == "text":
            block = body.rstrip("\n").splitlines()
            if block and not in_some_output(block):
                errors.append(f"OUTPUT   {md}: does not match any real run:\n         " + "\n         ".join(block))
    text = md.read_text()
    if (n := text.count("VISUAL TODO")):
        warnings.append(f"TODO     {md}: {n} × VISUAL TODO")
    # A screenshot note names its file; it is done once that file is saved in assets/screenshots/<course folder>/.
    for note in re.findall(r"<!-- SCREENSHOT TODO:? ?(.*?) -->", text, re.S):
        named = re.match(r"file: ([^;]+);", note.strip())
        shot = ROOT / "assets/screenshots" / lesson.parts[-3] / named.group(1) if named else None
        if not shot:
            warnings.append(f"SHOT     {md}: a screenshot note with no file name")
        elif not shot.exists():
            warnings.append(f"SHOT     {md}: capture {shot.relative_to(ROOT)}")

# --- English and Khmer match ----------------------------------------------------
en, km = lesson / "en", lesson / "km"
slide_id = re.compile(r"^<!-- (\d+\.\d+) -->$", re.M)
script_id = re.compile(r"^### (\d+\.\d+) ", re.M)
fixed_lines = re.compile(r"^\*\*(?:Show|Do|Time):\*\*.*$", re.M)


def read(p):
    return p.read_text() if p.exists() else None


def code_blocks(p):
    return [(lang, body) for lang, body, _ in blocks(p)]


for lang_dir in (en, km):
    slides, script = read(lang_dir / "slides.md"), read(lang_dir / "script.md")
    if slides and script and slide_id.findall(slides) != script_id.findall(script):
        errors.append(f"IDS      {lang_dir.name}/script.md slide IDs differ from {lang_dir.name}/slides.md")

if read(en / "slides.md") and read(km / "slides.md"):
    if slide_id.findall(read(en / "slides.md")) != slide_id.findall(read(km / "slides.md")):
        errors.append("IDS      km/slides.md slide IDs differ from en/slides.md")
    if code_blocks(en / "slides.md") != code_blocks(km / "slides.md"):
        errors.append("BLOCKS   km/slides.md code/output blocks differ from en/slides.md")

if read(en / "script.md") and read(km / "script.md"):
    if fixed_lines.findall(read(en / "script.md")) != fixed_lines.findall(read(km / "script.md")):
        errors.append("SCRIPT   km/script.md Show/Do/Time lines differ from en/script.md")

if read(en / "book.md") and read(km / "book.md"):
    if code_blocks(en / "book.md") != code_blocks(km / "book.md"):
        errors.append("BLOCKS   km/book.md code/output blocks differ from en/book.md")

# --- Khmer style: no transliterated technical terms -----------------------------
TRANSLITERATED = ("ប៉ារ៉ាម៉ែត្រ", "អាគុយម៉ង់", "បោះតម្លៃ")
for md in sorted(km.glob("*.md")) if km.exists() else []:
    for word in TRANSLITERATED:
        if (n := md.read_text().count(word)):
            warnings.append(f"KHMER    {md}: {n} × {word} (keep the English term instead)")

# --- learners never get examples/: book and slides must not mention those files ---
PRIVATE = re.compile(r"examples/|\b\d{2}_[a-z_]+\.(?:dart|swift|c|cpp|h|hpp|kt|js|mjs|ts|tsx|input)\b")
for md in [p for d in (en, km) for p in (d / "book.md", d / "slides.md") if p.exists()]:
    for n, line in enumerate(md.read_text().splitlines(), 1):
        if PRIVATE.search(line):
            errors.append(f"PRIVATE  {md}:{n}: learners do not get example files: {line.strip()[:90]}")

# --- book examples are complete: a learner can type one and run it on its own ------
book = en / "book.md"
if book.exists():
    teaching = book.read_text().split("## Common Mistakes")[0]
    # A code block is paired with the next output block in the same section (no fence or heading between).
    pair = re.compile(r"```(" + "|".join(FENCES[LANG]) + r")\n(.*?)```(?:(?:(?!```|\n#).)*?```text\n(.*?)```)?", re.S)
    for m in pair.finditer(teaching):
        fence, code, shown = m.group(1), m.group(2), m.group(3)
        first = code.strip().splitlines()[0][:60]
        wanted = {l.strip() for l in code.splitlines() if l.strip()}
        typed = ""
        for f in examples:
            if wanted <= {l.strip() for l in f.read_text().splitlines()} and f.with_suffix(".input").exists():
                typed = f.with_suffix(".input").read_text()
                break
        got, problem = book_example(code, typed, fence)
        if problem:
            errors.append(f"BOOK     {book}: {problem.splitlines()[0]}: {first}"
                          + ("\n" + "\n".join(problem.splitlines()[1:]) if "\n" in problem else ""))
        elif shown is not None:
            want = [steady(line) for line in shown.rstrip("\n").splitlines()]
            if not any(got[i:i + len(want)] == want for i in range(len(got) - len(want) + 1)):
                errors.append(f"BOOK     {book}: output shown does not match this example: {first}")

# --- report ---------------------------------------------------------------------
for line in errors:
    print(line)
for line in warnings:
    print("warning  " + line)
print(f"{len(examples)} examples, {len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)

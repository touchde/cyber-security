"""Build PDFs of a course's lessons: book and slides, in English and Khmer.

Usage (from the repo root). The first word is the course (see COURSES); without it, the course is Dart.

    python3 tools/build_lessons.py dart                  # every written Dart lesson
    python3 tools/build_lessons.py dart 04-functions     # one lesson
    python3 tools/build_lessons.py swift --book          # the full Swift book, in English and Khmer
    python3 tools/build_lessons.py swift --cover         # only the full book's cover, saved as an image the book uses

Output goes to output/<course folder>/<lesson>/ and output/<course folder>/<title>/, for example output/01-dart/04-functions/ (PDFs are committed; HTML is not). Uses only Python and Google Chrome:
Markdown -> HTML with the course theme, formatted with Prettier -> Chrome prints the HTML to PDF.
The script reports any slide whose text had to shrink, and fails if a slide does not fit.
"""
import datetime
import html
import json
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "output"

# Everything that differs between courses. The cover colors: page gradient, title text, accent (badge and ticks),
# and the two colors that tint the cover photo (light and dark).
COURSES = {
    "dart": {
        "folder": "01-dart", "code": "dart", "name": "Dart",
        "logo_dark": "assets/logos/dart/dart-logo-dark-bg.svg", "logo_light": "assets/logos/dart/dart-logo-light-bg.svg",
        "icon": "assets/logos/dart/dart-icon.svg",
        "credit": "Dart and the related logo are trademarks of Google LLC. We are not endorsed by or affiliated with Google LLC.",
        "cover": {"page": ("#F7FBFF", "#E6F1FC", "#D7E8FA"), "text": "#0B1F4B", "accent": "#1F5FD6",
                  "tint": ("#B4D2F5", "#0B1F4B"), "glow": "rgba(11,31,75,.18)", "square": True,
                  "art": "assets/covers/art/01-dart-cover-art.png"},
        "text": {
            "en": {"title": "Dart Programming", "second": "Programming", "badge": "A Practical Guide", "toc": "Contents", "inside": "In this section",
                   "points": ["Learn the Dart language, step by step", "Build real programs for a coffee shop", "Get ready for Flutter apps"]},
            "km": {"title": "Dart Programming", "second": "Programming", "badge": "រៀន និងអនុវត្តជាក់ស្ដែង", "toc": "មាតិកា", "inside": "ក្នុងផ្នែកនេះ",
                   "points": ["រៀនភាសា Dart ម្ដងមួយជំហាន", "បង្កើតកម្មវិធីសម្រាប់ហាងកាហ្វេ", "ត្រៀមខ្លួនសម្រាប់បង្កើត Flutter apps"]},
        },
    },
    "swift": {
        "folder": "03-swift", "code": "swift", "name": "Swift",
        "logo_dark": "assets/logos/swift/swift-logo-dark-bg.svg", "logo_light": "assets/logos/swift/swift-logo-light-bg.svg",
        "icon": "assets/logos/swift/swift-icon.svg",
        "credit": "Swift, the Swift logo, and Xcode are trademarks of Apple Inc. We are not endorsed by or affiliated with Apple Inc.",
        # The same layout as the Dart cover, in Swift's colors: a warm light page, and the Independence Monument in
        # Phnom Penh at the bottom, toned orange (cover_art()). Square corners, like the rest of the Swift style.
        "cover": {"page": ("#FFFAF7", "#FDEEE6", "#FBE1D4"), "text": "#3B1209", "accent": "#E5462F",
                  "tint": ("#F7C2AC", "#3B1209"), "glow": "rgba(120,35,15,.20)", "square": True,
                  "photo": "assets/photos/independence-monument-unsplash.jpg", "photo_pos": "60% 30%",
                  "fade": "transparent 0%,rgba(0,0,0,.12) 18%,rgba(0,0,0,.45) 36%,rgba(0,0,0,.85) 52%,#000 62%",
                  "art": "assets/covers/art/03-swift-cover-art.png",
                  "photo_credit": ("Cover photo: the Independence Monument, Phnom Penh, from Unsplash (unsplash.com/license). "
                                   "Cropped and toned orange.")},
        # Its own look, so the Swift books and slides do not look like Dart's: see "Swift style" in 03-swift/planning/slide-design.md.
        "theme": {
            "light": {"text": "#1D1A24", "text-muted": "#5F5A69", "surface": "#FBF5F1", "border": "#EBDDD3", "primary": "#C2391F"},
            "dark": {"background": "#0B0E1C", "surface": "#161A2B", "border": "#2A2F45", "text": "#F4F2F7",
                     "text-muted": "#B5B1C4", "primary": "#FF8A65"},
            "code": {"background": "#1F2024", "border": "#2E3036", "highlight-line": "#2B2C31", "text": "#E9E9EB",
                     "comment": "#8A96A3", "keyword": "#FC5FA3", "string": "#FC6A5D", "number": "#D9C97C",
                     "type": "#5DD8FF", "function": "#67B7A4", "punctuation": "#E9E9EB", "output": "#A9E8BF"},
            "callout": {"note": {"accent": "#C2391F", "tint": "#FDF3EF", "text": "#8A2614", "label": "Note"}},
        },
        "fonts": ("IBM Plex Sans", "IBM Plex Mono"),
        "font_faces": [
            ("IBM Plex Sans", "assets/fonts/ibm-plex-sans/web/IBMPlexSans-Regular.woff2", "400", "woff2", "font-style:normal;"),
            ("IBM Plex Sans", "assets/fonts/ibm-plex-sans/web/IBMPlexSans-Italic.woff2", "400", "woff2", "font-style:italic;"),
            ("IBM Plex Sans", "assets/fonts/ibm-plex-sans/web/IBMPlexSans-SemiBold.woff2", "600", "woff2", "font-style:normal;"),
            ("IBM Plex Sans", "assets/fonts/ibm-plex-sans/web/IBMPlexSans-Bold.woff2", "700 900", "woff2", "font-style:normal;"),
            ("IBM Plex Sans", "assets/fonts/ibm-plex-sans/web/IBMPlexSans-BoldItalic.woff2", "700 900", "woff2", "font-style:italic;"),
            ("IBM Plex Mono", "assets/fonts/ibm-plex-mono/web/IBMPlexMono-Regular.woff2", "400", "woff2", "font-style:normal;"),
            ("IBM Plex Mono", "assets/fonts/ibm-plex-mono/web/IBMPlexMono-Italic.woff2", "400", "woff2", "font-style:italic;"),
            ("IBM Plex Mono", "assets/fonts/ibm-plex-mono/web/IBMPlexMono-Bold.woff2", "700", "woff2", "font-style:normal;"),
        ],
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 120px; height: 8px; background: #F05138; margin-top: 22px; }
section.dark h2 { color: #FF8A65; }
section.recap { background: #FBF5F1; border-top: 10px solid #F05138; }
pre.output { border-left-color: #F05138; }
.footer span:first-child::before { content: ""; display: inline-block; width: 10px; height: 10px; background: #F05138; margin-right: 10px; }
""",
        "book_css": """
pre.output { border-left-color: #F05138; }
@page { @top-left { border-bottom-color: #F05138; } @top-right { border-bottom-color: #F05138; } }
""",
        "text": {
            "en": {"title": "Swift Programming", "second": "Programming", "badge": "A Practical Guide", "toc": "Contents", "inside": "In this section",
                   "points": ["Learn the Swift language, step by step", "Build real programs for a coffee shop", "Get ready for iOS apps"]},
            "km": {"title": "Swift Programming", "second": "Programming", "badge": "រៀន និងអនុវត្តជាក់ស្ដែង", "toc": "មាតិកា", "inside": "ក្នុងផ្នែកនេះ",
                   "points": ["រៀនភាសា Swift ម្ដងមួយជំហាន", "បង្កើតកម្មវិធីពិតសម្រាប់ហាងកាហ្វេ", "ត្រៀមខ្លួនសម្រាប់ app iOS"]},
        },
    },
    "c-cpp": {
        "folder": "21-c-cpp", "code": "c", "name": "C/C++", "slug": "c-cpp-programming",
        # Two marks, side by side and never merged. See assets/logos/README.md for their rules.
        "logos": ["assets/logos/c/c-icon.svg", "assets/logos/cpp/cpp-icon.svg"],
        "icon": "assets/logos/cpp/cpp-icon.svg",
        "credit": ("The C++ logo is a trademark of the Standard C++ Foundation. We are not endorsed by or affiliated with the "
                   "Standard C++ Foundation. C icon from programming-languages-logos by Carlos Abraham, MIT License."),
        "cover": {"style": "grid", "accent": "#0B7A75", "art": "assets/covers/patterns/c-cpp-cover-background.png"},
        # Its own look: graphite and teal, with memory as the visual idea. See 21-c-cpp/planning/slide-design.md.
        "theme": {
            "light": {"text": "#172026", "text-muted": "#56636B", "surface": "#F1F7F6", "border": "#D5E3E1", "primary": "#0B7A75"},
            "dark": {"background": "#12171C", "surface": "#1C242B", "border": "#2C3840", "text": "#EEF3F3",
                     "text-muted": "#A9B6BA", "primary": "#4FD1C5"},
            "code": {"background": "#171D22", "border": "#2C3840", "highlight-line": "#222B32", "text": "#E6EDEE",
                     "comment": "#84959C", "keyword": "#7EE0B8", "string": "#F2C572", "number": "#F2A36B",
                     "type": "#6FD3E8", "function": "#C3E88D", "punctuation": "#C7D2D4", "output": "#A8E6D4"},
            "callout": {"note": {"accent": "#0B7A75", "tint": "#EFF8F7", "text": "#075B57", "label": "Note"}},
        },
        "fonts": ("Source Sans 3", "Source Code Pro"),
        "font_faces": [
            ("Source Sans 3", "assets/fonts/source-sans-3/web/SourceSans3-Regular.woff2", "400", "woff2", "font-style:normal;"),
            ("Source Sans 3", "assets/fonts/source-sans-3/web/SourceSans3-It.woff2", "400", "woff2", "font-style:italic;"),
            ("Source Sans 3", "assets/fonts/source-sans-3/web/SourceSans3-Semibold.woff2", "600", "woff2", "font-style:normal;"),
            ("Source Sans 3", "assets/fonts/source-sans-3/web/SourceSans3-Bold.woff2", "700 900", "woff2", "font-style:normal;"),
            ("Source Sans 3", "assets/fonts/source-sans-3/web/SourceSans3-BoldIt.woff2", "700 900", "woff2", "font-style:italic;"),
            ("Source Code Pro", "assets/fonts/source-code-pro/web/SourceCodePro-Regular.woff2", "400", "woff2", "font-style:normal;"),
            ("Source Code Pro", "assets/fonts/source-code-pro/web/SourceCodePro-It.woff2", "400", "woff2", "font-style:italic;"),
            ("Source Code Pro", "assets/fonts/source-code-pro/web/SourceCodePro-Bold.woff2", "700", "woff2", "font-style:normal;"),
        ],
        "slide_css": """
section.dark h1::after { content: ""; display: block; width: 120px; height: 8px; background: #4FD1C5; margin-top: 22px; }
section.dark::before { content: "0x7FF0  4D 49 4E 41  20 43 4F 46  46 45 45 00"; position: absolute; right: 60px; bottom: 44px;
  font-family: 'Source Code Pro', monospace; font-size: 17px; color: #4FD1C5; opacity: .35; }
section.recap { background: #F1F7F6; border-top: 10px solid #0B7A75; }
pre.output { border-left-color: #0B7A75; }
.logos { display: flex; gap: 16px; align-items: center; }
section.dark .logos img { height: 66px; display: block; }
.footer span:first-child::before { content: "0x"; font-family: 'Source Code Pro', monospace; font-weight: 700; color: #0B7A75; margin-right: 8px; }
section.dark .footer span:first-child::before { color: #4FD1C5; }
""",
        "book_css": """
pre.output { border-left-color: #0B7A75; }
@page { @top-left { border-bottom-color: #0B7A75; } @top-right { border-bottom-color: #0B7A75; } }
.cover .logos { display: flex; gap: 6mm; align-items: center; margin-bottom: 14mm; }
.cover .logos img { height: 22mm; margin: 0; }
""",
        "text": {
            "en": {"title": "C/C++ Programming", "second": "Programming", "badge": "From Your First Program to Advanced", "toc": "Contents", "inside": "In this section",
                   "points": ["Start with how a computer works", "Learn C, then modern C++, step by step", "Use them in real mobile apps"]},
            "km": {"title": "C/C++ Programming", "second": "Programming", "badge": "ពីកម្មវិធីដំបូង ដល់កម្រិតខ្ពស់", "toc": "មាតិកា", "inside": "ក្នុងផ្នែកនេះ",
                   "points": ["ចាប់ផ្ដើមពីរបៀបដែលកុំព្យូទ័រដំណើរការ", "រៀន C រួច C++ ទំនើប ម្ដងមួយជំហាន", "ប្រើវាក្នុង app ទូរស័ព្ទពិតៗ"]},
        },
    },
}
# The newer courses live in course_themes.py, so this file stays readable.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from course_themes import COURSES as MORE_COURSES  # noqa: E402

COURSES.update(MORE_COURSES)
from course_themes import apply_covers  # noqa: E402

apply_covers(COURSES)  # every book cover: a photo of Cambodian heritage, with a caption
from course_themes import apply_logo_sets  # noqa: E402

apply_logo_sets(COURSES)  # covers of topic books: a honeycomb of the platforms they cover
# A course can also be named by its folder, for example 01-dart instead of dart.
if len(sys.argv) > 1:
    sys.argv[1] = next((k for k, v in COURSES.items() if v["folder"] == sys.argv[1].rstrip("/")), sys.argv[1])
# The course being built is the first command-line word (see main). It is chosen here, before the CSS below
# is made, because each course can change the theme colors and fonts.
COURSE = COURSES[sys.argv[1]] if len(sys.argv) > 1 and sys.argv[1] in COURSES else COURSES["dart"]
PRETTIER = "prettier@3.3.3"
SMALLEST_OK = 20  # px; slide text below this is hard to read in a video
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
T = json.loads((ROOT / "assets/theme/tokens.json").read_text())
for group, values in COURSE.get("theme", {}).items():  # a course can change any color group
    T[group] = {**T[group], **values}
SANS, MONO = COURSE.get("fonts", ("Inter", "JetBrains Mono"))
L, DK, C, CO = T["light"], T["dark"], T["code"], T["callout"]
KHMER_DIGITS = str.maketrans("0123456789", "០១២៣៤៥៦៧៨៩")
AUTHOR = {"en": "TOUCH DEN", "km": "ទូច ដែន"}


def byline(lang):
    """Author and today's date, in the language of the page."""
    d = datetime.date.today()
    if lang == "km":
        months = ["មករា", "កុម្ភៈ", "មីនា", "មេសា", "ឧសភា", "មិថុនា", "កក្កដា", "សីហា", "កញ្ញា", "តុលា", "វិច្ឆិកា", "ធ្នូ"]
        return f"រៀបរៀងដោយ {AUTHOR['km']} · ថ្ងៃទី {str(d.day).translate(KHMER_DIGITS)} ខែ{months[d.month - 1]} ឆ្នាំ {str(d.year).translate(KHMER_DIGITS)}"
    return f"By {AUTHOR['en']} · {d.strftime('%B')} {d.day}, {d.year}"


# ---------------------------------------------------------------- embedded assets

def asset_url(path):
    """A file in the repo, as a file:// URL, so a page works at any depth under output/."""
    return (ROOT / path).as_uri()


def font_css():
    khmer = "unicode-range: U+1780-17FF, U+19E0-19FF, U+200B-200D;"
    faces = [
        # Google Sans (SIL Open Font License) is used only for Khmer letters; English keeps each course's own font.
        ("Google Sans Khmer", "assets/fonts/google-sans/GoogleSans[GRAD,opsz,wght].ttf", "400 700", "truetype", khmer),
    ] + COURSE.get("font_faces", [
        ("Inter", "assets/fonts/inter/web/InterVariable.woff2", "100 900", "woff2", ""),
        ("JetBrains Mono", "assets/fonts/jetbrains-mono/web/JetBrainsMono-Regular.woff2", "400", "woff2", ""),
        ("JetBrains Mono", "assets/fonts/jetbrains-mono/web/JetBrainsMono-Bold.woff2", "700", "woff2", ""),
    ])
    return "".join(
        f"@font-face{{font-family:'{n}';src:url({asset_url(p)}) format('{f}');font-weight:{w};{x}}}\n"
        for n, p, w, f, x in faces
    )


def image_uri(path):
    return asset_url(path)


SHOT = re.compile(r"<!-- SCREENSHOT TODO:? ?(.*?) -->", re.S)
PHONE = re.compile(r"iPhone|phone|Pixel|simulator|Emulator|Expo Go", re.I)


def screenshot(todo):
    """A screenshot note becomes the picture once it is saved under assets/screenshots/<course folder>/,
    and until then a placeholder box that says what to capture and where to save it."""
    m = re.match(r"file: ([^;]+);\s*(.*)", todo.strip(), re.S)
    if not m:
        return f'<div class="shot-box wide"><div><strong>Screenshot</strong><p>{html.escape(todo)}</p></div></div>'
    name, rest = m.groups()
    rel = f"assets/screenshots/{COURSE['folder']}/{name}"
    if (ROOT / rel).exists():
        return f'<img class="shot-img" src="{image_uri(rel)}" alt="Screenshot">'
    device = (re.search(r"Device:\s*([^;]*)", rest) or [None, ""])[1].strip()
    show = (re.search(r"Show:\s*(.*?)(?:\.\s+(?:Crop|No |Hide)|$)", rest, re.S) or [None, rest])[1].strip().rstrip(".")
    shape = "phone" if PHONE.search(device) and not re.search(r"\bMac\b|browser|Chrome", device) else "wide"
    return (f'<div class="shot-box {shape}"><div><strong>Screenshot to capture</strong>'
            f'<p>{html.escape(show[:1].upper() + show[1:])}.</p><p class="dev">{html.escape(device)}</p>'
            f'<code>{html.escape(rel)}</code></div></div>')


def course_logo(key, plain=False):
    """The course's logo: one image, or several side by side for a course with "logos"."""
    if "logos" in COURSE:
        return '<div class="logos">' + "".join(f'<img src="{image_uri(path)}" alt="">' for path in COURSE["logos"]) + "</div>"
    style = "" if plain else ' class="logo"'
    return f'<img{style} src="{image_uri(COURSE[key])}" alt="{COURSE["name"]}">'


def write_html(page, content):
    """Save a generated page, formatted with Prettier. output/ is in .gitignore, which Prettier obeys by default."""
    page.write_text(content)
    done = subprocess.run(["npx", "--yes", PRETTIER, "--parser", "html", "--ignore-path", "/dev/null", "--write", str(page)], capture_output=True, text=True, timeout=120)
    if done.returncode != 0:
        print(f"warning: Prettier could not format {page.name}: {done.stderr.strip()[:200]}")


# ---------------------------------------------------------------- code highlighting

C_TOKEN = re.compile(r"""(?P<comment>//[^\n]*|/\*.*?\*/)|(?P<string>"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')|(?P<number>\b0[xX][0-9a-fA-F]+\b|\b\d+(?:\.\d+)?[fFuUlL]*\b)
|(?P<kw>^[ \t]*\#[ \t]*[a-z]+)|(?P<word>[A-Za-z_]\w*)|(?P<punct>[{}()\[\];,.:?=<>+\-*/%!&|~^]+)""", re.X | re.S | re.M)
C_TYPES = ("size_t", "int8_t", "int16_t", "int32_t", "int64_t", "uint8_t", "uint16_t", "uint32_t", "uint64_t")
LANGUAGES = {
    "c": {"keywords": set("""auto break case char const continue default do double else enum extern false float for goto if inline int long nullptr register restrict return short signed sizeof static struct switch true typedef union unsigned void volatile while bool""".split()), "types": C_TYPES, "token": C_TOKEN},
    "cpp": {"keywords": set("""auto break case char const continue default do double else enum extern false float for goto if inline int long nullptr register restrict return short signed sizeof static struct switch true typedef union unsigned void volatile while bool alignas alignof catch class concept consteval constexpr constinit const_cast co_await co_return co_yield decltype delete dynamic_cast explicit export final friend mutable namespace new noexcept operator override private protected public reinterpret_cast requires static_assert static_cast template this thread_local throw try typeid typename using virtual""".split()), "types": C_TYPES, "token": C_TOKEN},
    "dart": {
        "keywords": set("""abstract as assert async await break case catch class const continue default do dynamic else enum
extends factory false final finally for get if implements import in interface is late mixin new null on override required rethrow return sealed set static super switch
this throw true try typedef var void when while with""".split()),
        "types": ("int", "double", "num", "bool"),
        "token": re.compile(r"""(?P<comment>//[^\n]*)|(?P<string>'(?:[^'\\\n]|\\.)*'|"(?:[^"\\\n]|\\.)*")|(?P<number>\b\d+(?:\.\d+)?\b)
|(?P<word>[A-Za-z_]\w*)|(?P<punct>[{}()\[\];,.:?=<>+\-*/%!&|~^]+)""", re.X),
    },
    "swift": {
        "keywords": set("""actor any associatedtype async await borrowing break case catch class consuming continue convenience default defer
deinit didSet do else enum extension fallthrough false fileprivate final for func get guard if import in indirect init inout internal is
lazy let mutating nil nonisolated open operator override package private protocol public repeat required rethrows return self Self sending
set some static struct subscript super switch throw throws true try typealias unowned var weak where while willSet""".split()),
        "types": (),
        # Swift also has attributes and macros, such as @MainActor and #expect: shown like keywords.
        "token": re.compile(r"""(?P<comment>//[^\n]*)|(?P<string>"(?:[^"\\\n]|\\.)*")|(?P<number>\b\d+(?:\.\d+)?\b)
|(?P<kw>[@#][A-Za-z_]\w*)|(?P<word>[A-Za-z_]\w*)|(?P<punct>[{}()\[\];,.:?=<>+\-*/%!&|~^]+)""", re.X),
    },
    "kotlin": {
        "keywords": set("""as break class continue do else false for fun if in interface is null object package return super this throw
true try typealias typeof val var when while by catch constructor delegate dynamic field file finally get import init param property
receiver set setparam where actual abstract annotation companion const crossinline data enum expect external final infix inline inner
internal lateinit noinline open operator out override private protected public reified sealed suspend tailrec vararg value""".split()),
        "types": (),
        "token": re.compile(r"""(?P<comment>//[^\n]*|/\*.*?\*/)|(?P<string>"{3}.*?"{3}|"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')
|(?P<number>\b\d[\d_]*(?:\.\d+)?[LFf]?\b)|(?P<kw>@[A-Za-z_]\w*)|(?P<word>[A-Za-z_]\w*)|(?P<punct>[{}()\[\];,.:?=<>+\-*/%!&|~^]+)""", re.X | re.S),
    },
    "javascript": {
        "keywords": set("""async await break case catch class const continue debugger default delete do else export extends false finally
for from function if import in instanceof let new null of return static super switch this throw true try typeof undefined var void while
yield""".split()),
        "types": (),
        "token": re.compile(r"""(?P<comment>//[^\n]*|/\*.*?\*/)|(?P<string>`(?:[^`\\]|\\.)*`|"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')
|(?P<number>\b\d[\d_]*(?:\.\d+)?n?\b)|(?P<word>[A-Za-z_$][\w$]*)|(?P<punct>[{}()\[\];,.:?=<>+\-*/%!&|~^]+)""", re.X | re.S),
    },
}
LANGUAGES["typescript"] = {**LANGUAGES["javascript"], "keywords": LANGUAGES["javascript"]["keywords"] | set(
    "type interface enum implements private public protected readonly as satisfies keyof declare namespace abstract".split()),
    "types": ("string", "number", "boolean", "void", "unknown", "never", "any")}
LANGUAGES["tsx"] = LANGUAGES["typescript"]
# YAML (CI workflows): keys like keywords, quoted text like strings, # comments. Values are left plain.
LANGUAGES["yaml"] = {"keywords": set(), "types": (), "token": re.compile(
    r"""(?P<comment>(?<![\w"'])\#[^\n]*)|(?P<string>"(?:[^"\\\n]|\\.)*"|'[^'\n]*')|(?P<kw>^[ \t]*(?:-[ \t]+)?[\w.\-/]+(?=:))
|(?P<number>\b\d+(?:\.\d+)*\b)|(?P<punct>[:\-\[\]{}|>,]+)""", re.X | re.M)}
LANGUAGES["jsx"] = LANGUAGES["javascript"]
# HTML (web pages): tags and attribute names like keywords, attribute values like strings, <!-- --> comments.
LANGUAGES["html"] = {"keywords": set(), "types": (), "token": re.compile(
    r"""(?P<comment><!--.*?-->)|(?P<kw></?[A-Za-z][\w-]*|/?>|<!DOCTYPE[^>]*>)|(?P<string>"[^"]*"|'[^']*')|(?P<type>(?<=\s)[\w:-]+(?==))""", re.X | re.S | re.I)}
# CSS: selectors and @rules like keywords, property names like types, values with units like numbers.
LANGUAGES["css"] = {"keywords": set(), "types": (), "token": re.compile(
    r"""(?P<comment>/\*.*?\*/)|(?P<string>"[^"\n]*"|'[^'\n]*')|(?P<kw>@[\w-]+|^[ \t]*[^\s{};][^{};\n]*(?=\s*\{))
|(?P<type>(?<=[\s;{])[\w-]+(?=\s*:))|(?P<number>\#[0-9a-fA-F]{3,8}\b|-?\b\d+(?:\.\d+)?(?:px|rem|em|%|vh|vw|s|ms|fr|deg)?\b)
|(?P<punct>[{}():;,]+)""", re.X | re.S | re.M)}

# Rust: macros such as println! like functions, attributes such as #[derive] like keywords, lifetimes like types.
LANGUAGES["rust"] = {
    "keywords": set("""as async await break const continue crate dyn else enum extern false fn for if impl in let loop match mod move mut pub
ref return self Self static struct super trait true type unsafe use where while""".split()),
    "types": ("i8", "i16", "i32", "i64", "i128", "isize", "u8", "u16", "u32", "u64", "u128", "usize", "f32", "f64", "bool", "char", "str"),
    "token": re.compile(r"""(?P<comment>//[^\n]*|/\*.*?\*/)|(?P<string>b?r\#*".*?"\#*|b?"(?:[^"\\]|\\.)*"|b?'(?:[^'\\\n]|\\.)')
|(?P<type>'[a-z_]\w*)|(?P<number>\b\d[\d_]*(?:\.\d+)?(?:[iuf](?:8|16|32|64|128|size))?\b)|(?P<kw>\#!?\[[^\]\n]*\])
|(?P<fn>[a-z_]\w*!)|(?P<word>[A-Za-z_]\w*)|(?P<punct>[{}()\[\];,.:?=<>+\-*/%!&|~^@]+)""", re.X | re.S),
}

# Java: modern Java including records, sealed classes, pattern matching, annotations (@Override, @SpringBootApplication)
LANGUAGES["java"] = {
    "keywords": set("""abstract assert boolean break byte case catch char class const continue default do double else enum
extends final finally float for goto if implements import instanceof int interface long native new package private
protected public return short static strictfp super switch synchronized this throw throws transient try void volatile while
record sealed permits non-sealed yield var""".split()),
    "types": ("String", "int", "boolean", "double", "long", "float", "char", "byte", "short", "void", "Object", "List", "Map", "Set", "Optional"),
    "token": re.compile(r"""(?P<comment>//[^\n]*|/\*.*?\*/)|(?P<string>"{3}.*?"{3}|"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')
|(?P<number>\b\d[\d_]*(?:\.\d+)?[fFdDlL]?\b)|(?P<kw>@[A-Za-z_]\w*)|(?P<word>[A-Za-z_]\w*)|(?P<punct>[{}()\[\];,.:?=<>+\-*/%!&|~^]+)""", re.X | re.S),
}


def highlight(code, language):
    spec = LANGUAGES[language]
    KEYWORDS = spec["keywords"]
    out, pos = [], 0
    for m in spec["token"].finditer(code):
        out.append(html.escape(code[pos:m.start()]))
        pos = m.end()
        text, kind = m.group(), m.lastgroup
        if kind == "word":
            after = code[m.end():m.end() + 1]
            if text in KEYWORDS:
                kind = "kw"
            elif text[0].isupper() or text in spec["types"]:
                kind = "type"
            elif after == "(":
                kind = "fn"
            else:
                out.append(html.escape(text))
                continue
        out.append(f'<span class="t-{kind}">{html.escape(text)}</span>')
    out.append(html.escape(code[pos:]))
    return "".join(out)


# ---------------------------------------------------------------- small Markdown converter

def inline(s, base=None):
    codes = []

    def keep_code(m):
        codes.append(f"<code>{html.escape(m.group(1))}</code>")
        return f"\x00{len(codes) - 1}\x00"

    s = re.sub(r"`([^`]+)`", keep_code, s)
    s = html.escape(s, quote=False)

    def image(m):
        src = (base / m.group(2)).resolve().relative_to(ROOT) if base else m.group(2)
        alt = m.group(1).replace('"', "&quot;")
        return f'<img src="{image_uri(str(src))}" alt="{alt}">'

    s = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", image, s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)  # links become plain text in print
    s = re.sub(r"&lt;(https?://[^&]+)&gt;", r"\1", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", s)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], s)


def code_block(lang, body, label=False):
    if lang in LANGUAGES:
        long = " long" if body.count("\n") >= 18 else ""
        return f'<pre class="code{long}"><code>{highlight(body, lang)}</code></pre>'
    if lang == "text":
        tag = '<div class="output-label">OUTPUT</div>' if label else ""
        return f'<pre class="output">{tag}<code>{html.escape(body)}</code></pre>'
    return f'<pre class="shell"><code>{html.escape(body)}</code></pre>'


def table_cells(line):
    """Split a table row on |, ignoring any | inside `inline code`. An escaped pipe, \\|, is a literal |
    (GitHub needs the backslash inside tables, even in code, so lessons write `\\|\\|` for ||)."""
    cells, current, in_code = [], "", False
    row = line.strip().strip("|")
    i = 0
    while i < len(row):
        ch = row[i]
        if ch == "\\" and row[i + 1:i + 2] == "|":
            current += "|"
            i += 2
            continue
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(current)
            current = ""
        else:
            current += ch
        i += 1
    return cells + [current]


def blocks(md, base=None):
    """Split Markdown into (kind, html) blocks. Kinds: h1 h2 h3 p ul ol table code output hr quote img."""
    lines, i, out = md.split("\n"), 0, []
    while i < len(lines):
        line = lines[i]
        if SHOT.fullmatch(line.strip()):
            out.append(("img", f'<div class="figure">{screenshot(SHOT.fullmatch(line.strip()).group(1))}</div>'))
            i += 1
        if not line.strip() or (line.startswith("<!--") and line.rstrip().endswith("-->")):
            i += 1
        elif line.startswith("```"):
            lang, body = line[3:].strip(), []
            i += 1
            while not lines[i].startswith("```"):
                body.append(lines[i])
                i += 1
            i += 1
            # <language>-library: a library file shown in full. <language>-wrong: code that is meant to show a problem.
            # Both are highlighted; the checker does not run either on its own.
            code = re.fullmatch(r"(\w+?)(?:-(library|wrong))?", lang)
            if code and code.group(1) in LANGUAGES:
                out.append(("code", (code.group(1), "\n".join(body), code.group(2) or "")))
            else:
                out.append(("output" if lang == "text" else "shell", "\n".join(body)))
        elif m := re.match(r"(#{1,4}) (.*)", line):
            n = len(m.group(1))
            out.append((f"h{n}", f"<h{n}>{inline(m.group(2), base)}</h{n}>"))
            i += 1
        elif line.strip() == "---":
            out.append(("hr", "<hr>"))
            i += 1
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append([c.strip() for c in table_cells(lines[i])])
                i += 1
            head = "".join(f"<th>{inline(c, base)}</th>" for c in rows[0])
            body = "".join("<tr>" + "".join(f"<td>{inline(c, base)}</td>" for c in r) + "</tr>" for r in rows[2:])
            out.append(("table", f"<table><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>"))
        elif line.startswith(">"):
            q = []
            while i < len(lines) and lines[i].startswith(">"):
                q.append(lines[i].lstrip("> "))
                i += 1
            out.append(("quote", f"<blockquote>{inline(' '.join(q), base)}</blockquote>"))
        elif re.match(r"(\d+\.|-) ", line):
            kind = "ol" if line[0].isdigit() else "ul"
            items = []
            while i < len(lines) and (re.match(r"\s*(\d+\.|-) ", lines[i])):
                indent = len(lines[i]) - len(lines[i].lstrip())
                text = re.sub(r"^\s*(\d+\.|-) ", "", lines[i])
                if indent and items:
                    items[-1][1].append(text)
                else:
                    items.append((text, []))
                i += 1
            li = ""
            for text, sub in items:
                inner = "".join(f"<li>{inline(x, base)}</li>" for x in sub)
                li += f"<li>{inline(text, base)}" + (f"<ul>{inner}</ul>" if inner else "") + "</li>"
            # A numbered list that continues after a code block starts at its own number (e.g. "3.").
            first = int(line.split(".")[0]) if kind == "ol" else 1
            start = f' start="{first}"' if first != 1 else ""
            out.append((kind, f"<{kind}{start}>{li}</{kind}>"))
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"(```|#{1,4} |\||>|<!--|---$|(\d+\.|-) )", lines[i]):
                para.append(lines[i])
                i += 1
            if not para:  # a line the rules above did not consume
                i += 1
                continue
            text = " ".join(para)
            if re.fullmatch(r"!\[[^\]]*\]\([^)]+\)", text):
                out.append(("img", f'<div class="figure">{inline(text, base)}</div>'))
            else:
                # A line that is only a bold label (e.g. "**VS Code**" or "**Solution:**") is not a paragraph.
                label = ' class="label"' if re.fullmatch(r"\*\*[^*]+\*\*[:៖]?", text) else ""
                out.append(("p", f"<p{label}>{inline(text, base)}</p>"))
    def render(kind, value):
        if kind == "code":
            return code_block(*value[:2])
        if kind in ("output", "shell"):
            return code_block("text" if kind == "output" else "shell", value)
        return value
    return [(k, render(k, v)) for k, v in out]


def strip_front_matter(md):
    return re.sub(r"\A---\n.*?\n---\n", "", md, count=1, flags=re.S)


# ---------------------------------------------------------------- shared CSS

BASE_CSS = f"""
{{FONTS}}
* {{ box-sizing: border-box; }}
html {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
body {{ margin: 0; color: {L['text']}; background: {L['background']};
  font-family: 'Google Sans Khmer', '{SANS}', system-ui, sans-serif; }}
code {{ font-family: '{MONO}', 'Google Sans Khmer', monospace; font-size: .88em; }}
p code, li code, td code, th code, blockquote code, h1 code, h2 code, h3 code {{
  background: {L['surface']}; padding: .08em .3em; }}
code, pre {{ font-variant-ligatures: none; font-feature-settings: 'liga' 0, 'calt' 0; }}  /* show >= and => exactly as typed */
pre {{ margin: 0; font-family: '{MONO}', 'Google Sans Khmer', monospace; white-space: pre-wrap; line-height: 1.45; }}
pre code {{ font-size: 1em; }}
pre.code {{ background: {C['background']}; color: {C['text']}; padding: .8em 1em; }}
pre.output {{ background: {L['surface']}; color: {L['text']}; border-left: .25em solid {CO['tip']['accent']}80; padding: .55em .9em; }}
pre.shell {{ background: {DK['surface']}; color: {C['output']}; padding: .55em .9em; }}
.t-comment {{ color: {C['comment']}; font-style: italic; }}
.t-string {{ color: {C['string']}; }}
.t-number {{ color: {C['number']}; }}
.t-kw {{ color: {C['keyword']}; }}
.t-type {{ color: {C['type']}; }}
.t-fn {{ color: {C['function']}; }}
.t-punct {{ color: {C['punctuation']}; }}
table {{ border-collapse: collapse; width: 100%; }}
th {{ text-align: left; border-bottom: 2px solid {L['text']}; }}
th, td {{ padding: .4em .6em; vertical-align: top; }}
td {{ border-bottom: 1px solid {L['border']}; }}
strong {{ font-weight: 700; }}
img {{ max-width: 100%; }}
"""


# ---------------------------------------------------------------- slides

SLIDE_CSS = f"""
@page {{ size: 1280px 720px; margin: 0; }}
section.slide {{ width: 1280px; height: 720px; position: relative; overflow: hidden; break-after: page;
  padding: 44px 60px 50px; font-size: 25px; line-height: 1.6; background: {L['background']}; }}
section.slide h1 {{ font-size: 1.65em; line-height: 1.35; margin: 0 0 .35em; color: {L['text']}; }}
section.slide p {{ margin: 0 0 .5em; }}
section.slide ul, section.slide ol {{ margin: 0 0 .5em; padding-left: 1.15em; }}
section.slide li {{ margin-bottom: .3em; }}
section.slide pre {{ font-size: .8em; margin-bottom: .45em; }}
section.slide table {{ font-size: .86em; margin-bottom: .5em; }}
.cols {{ display: grid; grid-template-columns: 62% 1fr; gap: 26px; align-items: start; }}
.cols ul {{ margin: 0; }}
.footer {{ position: absolute; left: 60px; right: 60px; bottom: 14px; display: flex; justify-content: space-between;
  font-size: 15px; color: {L['text-muted']}; }}
.callout {{ border-left: .3em solid; padding: .4em .8em; font-size: .92em; margin-top: .35em; }}
.callout strong {{ margin-right: .4em; }}
section.dark {{ background: {DK['background']}; color: {DK['text']}; }}
section.dark h1 {{ color: {DK['text']}; font-size: 2.6em; margin-top: 20px; }}
section.dark h2 {{ color: {DK['primary']}; font-size: 1.35em; margin: 0 0 .3em; font-weight: 700; }}
section.dark p {{ color: {DK['text-muted']}; }}
section.dark code {{ background: {DK['surface']}; color: {DK['text']}; }}  /* inline code on dark slides stays readable */
section.dark .footer {{ color: {DK['text-muted']}; }}
section.dark .logo {{ height: 66px; display: block; }}
.byline {{ position: absolute; top: 58px; right: 60px; font-size: 19px; color: {DK['text-muted']}; }}
section.recap {{ background: {L['surface']}; }}
section.diagram img {{ display: block; margin: 0 auto; max-height: 640px; }}
section.screenshot {{ display: flex; align-items: center; justify-content: center; }}
section.screenshot img {{ max-width: 100%; max-height: 600px; }}
section.credits {{ display: flex; flex-direction: column; justify-content: center; }}
section.overflow {{ outline: 6px solid red; outline-offset: -6px; }}
.shot-box {{ display: flex; align-items: center; justify-content: center; text-align: center; border: 3px dashed {L['text-muted']};
  background: {L['surface']}; color: {L['text-muted']}; }}
.shot-box > div {{ padding: 0 6%; }}
.shot-box strong {{ display: block; color: {L['text']}; font-size: 1.05em; margin-bottom: .4em; }}
.shot-box p {{ margin: .2em 0; line-height: 1.4; }}
.shot-box p.dev {{ font-size: .8em; }}
.shot-box code {{ display: inline-block; margin-top: .7em; font-size: .7em; }}
section.screenshot .shot-box.wide {{ width: 1000px; height: 600px; font-size: 26px; }}
section.screenshot .shot-box.phone {{ width: 330px; height: 590px; font-size: 21px; }}
section.screenshot img.shot-img {{ max-width: 100%; max-height: 640px; }}
"""

CALLOUT_LABEL = {"en": {"tip": "Tip", "warning": "Warning", "note": "Note", "practice": "Practice"},
                 "km": {"tip": "ចំណាំ", "warning": "ប្រយ័ត្ន", "note": "ចំណាំ", "practice": "លំហាត់"}}

FIT_JS = """
document.fonts.ready.then(() => {
  const report = [];
  document.querySelectorAll('section.slide').forEach(s => {
    if (s.classList.contains('diagram')) return;
    let size = 25;
    const limit = () => s.clientHeight - 34;
    const used = () => Math.max(...[...s.children].filter(c => !c.classList.contains('footer') && !c.classList.contains('byline'))
      .map(c => c.getBoundingClientRect().bottom - s.getBoundingClientRect().top));
    while (used() > limit() && size > 17) { size -= 0.5; s.style.fontSize = size + 'px'; }
    s.dataset.size = size;
    if (used() > limit()) { s.classList.add('overflow'); report.push(s.dataset.id + ':overflow'); }
    else if (size < 25) report.push(s.dataset.id + ':' + size);
  });
  document.body.dataset.report = report.join(' ');
  document.body.dataset.done = '1';
});
"""


def lesson_names(lesson, lang):
    """From the slides title: ('Dart Programming · Section 4', 'Functions')."""
    title = re.search(r'^title: "(.*)"$', (lesson / lang / "slides.md").read_text(), re.M).group(1)
    course, _, rest = title.partition(" — ")
    section, name = re.split(r"(?:: |៖ ?)", rest, maxsplit=1)
    return f"{course} · {section}", name


def build_slides(lesson, lang):
    md = strip_front_matter((lesson / lang / "slides.md").read_text())
    sections, count = [], 0
    for raw in re.split(r"\n---\n", md):
        id_m = re.search(r"<!-- (\d+\.\d+) -->", raw)
        if not id_m:
            continue
        sid = id_m.group(1)
        layout = (re.search(r"<!-- layout: ([^>]*?) -->", raw) or [None, ""])[1]
        callouts = re.findall(r"<!-- callout (\w+): (.*?) -->", raw, re.S)
        visuals = re.findall(r"<!-- visual: (\S+) -->", raw)
        # A screenshot note gets a slide of its own (below), so it is not drawn inside this slide too.
        items = blocks(SHOT.sub("", raw))
        cls = "slide"
        if layout.startswith("title"):
            cls += " dark"
        elif layout.startswith("recap"):
            cls += " recap"
        elif layout.startswith("credits"):
            cls += " credits"

        body = ""
        if layout.startswith("title"):
            body += f'{course_logo("logo_dark")}<div class="byline">{byline(lang)}</div>'
        if layout.startswith("two-column"):
            first_code = next((n for n, (k, _) in enumerate(items) if k in ("code", "output", "table")), len(items))
            intro, rest = items[:first_code], items[first_code:]
            # When code and output together are tall, the output moves above the key points.
            stacked = sum(v.count("\n") + 1 for k, v in rest if k in ("code", "output"))
            to_right = ["ul", "ol"]
            if stacked > 15 or "output right" in layout:
                to_right.append("output")
            left = "".join(v for k, v in rest if k not in to_right)
            order = ("output", "table", "ul", "ol")
            right = "".join(v for want in order if want in to_right for k, v in rest if k == want)
            body += "".join(v for _, v in intro) + f'<div class="cols"><div>{left}</div><div>{right}</div></div>'
        else:
            body += "".join(v for _, v in items)
        for kind, text in callouts:
            c = CO[kind]
            body += (f'<div class="callout" style="background:{c["tint"]};border-color:{c["accent"]}80;color:{c["text"]}">'
                     f'<strong>{CALLOUT_LABEL[lang][kind]}</strong>{inline(text)}</div>')
        count += 1
        sections.append((sid, cls, body))
        for todo in SHOT.findall(raw):
            count += 1
            sections.append((sid + "s", "slide screenshot", screenshot(todo)))
        for v in visuals:
            count += 1
            if v.startswith("assets/screenshots/"):
                sections.append((sid + "b", "slide screenshot", f'<img src="{image_uri(v)}" alt="Screenshot">'))
            else:
                sections.append((sid + "b", "slide diagram", f'<img src="{image_uri(v)}" alt="Diagram">'))

    total = len(sections)
    label = lesson_names(lesson, lang)[0]
    pages = "".join(
        f'<section class="{cls}" data-id="{sid}">{body}'
        f'<div class="footer"><span>{label}</span><span>{sid} · {n}/{total}</span></div></section>'
        for n, (sid, cls, body) in enumerate(sections, 1)
    )
    css = BASE_CSS.replace("{FONTS}", font_css()) + SLIDE_CSS + COURSE.get("slide_css", "")
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>Slides</title>'
            f"<style>{css}</style></head><body>{pages}<script>{FIT_JS}</script></body></html>")


# ---------------------------------------------------------------- book

BOOK_CSS = f"""
@page {{ size: A4; margin: 24mm 20mm 22mm 20mm;
  @top-left {{ content: var-kicker; width: 50%; font-family: 'Google Sans Khmer', '{SANS}', sans-serif; font-size: 8.5pt; line-height: 14pt; color: {L['text-muted']};
    vertical-align: bottom; padding-bottom: 2.5mm; margin-bottom: 4mm; border-bottom: 1px solid {L['text-muted']}; }}
  @top-right {{ content: var-title; width: 50%; font-family: 'Google Sans Khmer', '{SANS}', sans-serif; font-size: 8.5pt; line-height: 14pt; color: {L['text-muted']};
    vertical-align: bottom; padding-bottom: 2.5mm; margin-bottom: 4mm; border-bottom: 1px solid {L['text-muted']}; }}
  @bottom-left {{ content: var-author; width: 50%; font-family: 'Google Sans Khmer', '{SANS}', sans-serif; font-size: 8.5pt; line-height: 14pt; color: {L['text-muted']};
    vertical-align: top; padding-top: 2.5mm; margin-top: 4mm; border-top: 1px solid {L['text-muted']}; }}
  @bottom-right {{ content: var-page; width: 50%; font-family: 'Google Sans Khmer', '{SANS}', sans-serif; font-size: 8.5pt; line-height: 14pt; color: {L['text-muted']};
    vertical-align: top; padding-top: 2.5mm; margin-top: 4mm; border-top: 1px solid {L['text-muted']}; }} }}
body {{ font-size: 10.5pt; line-height: 1.75; }}
@page front {{ counter-increment: page 0;
  @top-left {{ content: none; border: 0; }} @top-right {{ content: none; border: 0; }}
  @bottom-left {{ content: none; border: 0; }} @bottom-right {{ content: none; border: 0; }} }}
.cover, .toc {{ page: front; }}
.cover {{ height: 245mm; display: flex; flex-direction: column; justify-content: center; break-after: page; }}
.cover img {{ height: 22mm; align-self: flex-start; margin-bottom: 14mm; }}
.cover .kicker {{ font-size: 13pt; color: {L['primary']}; font-weight: 700; }}
.cover h1 {{ font-size: 34pt; line-height: 1.3; margin: 3mm 0 6mm; }}
.cover .sub {{ font-size: 12pt; color: {L['text-muted']}; }}
.cover .byline {{ font-size: 11pt; margin-top: 12mm; color: {L['text']}; }}
.toc {{ break-after: page; }}
.toc h2 {{ margin-top: 0; }}
.toc ol {{ list-style: none; padding: 0; columns: 1; }}
.toc li {{ padding: 1.2mm 0; border-bottom: 1px solid {L['border']}; }}
.toc a {{ display: flex; justify-content: space-between; gap: 6mm; color: inherit; text-decoration: none; }}
.toc .num {{ flex: none; color: {L['text-muted']}; }}
h1 {{ font-size: 24pt; line-height: 1.35; margin: 0 0 4mm; }}
h2 {{ font-size: 15.5pt; line-height: 1.4; margin: 9mm 0 2.5mm; color: {L['primary']}; break-after: avoid; }}
p {{ margin: 0 0 2.6mm; orphans: 3; widows: 3; }}
html[lang=km] p:not(.label) {{ text-indent: 2em; }}  /* Khmer books indent the first line of each paragraph */
ul, ol {{ margin: 0 0 3mm; padding-left: 6mm; }}
li {{ margin-bottom: 1mm; }}
hr {{ border: 0; border-top: 1px solid {L['border']}; margin: 7mm 0; }}
pre {{ font-size: 8.8pt; margin: 2mm 0 3mm; break-inside: avoid; }}
pre.code + p {{ margin-top: 3mm; }}
p:has(+ pre), p:has(+ ul), p:has(+ ol), p:has(+ table) {{ break-after: avoid; }}  /* keep a label with what it introduces */
pre.long {{ break-inside: auto; }}  /* a long program may split, instead of leaving half a page empty */
blockquote {{ margin: 2mm 0 3mm; padding: 2mm 4mm; background: {CO['warning']['tint']}; border-left: 1mm solid {CO['warning']['accent']}80;
  color: {CO['warning']['text']}; font-size: 9.5pt; break-inside: avoid; }}
table {{ font-size: 9.3pt; margin: 2mm 0 4mm; break-inside: avoid; }}
thead {{ display: table-header-group; }}
.figure {{ margin: 3mm 0 4mm; text-align: center; break-inside: avoid; }}
.shot-box {{ display: flex; align-items: center; justify-content: center; text-align: center; border: 2px dashed {L['text-muted']};
  background: {L['surface']}; color: {L['text-muted']}; }}
.shot-box > div {{ padding: 0 6%; }}
.shot-box strong {{ display: block; color: {L['text']}; margin-bottom: .4em; }}
.shot-box p {{ margin: .2em 0; line-height: 1.4; }}
.shot-box p.dev {{ font-size: .85em; }}
.shot-box code {{ display: inline-block; margin-top: .7em; font-size: .8em; background: none; }}
.figure .shot-box {{ margin: 0 auto; font-size: 9pt; }}
.figure .shot-box.wide {{ width: 88%; aspect-ratio: 16 / 9; }}
.figure .shot-box.phone {{ width: 36%; aspect-ratio: 9 / 18; }}
.figure img.shot-img {{ max-width: 100%; max-height: 120mm; }}
.credits {{ margin-top: 9mm; font-size: 8.5pt; color: {L['text-muted']}; border-top: 1px solid {L['border']}; padding-top: 3mm; }}
"""


def build_book(source, lang, kicker, title, subtitle="", note="", pages=None):
    items = blocks(source.read_text(), base=source.parent)
    if items and items[0][0] == "h1":
        items = items[1:]
    if items and items[0][0] == "quote":  # the "Covers chapter N" note is for us, not learners
        items = items[1:]
    # Each topic heading gets an id, so its line on the contents page can link to it.
    numbered, toc, n = [], "", 0
    for kind, value in items:
        if kind == "h2":
            label = re.sub(r"</?h2>", "", value)
            number = ""
            if pages:
                number = str(pages[n]).translate(KHMER_DIGITS) if lang == "km" else str(pages[n])
            toc += f'<li><a href="#topic-{n}"><span>{label}</span><span class="num">{number}</span></a></li>'
            value = f'<h2 id="topic-{n}">{label}</h2>'
            n += 1
        numbered.append((kind, value))
    items = numbered
    toc_title = "Contents" if lang == "en" else "មាតិកា"
    body = "".join(v for _, v in items)
    def css_text(text):
        return '"' + text.replace('"', '\\"') + '"'

    page_label = '"ទំព័រ " counter(page, khmer)' if lang == "km" else '"Page " counter(page)'
    running = (BOOK_CSS.replace("var-kicker", css_text(kicker)).replace("var-title", css_text(title))
               .replace("var-author", css_text(AUTHOR[lang])).replace("var-page", page_label))
    credit = COURSE["credit"]
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{html.escape(title)}</title>'
            f'<style>{BASE_CSS.replace("{FONTS}", font_css())}{running}{COURSE.get("book_css", "")}</style></head><body>'
            f'<div class="cover">{course_logo("logo_light", plain=True)}<div class="kicker">{kicker}</div><h1>{title}</h1>'
            f'<div class="sub">{subtitle}</div><div class="byline">{byline(lang)}</div></div>'
            f'<div class="toc"><h2>{toc_title}</h2><ol>{toc}</ol></div>'
            f'{body}{note}<div class="credits">{credit}</div></body></html>')


# ---------------------------------------------------------------- printing

def chrome(*args):
    return subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check",
                           "--allow-file-access-from-files", *args],
                          capture_output=True, text=True, timeout=180)


def to_pdf(page, pdf, wait=4000):
    chrome(f"--virtual-time-budget={wait}", "--no-pdf-header-footer", "--generate-pdf-document-outline", f"--print-to-pdf={pdf}", page.as_uri())
    pages = len(re.findall(rb"/Type\s*/Page[^s]", pdf.read_bytes()))
    print(f"wrote {pdf.relative_to(ROOT)}  {pages} pages, {pdf.stat().st_size // 1024} KB")


OUTLINE_JS = """
ObjC.import('PDFKit');
function run(argv) {
  const doc = $.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(argv[0]));
  const out = [];
  function walk(node, depth) {
    for (let i = 0; i < node.numberOfChildren; i++) {
      const c = node.childAtIndex(i);
      out.push([depth, doc.indexForPage(c.destination.page)]);
      walk(c, depth + 1);
    }
  }
  walk(doc.outlineRoot, 0);
  return JSON.stringify(out);
}
"""


def topic_pages(pdf):
    """Printed page number of each topic heading, read from the outline Chrome puts in the PDF."""
    done = subprocess.run(["osascript", "-l", "JavaScript", "-e", OUTLINE_JS, str(pdf)], capture_output=True, text=True, timeout=120)
    if done.returncode != 0:
        raise SystemExit(f"could not read the outline of {pdf}: {done.stderr}")
    # Depth 0 is the title. Depth 1 is the contents heading, then every topic. The first topic is Page 1.
    indexes = [int(page) for depth, page in json.loads(done.stdout) if depth == 1][1:]
    return [i - indexes[0] + 1 for i in indexes]


def book_pdf(out, name, *args):
    """Print twice: the first print shows where each topic lands, the second adds those page numbers."""
    page, pdf = out / f"{name}.html", out / f"{name}.pdf"
    numbers = None
    for _ in range(3):
        write_html(page, build_book(*args, pages=numbers))
        chrome("--virtual-time-budget=4000", "--no-pdf-header-footer", "--generate-pdf-document-outline", f"--print-to-pdf={pdf}", page.as_uri())
        found = topic_pages(pdf)
        if found == numbers:
            break
        numbers = found
    else:
        raise SystemExit(f"page numbers did not settle for {pdf}")
    print(f"wrote {pdf.relative_to(ROOT)}  {numbers[-1]} content pages, {len(numbers)} topics, {pdf.stat().st_size // 1024} KB")


# ---------------------------------------------------------------- full book

COVER_PHOTO = "assets/photos/angkor-wat-sunrise.jpg"  # each course's cover art is made from it by cover_art()
PHOTO_CREDIT = ("Cover photo: \u201cSiem Reap Reflections (CAMBODIA-REFLECTION-ANGKOR WAT) III\u201d by Chi King, "
                "CC BY 2.0 (creativecommons.org/licenses/by/2.0), via Wikimedia Commons. Colors changed to blue.")
# Headings that every lesson has. The full contents page leaves them out, so it lists only the real topics.
SAME_IN_EVERY_LESSON = ("What You Will Learn", "Before You Start", "Common Mistakes", "Summary", "Check Your Understanding", "Practice",
                        "អ្វីដែលអ្នកនឹងរៀន", "មុនពេលចាប់ផ្ដើម", "កំហុសដែល", "សង្ខេប", "ពិនិត្យការយល់ដឹង", "លំហាត់អនុវត្ត")
FULL_CSS_TEMPLATE = f"""
.toc.full ol {{ columns: 2; column-gap: 10mm; font-size: 9pt; }}
.toc.full li {{ padding: 0.8mm 0 0.8mm 4mm; break-inside: avoid; }}
.toc.full li.chapter {{ padding-left: 0; margin-top: 3mm; font-weight: 700; color: {L['primary']}; break-after: avoid; border-bottom-color: {L['primary']}; }}
.toc.full li.chapter:first-child {{ margin-top: 0; }}
.intro {{ page: front; break-after: page; }}
.intro h2 {{ margin-top: 0; }}
.chapter {{ break-before: page; }}

/* The book cover: one full page, edge to edge. A light page in the course's color, the title, a checklist,
   the course icon, and a toned photo of Angkor Wat at the bottom that fades into the page. */
@page cover {{ margin: 0; counter-increment: page 0;
  @top-left {{ content: none; border: 0; }} @top-right {{ content: none; border: 0; }}
  @bottom-left {{ content: none; border: 0; }} @bottom-right {{ content: none; border: 0; }} }}
.bookcover {{ page: cover; position: relative; overflow: hidden; width: 210mm; height: 297mm; margin-bottom: -1mm; break-after: page;
  background: linear-gradient(170deg, @@page0@@ 0%, @@page1@@ 60%, @@page2@@ 100%); color: @@text@@; font-family: '{SANS}', 'Google Sans Khmer', sans-serif; }}
.bookcover .shape {{ position: absolute; transform: rotate(45deg); }}
.bookcover .photo {{ position: absolute; left: 0; bottom: 0; width: 210mm; height: 128mm; }}
.bookcover .icon {{ position: absolute; right: 20mm; top: 92mm; width: 66mm; filter: drop-shadow(0 6mm 8mm @@glow@@); }}
.bookcover .text {{ position: absolute; left: 20mm; top: 24mm; right: 20mm; }}
.bookcover h1 {{ margin: 0; color: @@text@@; }}
.bookcover h1 .first {{ display: block; font-size: 104pt; font-weight: 800; line-height: .92; letter-spacing: -.035em; }}
.bookcover h1 .second {{ display: block; font-size: 44pt; font-weight: 800; line-height: 1.1; letter-spacing: -.02em; margin-top: 2mm; }}
.bookcover h1 .second:lang(km) {{ font-size: 36pt; line-height: 1.5; letter-spacing: 0; font-weight: 700; }}
.bookcover .badge {{ display: inline-block; margin-top: 6mm; background: @@accent@@; color: #fff; font-size: 15pt; font-weight: 600; padding: 2.2mm 7mm; border-radius: 6mm; }}
.bookcover .points {{ margin-top: 12mm; font-size: 12.5pt; font-weight: 500; max-width: 98mm; }}  /* wraps before the icon, which starts 124 mm from the left */
.bookcover .points div {{ display: flex; align-items: center; gap: 4mm; margin-bottom: 4mm; }}
.bookcover .tick {{ flex: none; width: 8mm; height: 8mm; border-radius: 50%; background: @@accent@@; display: inline-flex; align-items: center; justify-content: center; }}
.bookcover .author {{ position: absolute; right: 20mm; bottom: 12mm; font-size: 16pt; font-weight: 700; color: #fff; letter-spacing: .03em; }}
.bookcover .author[lang=km] {{ letter-spacing: 0; }}
.bookcover .label {{ display: inline-block; font-size: 12pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: @@accent@@; border-bottom: .8mm solid @@accent@@; padding-bottom: 1mm; margin-bottom: 5mm; }}
.bookcover .label:lang(km) {{ letter-spacing: 0; text-transform: none; font-size: 13pt; }}
.bookcover .badge.pill {{ margin-left: 3mm; background: transparent; color: @@accent@@; box-shadow: inset 0 0 0 .6mm @@accent@@; }}
.bookcover h1 .second small.inline {{ font-size: .5em; font-weight: 600; color: @@accent@@; letter-spacing: 0; margin-left: 2mm; vertical-align: .35em; }}
.bookcover .caption {{ position: absolute; left: 20mm; bottom: 11.5mm; max-width: 112mm; color: #fff; text-shadow: 0 .3mm 2.2mm rgba(0,0,0,.7); }}
.bookcover .caption b {{ display: block; font-size: 12.5pt; font-weight: 700; line-height: 1.3; }}
.bookcover .caption span {{ display: block; font-size: 8.5pt; font-weight: 500; line-height: 1.4; margin-top: .6mm; }}
.bookcover .icons {{ position: absolute; right: 20mm; top: 98mm; display: flex; gap: 6mm; filter: drop-shadow(0 6mm 8mm @@glow@@); }}
.bookcover .icons img {{ height: 46mm; }}

/* The opening page of each section: no header or footer, but it counts as a page. */
@page divider {{
  @top-left {{ content: none; border: 0; }} @top-right {{ content: none; border: 0; }}
  @bottom-left {{ content: none; border: 0; }} @bottom-right {{ content: none; border: 0; }} }}
.divider {{ page: divider; break-after: page; padding-top: 30mm; }}
.divider .big {{ font-size: 110pt; line-height: 1; font-weight: 700; color: {L['primary']}; opacity: .22; margin-bottom: 5mm; }}
.divider h1 {{ font-size: 32pt; line-height: 1.3; margin: 0 0 3mm; position: relative; }}
.divider h1 .kicker {{ display: block; font-size: 13pt; color: {L['primary']}; font-weight: 700; margin-bottom: 1mm; }}
.divider .rule {{ width: 30mm; height: 1.5mm; background: {L['primary']}; margin: 6mm 0 10mm; }}
.divider .inside {{ font-size: 9pt; font-weight: 700; letter-spacing: .08em; text-transform: uppercase; color: {L['text-muted']}; margin-bottom: 2mm; }}
.divider ol {{ list-style: none; padding: 0; margin: 0; font-size: 10pt; }}
.divider ol.two {{ columns: 2; column-gap: 10mm; font-size: 9pt; }}
.divider li {{ padding: 1.3mm 0; border-bottom: 1px solid {L['border']}; break-inside: avoid; margin: 0; }}
.divider li a {{ display: flex; justify-content: space-between; gap: 5mm; color: inherit; text-decoration: none; }}
.divider li .num {{ flex: none; color: {L['text-muted']}; }}

/* References at the end of the book. */
.back {{ break-before: page; page: back; }}
.back h2 {{ margin-top: 0; font-size: 22pt; color: {L['text']}; }}
.back h3 {{ font-size: 12pt; color: {L['primary']}; margin: 7mm 0 2mm; }}
.back ul {{ list-style: none; padding: 0; }}
.back li {{ padding: 1.6mm 0; border-bottom: 1px solid {L['border']}; margin: 0; overflow-wrap: anywhere; }}
"""


DARK_COVER_CSS = """
/* The dark cover: a navy page with rings and a glow (made by dark_cover_art()),
   the title in white at the top left, and the course icon at the top right, clear of the monument.
   The glow and rings are baked into an image by dark_cover_art(), because Chrome's PDF output draws big glows in tiles. */
.bookcover.dark { background: #0B0E1C; color: #fff; }
.bookcover.dark .bg { position: absolute; left: 0; top: 0; width: 210mm; height: 297mm; }
.bookcover.dark h1, .bookcover.dark h1 .first { color: #fff; }
.bookcover.dark h1 .second { color: #F6A58E; }
.bookcover.dark .badge { background: @@accent@@; border-radius: 0; }
.bookcover.dark .icon { left: auto; right: 20mm; top: 22mm; width: 34mm; filter: none; }
.bookcover.dark .points { position: absolute; left: 20mm; bottom: 26mm; margin: 0; color: #F2F4FA; }
.bookcover.dark .tick { background: @@accent@@; }
.bookcover.dark .author { bottom: 14mm; }
"""


GRID_COVER_CSS = """
/* The grid cover: a graphite page, a memory dump along the bottom, and the logos on a clear area (they must not overlap other art). */
.bookcover.grid { background: #12171C; color: #fff; }
.bookcover.grid .bg { position: absolute; left: 0; top: 0; width: 210mm; height: 297mm; }
.bookcover.grid h1, .bookcover.grid h1 .first { color: #fff; }
.bookcover.grid h1 .second { color: #4FD1C5; }
.bookcover.grid .badge { background: @@accent@@; border-radius: 0; }
.bookcover.grid .points { position: absolute; left: 20mm; top: 118mm; margin: 0; width: 108mm; color: #DCE5E6; }
.bookcover.grid .tick { background: @@accent@@; border-radius: 0; }
.bookcover.grid .marks { position: absolute; right: 20mm; top: 116mm; display: flex; gap: 6mm; align-items: center; }
.bookcover.grid .marks img { position: static; display: block; width: 26mm; height: auto; }
.bookcover.grid .author { bottom: 11mm; }
"""


MOTIF_COVER_CSS = """
/* The motif cover: a page in the course's own color, a pattern drawn for the course (baked into an image by
   motif_cover_art()), and the course marks on a clear area, so no logo overlaps the art. */
.bookcover.motif { background: @@bg@@; color: @@ink@@; }
.bookcover.motif .bg { position: absolute; left: 0; top: 0; width: 210mm; height: 297mm; }
.bookcover.motif h1, .bookcover.motif h1 .first { color: @@ink@@; }
.bookcover.motif h1 .first { font-size: @@size@@; }
.bookcover.motif h1 .second { color: @@second@@; }
.bookcover.motif .badge { background: @@accent@@; color: @@badge-ink@@; border-radius: 0; }
.bookcover.motif .points { position: absolute; left: 20mm; top: 122mm; margin: 0; width: 112mm; color: @@ink@@; opacity: .9; }
.bookcover.motif .tick { background: @@accent@@; border-radius: 0; }
.bookcover.motif .marks { position: absolute; right: 20mm; top: 120mm; display: flex; gap: 6mm; align-items: center; }
.bookcover.motif .marks img { position: static; display: block; width: 26mm; height: auto; }
.bookcover.motif .author { bottom: 11mm; @@author-side@@: 20mm; @@author-other@@: auto; color: @@author@@; }
"""


def full_css():
    c = COURSE["cover"]
    if c.get("style") == "motif":
        css = FULL_CSS_TEMPLATE.replace("@@page0@@", c["bg"]).replace("@@page1@@", c["bg"]).replace("@@page2@@", c["bg"]) \
            .replace("@@text@@", c["ink"]).replace("@@glow@@", "transparent").replace("@@accent@@", c["accent"]) + MOTIF_COVER_CSS
        for key, value in {"bg": c["bg"], "ink": c["ink"], "second": c["second"], "accent": c["accent"], "size": c.get("size", "104pt"),
                           "badge-ink": c.get("badge_ink", "#fff"), "author": c.get("author", c["ink"]),
                           "author-side": c.get("author_side", "left"), "author-other": "left" if c.get("author_side") == "right" else "right"}.items():
            css = css.replace(f"@@{key}@@", value)
        return css
    if c.get("style") == "grid":
        return FULL_CSS_TEMPLATE.replace("@@page0@@", "#000").replace("@@page1@@", "#000").replace("@@page2@@", "#000") \
            .replace("@@text@@", "#fff").replace("@@glow@@", "transparent").replace("@@accent@@", c["accent"]) \
            + GRID_COVER_CSS.replace("@@accent@@", c["accent"])
    if c.get("style") == "dark":
        return FULL_CSS_TEMPLATE.replace("@@page0@@", "#000").replace("@@page1@@", "#000").replace("@@page2@@", "#000") \
            .replace("@@text@@", "#fff").replace("@@glow@@", "transparent").replace("@@accent@@", c["accent"]) \
            + DARK_COVER_CSS.replace("@@accent@@", c["accent"])
    values = {"page0": c["page"][0], "page1": c["page"][1], "page2": c["page"][2], "text": c["text"], "accent": c["accent"], "glow": c["glow"]}
    css = FULL_CSS_TEMPLATE
    for name, value in values.items():
        css = css.replace(f"@@{name}@@", value)
    if c.get("square"):  # the shapes set their corners inline, so this needs !important
        css += ".bookcover .badge, .bookcover .shape { border-radius: 0 !important; }"
    return css


def dark_cover_art():
    """The dark cover's background: a navy page, rings, and an orange glow around the place where the icon goes
    (the middle of the page, 160 mm from the top), as a PNG at 300 dpi."""
    art_path = COURSE["cover"]["art"]
    art = ROOT / art_path
    if art.exists():
        return art_path
    art.parent.mkdir(parents=True, exist_ok=True)
    w, h, mm = 2480, 3508, 2480 / 210
    cx, cy = 105 * mm, 160 * mm
    rings = "".join(f'<div class="r" style="width:{d * mm}px;height:{d * mm}px"></div>' for d in (110, 160, 215, 275, 345))
    page = OUT / f"cover-art-{COURSE['folder']}.html"  # one per course, so covers can be made in parallel
    OUT.mkdir(exist_ok=True)
    page.write_text(f"""<!doctype html><html><head><style>html,body{{margin:0}}
.a{{position:relative;width:{w}px;height:{h}px;overflow:hidden;
  background:radial-gradient(ellipse {150 * mm}px {170 * mm}px at {cx}px {cy}px,#2E1A22 0%,#151A2E 50%,#090C18 100%)}}
.a div{{position:absolute;left:{cx}px;top:{cy}px;transform:translate(-50%,-50%);border-radius:50%}}
.a .r{{border:{0.35 * mm}px solid rgba(255,255,255,.07)}}
.a .g{{width:{200 * mm}px;height:{200 * mm}px;background:radial-gradient(circle,rgba(240,81,56,.75) 0%,rgba(240,81,56,.32) 22%,rgba(240,81,56,.10) 42%,rgba(240,81,56,0) 62%)}}
</style></head><body><div class="a"><div class="g"></div>{rings}</div></body></html>""")
    chrome("--hide-scrollbars", "--virtual-time-budget=4000", f"--window-size={w},{h}", f"--screenshot={art}", page.as_uri())
    page.unlink()
    print(f"wrote {art.relative_to(ROOT)}")
    return art_path


def grid_cover_art():
    """The grid cover's background: a graphite page with a memory dump along the bottom, as a PNG at 300 dpi.
    One row spells MINA COFFEE in hexadecimal, in teal. It is the same on every build."""
    art_path = COURSE["cover"]["art"]
    art = ROOT / art_path
    if art.exists():
        return art_path
    art.parent.mkdir(parents=True, exist_ok=True)
    w, h, mm = 2480, 3508, 2480 / 210
    message = "MINA COFFEE".encode().hex(" ").upper().split()
    value = 41
    rows = ""
    for row in range(9):
        address = f"0x{0x7FF0 + row * 16:04X}"
        cells = ""
        for col in range(11):
            value = (value * 137 + 61) % 256
            if row == 4:
                cells += f'<b class="on">{message[col]}</b>'
            else:
                cells += f"<b>{value:02X}</b>"
        rows += f'<div class="row"><i>{address}</i>{cells}</div>'
    font = asset_url("assets/fonts/source-code-pro/web/SourceCodePro-Regular.woff2")
    page = OUT / f"cover-art-{COURSE['folder']}.html"  # one per course, so covers can be made in parallel
    OUT.mkdir(exist_ok=True)
    page.write_text(f"""<!doctype html><html><head><style>@font-face{{font-family:SCP;src:url({font})}}
html,body{{margin:0;background:#12171C}}
.a{{position:absolute;left:0;top:{165 * mm}px;width:{w}px;height:{h - 165 * mm}px;overflow:hidden;padding-left:{20 * mm}px;box-sizing:border-box;
  -webkit-mask-image:linear-gradient(180deg,transparent 0%,#000 16%)}}
.row{{display:flex;gap:{2 * mm}px;margin-bottom:{2 * mm}px;font:{5 * mm}px SCP;align-items:center}}
i{{font-style:normal;color:#55676F;width:{27 * mm}px}}
b{{font-weight:400;color:#6F8088;background:#1C242B;width:{11.4 * mm}px;height:{9.4 * mm}px;display:flex;align-items:center;justify-content:center}}
b.on{{background:#0B7A75;color:#fff}}</style></head><body><div class="a">{rows}</div></body></html>""")
    chrome("--hide-scrollbars", "--allow-file-access-from-files", "--virtual-time-budget=4000", f"--window-size={w},{h}", f"--screenshot={art}", page.as_uri())
    page.unlink()
    print(f"wrote {art.relative_to(ROOT)}")
    return art_path


def motif_cover_art():
    """The motif cover's background: the course's own pattern (HTML from course_themes.py), as a PNG at 300 dpi."""
    c = COURSE["cover"]
    art = ROOT / c["art"]
    if art.exists():
        return c["art"]
    art.parent.mkdir(parents=True, exist_ok=True)
    w, h, mm = 2480, 3508, 2480 / 210
    page = OUT / f"cover-art-{COURSE['folder']}.html"  # one per course, so covers can be made in parallel
    OUT.mkdir(exist_ok=True)
    page.write_text(f"""<!doctype html><html><head><style>html,body{{margin:0;background:{c['bg']}}}
.a{{position:relative;width:{w}px;height:{h}px;overflow:hidden}}</style></head><body><div class="a">{c['motif'](w, h, mm)}</div></body></html>""")
    chrome("--hide-scrollbars", "--allow-file-access-from-files", "--virtual-time-budget=4000", f"--window-size={w},{h}", f"--screenshot={art}", page.as_uri())
    page.unlink()
    print(f"wrote {art.relative_to(ROOT)}")
    return c["art"]


def cover_art():
    """The cover photo, blue-toned and fading into the page at the top, as a PNG with transparency.
    Chrome's PDF output does not apply CSS blend modes and masks reliably, but a screenshot does,
    so the effects are baked into an image once. It also adds a soft dark glow behind the author's name."""
    art_path, (light, dark) = COURSE["cover"]["art"], COURSE["cover"]["tint"]
    source, position = COURSE["cover"].get("photo", COVER_PHOTO), COURSE["cover"].get("photo_pos", "center 20%")
    fade = COURSE["cover"].get("fade", "transparent 0%,#000 22%")  # how the photo fades into the page at its top
    art = ROOT / art_path
    if art.exists() and art.stat().st_mtime > (ROOT / source).stat().st_mtime:
        return art_path
    w, h = 2480, 1512  # 210 x 128 mm at 300 dpi
    page = OUT / f"cover-art-{COURSE['folder']}.html"  # one per course, so covers can be made in parallel
    OUT.mkdir(exist_ok=True)
    page.write_text(f"""<!doctype html><html><head><style>html,body{{margin:0;background:transparent}}
.a{{position:relative;width:{w}px;height:{h}px;overflow:hidden;
  -webkit-mask-image:linear-gradient(180deg,{fade})}}
.a div{{position:absolute;inset:0}}</style></head><body><div class="a"><div style="background:{light}">
<div style="background:url(../{source}) {position}/cover;filter:grayscale(1) contrast(1.2) brightness(1.2);mix-blend-mode:multiply"></div>
<div style="background:{dark};mix-blend-mode:lighten"></div></div>
<div style="background:radial-gradient(ellipse 520px 170px at {w - 480}px {h - 175}px,rgba(5,12,30,.6),rgba(5,12,30,0))"></div>
</div></body></html>""")
    chrome("--hide-scrollbars", "--default-background-color=00000000", "--virtual-time-budget=4000",
           f"--window-size={w},{h}", f"--screenshot={art}", page.as_uri())
    page.unlink()
    print(f"wrote {art.relative_to(ROOT)}")
    return art_path


def build_full_book(lang, pages=None):
    """All lessons in one book: one cover, one contents page, and each lesson as a chapter."""
    lessons = [d for d in sorted(sections().iterdir())
               if d.is_dir() and (d / lang / "book.md").exists() and (d / lang / "slides.md").exists()]
    words = COURSE["text"][lang]
    count = 0

    def number():
        nonlocal count
        value = "" if not pages else str(pages[count])
        count += 1
        return value.translate(KHMER_DIGITS) if lang == "km" else value

    def css_text(text):
        return '"' + text.replace('"', '\\"') + '"'

    toc, chapters, named = "", [], ""
    for i, lesson in enumerate(lessons, 1):
        kicker, title = lesson_names(lesson, lang)
        section = kicker.split(" · ", 1)[1]
        source = lesson / lang / "book.md"
        items = blocks(source.read_text(), base=source.parent)
        if items and items[0][0] == "h1":
            items = items[1:]
        if items and items[0][0] == "quote":  # the "Covers chapter N" note is for us, not learners
            items = items[1:]
        toc += f'<li class="chapter"><a href="#ch-{i}"><span>{section}: {title}</span><span class="num">{number()}</span></a></li>'
        body, inside, topic = "", "", 0
        for kind, value in items:
            if kind == "h2":
                label = re.sub(r"</?h2>", "", value)
                entry = number()  # every heading keeps its place in the list of page numbers
                if not label.startswith(SAME_IN_EVERY_LESSON):  # the PDF bookmarks still list these
                    line = f'<li><a href="#ch-{i}-t{topic}"><span>{label}</span><span class="num">{entry}</span></a></li>'
                    toc += line
                    inside += line
                value = f'<h2 id="ch-{i}-t{topic}">{label}</h2>'
                topic += 1
            body += value
        big = str(i).translate(KHMER_DIGITS) if lang == "km" else str(i)
        columns = ' class="two"' if inside.count("<li>") > 14 else ""
        divider = (f'<div class="divider"><div class="big">{big}</div>'
                   f'<h1 id="ch-{i}"><span class="kicker">{section}</span>{title}</h1><div class="rule"></div>'
                   f'<div class="inside">{words["inside"]}</div><ol{columns}>{inside}</ol></div>')
        chapters.append(f'<section class="chapter ch-{i}">{divider}{body}</section>')
        # Each chapter is a named page, so the page header shows the chapter's name.
        named += f"@page ch{i} {{ @top-right {{ content: {css_text(section + ': ' + title)}; }} }}\n.ch-{i} {{ page: ch{i}; }}\n"

    back = ""
    refs_md = book_dir() / f"references.{lang}.md"
    if refs_md.exists():
        refs = blocks(refs_md.read_text(), base=refs_md.parent)
        heading = re.sub(r"</?h2>", "", refs[0][1])
        toc += f'<li class="chapter"><a href="#refs"><span>{heading}</span><span class="num">{number()}</span></a></li>'
        back = f'<section class="back"><h2 id="refs">{heading}</h2>' + "".join(v for _, v in refs[1:]) + "</section>"
        named += f"@page back {{ @top-right {{ content: {css_text(heading)}; }} }}\n"

    intro_md = book_dir() / f"how-to-use.{lang}.md"
    intro = "".join(v for _, v in blocks(intro_md.read_text(), base=intro_md.parent)) if intro_md.exists() else ""
    page_label = '"ទំព័រ " counter(page, khmer)' if lang == "km" else '"Page " counter(page)'
    running = (BOOK_CSS.replace("var-kicker", css_text(words["title"])).replace("var-title", '""')
               .replace("var-author", css_text(AUTHOR[lang])).replace("var-page", page_label))
    style = COURSE["cover"].get("style")
    photo = COURSE["cover"].get("photo_credit", None if style in ("dark", "grid", "motif") else PHOTO_CREDIT)
    credit = f'{COURSE["credit"]}<br>{photo}' if photo else COURSE["credit"]
    image = cover_png(lang)
    if image.exists():  # the approved cover, made by --cover
        cover = f'<div class="bookcover image"><img src="{image_uri(image.relative_to(ROOT))}" alt="" style="position:absolute;left:0;top:0;width:210mm;height:297mm"></div>'
    else:
        print(f"   no cover image {image.relative_to(ROOT)}: drawing the cover now (run --cover to make the image)")
        cover = cover_html(lang)
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{words["title"]}</title>'
            f'<style>{BASE_CSS.replace("{FONTS}", font_css())}{running}{COURSE.get("book_css", "")}{full_css()}{named}</style></head><body>'
            f'{cover}'
            f'<div class="toc full"><h2>{words["toc"]}</h2><ol>{toc}</ol></div>'
            f'<div class="intro">{intro}<div class="credits">{credit}</div></div>'
            f'{"".join(chapters)}{back}</body></html>')


def cover_png(lang):
    """Where the finished cover of the full book is kept, for example assets/covers/km/05-kotlin-cover.png."""
    return ROOT / "assets/covers" / lang / f'{COURSE["folder"]}-cover.png'


def build_cover(lang):
    """Draw the full book's cover and save it as an A4 image at 300 dpi. The book build only places this image,
    so a cover is changed and checked on its own (--cover), without building the book."""
    page = OUT / f'cover-{COURSE["folder"]}-{lang}.html'
    OUT.mkdir(exist_ok=True)
    page.write_text(f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{BASE_CSS.replace("{FONTS}", font_css())}'
                    f'{COURSE.get("book_css", "")}{full_css()}html,body{{margin:0}}</style></head><body>{cover_html(lang)}</body></html>')
    out = cover_png(lang)
    out.parent.mkdir(parents=True, exist_ok=True)
    chrome("--hide-scrollbars", "--force-device-scale-factor=3.125", "--virtual-time-budget=6000",
           "--window-size=794,1123", f"--screenshot={out}", page.as_uri())
    page.unlink()
    print(f"wrote {out.relative_to(ROOT)}")


def cover_html(lang):
    """The cover page as HTML, in the course's cover style."""
    words = COURSE["text"][lang]
    style = COURSE["cover"].get("style")
    dark = style == "dark"
    icon = image_uri(COURSE["icon"])
    # A wide icon (several logos) can be drawn larger, in mm; the checklist then wraps earlier, so the two never touch.
    width = COURSE["cover"].get("icon_width")
    icon_style = f' style="width:{width}mm"' if width else ""
    points_style = f' style="max-width:{210 - 20 - width - 26}mm"' if width else ""  # 20 mm margins on both sides, 6 mm gap
    if "logos" in COURSE and "honeycomb" not in COURSE["icon"]:
        points_style = ' style="max-width:74mm"'  # two logos side by side start about 100 mm from the left
    tick = ('<span class="tick"><svg viewBox="0 0 24 24" width="13" height="13"><path d="M5 12.5l4.5 4.5L19 7.5" stroke="#fff" '
            'stroke-width="3.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></span>')
    points = "".join(f"<div>{tick}<span>{p}</span></div>" for p in words["points"])
    title = (f'<h1><span class="first">{COURSE["name"]}</span><span class="second" lang="{"en" if words["second"].isascii() else lang}">{words["second"]}</span></h1>'
             f'<div class="badge" lang="{lang}">{words["badge"]}</div>')
    if style == "motif":
        marks = "".join(f'<img src="{image_uri(path)}" alt="">' for path in COURSE.get("logos", [COURSE["icon"]]))
        cover = (f'<div class="bookcover motif"><img class="bg" src="{image_uri(motif_cover_art())}" alt="">'
                 f'<div class="text">{title}</div><div class="points" lang="{lang}">{points}</div><div class="marks">{marks}</div>'
                 f'<div class="author" lang="{lang}">{AUTHOR[lang]}</div></div>')
    elif style == "grid":
        marks = "".join(f'<img src="{image_uri(path)}" alt="">' for path in COURSE["logos"])
        cover = (f'<div class="bookcover grid"><img class="bg" src="{image_uri(grid_cover_art())}" alt="">'
                 f'<div class="text">{title}</div><div class="points" lang="{lang}">{points}</div><div class="marks">{marks}</div>'
                 f'<div class="author" lang="{lang}">{AUTHOR[lang]}</div></div>')
    elif dark:
        cover = (f'<div class="bookcover dark"><img class="bg" src="{image_uri(dark_cover_art())}" alt="">'
                 f'<img class="icon" src="{icon}" alt="">'
                 f'<div class="text">{title}</div><div class="points" lang="{lang}">{points}</div>'
                 f'<div class="author" lang="{lang}">{AUTHOR[lang]}</div></div>')
    else:
        photo = image_uri(cover_art())
        fit = "white-space:nowrap"  # one line; the script below shrinks it to fit inside the margins
        label = COURSE["cover"].get("label", {}).get(lang)  # says what the book is for, such as "For mobile apps"
        style_of_label = COURSE["cover"].get("label_style", "above")  # above the title, inline, in the badge, or a pill
        name, note = COURSE["cover"].get("caption", {}).get(lang, (None, None))
        caption = f'<div class="caption" lang="{lang}"><b>{name}</b><span>{note}</span></div>' if name else ""
        cover = (f'<div class="bookcover">'
                 '<div class="shape" style="right:-75mm;top:-45mm;width:190mm;height:190mm;border-radius:10mm;background:linear-gradient(135deg,#ffffff00,#ffffffcc)"></div>'
                 '<div class="shape" style="left:-60mm;top:105mm;width:120mm;height:120mm;border-radius:8mm;background:#fff;opacity:.45"></div>'
                 f'<img class="photo" src="{photo}" alt="">'
                 + (f'<div class="icons">{"".join(f"<img src={chr(34)}{image_uri(p)}{chr(34)} alt={chr(34)}{chr(34)}>" for p in COURSE["logos"])}</div>'
                    if "logos" in COURSE and "honeycomb" not in COURSE["icon"] else f'<img class="icon" src="{icon}" alt=""{icon_style}>') +
                 '<div class="text">' + (f'<div class="label" lang="{lang}">{label}</div>' if label and style_of_label == "above" else "") +
                 f'<h1><span class="first" style="{fit}">{COURSE["name"]}</span><span class="second" lang="{"en" if words["second"].isascii() else lang}">{words["second"]}'
                 + (f' <small class="inline" lang="{lang}">{label}</small>' if label and style_of_label == "inline" else "") + '</span>'
                 '</h1>'
                 f'<div class="badge" lang="{lang}">{words["badge"] + (" · " + label if label and style_of_label == "badge" else "")}</div>'
                 + (f'<div class="badge pill" lang="{lang}">{label}</div>' if label and style_of_label == "pill" else "") +
                 f'<div class="points" lang="{lang}"{points_style}>{points}</div></div>'
                 f'{caption}<div class="author" lang="{lang}">{AUTHOR[lang]}</div></div>'
                 # Shrink each title line until it fits between the 20 mm margins, measured in the page itself,
                 # because letter widths differ from font to font.
                 '<script>document.fonts.ready.then(function () {'
                 ' document.querySelectorAll(".bookcover h1 span").forEach(function (s) {'
                 ' var room = s.parentNode.parentNode.clientWidth, size = parseFloat(getComputedStyle(s).fontSize);'
                 ' s.style.display = "inline-block"; s.style.whiteSpace = "nowrap";'
                 ' while (s.getBoundingClientRect().width > room && size > 10) { size -= 1; s.style.fontSize = size + "px"; }'
                 ' s.style.display = "block"; }); });</script>')
    return cover


def heading_pages(pdf, front):
    """Printed page number of each chapter and topic heading. The first `front` headings are the front matter."""
    done = subprocess.run(["osascript", "-l", "JavaScript", "-e", OUTLINE_JS, str(pdf)], capture_output=True, text=True, timeout=120)
    if done.returncode != 0:
        raise SystemExit(f"could not read the outline of {pdf}: {done.stderr}")
    indexes = [int(page) for depth, page in json.loads(done.stdout) if depth in (0, 1)][front:]
    return [i - indexes[0] + 1 for i in indexes]


def full_book_pdf(lang):
    """Print until the page numbers on the contents page match where each heading really lands."""
    full_out = OUT / COURSE["folder"] / COURSE.get("slug", COURSE["text"]["en"]["title"].lower().replace(" ", "-"))
    full_out.mkdir(parents=True, exist_ok=True)
    page, pdf = full_out / f"book-{lang}.html", full_out / f"book-{lang}.pdf"
    front = 3 if (book_dir() / f"how-to-use.{lang}.md").exists() else 2  # cover title, contents, how to use
    if cover_png(lang).exists():  # an image cover has no title heading
        front -= 1
    numbers = None
    for _ in range(4):
        write_html(page, build_full_book(lang, pages=numbers))
        chrome("--virtual-time-budget=8000", "--no-pdf-header-footer", "--generate-pdf-document-outline", f"--print-to-pdf={pdf}", page.as_uri())
        found = heading_pages(pdf, front)
        if found == numbers:
            break
        numbers = found
    else:
        raise SystemExit(f"page numbers did not settle for {pdf}")
    print(f"wrote {pdf.relative_to(ROOT)}  {numbers[-1]} content pages, {len(numbers)} headings, {pdf.stat().st_size // 1024} KB")



def course_key():
    return next(k for k, v in COURSES.items() if v is COURSE)


def sections():
    return ROOT / COURSE["folder"] / "sections"


def book_dir():
    return ROOT / COURSE["folder"] / "book"


def main():
    args = sys.argv[1:]
    if args and args[0] in COURSES:
        args.pop(0)  # the course; COURSE was set from it when the script started
    if args == ["--cover"]:
        for lang in ("en", "km"):
            build_cover(lang)
        return
    if args == ["--book"]:
        for lang in ("en", "km"):
            if any((d / lang / "book.md").exists() for d in sections().iterdir() if d.is_dir()):  # no lessons yet: no book
                full_book_pdf(lang)
        return
    wanted = args
    lessons = [d for d in sorted(sections().iterdir()) if (d / "en/slides.md").exists() and (not wanted or d.name in wanted)]
    if wanted and not lessons:
        sys.exit(f"No lesson named {', '.join(wanted)}. Name a course first, for example: dart or 01-dart.")
    problems = 0
    for lesson in lessons:
        out = OUT / COURSE["folder"] / lesson.name
        out.mkdir(parents=True, exist_ok=True)
        print(f"== {lesson.name}")
        for lang in ("en", "km"):
            if not (lesson / lang / "slides.md").exists():
                continue
            page = out / f"slides-{lang}.html"
            write_html(page, build_slides(lesson, lang))
            dom = chrome("--virtual-time-budget=9000", "--dump-dom", page.as_uri()).stdout
            report = re.search(r'data-report="([^"]*)"', dom)
            items = report.group(1).split() if report else ["REPORT-MISSING:overflow"]
            over = [x for x in items if x.endswith(":overflow")]
            small = [x for x in items if not x.endswith(":overflow") and float(x.split(":")[1]) < SMALLEST_OK]
            problems += len(over)
            print(f"   {lang} slides: {len(items)} shrunk, too small: {small or 'none'}, do not fit: {over or 'none'}")
            to_pdf(page, out / f"slides-{lang}.pdf", 9000)
        kicker, title = lesson_names(lesson, "en")
        book_pdf(out, "book-en", lesson / "en/book.md", "en", kicker, title)
        km_book = lesson / "km/book.md"
        if km_book.exists():
            kicker, title = lesson_names(lesson, "km")
            book_pdf(out, "book-km", km_book, "km", kicker, title)
    print(f"{len(lessons)} lesson(s), {problems} slide(s) do not fit")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()

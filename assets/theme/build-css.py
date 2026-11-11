"""Generate tokens.css from tokens.json. Run from the repo root:

    python3 assets/theme/build-css.py
"""
import json
import pathlib

here = pathlib.Path(__file__).parent
tokens = json.loads((here / "tokens.json").read_text())

lines = [
    "/* Generated from tokens.json by build-css.py. Do not edit by hand. */",
    "",
    "@font-face { font-family: 'Inter'; src: url('../fonts/inter/web/InterVariable.woff2') format('woff2'); font-weight: 100 900; font-style: normal; font-display: swap; }",
    "@font-face { font-family: 'Inter'; src: url('../fonts/inter/web/InterVariable-Italic.woff2') format('woff2'); font-weight: 100 900; font-style: italic; font-display: swap; }",
]
for weight, name in ((400, "Regular"), (500, "Medium"), (700, "Bold")):
    lines.append(f"@font-face {{ font-family: 'JetBrains Mono'; src: url('../fonts/jetbrains-mono/web/JetBrainsMono-{name}.woff2') format('woff2'); font-weight: {weight}; font-style: normal; font-display: swap; }}")
lines.append("@font-face { font-family: 'JetBrains Mono'; src: url('../fonts/jetbrains-mono/web/JetBrainsMono-Italic.woff2') format('woff2'); font-weight: 400; font-style: italic; font-display: swap; }")
# unicode-range limits Google Sans to Khmer characters, so Latin text keeps its own font.
lines.append("@font-face { font-family: 'Google Sans Khmer'; src: url('../fonts/google-sans/GoogleSans[GRAD,opsz,wght].ttf') format('truetype'); font-weight: 300 700; font-style: normal; font-display: swap; unicode-range: U+1780-17FF, U+19E0-19FF, U+200B-200D; }")
lines += ["", ":root {"]
lines.append(f"  --font-sans: '{tokens['font']['sans']}', system-ui, sans-serif;")
lines.append(f"  --font-mono: '{tokens['font']['mono']}', ui-monospace, monospace;")
lines.append(f"  --font-khmer: '{tokens['font']['khmer']}', '{tokens['font']['sans']}', sans-serif;")


def emit(prefix, group):
    for key, value in group.items():
        name = f"{prefix}-{key}"
        if isinstance(value, dict):
            emit(name, value)
        elif isinstance(value, list):
            for i, item in enumerate(value, 1):
                lines.append(f"  --{name}-{i}: {item};")
        elif key != "label":
            lines.append(f"  --{name}: {value};")


for group in ("light", "dark", "code", "callout", "diagram", "topic-accent"):
    emit(group, tokens[group])
lines += ["}", ""]

(here / "tokens.css").write_text("\n".join(lines))
print(f"wrote {here / 'tokens.css'}")

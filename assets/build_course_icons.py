"""Course marks for the courses that have no brand logo: Web Development (09) and the topic courses (11-20).

    python3 assets/build_course_icons.py

Each mark is a square tile in the course's color, with a Material Symbols icon (Apache License 2.0, see
icons/material-symbols/LICENSE) in white, scaled into the middle. Written to icons/courses/<course>.svg.
"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ICONS = HERE / "icons/material-symbols"
COURSES = {  # course: (Material Symbols icon, tile color, small corner square color)
    "ci-cd": ("sync", "#3E5C76", "#9BE15D"),
    "automated-testing": ("check_circle", "#6B3FA0", "#2FB36B"),
    "mobile-architecture": ("account_tree", "#1F5F9E", "#BFE0FF"),
    "mobile-security": ("shield", "#B3123A", "#1A0A0F"),
    "observability": ("monitoring", "#4F6B00", "#A3D139"),
    "performance": ("speed", "#D9480F", "#FFC078"),
    "release-engineering": ("rocket_launch", "#1C2B4A", "#C8102E"),
    "data-networking": ("cloud_sync", "#D2462A", "#101828"),
    "accessibility-localization": ("accessibility", "#1A4FD6", "#FFD500"),
    "developer-workflow": ("fork_right", "#5B3FC4", "#F0B429"),
    "web-development": ("language", "#B0204F", "#7DE2D1"),
    "security-fundamentals": ("shield", "#0E2A5A", "#F2A541"),
}
out = HERE / "icons/courses"
out.mkdir(parents=True, exist_ok=True)
for course, (icon, color, corner) in COURSES.items():
    path = re.search(r'<path d="([^"]+)"', (ICONS / f"{icon}.svg").read_text()).group(1)
    (out / f"{course}.svg").write_text(
        '<svg xmlns="http://www.w3.org/2000/svg" width="240" height="240" viewBox="0 0 240 240">'
        f'<rect width="240" height="240" fill="{color}"/><rect x="196" y="0" width="44" height="44" fill="{corner}"/>'
        f'<g transform="translate(40 200) scale(0.1667)"><path d="{path}" fill="#FFFFFF"/></g></svg>')
print("wrote", len(COURSES), "course marks")

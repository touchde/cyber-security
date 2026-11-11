"""Generate the Android course's diagrams, in its green palette, into assets/diagrams/.

    python3 assets/build_android_diagrams.py

They are written to diagrams/06-android-development/.
"""
from diagram_kit import OUT, Kit

k = Kit(folder="06-android-development", primary="#1B7A44", tint="#EFF8EC", ink="#13241A", muted="#4F6356", line="#C9DFC0",
        sans="'Roboto', 'Helvetica Neue', Arial, sans-serif", mono="'Roboto Mono', Menlo, monospace", accent="#2FB86A")
MINT = "#E3FAEC"


def views_and_compose():
    b = [k.text(60, 140, "Views (XML): find the view, then change it", 22, k.primary, 700, "start"),
         k.node(60, 160, 300, 90, "activity_orders.xml", "a TextView with an id", "#FFFFFF"),
         k.node(400, 160, 300, 90, "findViewById", "get the TextView", "#FFFFFF"),
         k.node(740, 160, 300, 90, "ordersText.text = ...", "change it, every time", "#FFFFFF"),
         k.arrow(360, 205, 398, 205), k.arrow(700, 205, 738, 205),
         k.text(60, 285, "Every change to the data needs code that updates the right view.", 18, k.muted, 400, "start"),
         k.text(60, 360, "Compose: describe the screen from the state", 22, k.primary, 700, "start"),
         k.node(60, 380, 300, 100, "State", "orders = 3", MINT, "#2FB86A"),
         k.node(400, 380, 300, 100, "@Composable", "Text(\"Orders waiting: $orders\")", k.tint),
         k.node(740, 380, 300, 100, "Screen", "Orders waiting: 3", "#FFFFFF"),
         k.arrow(360, 430, 398, 430), k.arrow(700, 430, 738, 430),
         f'<path d="M210,480 L210,525 L890,525 L890,484" fill="none" stroke="{k.muted}" stroke-width="2.5" marker-end="url(#head)"/>',
         k.text(550, 552, "When the state changes, Compose calls the function again: this is recomposition.", 18, k.muted)]
    k.svg("views-and-compose", 1100, 590, "Two ways to build a screen", "The older View system changes views; Compose describes the screen", "".join(b))


def app_parts():
    b = [k.node(60, 130, 330, 95, "AndroidManifest.xml", "names the app and its activities", "#FFFFFF"),
         k.node(60, 260, 330, 95, "MainActivity", "an entry point: one screen", MINT, "#2FB86A"),
         k.node(60, 390, 330, 95, "setContent { }", "the Compose UI starts here", k.tint),
         k.arrow(225, 225, 225, 258), k.arrow(225, 355, 225, 388),
         k.node(470, 130, 270, 95, "Composables", "OrderBoard, Text, Column", k.tint),
         k.node(780, 130, 270, 95, "Resources", "strings, images, icons", "#FFFFFF"),
         k.node(470, 260, 580, 95, "Jetpack libraries (AndroidX)", "Compose, Activity, Navigation, Room, and more", "#FFFFFF"),
         k.node(470, 390, 580, 95, "Android SDK", "the platform: activities, files, network, sensors", "#FFFFFF"),
         k.arrow(392, 437, 468, 190),
         k.text(550, 540, "Gradle builds all of this into one APK or app bundle.", 19, k.ink, 700)]
    k.svg("app-parts", 1100, 580, "The parts of an Android app", "What Android Studio creates, and what it builds on", "".join(b))


for make in (views_and_compose, app_parts):
    make()
print("diagrams written")

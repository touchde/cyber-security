"""Generate the React Native course's diagrams, in its slate and cyan palette, into assets/diagrams/.

    python3 assets/build_react_native_diagrams.py

They are written to diagrams/10-react-native/.
"""
from diagram_kit import OUT, Kit

k = Kit(folder="10-react-native", primary="#0E6E8C", tint="#EBF7FB", ink="#15191F", muted="#525C66", line="#CDE6EE",
        sans="'Outfit', 'Helvetica Neue', Arial, sans-serif", mono="'Chivo Mono', Menlo, monospace", accent="#0E6E8C")
GREY = "#F3F4F6"


def how_it_works():
    b = [k.text(60, 135, "JavaScript side", 20, k.primary, 700, "start"), k.text(700, 135, "Native side", 20, k.ink, 700, "start"),
         k.node(60, 155, 360, 100, "Your components", "App.tsx: <View>, <Text>", k.tint),
         k.node(60, 300, 360, 100, "React", "works out what changed", k.tint),
         k.node(700, 155, 340, 100, "Native views", "a real Android or iOS view", GREY, k.muted),
         k.node(700, 300, 340, 100, "Native modules", "camera, storage, location", GREY, k.muted),
         k.arrow(240, 255, 240, 298),
         k.box(470, 225, 180, 110, "#FFFFFF", k.primary), k.text(560, 272, "JSI", 26, k.primary, 700), k.text(560, 302, "direct calls", 17, k.muted),
         k.arrow(420, 350, 468, 300), k.arrow(652, 260, 698, 205), k.arrow(652, 300, 698, 350, both=True),
         k.text(550, 470, "<Text> on Android becomes an Android text view; on iOS, an iOS text view.", 19, k.ink, 700),
         k.text(550, 500, "So the app looks and feels native, from one JavaScript codebase.", 18, k.muted)]
    k.svg("how-it-works", 1100, 540, "How React Native works", "Your JavaScript describes the screen; the system draws real native views", "".join(b))


def expo_go():
    b = [k.node(60, 160, 280, 110, "Your computer", "npx expo start (Metro)", k.tint),
         k.node(420, 160, 260, 110, "QR code", "the address of your code", "#FFFFFF"),
         k.node(760, 160, 290, 110, "Your phone", "Expo Go app", GREY, k.muted),
         k.arrow(340, 215, 418, 215), k.arrow(680, 215, 758, 215),
         f'<path d="M905,270 L905,330 L200,330 L200,274" fill="none" stroke="{k.muted}" stroke-width="2.5" marker-end="url(#head)" marker-start="url(#tail)"/>',
         k.text(552, 360, "Expo Go downloads your JavaScript from Metro, and runs it. Save a file, and the phone updates.", 18, k.muted),
         k.text(552, 420, "Phone and computer must be on the same Wi-Fi network.", 19, k.ink, 700)]
    k.svg("expo-go", 1100, 460, "Running your app with Expo Go", "No Android Studio or Xcode needed for the first steps", "".join(b))


for make in (how_it_works, expo_go):
    make()
print("diagrams written")

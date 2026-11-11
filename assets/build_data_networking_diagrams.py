"""Generate the Data and Networking course's diagrams, in its navy and coral palette, into assets/diagrams/.

    python3 assets/build_data_networking_diagrams.py

They are written to diagrams/18-data-networking/.
"""
from diagram_kit import Kit

k = Kit(folder="18-data-networking", primary="#C03A1F", tint="#FFF2EE", ink="#141B2B", muted="#566078", line="#F4D7CE",
        sans="'Nunito Sans', 'Helvetica Neue', Arial, sans-serif", mono="'Anonymous Pro', Menlo, monospace", accent="#C03A1F")


def request_path():
    b = [k.node(40, 170, 220, 110, "App", "the counter tablet", k.tint), k.node(840, 170, 220, 110, "Server", "the shop's menu", k.tint),
         k.text(550, 148, "across the network: Wi-Fi, providers, and more", 16, k.muted),
         k.arrow(262, 205, 838, 205), k.text(550, 192, "GET /menu/iced-latte", 19, k.ink, 700, True),
         f'<line x1="838" y1="250" x2="276" y2="250" stroke="{k.primary}" stroke-width="2.5"/>',
         f'<path d="M276,244 L262,250 L276,256 z" fill="{k.primary}"/>',
         k.text(550, 280, "200 OK + the iced latte as JSON", 17, k.primary, 700, True),
         k.text(40, 370, "1. The app sends a request: a method, a path, and headers.", 19, k.ink, 400, "start"),
         k.text(40, 402, "2. The server finds the data, and sends a response: a status code, headers, and a body.", 19, k.ink, 400, "start"),
         k.text(40, 434, "3. The app reads the body (JSON), and shows the price.", 19, k.ink, 400, "start"),
         k.text(40, 486, "Any step can fail, or be slow: the app must be ready for that.", 19, k.primary, 700, "start")]
    k.svg("request-path", 1100, 520, "The path of a request", "What happens when the counter app asks for a price", "".join(b))


def where_data_lives():
    rows = [("In memory", "fast; lost when the app closes", "the menu on screen right now"),
            ("On the device", "kept between launches; only this phone", "saved orders, a cached menu"),
            ("On the server", "shared by every app; needs the network", "the real menu, every sale")]
    b = []
    for i, (name, sub, example) in enumerate(rows):
        y = 130 + i * 120
        b += [k.node(40, y, 420, 95, name, sub, k.tint if i == 2 else "#FFFFFF"), k.text(490, y + 55, "e.g. " + example, 19, k.ink, 400, "start")]
    b.append(k.text(40, 520, "The server holds the true copy. The others are copies, and can be out of date.", 19, k.primary, 700, "start"))
    k.svg("where-data-lives", 1100, 560, "Where an app's data lives", "Three places, each with its own trade-offs", "".join(b))


for make in (request_path, where_data_lives):
    make()
print("wrote 2 diagrams")

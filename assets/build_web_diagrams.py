"""Generate the Web Development course's diagrams, in its aubergine and raspberry palette, into assets/diagrams/.

    python3 assets/build_web_diagrams.py

They are written to diagrams/09-web-development/.
"""
from diagram_kit import Kit

k = Kit(folder="09-web-development", primary="#B0204F", tint="#FBE9F0", ink="#1C1426", muted="#5E5366", line="#EED3DD",
        sans="'Geist', 'Helvetica Neue', Arial, sans-serif", mono="'Geist Mono', Menlo, monospace", accent="#B0204F")
MINT = "#E2F7F2"


def path_to_server():
    hops = [("Phone", "at Mina Coffee", MINT), ("Wi-Fi router", "the shop's network", "#FFFFFF"), ("Internet provider", "for example, a Cambodian ISP", "#FFFFFF"),
            ("The internet", "many networks, joined", k.tint), ("Data center", "the server", MINT)]
    b = []
    for i, (name, sub, fill) in enumerate(hops):
        x = 30 + i * 214
        b.append(k.node(x, 140, 184, 100, name, sub, fill))
        if i:
            b.append(k.arrow(x - 28, 190, x - 2, 190, both=True))
    b += [k.text(30, 300, "A request leaves the phone, crosses several networks, and reaches a server in a data center.", 19, k.ink, 700, "start"),
          k.text(30, 330, "The answer comes back the same way. Each step is a router that passes the data on.", 19, k.muted, 400, "start")]
    k.svg("path-to-a-server", 1100, 370, "From a phone to a server", "The networks between Mina's phone and a website", "".join(b))


def packets():
    b = [k.node(40, 150, 200, 110, "Photo of a latte", "300 KB", MINT)]
    for i in range(4):
        b += [k.box(290, 120 + i * 45, 120, 34, k.tint, k.primary), k.text(350, 143 + i * 45, f"packet {i + 1}", 16, k.primary, 700)]
    b.append(k.arrow(242, 205, 288, 205))
    routers = [(520, 110), (520, 250), (690, 180), (690, 320)]
    for x, y in routers:
        b.append(k.node(x, y, 120, 56, "Router", None, "#FFFFFF"))
    b += [k.arrow(412, 137, 518, 132), k.arrow(412, 182, 518, 150), k.arrow(412, 227, 518, 272), k.arrow(412, 272, 518, 290),
          k.arrow(640, 138, 688, 205), k.arrow(640, 278, 688, 345),
          k.arrow(812, 208, 878, 230), k.arrow(812, 348, 878, 260)]
    b += [k.node(880, 190, 190, 110, "Phone", "puts packets back in order", MINT),
          k.text(40, 420, "Data is cut into small packets. Each packet can take a different path, and the phone puts them back together.", 18, k.ink, 700, "start"),
          k.text(40, 450, "If a packet is lost, TCP asks for it again, so the photo arrives complete.", 18, k.muted, 400, "start")]
    k.svg("packets", 1110, 490, "Packets", "How a photo travels across the internet", "".join(b))


def layers():
    rows = [("Application", "HTTP, DNS: what the data means", "a web page, an order"),
            ("Transport", "TCP or UDP: deliver it between two programs", "port 443"),
            ("Internet", "IP: find the way between networks", "104.18.26.120"),
            ("Link", "Wi-Fi, mobile data, cable: one step", "the shop's Wi-Fi")]
    b = []
    for i, (name, job, example) in enumerate(rows):
        y = 120 + i * 82
        b += [k.box(40, y, 190, 66, k.tint if i == 0 else "#FFFFFF"), k.text(135, y + 41, name, 21, k.primary, 700),
              k.box(230, y, 470, 66, "#FFFFFF", k.line), k.text(250, y + 41, job, 18, k.ink, 400, "start"),
              k.box(700, y, 260, 66, MINT, k.line), k.text(830, y + 41, example, 17, k.ink, 600, mono=True)]
    b += [k.text(40, 480, "Each layer does one job, and uses the layer below it. The web lives at the top.", 19, k.ink, 700, "start")]
    k.svg("internet-layers", 1000, 520, "The layers of the internet", "Four layers, from the meaning down to the wire", "".join(b))


def dns():
    b = [k.node(40, 170, 200, 100, "Browser", "minacoffee.example?", MINT),
         k.node(330, 170, 230, 100, "DNS resolver", "your provider, or 1.1.1.1", "#FFFFFF"),
         k.arrow(242, 220, 328, 220, both=True)]
    servers = [("Root server", "Ask the .example servers", 110), ("Top-level domain", ".example: ask the shop's DNS host", 230), ("Authoritative server", "minacoffee.example is 203.0.113.10", 350)]
    for i, (name, sub, y) in enumerate(servers):
        b += [k.node(680, y - 45, 330, 90, name, sub, k.tint if i == 2 else "#FFFFFF"), k.arrow(562, 220, 678, y, both=True),
              k.step(655, y - 32, i + 2)]
    b += [k.step(285, 205, 1), k.step(285, 285, 5), k.text(285, 320, "answer, kept for later", 15, k.muted),
          k.text(40, 460, "A DNS lookup turns a name into an address. The resolver remembers the answer, so the next lookup is instant.", 18, k.ink, 700, "start"),
          k.text(40, 490, "203.0.113.10 is an address kept for examples; a real shop has its own.", 17, k.muted, 400, "start")]
    k.svg("dns-lookup", 1060, 530, "How DNS finds an address", "From a name to an IP address, in a few questions", "".join(b))


def clients_servers():
    clients = [("Phone", "Mina Coffee app"), ("Laptop", "a browser"), ("Counter tablet", "the till")]
    b = [k.node(640, 120, 260, 330, "Server", "the shop's menu and orders", k.tint)]
    for i, (name, sub) in enumerate(clients):
        y = 120 + i * 120
        b += [k.node(40, y, 230, 90, name, sub, MINT), k.arrow(272, y + 28, 638, y + 28), k.arrow(638, y + 62, 272, y + 62)]
        b += [k.text(455, y + 20, "request", 15, k.muted, 600), k.text(455, y + 84, "response", 15, k.muted, 600)]
    b += [k.text(40, 510, "A client asks; a server answers. One server can answer thousands of clients.", 19, k.ink, 700, "start")]
    k.svg("clients-and-servers", 940, 550, "Clients and servers", "Who asks, and who answers", "".join(b))


for make in (path_to_server, packets, layers, dns, clients_servers):
    make()
print("diagrams written")

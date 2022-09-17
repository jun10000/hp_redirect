import os

html_template = """<html>
    <head>
        <meta http-equiv="refresh" content="{{1}};URL='{{2}}'" />
    </head>
    <body>
        {{1}}秒後に新URLにリダイレクトします。<br>
        移動しない場合は、<a href="{{2}}">こちら</a>をクリックしてください。
    </body>
</html>"""

wait_seconds = 5
html_template = html_template.replace("{{1}}", str(wait_seconds), 2)

redirect_pairs = [
    ["./sitemap/index.html", "https://jun10000.github.io/"],
    ["./index.html", "https://jun10000.github.io/"],
    ["./category/handmade-keyboard/index.html", "https://jun10000.github.io/"],
    ["./introduce-fortitude60-keymap/index.html", "https://jun10000.github.io/introduce-fortitude60-keymap/"],
    ["./new-tecsee-switches/index.html", "https://jun10000.github.io/new-tecsee-switches/"],
    ["./change-key-switch-fortitude60/index.html", "https://jun10000.github.io/change-key-switch-fortitude60/"],
    ["./lube-keyboard-switch/index.html", "https://jun10000.github.io/lube-keyboard-switch/"],
    ["./build-log-fortitude60/index.html", "https://jun10000.github.io/build-log-fortitude60/"],
    ["./privacy-policy/index.html", "https://jun10000.github.io/about/"]
]

for filepath, new_url in redirect_pairs:
    html = html_template.replace("{{2}}", new_url, 2)
    filepath = os.path.abspath(filepath)
    filedir = os.path.dirname(filepath)
    os.makedirs(filedir, exist_ok=True)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(html)

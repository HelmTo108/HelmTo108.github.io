import csv, json, urllib.request

urls = [
    "https://standards-oui.ieee.org/oui/oui.csv",
    "https://standards-oui.ieee.org/oui28/mam.csv",
    "https://standards-oui.ieee.org/oui36/oui36.csv"
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0 Safari/537.36'}

db = {}
for url in urls:
    print(f"Downloading {url}...")
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        content = response.read().decode('utf-8').splitlines()
        reader = csv.DictReader(content)
        for row in reader:
            assignment = row['Assignment'].strip().upper()
            org = row['Organization Name'].strip()
            if assignment not in db:
                db[assignment] = org

print(f"Writing oui.json...")
with open("oui.json", "w") as f:
    json.dump(db, f, separators=(',', ':'))

print(f"Done! {len(db)} entries saved to oui.json")
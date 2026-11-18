"""Czyści klienci_brudne.csv: normalizuje NIP/telefon/e-mail/nazwę, usuwa duplikaty po NIP.
Wyniki: klienci_czyste.csv oraz usuniete_duplikaty.csv (do sprawdzenia przez człowieka)."""
import csv, re

def nip(v):
    d = re.sub(r"\D", "", v)
    return d[2:] if len(d) == 12 and v.strip().upper().startswith("PL") else d
def tel(v):
    d = re.sub(r"\D", "", v)
    d = d[2:] if len(d) == 11 and d.startswith("48") else d
    return f"{d[:3]} {d[3:6]} {d[6:]}" if len(d) == 9 else v.strip()
def nazwa(v): return " ".join(v.split()).title()

with open("klienci_brudne.csv", encoding="utf-8-sig", newline="") as f:
    wiersze = list(csv.DictReader(f, delimiter=";"))
czyste, usuniete, widziane = [], [], set()
for r in wiersze:
    n = {"Nazwa": nazwa(r["Nazwa"]), "NIP": nip(r["NIP"]), "Telefon": tel(r["Telefon"]),
         "Email": r["Email"].strip().lower(), "Miasto": r["Miasto"].strip()}
    (usuniete if n["NIP"] in widziane else czyste).append(n)
    widziane.add(n["NIP"])
pola = ["Nazwa", "NIP", "Telefon", "Email", "Miasto"]
for plik, dane in (("klienci_czyste.csv", czyste), ("usuniete_duplikaty.csv", usuniete)):
    with open(plik, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, pola, delimiter=";"); w.writeheader(); w.writerows(dane)
print(f"Wejście: {len(wiersze)}, unikalnych klientów: {len(czyste)}, usunięte duplikaty: {len(usuniete)}")

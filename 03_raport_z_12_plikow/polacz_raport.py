"""Łączy wszystkie pliki z dane_wejsciowe/ w jeden raport Excel:
arkusz Dane (oczyszczone), Podsumowanie miesięczne, Top klienci i produkty."""
from pathlib import Path
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font
from collections import defaultdict

WEJ = Path("dane_wejsciowe")
WYJ = Path("raport_sprzedazy.xlsx")
rows, odrzucone = [], 0
widziane = set()

for plik in sorted(WEJ.glob("*.xlsx")):
    ws = load_workbook(plik).active
    for r in list(ws.iter_rows(values_only=True))[1:]:   # pomiń nagłówek (nazwy bywają różne)
        if not r or all(c is None for c in r):
            odrzucone += 1; continue                       # pusty wiersz
        data, klient, produkt, ilosc, cena = r[:5]
        klient = " ".join(str(klient).split())             # usuń zbędne spacje
        klucz = (data, klient, produkt, ilosc, cena)
        if klucz in widziane:
            odrzucone += 1; continue                       # duplikat
        widziane.add(klucz)
        rows.append((data, klient, produkt, ilosc, cena, round(ilosc * cena, 2)))

wb = Workbook()
d = wb.active; d.title = "Dane"
d.append(["Data", "Klient", "Produkt", "Ilość", "Cena", "Wartość"])
for r in rows: d.append(r)

def zestaw(nazwa, idx_klucza, klucz_fn=lambda x: x):
    s = defaultdict(float)
    for r in rows: s[klucz_fn(r[idx_klucza])] += r[5]
    w = wb.create_sheet(nazwa); w.append([{"Podsumowanie miesiac":"Miesiąc","Top klient":"Klient","Top produkt":"Produkt"}[nazwa], "Wartość"])
    for k, v in sorted(s.items(), key=lambda kv: -kv[1]): w.append([k, round(v, 2)])
    return w

zestaw("Podsumowanie miesiac", 0, lambda x: str(x)[:7])
zestaw("Top klient", 1)
zestaw("Top produkt", 2)
for ws in wb:
    for c in ws[1]: c.font = Font(bold=True)
    ws.column_dimensions["A"].width = 22; ws.column_dimensions["B"].width = 22
wb.save(WYJ)
print(f"Wierszy w raporcie: {len(rows)}, odrzucone (puste/duplikaty): {odrzucone}")
print("Zapisano:", WYJ)

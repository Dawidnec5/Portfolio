"""Tworzy 12 fikcyjnych plików Excel (sprzedaż miesięczna) z typowymi bałaganami:
różne nazwy kolumn, spacje, duplikaty, puste wiersze. Dane są wymyślone."""
import random
from pathlib import Path
from openpyxl import Workbook

random.seed(7)
OUT = Path("dane_wejsciowe")
OUT.mkdir(exist_ok=True)
MIESIACE = ["styczen", "luty", "marzec", "kwiecien", "maj", "czerwiec",
            "lipiec", "sierpien", "wrzesien", "pazdziernik", "listopad", "grudzien"]
PRODUKTY = ["Plomba A", "Plomba B", "Kłódka X", "Zawleczka Z", "Taśma T"]
KLIENCI = ["Firma Alfa", "Beta Sp. z o.o.", "Gamma", "Delta Trans", "Omega"]
# różne nagłówki w różnych plikach (typowy bałagan)
NAGLOWKI = [("Data", "Klient", "Produkt", "Ilość", "Cena"),
            ("data", "klient", "produkt", "ilosc", "cena netto"),
            ("Data sprzedaży", "Nazwa klienta", "Towar", "Szt.", "Cena")]

for i, m in enumerate(MIESIACE):
    wb = Workbook()
    ws = wb.active
    ws.append(NAGLOWKI[i % 3])
    wiersze = []
    for _ in range(random.randint(15, 25)):
        wiersze.append([f"2025-{i+1:02d}-{random.randint(1,28):02d}",
                        random.choice(KLIENCI) + random.choice(["", " ", "  "]),
                        random.choice(PRODUKTY),
                        random.randint(1, 50),
                        round(random.uniform(2, 40), 2)])
    wiersze.append(list(wiersze[0]))      # duplikat
    wiersze.insert(5, [None] * 5)         # pusty wiersz
    for w in wiersze:
        ws.append(w)
    wb.save(OUT / f"sprzedaz_{i+1:02d}_{m}.xlsx")
print("Gotowe: 12 plików w", OUT)

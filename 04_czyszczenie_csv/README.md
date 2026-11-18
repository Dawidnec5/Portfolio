# Czyszczenie listy klientów (CSV)

**Problem:** ta sama firma wpisana kilka razy, za każdym razem inaczej: WIELKIE litery, spacje, NIP z myślnikami lub „PL”, telefon z „+48”.

**Rozwiązanie:** [czysc_csv.py](czysc_csv.py) ujednolica nazwę, NIP, telefon i e-mail, a duplikaty usuwa po NIP. Usunięte wiersze trafiają do [usuniete_duplikaty.csv](usuniete_duplikaty.csv), żeby można je było sprawdzić.

**Wynik:** 400 wierszy → 300 unikalnych klientów, 100 duplikatów.

| Przed (5 wpisów) | Po (1 wpis) |
|---|---|
| `KAPPA MEBLE 106`, `100-000-39-22`, `+48544424909` | `Kappa Meble 106`, `1000003922`, `544 424 909` |
| `kappa meble 106`, `PL1-000-00-3922`, `544 424 909` | |
| `Kappa Meble 106`, `PL1000003922`, `BIURO106@EXAMPLE.COM` | |

```bash
python3 generuj_dane.py   # klienci_brudne.csv
python3 czysc_csv.py      # klienci_czyste.csv + usuniete_duplikaty.csv
```
Bez dodatkowych bibliotek. Pliki otwierają się w Excelu (UTF-8, separator `;`).

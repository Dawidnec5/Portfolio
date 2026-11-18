"""Tworzy fikcyjny, brudny plik CSV z listą klientów (ok. 400 wierszy).
Bałagan: duplikaty z innym zapisem, spacje, wielkość liter, różne formaty NIP i telefonu."""
import csv, random
random.seed(11)
NAZWY = ["Alfa Trans", "Beta Bud", "Gamma Serwis", "Delta Foods", "Omega Print", "Sigma Pack",
         "Kappa Meble", "Lambda Auto", "Zeta Med", "Theta Home"]
MIASTA = ["Szczecin", "Gdańsk", "Poznań", "Wrocław", "Łódź", "Kraków"]
def nip(n): return f"{n:010d}"
rows = []
for i in range(1, 301):
    n = random.choice(NAZWY) + f" {i}"
    rows.append([n, nip(1000000000 + i * 37), f"{random.randint(500,799)}{random.randint(100000,999999)}",
                 f"biuro{i}@example.com", random.choice(MIASTA)])
for _ in range(100):                       # duplikaty w innym zapisie
    n, np_, tel, mail, m = random.choice(rows)
    rows.append([random.choice([n.upper(), " " + n + " ", n.lower()]),
                 random.choice([np_, np_[:3] + "-" + np_[3:6] + "-" + np_[6:8] + "-" + np_[8:], "PL" + np_]),
                 random.choice([tel, tel[:3] + " " + tel[3:6] + " " + tel[6:], "+48" + tel]),
                 random.choice([mail, mail.upper()]), m])
random.shuffle(rows)
with open("klienci_brudne.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f, delimiter=";"); w.writerow(["Nazwa", "NIP", "Telefon", "Email", "Miasto"]); w.writerows(rows)
print("Wierszy:", len(rows))

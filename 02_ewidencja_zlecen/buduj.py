from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule
from datetime import date, timedelta

wb = Workbook()
HEAD = PatternFill("solid", fgColor="1F4E78"); WHITE = Font(bold=True, color="FFFFFF")
thin = Side(style="thin", color="BBBBBB"); BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
N = 500  # liczba przygotowanych wierszy

# ---- Instrukcja
ws = wb.active; ws.title = "Instrukcja"
for i, t in enumerate([
    "EWIDENCJA ZLECEŃ I PŁATNOŚCI",
    "",
    "1. Wejdź do arkusza 'Zlecenia' i wpisuj każde zlecenie w nowej linii.",
    "2. Wypełniaj tylko białe kolumny: Data, Klient, Opis, Kwota, Wpłacono, Termin płatności, Status.",
    "3. Szare kolumny (Pozostało, Czy po terminie) liczą się same. Nie wpisuj w nie nic.",
    "4. Status wybierasz z listy: Nowe / W realizacji / Wykonane / Zapłacone / Anulowane.",
    "5. Czerwone wiersze = płatność po terminie. Żółte = zlecenie jeszcze nie zapłacone.",
    "6. Arkusz 'Podsumowanie' pokazuje: ile zlecono, ile wpłynęło, ile klienci jeszcze winni, wyniki miesięczne.",
    "",
    f"Gotowe na {N} zleceń. Przykładowe wiersze usuń przed użyciem (zaznacz i Delete, nie usuwaj kolumn z formułami).",
    "Dane zapisują się tylko w Twoim pliku. Nic nie jest wysyłane do internetu.",
], 1):
    ws.cell(i, 1, t)
ws["A1"].font = Font(bold=True, size=16); ws.column_dimensions["A"].width = 110

# ---- Zlecenia
z = wb.create_sheet("Zlecenia")
cols = ["Data", "Klient", "Opis", "Kwota (zł)", "Wpłacono (zł)", "Termin płatności", "Status", "Pozostało (zł)", "Czy po terminie"]
z.append(cols)
for c in z[1]:
    c.fill = HEAD; c.font = WHITE; c.alignment = Alignment(horizontal="center", wrap_text=True); c.border = BOX
today = date.today()
demo = [
    (today - timedelta(days=40), "Jan Kowalski (przykład)", "Montaż baterii", 350, 350, today - timedelta(days=26), "Zapłacone"),
    (today - timedelta(days=30), "Firma ABC (przykład)", "Przegląd instalacji", 1200, 600, today - timedelta(days=16), "Wykonane"),
    (today - timedelta(days=10), "Anna Nowak (przykład)", "Wymiana kranu", 280, 0, today + timedelta(days=4), "Wykonane"),
    (today - timedelta(days=2), "Sklep XYZ (przykład)", "Wycena remontu", 500, 0, today + timedelta(days=12), "Nowe"),
]
for i in range(2, N + 2):
    if i - 2 < len(demo):
        for j, v in enumerate(demo[i - 2], 1): z.cell(i, j, v)
    z.cell(i, 8, f'=IF(D{i}="","",D{i}-E{i})')
    z.cell(i, 9, f'=IF(OR(D{i}="",G{i}="Zapłacone",G{i}="Anulowane",H{i}<=0,F{i}=""),"",IF(F{i}<TODAY(),"TAK","nie"))')
    z.cell(i, 1).number_format = z.cell(i, 6).number_format = "yyyy-mm-dd"
    for col in (4, 5, 8): z.cell(i, col).number_format = '#,##0.00'
    for col in range(1, 10):
        z.cell(i, col).border = BOX
        if col in (8, 9): z.cell(i, col).fill = PatternFill("solid", fgColor="E7E6E6")
dv = DataValidation(type="list", formula1='"Nowe,W realizacji,Wykonane,Zapłacone,Anulowane"', allow_blank=True)
z.add_data_validation(dv); dv.add(f"G2:G{N+1}")
dv2 = DataValidation(type="decimal", operator="greaterThanOrEqual", formula1="0", allow_blank=True,
                     errorTitle="Błąd", error="Wpisz liczbę większą lub równą 0.")
z.add_data_validation(dv2); dv2.add(f"D2:E{N+1}")
z.conditional_formatting.add(f"A2:I{N+1}", FormulaRule(formula=['$I2="TAK"'], fill=PatternFill("solid", bgColor="F8CBAD")))
z.conditional_formatting.add(f"A2:I{N+1}", FormulaRule(formula=['AND($D2<>"",$H2>0,$G2<>"Anulowane",$I2<>"TAK")'], fill=PatternFill("solid", bgColor="FFF2CC")))
for col, w in zip("ABCDEFGHI", (12, 26, 32, 13, 13, 16, 14, 14, 14)): z.column_dimensions[col].width = w
z.freeze_panes = "A2"; z.auto_filter.ref = f"A1:I{N+1}"; z.row_dimensions[1].height = 32

# ---- Podsumowanie
p = wb.create_sheet("Podsumowanie")
p["A1"] = "PODSUMOWANIE"; p["A1"].font = Font(bold=True, size=14)
R = f"Zlecenia!$D$2:$D${N+1}"
rows = [
    ("Wartość wszystkich zleceń (bez anulowanych)", f'=SUMIFS({R},Zlecenia!$G$2:$G${N+1},"<>Anulowane")'),
    ("Wpłacono", f'=SUMIFS(Zlecenia!$E$2:$E${N+1},Zlecenia!$G$2:$G${N+1},"<>Anulowane")'),
    ("Do zapłaty przez klientów", "=B3-B4"),
    ("W tym po terminie", f'=SUMIFS(Zlecenia!$H$2:$H${N+1},Zlecenia!$I$2:$I${N+1},"TAK")'),
    ("Liczba zleceń po terminie", f'=COUNTIF(Zlecenia!$I$2:$I${N+1},"TAK")'),
    ("Liczba wszystkich zleceń", f'=COUNTA(Zlecenia!$B$2:$B${N+1})'),
]
for i, (a, f) in enumerate(rows, 3):
    p.cell(i, 1, a); p.cell(i, 2, f); p.cell(i, 2).number_format = '#,##0.00'
p["B7"].number_format = p["B8"].number_format = "0"
p["A10"] = "Według statusu"; p["A10"].font = Font(bold=True)
for i, s in enumerate(["Nowe", "W realizacji", "Wykonane", "Zapłacone", "Anulowane"], 11):
    p.cell(i, 1, s); p.cell(i, 2, f'=COUNTIF(Zlecenia!$G$2:$G${N+1},A{i})')
p["A17"] = "Według miesiąca (rok):"; p["A17"].font = Font(bold=True); p["B17"] = today.year
p["B17"].fill = PatternFill("solid", fgColor="FFF2CC")
p["A18"], p["B18"], p["C18"] = "Miesiąc", "Zlecono (zł)", "Wpłacono (zł)"
for c in p[18][:3]: c.font = WHITE; c.fill = HEAD
for m in range(1, 13):
    r = 18 + m
    p.cell(r, 1, m)
    p.cell(r, 2, f'=SUMIFS({R},Zlecenia!$A$2:$A${N+1},">="&DATE($B$17,A{r},1),Zlecenia!$A$2:$A${N+1},"<"&DATE($B$17,A{r}+1,1),Zlecenia!$G$2:$G${N+1},"<>Anulowane")')
    p.cell(r, 3, f'=SUMIFS(Zlecenia!$E$2:$E${N+1},Zlecenia!$A$2:$A${N+1},">="&DATE($B$17,A{r},1),Zlecenia!$A$2:$A${N+1},"<"&DATE($B$17,A{r}+1,1),Zlecenia!$G$2:$G${N+1},"<>Anulowane")')
    p.cell(r, 2).number_format = p.cell(r, 3).number_format = '#,##0.00'
p.column_dimensions["A"].width = 46; p.column_dimensions["B"].width = 18; p.column_dimensions["C"].width = 18
wb.move_sheet("Zlecenia", offset=-1)
wb.save("Ewidencja_zlecen_i_platnosci.xlsx")
print("OK")

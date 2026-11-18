import random
from datetime import date, timedelta
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.chart import BarChart, LineChart, Reference

random.seed(3)
ROK = 2026; N = 1000
HEAD = PatternFill("solid", fgColor="1F4E78"); WF = Font(bold=True, color="FFFFFF")
GREY = PatternFill("solid", fgColor="EDEDED"); INPUT = PatternFill("solid", fgColor="FFF2CC")
B = Font(bold=True); thin = Side(style="thin", color="BFBFBF"); BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
MON = ["Sty","Lut","Mar","Kwi","Maj","Cze","Lip","Sie","Wrz","Paź","Lis","Gru"]
ZL = '#,##0.00 "zł";[Red]-#,##0.00 "zł"'
def head(ws, row, vals, col=1):
    for j, v in enumerate(vals):
        c = ws.cell(row, col + j, v); c.fill = HEAD; c.font = WF; c.border = BOX
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

PROJ = ["Projekt Alfa", "Projekt Beta", "Projekt Gamma", "Ogólne (firma)"]
KP = ["Sprzedaż usług", "Sprzedaż produktów", "Dotacje", "Inne przychody"]
KK = ["Wynagrodzenia", "Podwykonawcy", "Materiały", "Biuro i czynsz", "Marketing", "Oprogramowanie", "Transport", "Inne koszty"]

wb = Workbook()
# ---------- Instrukcja
ins = wb.active; ins.title = "Instrukcja"
for i, t in enumerate([
 "BUDŻET SPÓŁKI: planowanie, monitorowanie i cash flow (wersja demonstracyjna, dane fikcyjne)", "",
 "1. Ustawienia: rok, saldo początkowe konta, listy projektów i kategorii (żółte pola).",
 "2. Transakcje: każdy przychód i koszt w osobnym wierszu. Szare kolumny liczą się same.",
 "   Data zapłaty pusta = jeszcze nie zapłacone (trafia do prognozy cash flow wg terminu płatności).",
 "3. Plan: zaplanowane kwoty netto na każdy miesiąc i kategorię.",
 "4. Plan vs Wykonanie: wybierz miesiąc (żółte pole), zobaczysz plan, wykonanie i odchylenia (miesiąc i narastająco).",
 "5. Cash flow: wpływy i wydatki wg daty zapłaty, saldo konta, prognoza z nierozliczonych faktur, wykres.",
 "6. Projekty: przychody, koszty, wynik i marża dla każdego projektu.", "",
 "Wykonanie (rachunek wyników) liczone jest netto wg daty dokumentu. Cash flow liczone jest brutto wg daty zapłaty.",
 "Arkusz działa w Excelu bez makr. Wszystkie wyliczenia to zwykłe formuły, które można podejrzeć i zmienić.",
], 1): ins.cell(i, 1, t)
ins["A1"].font = Font(bold=True, size=14); ins.column_dimensions["A"].width = 120

# ---------- Ustawienia
u = wb.create_sheet("Ustawienia")
u["A1"] = "USTAWIENIA"; u["A1"].font = Font(bold=True, size=14)
u["A3"], u["B3"] = "Rok budżetu", ROK
u["A4"], u["B4"] = "Saldo początkowe konta (1 stycznia)", 50000
u["B4"].number_format = ZL
for c in ("B3", "B4"): u[c].fill = INPUT
head(u, 6, ["Projekty", "", "Kategorie przychodów", "", "Kategorie kosztów"])
for i in range(15):
    for col, lst in ((1, PROJ), (3, KP), (5, KK)):
        c = u.cell(7 + i, col, lst[i] if i < len(lst) else None); c.fill = INPUT; c.border = BOX
for col in "ACE": u.column_dimensions[col].width = 26
u.column_dimensions["A"].width = 36

# ---------- Transakcje
t = wb.create_sheet("Transakcje")
cols = ["Data dokumentu", "Typ", "Projekt", "Kategoria", "Opis / kontrahent", "Kwota netto", "VAT %", "Kwota brutto",
        "Termin płatności", "Data zapłaty", "Status", "Miesiąc"]
head(t, 1, cols)
demo = []
for m in range(1, 11):
    for _ in range(random.randint(5, 8)):
        typ = random.choice(["Przychód", "Koszt", "Koszt"])
        d = date(ROK, m, random.randint(1, 28))
        kat = random.choice(KP[:2]) if typ == "Przychód" else random.choice(KK)
        netto = round(random.uniform(8000, 30000) if typ == "Przychód" else random.uniform(500, 9000), -1)
        vat = 0 if kat == "Wynagrodzenia" else 23
        termin = d + timedelta(days=random.choice([7, 14, 30]))
        zap = termin + timedelta(days=random.randint(-3, 10)) if termin < date(ROK, 10, 20) else None
        demo.append((d, typ, random.choice(PROJ if typ == "Koszt" else PROJ[:3]), kat,
                     ("Klient " if typ == "Przychód" else "Dostawca ") + random.choice("ABCDEFG") + " (fikcyjny)",
                     netto, vat, termin, zap))
demo.sort()
for i in range(2, N + 2):
    if i - 2 < len(demo):
        d, typ, pr, kat, op, net, vat, ter, zap = demo[i - 2]
        for col, v in ((1, d), (2, typ), (3, pr), (4, kat), (5, op), (6, net), (7, vat), (9, ter), (10, zap)):
            t.cell(i, col, v)
    t.cell(i, 8, f'=IF(F{i}="","",ROUND(F{i}*(1+G{i}/100),2))')
    t.cell(i, 11, f'=IF(F{i}="","",IF(J{i}<>"","Zapłacone",IF(I{i}="","Niezapłacone",IF(I{i}<TODAY(),"PO TERMINIE","Niezapłacone"))))')
    t.cell(i, 12, f'=IF(A{i}="","",MONTH(A{i}))')
    for col in (1, 9, 10): t.cell(i, col).number_format = "yyyy-mm-dd"
    for col in (6, 8): t.cell(i, col).number_format = ZL
    for col in range(1, 13):
        t.cell(i, col).border = BOX
        if col in (8, 11, 12): t.cell(i, col).fill = GREY
for rng, f in ((f"B2:B{N+1}", '"Przychód,Koszt"'), (f"C2:C{N+1}", "=Ustawienia!$A$7:$A$21"),
               (f"D2:D{N+1}", "=Ustawienia!$C$7:$C$21,Ustawienia!$E$7:$E$21"), (f"G2:G{N+1}", '"0,5,8,23"')):
    if "," in f and f.startswith("=Ust") and f.count("!") > 1:   # dwie listy -> połączona lista statyczna
        f = '"' + ",".join(KP + KK) + '"'
    dv = DataValidation(type="list", formula1=f, allow_blank=True); t.add_data_validation(dv); dv.add(rng)
t.conditional_formatting.add(f"K2:K{N+1}", CellIsRule(operator="equal", formula=['"PO TERMINIE"'], fill=PatternFill("solid", bgColor="F8CBAD"), font=Font(bold=True, color="9C0006")))
t.conditional_formatting.add(f"K2:K{N+1}", CellIsRule(operator="equal", formula=['"Niezapłacone"'], fill=PatternFill("solid", bgColor="FFF2CC")))
for col, w in zip("ABCDEFGHIJKL", (13, 11, 16, 20, 28, 14, 7, 14, 14, 13, 14, 8)): t.column_dimensions[col].width = w
t.freeze_panes = "A2"; t.auto_filter.ref = f"A1:L{N+1}"; t.row_dimensions[1].height = 30

TR = lambda c: f"Transakcje!${c}$2:${c}${N+1}"
# ---------- Plan
p = wb.create_sheet("Plan")
p["A1"] = "PLAN BUDŻETU (netto)"; p["A1"].font = Font(bold=True, size=14)
head(p, 3, ["Kategoria", "Typ"] + MON + ["Razem rok"])
r = 4
plan_rows = {}
for typ, lst, base in (("Przychód", KP, 30000), ("Koszt", KK, 6000)):
    for k in lst:
        p.cell(r, 1, k); p.cell(r, 2, typ)
        for m in range(12):
            val = 0 if k in ("Dotacje", "Inne przychody", "Inne koszty") else round(base * random.uniform(0.6, 1.3), -2)
            c = p.cell(r, 3 + m, val); c.fill = INPUT; c.number_format = '#,##0'
        p.cell(r, 15, f"=SUM(C{r}:N{r})").number_format = '#,##0'
        plan_rows[k] = r; r += 1
p.cell(r, 1, "WYNIK PLANOWANY").font = B
for m in range(13):
    col = p.cell(3, 3 + m).column_letter
    p.cell(r, 3 + m, f'=SUMIF($B$4:$B${r-1},"Przychód",{col}4:{col}{r-1})-SUMIF($B$4:$B${r-1},"Koszt",{col}4:{col}{r-1})').number_format = '#,##0;[Red]-#,##0'
    p.cell(r, 3 + m).font = B
p.column_dimensions["A"].width = 22; p.freeze_panes = "C4"
PLAN_LAST = r - 1

# ---------- Plan vs Wykonanie
v = wb.create_sheet("Plan vs Wykonanie")
v["A1"] = "PLAN VS WYKONANIE (netto, wg daty dokumentu)"; v["A1"].font = Font(bold=True, size=14)
v["A2"], v["B2"] = "Wybierz miesiąc (1–12):", 10; v["B2"].fill = INPUT
dv = DataValidation(type="whole", operator="between", formula1="1", formula2="12"); v.add_data_validation(dv); dv.add("B2")
head(v, 4, ["Kategoria", "Typ", "Plan (miesiąc)", "Wykonanie (miesiąc)", "Odchylenie", "% planu",
            "Plan (narastająco)", "Wykonanie (narastająco)", "Odchylenie", "% planu"])
r = 5
for typ, lst in (("Przychód", KP), ("Koszt", KK)):
    for k in lst:
        pr = plan_rows[k]
        v.cell(r, 1, k); v.cell(r, 2, typ)
        v.cell(r, 3, f"=INDEX(Plan!$C${pr}:$N${pr},$B$2)")
        v.cell(r, 4, f'=SUMIFS({TR("F")},{TR("D")},A{r},{TR("B")},B{r},{TR("L")},$B$2)')
        v.cell(r, 7, f"=SUM(OFFSET(Plan!$C${pr},0,0,1,$B$2))")
        v.cell(r, 8, f'=SUMIFS({TR("F")},{TR("D")},A{r},{TR("B")},B{r},{TR("L")},"<="&$B$2)')
        for a, b, o, pc in ((3, 4, 5, 6), (7, 8, 9, 10)):
            A_, B_ = v.cell(r, a).coordinate, v.cell(r, b).coordinate
            v.cell(r, o, f"={B_}-{A_}")
            v.cell(r, pc, f'=IF({A_}=0,"",{B_}/{A_})').number_format = "0%"
        for c in (3, 4, 5, 7, 8, 9): v.cell(r, c).number_format = '#,##0;[Red]-#,##0'
        r += 1
v.cell(r, 1, "WYNIK").font = B
for c in (3, 4, 5, 7, 8, 9):
    L = v.cell(4, c).column_letter
    v.cell(r, c, f'=SUMIF($B$5:$B${r-1},"Przychód",{L}5:{L}{r-1})-SUMIF($B$5:$B${r-1},"Koszt",{L}5:{L}{r-1})').number_format = '#,##0;[Red]-#,##0'
    v.cell(r, c).font = B
# koszty ponad plan = czerwone, przychody poniżej planu = czerwone
v.conditional_formatting.add(f"E5:E{r-1}", FormulaRule(formula=[f'OR(AND($B5="Koszt",E5>0),AND($B5="Przychód",E5<0))'], font=Font(color="C00000", bold=True)))
v.conditional_formatting.add(f"I5:I{r-1}", FormulaRule(formula=[f'OR(AND($B5="Koszt",I5>0),AND($B5="Przychód",I5<0))'], font=Font(color="C00000", bold=True)))
v.column_dimensions["A"].width = 24
for L in "CDEFGHIJ": v.column_dimensions[L].width = 14

# ---------- Cash flow
cf = wb.create_sheet("Cash flow")
cf["A1"] = "CASH FLOW (brutto, wg daty zapłaty) + prognoza"; cf["A1"].font = Font(bold=True, size=14)
head(cf, 3, ["Miesiąc", "Wpływy (zapłacone)", "Wydatki (zapłacone)", "Przepływ netto", "Saldo konta (faktyczne)",
             "Oczekiwane wpływy (nierozliczone)", "Oczekiwane wydatki (nierozliczone)", "Saldo z prognozą"])
for m in range(1, 13):
    r = 3 + m
    od, do = f"DATE(Ustawienia!$B$3,{m},1)", f"DATE(Ustawienia!$B$3,{m+1},1)"
    cf.cell(r, 1, MON[m - 1])
    cf.cell(r, 2, f'=SUMIFS({TR("H")},{TR("B")},"Przychód",{TR("J")},">="&{od},{TR("J")},"<"&{do})')
    cf.cell(r, 3, f'=SUMIFS({TR("H")},{TR("B")},"Koszt",{TR("J")},">="&{od},{TR("J")},"<"&{do})')
    cf.cell(r, 4, f"=B{r}-C{r}")
    cf.cell(r, 5, f"=Ustawienia!$B$4+SUM($D$4:D{r})")
    cf.cell(r, 6, f'=SUMIFS({TR("H")},{TR("B")},"Przychód",{TR("J")},"",{TR("I")},">="&{od},{TR("I")},"<"&{do})')
    cf.cell(r, 7, f'=SUMIFS({TR("H")},{TR("B")},"Koszt",{TR("J")},"",{TR("I")},">="&{od},{TR("I")},"<"&{do})')
    cf.cell(r, 8, f"=Ustawienia!$B$4+SUM($D$4:D{r})+SUM($F$4:F{r})-SUM($G$4:G{r})")
    for c in range(2, 9): cf.cell(r, c).number_format = '#,##0;[Red]-#,##0'
cf.cell(16, 1, "RAZEM").font = B
for c in (2, 3, 4, 6, 7):
    L = cf.cell(3, c).column_letter
    cf.cell(16, c, f"=SUM({L}4:{L}15)").number_format = '#,##0;[Red]-#,##0'; cf.cell(16, c).font = B
cf["A18"] = "Nierozliczone faktury z terminem przed 1 stycznia lub bez terminu nie są w prognozie: sprawdź filtr w arkuszu Transakcje."
cf["A18"].font = Font(italic=True, color="7F7F7F")
for L, w in zip("ABCDEFGH", (10, 16, 16, 15, 17, 18, 18, 16)): cf.column_dimensions[L].width = w
cf.row_dimensions[3].height = 42
ch = BarChart(); ch.title = "Wpływy i wydatki"; ch.height, ch.width = 8, 18
ch.add_data(Reference(cf, min_col=2, max_col=3, min_row=3, max_row=15), titles_from_data=True)
ch.set_categories(Reference(cf, min_col=1, min_row=4, max_row=15))
cf.add_chart(ch, "J3")
ln = LineChart(); ln.title = "Saldo konta: faktyczne i z prognozą"; ln.height, ln.width = 8, 18
ln.add_data(Reference(cf, min_col=5, min_row=3, max_row=15), titles_from_data=True)
ln.add_data(Reference(cf, min_col=8, min_row=3, max_row=15), titles_from_data=True)
ln.set_categories(Reference(cf, min_col=1, min_row=4, max_row=15))
for sr in ln.series: sr.smooth = False
cf.add_chart(ln, "J20")

# ---------- Projekty
pj = wb.create_sheet("Projekty")
pj["A1"] = "WYNIKI PROJEKTÓW (netto)"; pj["A1"].font = Font(bold=True, size=14)
head(pj, 3, ["Projekt", "Przychody", "Koszty", "Wynik", "Marża %", "Należności (niezapłacone przychody brutto)"])
for i in range(15):
    r = 4 + i
    pj.cell(r, 1, f'=IF(Ustawienia!A{7+i}="","",Ustawienia!A{7+i})')
    pj.cell(r, 2, f'=IF(A{r}="","",SUMIFS({TR("F")},{TR("C")},A{r},{TR("B")},"Przychód"))')
    pj.cell(r, 3, f'=IF(A{r}="","",SUMIFS({TR("F")},{TR("C")},A{r},{TR("B")},"Koszt"))')
    pj.cell(r, 4, f'=IF(A{r}="","",B{r}-C{r})')
    pj.cell(r, 5, f'=IF(OR(A{r}="",N(B{r})=0),"",D{r}/B{r})').number_format = "0.0%"
    pj.cell(r, 6, f'=IF(A{r}="","",SUMIFS({TR("H")},{TR("C")},A{r},{TR("B")},"Przychód",{TR("J")},""))')
    for c in (2, 3, 4, 6): pj.cell(r, c).number_format = '#,##0;[Red]-#,##0'
pj.cell(19, 1, "RAZEM").font = B
for c in (2, 3, 4, 6):
    L = pj.cell(3, c).column_letter
    pj.cell(19, c, f"=SUM({L}4:{L}18)").number_format = '#,##0;[Red]-#,##0'; pj.cell(19, c).font = B
pj.column_dimensions["A"].width = 22
for L in "BCDE": pj.column_dimensions[L].width = 14
pj.column_dimensions["F"].width = 24; pj.row_dimensions[3].height = 32
bc = BarChart(); bc.title = "Wynik projektów"; bc.height, bc.width = 7, 14
bc.add_data(Reference(pj, min_col=4, min_row=3, max_row=7), titles_from_data=True)
bc.set_categories(Reference(pj, min_col=1, min_row=4, max_row=7)); pj.add_chart(bc, "H3")

wb.save("Budzet_spolki_DEMO.xlsx")
# do weryfikacji w Pythonie
import json; json.dump([[str(x) if isinstance(x, date) else x for x in d] for d in demo], open("/tmp/claude-0/demo.json", "w"))
print("OK, transakcji demo:", len(demo))

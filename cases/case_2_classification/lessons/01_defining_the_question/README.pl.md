# Lekcja 1 — Definiowanie pytania

**Szacowany czas:** 25-35 min

## Po co to robimy

Nowy klient, nowy format. Dane Meridian Outlet nie przychodzą w schludnym CSV — przychodzą w eksporcie Excela zbudowanym dla człowieka, nie dla skryptu. Zanim dotkniemy tego bałaganu, ustalmy jasne pytanie biznesowe, tak samo jak przy TransLine — bałagan to problem kolejnej lekcji.

Pytanie na dziś: mając to, co Meridian Outlet już zapisuje o zamówieniu, co dokładnie powinniśmy przewidywać, i w jakim stanie faktycznie są te dane?

## Co masz zrobić

- `data/orders.xlsx` — dwuarkuszowy eksport Excela ("Orders" i "Customers").
- W `task.py` zaimplementuj `list_sheet_names`, `load_raw_orders_sheet`, `target_column_name`.
- W notebooku: wypisz nazwy arkuszy (są dwa, nie jeden), wczytaj arkusz Orders z domyślnymi ustawieniami pandas i przyjrzyj się nazwom kolumn i kształtowi. Potwierdź, że mimo bałaganu we wczytaniu da się nazwać kolumnę celu.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" opisz konkretnie, co jest nie tak z surowym wczytaniem — co widać w kolumnach i pierwszych wierszach. I: surowe wczytanie ma 702 wiersze, a Meridian Outlet mówi, że w tym kwartale wysłało 700 zamówień — zanim otworzysz Lekcję 2, jaki jest najlepszy strzał, skąd wzięły się te dwa dodatkowe wiersze?

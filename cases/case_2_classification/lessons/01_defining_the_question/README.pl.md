# Lekcja 1 — Definiowanie pytania

## Głos mentora

"Nowy klient, nowy format. Dane Meridian Outlet nie przychodzą w schludnym CSV — przychodzą w eksporcie Excela zbudowanym dla człowieka, nie dla skryptu. Zanim tego dotkniesz, ustal sobie jasno pytanie biznesowe, tak samo jak zrobiłeś/zrobiłaś dla TransLine. Bałagan to problem następnej lekcji."

## Cel lekcji

Zamienić skargę Meridian Outlet w konkretne, mierzalne pytanie analityczne i rzucić pierwsze, uczciwe spojrzenie na ich eksport Excela — łącznie z jego problemami.

## Pytanie analityczne dnia

Mając to, co Meridian Outlet już zapisuje o zamówieniu, co dokładnie powinniśmy przewidywać, i w jakim stanie faktycznie są te dane?

## Co dostajesz

- `data/orders.xlsx` — dwuarkuszowy eksport Excela ("Orders" i "Customers")
- `task.py` — trzy funkcje do zaimplementowania: `list_sheet_names`, `load_raw_orders_sheet`, `target_column_name`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Wypisz nazwy arkuszy — zauważ, że są dwa, nie jeden.
4. Wczytaj arkusz Orders z domyślnymi ustawieniami pandas i przyjrzyj się dokładnie nazwom kolumn i kształtowi.
5. Potwierdź, że mimo bałaganu w wczytaniu wciąż potrafisz nazwać kolumnę celu.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania opisujące dokładnie, co jest nie tak z surowym wczytaniem — bądź konkretny/konkretna co do tego, co widzisz w kolumnach i pierwszych wierszach.

## Refleksja

Mentor pyta: surowe wczytanie ma 702 wiersze, a Meridian Outlet mówi, że w tym kwartale wysłało 700 zamówień. Zanim jeszcze otworzysz Lekcję 2, jaki jest Twój najlepszy strzał, skąd wzięły się te dwa dodatkowe wiersze?

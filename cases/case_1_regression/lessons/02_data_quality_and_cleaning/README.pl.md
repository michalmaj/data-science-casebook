# Lekcja 2 — Jakość danych i czyszczenie

**Szacowany czas:** 35-45 min

## Efekty uczenia się

- Będziesz umieć dobrać inną, uzasadnioną strategię czyszczenia dla każdej kolumny zamiast jednego uniwersalnego `dropna()`.
- Będziesz umieć rozpoznać, kiedy usunięcie wierszy jest właściwą decyzją, a kiedy lepsza jest imputacja, na podstawie tego, co brak w danej konkretnej kolumnie faktycznie oznacza.
- Będziesz umieć złożyć pojedyncze decyzje czyszczące per kolumna w jedną, powtarzalną funkcję pipeline'u czyszczenia.

## Głos mentora

"Ostatnio znalazłeś/znalazłaś dwie kolumny z brakami i zapytałem, co byś z nimi zrobił/zrobiła. 'To zależy' było dobrym instynktem — teraz zróbmy to konkretnie. Brakująca wartość `weather` i brakująca wartość `driver_experience_years` to nie ten sam rodzaj problemu i nie zasługują na to samo rozwiązanie."

## Cel lekcji

Zdecydować — i uzasadnić — konkretne działanie czyszczące dla każdej kolumny z brakami danych, a nie jedno uniwersalne `dropna()`.

## Pytanie analityczne dnia

Dane TransLine mają 15 przesyłek z jakimś brakiem. Które wiersze, które kolumny, i co właściwie powinniśmy z każdym z nich zrobić?

## Co dostajesz

- Ten sam `data/transport_delays.csv` z Lekcji 1
- `task.py` — pięć funkcji do zaimplementowania: `load_shipments`, `rows_with_missing_data`, `drop_missing_weather`, `impute_missing_experience`, `clean_shipments`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Zobacz `rows_with_missing_data(df)` — potwierdź, które kolumny są naprawdę dotknięte i ile wierszy.
4. Zdecyduj (i bądź gotów/gotowa to obronić), czemu usunięcie wierszy to dobra decyzja dla `weather`, a uzupełnienie medianą to dobra decyzja dla `driver_experience_years`.
5. Potwierdź, że `clean_shipments(df)` nie zostawia żadnych braków danych.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania uzasadniające różne podejście do obu kolumn i zanotuj, co zmieniłoby Twoją decyzję (np. gdyby `weather` brakowało w 30% wierszy, a nie ~1%).

## Refleksja

Mentor pyta: jeśli TransLine powie Ci później, że brakujące wartości `weather` pochodziły z tego samego tygodnia (awaria czujnika, nie coś losowego), czy to zmienia, czy usunięcie tych wierszy było dobrą decyzją?

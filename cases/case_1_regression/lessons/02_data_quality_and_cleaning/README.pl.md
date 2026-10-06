# Lekcja 2 — Jakość danych i czyszczenie

**Szacowany czas:** 35-45 min

## Po co to robimy

W Lekcji 1 znalazłeś dwie kolumny z brakami i zastanawiałeś się, co z nimi zrobić. "To zależy" było dobrym instynktem — teraz trzeba to rozstrzygnąć konkretnie. Brakująca wartość `weather` i brakująca wartość `driver_experience_years` to nie ten sam rodzaj problemu i nie zasługują na to samo rozwiązanie.

Dane TransLine mają 15 przesyłek z jakimś brakiem. Pytanie na dziś: które wiersze, które kolumny, i co właściwie trzeba zrobić z każdym z nich?

## Co masz zrobić

- Ten sam `data/transport_delays.csv` z Lekcji 1.
- W `task.py` zaimplementuj `load_shipments`, `rows_with_missing_data`, `drop_missing_weather`.
- W notebooku: sprawdź `rows_with_missing_data(df)` i potwierdź, które kolumny są dotknięte i ile wierszy. Zdecyduj — i przygotuj się to obronić — czemu usunięcie wierszy jest dobrą decyzją dla `weather`, a `driver_experience_years` też wymaga naprawy, ale nie teraz. Uzupełnienie medianą wymaga policzenia tej mediany, a to wyliczenie nie jest bezpieczne, zanim wiadomo, które wiersze mogą ją informować — tym zajmie się Lekcja 3.

## Na co zwrócić uwagę

Nie każdą decyzję czyszczącą można podjąć w tym samym momencie. Usunięcie wiersza to stała reguła na poziomie wiersza — nie zależy od pozostałych danych, więc jest bezpieczne już teraz. Uzupełnienie medianą to statystyka wyliczona z danych — jeśli policzysz ją przed podziałem na zbiór treningowy i testowy, informacja z testu wycieknie do treningu. Dlatego `drop_missing_weather(df)` nie zostawia żadnych braków w `weather`, ale `driver_experience_years` wciąż ma braki po tej lekcji — tak ma być.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" zapisz: czemu usunięcie wierszy dla `weather` jest bezpieczne przed podziałem, a uzupełnienie `driver_experience_years` medianą — jeszcze nie. I: gdyby TransLine powiedziało później, że braki w `weather` pochodziły z tego samego tygodnia (awaria czujnika, nie coś losowego) — zmienia to, czy usunięcie tych wierszy wciąż było dobrą decyzją?

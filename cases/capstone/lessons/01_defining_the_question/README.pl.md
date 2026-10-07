# Lekcja 1 — Definiowanie pytania

**Szacowany czas:** 45-55 min

## Decyzja do podjęcia

W każdym poprzednim case'ie klient i pytanie były już dane. Tym razem wybierasz oba. Przeczytaj menu w `README.md` na poziomie case'u, wybierz klienta, którego problem Cię interesuje, i zamień jego niejasną skargę w coś, wobec czego dałoby się zbudować model — konkretne pytanie analityczne, zmienną celu i metrykę sukcesu.

Zdecyduj też samodzielnie, która technika — regresja, klasyfikacja czy klasteryzacja — faktycznie pasuje do problemu wybranego klienta. Nic w briefie tego nie podpowiada.

## Masz do dyspozycji

- Trzy zbiory danych w `data/`: `clinic_wait_times.csv`, `lendwell_loan_default.csv`, `retail_store_segments.csv` — każdy z lekkim briefem w `README.md` case'u, bez podanej zmiennej celu ani metryki.
- W `task.py` zaimplementuj `list_datasets`, `load_dataset`, `missing_value_counts`.
- W notebooku: wypisz dostępne zbiory, wczytaj wybrany zbiór, sprawdź jego kształt i braki danych, i zapisz swoje pytanie analityczne, zmienną celu i metrykę sukcesu.

## Uzasadnij

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Te testy sprawdzają jedynie, czy funkcje wczytujące działają poprawnie dla wszystkich trzech zbiorów — nie mogą sprawdzić, którego klienta wybrano, ani czy pytanie jest dobre.

Dwa do trzech zdań: dlaczego akurat ta zmienna celu i ta metryka? Ile kosztowałby błędny wybór na tym etapie w dalszej części projektu? I: który z trzech klientów z menu byłby najtrudniejszy do odmówienia, gdyby to był prawdziwy klient, nawet gdyby dane nie do końca wspierały odpowiedź na jego prawdziwe pytanie — i jak warto by się temu przeciwstawić?

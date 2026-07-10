# Lekcja 1 — Definiowanie pytania

## Głos mentora

"W każdym poprzednim case'ie dawałem Ci klienta i pytanie. Tym razem wybierasz oba. Przeczytaj menu, wybierz klienta, którego problem Cię interesuje, i zamień jego niejasną skargę w coś, wobec czego faktycznie dałoby się zbudować model."

## Cel lekcji

Wybrać jednego klienta z menu projektu końcowego, wczytać jego dane i samodzielnie zdefiniować konkretne pytanie analityczne, zmienną celu i metrykę sukcesu, z którymi będziesz pracować przez resztę projektu.

## Pytanie analityczne dnia

Jeszcze go nie ma — to właśnie budujesz w tej lekcji. Któremu klientowi pomożesz i na jakie konkretne, mierzalne pytanie mu odpowiesz?

## Co dostajesz

- Trzy zbiory danych w `data/`: `clinic_wait_times.csv`, `lendwell_loan_default.csv`, `retail_store_segments.csv`
- Lekkie briefy klienckie dla każdego w `README.md` na poziomie case'u — bez podanej zmiennej celu ani metryki
- `task.py` — trzy funkcje do zaimplementowania: `list_datasets`, `load_dataset`, `missing_value_counts`
- `lesson.ipynb` — notebook, w którym wybierzesz klienta i zaczniesz eksplorację

## Praca w notebooku

- Wypisz dostępne zbiory danych i przeczytaj ich briefy.
- Wczytaj ten, który wybrałeś/wybrałaś, i sprawdź jego kształt i braki danych.
- Zapisz własne pytanie analityczne, zmienną celu i metrykę sukcesu.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Te testy sprawdzają jedynie, czy Twoje funkcje wczytujące działają poprawnie dla wszystkich trzech zbiorów — nie mogą sprawdzić, którego klienta wybrałeś/wybrałaś ani czy Twoje pytanie jest dobre.

## Zadanie domowe

Dwa do trzech zdań: dlaczego wybrałeś/wybrałaś akurat tę zmienną celu i tę metrykę? Ile kosztowałby Cię błędny wybór na tym etapie w dalszej części projektu?

## Refleksja

Mentor pyta: któremu z trzech klientów z menu najtrudniej byłoby odmówić, gdyby to był prawdziwy klient, nawet gdyby dane nie do końca wspierały odpowiedź na jego prawdziwe pytanie — i jak byś to zakomunikował/zakomunikowała?

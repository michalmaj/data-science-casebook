# Lekcja 6 — Interpretacja reszt

**Szacowany czas:** 40-50 min

## Efekty uczenia się

- Będziesz umieć policzyć reszty modelu i traktować je jako dane do zbadania, nie tylko wynik dokładności.
- Będziesz umieć zgrupować reszty wg zmiennej kategorycznej, żeby wychwycić systematyczny wzorzec zamiast losowego szumu.
- Będziesz umieć powiązać wzorzec w resztach ze zmienną, której model nigdy nie dostał, i nazwać, co to oznacza dla ślepej plamki modelu.

## Głos mentora

"Model, który się myli, to nie problem — każdy model gdzieś się myli. Problemem jest nie wiedzieć, *gdzie*. Jeśli Twoje błędy to przypadkowy szum, dobrze, to najlepsze, co można osiągnąć. Jeśli układają się w konkretny wzorzec, to nie szum — to sygnał, który ignorujesz."

## Cel lekcji

Zdiagnozować, co model z Lekcji 5 systematycznie robi źle, i połączyć to ze zmienną, której nigdy nie dostał.

## Pytanie analityczne dnia

Czy błędy tego modelu są przypadkowe, czy mają wzorzec — a jeśli mają, na co wskazują?

## Co dostajesz

- Ten sam podział i model co w Lekcji 5, odtworzone tutaj (`load_shipments`, `split_shipments`, `impute_driver_experience`, `fit_model`)
- `task.py` — trzy nowe funkcje do zaimplementowania: `compute_residuals`, `mean_residual_by_weather`, `residual_correlation_with_feature`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Potwierdź, że korelacja reszt z każdą cechą już w modelu jest praktycznie zerowa — potem zastanów się, *czemu* to jest gwarantowane, a nie oznaka dobrej jakości.
4. Zobacz średnią resztę wg pogody — to jest sprawdzenie, które faktycznie coś mówi, bo `weather` nigdy nie zostało podane modelowi.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz prostym językiem, co model robi źle i dla jakich przesyłek, i zaproponuj jedną poprawkę, która nie wymaga zbierania nowych danych.

## Refleksja

Mentor pyta: ta lekcja analizowała reszty na zbiorze *treningowym*, nie testowym. Lekcja 5 była bardzo restrykcyjna co do nietykania danych testowych przed finalną oceną. Czemu tutaj mimo to jest w porządku patrzeć na reszty treningowe — do czego ich używamy, że różni się to od oceny skuteczności?

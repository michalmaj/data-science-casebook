# Lekcja 6 — Interpretacja reszt

**Szacowany czas:** 40-50 min

## Po co to robimy

Model, który się myli, to nie problem — każdy model gdzieś się myli. Problemem jest nie wiedzieć, *gdzie*. Jeśli błędy są przypadkowym szumem, to najlepsze, co można osiągnąć. Jeśli układają się w konkretny wzorzec, to nie szum — to sygnał, który ignorujemy.

Pytanie na dziś: czy błędy modelu z Lekcji 5 są przypadkowe, czy mają wzorzec — a jeśli mają, na co wskazują?

## Co masz zrobić

- Ten sam podział co w Lekcji 3 i ten sam model co w Lekcji 5, odtworzone tutaj (`load_shipments`, `split_shipments`, `impute_driver_experience`, `fit_model`).
- W `task.py` zaimplementuj trzy nowe funkcje: `compute_residuals`, `mean_residual_by_weather`, `residual_correlation_with_feature`.
- W notebooku: potwierdź, że korelacja reszt z każdą cechą już w modelu jest praktycznie zerowa, a potem zobacz średnią resztę wg pogody.

## Na co zwrócić uwagę

Zerowa korelacja reszt z cechami, które model już ma, jest gwarantowana przez sposób, w jaki regresja liniowa dopasowuje współczynniki — nie oznacza dobrej jakości modelu. Sprawdzeniem, które faktycznie coś mówi, jest średnia reszta wg pogody — bo `weather` nigdy nie zostało podane modelowi, więc wzorzec tam nie jest wymuszony matematycznie.

Ta lekcja analizuje reszty na zbiorze *treningowym*, nie testowym — i to jest w porządku, bo nie oceniamy tu skuteczności modelu, tylko szukamy wzorca w jego błędach, żeby zrozumieć, co model przeocza. To inne pytanie niż "jak dobrze model generalizuje", które Lekcja 5 już rozstrzygnęła na zbiorze testowym.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" napisz prostym językiem, co model robi źle i dla jakich przesyłek, i zaproponuj jedną poprawkę, która nie wymaga zbierania nowych danych.

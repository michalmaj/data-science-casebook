# data-science-casebook

[![CI](https://github.com/michalmaj/data-science-casebook/actions/workflows/ci.yml/badge.svg)](https://github.com/michalmaj/data-science-casebook/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Od niejasnego problemu do uzasadnionego wniosku.

## Czym to jest

`data-science-casebook` to kurs Data Science oparty na case studies. To nie jest kurs składni Pythona — uczy ścieżki analitycznej: **problem → dane → eksploracja → model → ewaluacja → komunikacja**. Python, pandas i scikit-learn są warsztatem, nie tematem.

Każdy case opowiada małą historię: organizacja ma problem, dane są niepełne lub niejednoznaczne, ktoś oczekuje odpowiedzi, a Ty decydujesz, co można uczciwie z nich wywnioskować. Kurs zakłada, że masz już podstawy Pythona i pierwsze zetknięcie z konceptami machine learningu.

## Struktura kursu

Cztery case'y, każdy to pełny cykl analityczny, z malejącym poziomem wsparcia:

| Case | Scenariusz | Technika | Lekcje | Wsparcie |
|---|---|---|---|---|
| [Case 1 — Regresja](cases/case_1_regression/) | Opóźnienia dostaw TransLine | Regresja liniowa | 8 | Mocno prowadzony |
| [Case 2 — Klasyfikacja](cases/case_2_classification/) | Zwroty w Meridian Outlet | Regresja logistyczna | 8 | Częściowo prowadzony |
| [Case 3 — Klasteryzacja](cases/case_3_clustering/) | Segmentacja subskrybentów Aurora Stream | KMeans | 8 | Sam brief + dane |
| [Capstone](cases/capstone/) | Twój wybór jednego z trzech zleceń klienckich | Twój wybór techniki | 6 | W pełni samodzielny |

## Szybki start

Zainstaluj zależności przy pomocy [uv](https://docs.astral.sh/uv/):

```bash
uv sync
```

Każda lekcja znajduje się w `cases/<case>/lessons/<NN_nazwa_lekcji>/` i ma tę samą strukturę:

- `task.py` — funkcje, które implementujesz (każda ma docstring `TODO` wyjaśniający co zrobić)
- `solution.py` — referencyjna implementacja (nie zaglądaj przed próbą rozwiązania `task.py`)
- `check.py` — self-check; uruchom go z katalogu lekcji poleceniem `uv run pytest`
- `lesson.ipynb` — notebook, w którym faktycznie pracujesz nad lekcją
- `README.md` / `README.pl.md` — brief lekcji

Zacznij od `cases/case_1_regression/lessons/01_defining_the_question/`.

## Dwujęzyczność

Każdy plik Markdown ma polski odpowiednik (`README.md` → `README.pl.md`). Angielski jest źródłem prawdy; kod, komentarze i komunikaty commitów są wyłącznie po angielsku.

## Współtworzenie

Znalazłeś/znalazłaś błąd w lekcji, problem z tłumaczeniem, albo chcesz zaproponować nowy case lub lekcję? [Otwórz issue](https://github.com/michalmaj/data-science-casebook/issues/new/choose) — wybór szablonu skieruje Cię do właściwego formularza.

## Licencja

[MIT](LICENSE)

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
| [Case 2 — Klasyfikacja](cases/case_2_classification/) | Zwroty w Meridian Outlet | Regresja logistyczna | 8 | Prowadzony |
| [Case 3 — Klasteryzacja](cases/case_3_clustering/) | Segmentacja subskrybentów Aurora Stream | KMeans | 8 | Prowadzony, mniej wsparcia w interpretacji |
| [Capstone](cases/capstone/) | Twój wybór jednego z trzech zleceń klienckich | Twój wybór techniki | 6 | Prowadzony capstone (ograniczony wybór) |

## Szybki start

Zainstaluj [uv](https://docs.astral.sh/uv/) — samo zarządza wersjami Pythona, więc nie musisz mieć go wcześniej zainstalowanego; poniższe komendy same pobiorą odpowiedni interpreter, jeśli będzie potrzebny.

```bash
git clone https://github.com/michalmaj/data-science-casebook.git
cd data-science-casebook
uv sync
```

Uruchom JupyterLab:

```bash
uv run jupyter lab
```

Każda lekcja znajduje się w `cases/<case>/lessons/<NN_nazwa_lekcji>/` i ma tę samą strukturę:

- `task.py` — funkcje, które implementujesz (każda ma docstring `TODO` wyjaśniający co zrobić)
- `solution.py` — referencyjna implementacja (nie zaglądaj przed próbą rozwiązania `task.py`)
- `check.py` — self-check; uruchom go z katalogu lekcji poleceniem `uv run pytest`
- `lesson.ipynb` — notebook, w którym faktycznie pracujesz nad lekcją
- `README.md` / `README.pl.md` — brief lekcji

`task.py` to miejsce, w którym implementujesz rozwiązanie; `lesson.ipynb` to miejsce, w którym je uruchamiasz, widzisz wyniki i piszesz interpretację — traktuj notebook jak swój raport analityczny, nie jak brudnopis do pisania kodu od zera.

**Praca nad lekcją:**

1. Przeczytaj `README.md` (albo `README.pl.md`) lekcji, żeby poznać kontekst i pytanie analityczne.
2. Uzupełnij `TODO` w `task.py`.
3. Z katalogu lekcji uruchom `uv run pytest`, żeby sprawdzić swoją pracę.
4. Otwórz `lesson.ipynb` i przejdź przez analizę i refleksję.

Jeśli edytujesz `task.py` po tym, jak już zaimportowałeś/aś go w działającym notebooku, zrestartuj kernel (albo ponownie uruchom komórkę z importem) — Python cache'uje zaimportowane moduły, więc samo ponowne uruchomienie komórki nie podłapie zmiany.

Zacznij od `cases/case_1_regression/lessons/01_defining_the_question/`.

## Dwujęzyczność

Każdy plik Markdown ma polski odpowiednik (`README.md` → `README.pl.md`). Angielski jest źródłem prawdy; kod, komentarze i komunikaty commitów są wyłącznie po angielsku. Dotyczy to również notebooków lekcji (`lesson.ipynb`) — ich tekst instruktażowy jest wyłącznie po angielsku, nawet tam, gdzie towarzyszący `README.pl.md` jest po polsku; brief lekcji jest dwujęzyczny, przestrzeń, w której piszesz kod, nie jest.

## Współtworzenie

Zobacz [`CONTRIBUTING.pl.md`](CONTRIBUTING.pl.md) po lokalne komendy deweloperskie, kontrakt dwujęzyczny i jak dodać lekcję lub case. Znalazłeś/znalazłaś błąd w lekcji, problem z tłumaczeniem, albo chcesz zaproponować nowy case lub lekcję? [Otwórz issue](https://github.com/michalmaj/data-science-casebook/issues/new/choose) — wybór szablonu skieruje Cię do właściwego formularza.

## Licencja

[MIT](LICENSE)

# Lekcja 4 — Modelowanie

## Głos mentora

"Tu ścieżka faktycznie się rozdziela. Regresja, klasyfikacja, klasteryzacja — cokolwiek wymaga Twój zbiór danych, najpierw dopasuj baseline. Jeśli nie potrafisz go pobić, nie masz jeszcze modelu, masz zbieg okoliczności."

## Cel lekcji

Podzielić dane, dopasować baseline i dopasować pierwszy prawdziwy model — używając techniki, jakiej faktycznie wymaga Twój wybrany zbiór danych.

## Pytanie analityczne dnia

Czy Twój pierwszy model faktycznie radzi sobie lepiej niż najprostszy możliwy baseline dla Twojego problemu?

## Co dostajesz

- Ten sam zbiór danych, który wybrałeś/wybrałaś w Lekcji 1
- `task.py` — pięć funkcji: `load_clean_dataset` (Lekcje 1-3, odtworzona), `split_dataset` (nowa, działa dla dowolnego zbioru) oraz po jednej funkcji dopasowującej na technikę: `fit_regression_baseline_and_model`, `fit_classification_baseline_and_model`, `fit_clustering_model` (nowe — użyj tylko tej, która pasuje do Twojego zbioru)
- `lesson.ipynb` — notebook, w którym dopasujesz swój baseline i model

## Praca w notebooku

- Wczytaj i podziel swój zbiór danych.
- Uruchom tylko tę komórkę z funkcją dopasowującą, która pasuje do typu problemu Twojego zbioru.
- Porównaj swój model z baseline'em.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Od tej lekcji te testy sprawdzają strukturę i rozsądność (kształty, zbieżność, „model pokonuje baseline na danych treningowych”), a nie dokładne wartości predykcji — nie ma jednego poprawnego modelu, gdy sam/sama wybierasz cechy.

## Zadanie domowe

Dwa do trzech zdań: używając konkretnego zestawu cech, który wybrałeś/wybrałaś (sugerowanego albo własnego), o ile lepszy jest Twój model od baseline'u i czy ta różnica jest wystarczająco duża, żeby miała znaczenie dla Twojego pytania z Lekcji 1?

## Refleksja

Mentor pyta: model, który dobrze dopasowuje się do danych treningowych, niekoniecznie zadziała na nowych danych. Co wzbudziłoby w Tobie podejrzenie, że ten model po prostu zapamiętuje swój zbiór treningowy, zamiast uczyć się czegoś rzeczywistego?

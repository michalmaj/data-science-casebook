# Lekcja 4 — Modelowanie

**Szacowany czas:** 55-65 min

## Efekty uczenia się

- Będziesz umieć zastosować tę samą generyczną sekwencję split/impute/(scale) niezależnie od tego, czy Twój problem okaże się regresją, klasyfikacją, czy klasteryzacją.
- Będziesz umieć dopasować model bazowy i pierwszy realny model pasujący do techniki, której faktycznie wymaga Twój własny wybrany dataset.
- Będziesz umieć powiedzieć, co daje "jeden generyczny pipeline na trzy techniki", a gdzie przestaje to wystarczać dla Twojego konkretnego problemu.

## Głos mentora

"Tu ścieżka faktycznie się rozdziela. Regresja, klasyfikacja, klasteryzacja — cokolwiek wymaga Twój zbiór danych, najpierw dopasuj baseline. Jeśli nie potrafisz go pobić, nie masz jeszcze modelu, masz zbieg okoliczności."

## Cel lekcji

Podzielić dane, dopasować baseline i dopasować pierwszy prawdziwy model — używając techniki, jakiej faktycznie wymaga Twój wybrany zbiór danych.

## Pytanie analityczne dnia

Czy Twój pierwszy model faktycznie radzi sobie lepiej niż najprostszy możliwy baseline dla Twojego problemu?

## Co dostajesz

- Ten sam zbiór danych, który wybrałeś/wybrałaś w Lekcji 1
- `task.py` — siedem funkcji: `load_dataset` (bez czyszczenia, zastępuje starą `load_clean_dataset`), `split_dataset` (działa dla dowolnego zbioru — przyjmuje opcjonalny `stratify_column`, żeby zachować balans klas między train/test przy klasyfikacji), `impute_missing` (uzupełnia braki statystykami wyłącznie ze zbioru treningowego, w kolumnach cech, które wskażesz, zastosowanymi do obu zbiorów), `scale_features` (standaryzuje cechy do zerowej średniej/jednostkowej wariancji, potrzebna przed klasteryzacją — zwraca też dopasowany scaler), oraz po jednej funkcji dopasowującej na technikę: `fit_regression_baseline_and_model`, `fit_classification_baseline_and_model`, `fit_clustering_model` (użyj tylko tej, która pasuje do Twojego zbioru)
- `lesson.ipynb` — notebook, w którym dopasujesz swój baseline i model

## Praca w notebooku

- Ustaw `DATASET_NAME` zgodnie z tym, co wybrałeś/wybrałaś w Lekcji 1 — komórka podglądu pokaże rozmiary Twojego podziału train/test.
- Uruchom komórkę poniżej — wczytuje, dzieli, imputuje (statystykami wyłącznie ze zbioru treningowego) i, dla klasteryzacji, skaluje Twój zbiór danych, a następnie dopasowuje model, wszystko w jednym miejscu.
- Porównaj swój model z baseline'em.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Od tej lekcji te testy sprawdzają zarówno strukturę/rozsądność (kształty, zbieżność, „model pokonuje baseline na danych treningowych”), jak i dokładne wartości dla sugerowanych zestawów cech (np. sam baseline, liczbę współczynników modelu) — potwierdzają, że Twoje generyczne funkcje działają poprawnie, a nie że Twój konkretny wybór cech jest najlepszy. Nie ma jednego poprawnego modelu, gdy sam/sama wybierasz cechy, i te testy tego wyboru nie oceniają.

## Zadanie domowe

Dwa do trzech zdań: używając konkretnego zestawu cech, który wybrałeś/wybrałaś (sugerowanego albo własnego), o ile lepszy jest Twój model od baseline'u i czy ta różnica jest wystarczająco duża, żeby miała znaczenie dla Twojego pytania z Lekcji 1?

## Refleksja

Mentor pyta: model, który dobrze dopasowuje się do danych treningowych, niekoniecznie zadziała na nowych danych. Co wzbudziłoby w Tobie podejrzenie, że ten model po prostu zapamiętuje swój zbiór treningowy, zamiast uczyć się czegoś rzeczywistego?

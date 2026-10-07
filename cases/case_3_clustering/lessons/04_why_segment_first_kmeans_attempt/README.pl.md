# Lekcja 4 — Po co segmentować? Pierwsza próba z KMeans

**Szacowany czas:** 40-50 min

## Po co to robimy

Aurora Stream nie chce modelu dla samego modelu — chce wiedzieć, czy "traktuj każdego subskrybenta tak samo" to rzeczywiście zły pomysł. Sprawdźmy to: dopasujmy model KMeans, wybierzmy na razie jakąś okrągłą liczbę klastrów i zobaczmy, co z tego wyjdzie. Czy to *właściwa* liczba — to problem na następną lekcję.

Pytanie na dziś: jeśli podzielimy subskrybentów na kilka grup wyłącznie na podstawie ich zachowania podczas oglądania, otrzymamy grupy różniące się znacząco wielkością — i czy samo to mówi coś wartego działania?

## Co masz zrobić

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-3.
- W `task.py` zaimplementuj `load_scaled_features`, `fit_kmeans`.
- W notebooku: wczytaj ponownie przeskalowaną tabelę per subskrybent, dopasuj `fit_kmeans` z domyślnym `k=4` i sprawdź wynikową bezwładność (inertia). Zobacz, ilu subskrybentów trafiło do każdego z czterech klastrów.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Jedno zdanie: dwa z czterech klastrów są zauważalnie mniejsze od pozostałych dwóch. Co warto by sprawdzić, zanim zarekomendujesz Aurora Stream zbudowanie oferty retencyjnej wokół jednego z mniejszych? I: `k=4` zostało wybrane bez żadnego rzeczywistego uzasadnienia — to po prostu okrągła liczba. Co to oznacza dla rekomendacji biznesowej, jeśli "segmenty", które zaraz opiszesz, zależą od liczby, której nikt jeszcze nie obronił?

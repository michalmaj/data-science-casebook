# Lekcja 4 — Po co segmentować? Pierwsza próba z KMeans

**Szacowany czas:** 40-50 min

## Efekty uczenia się

- Będziesz umieć uzasadnić biznesowo potrzebę segmentacji, zanim dopasujesz jakikolwiek model.
- Będziesz umieć dopasować pierwszy model `KMeans` przy dowolnie wybranym k i krytycznie odczytać rozmiary klastrów, nie jako dowód, że podział ma już jakikolwiek sens.

## Głos mentora

"Aurora Stream nie chce modelu dla samego modelu — chcą wiedzieć, czy 'traktuj każdego subskrybenta tak samo' to rzeczywiście zły pomysł. Sprawdźmy to. Dopasuj model KMeans, wybierz na razie jakąś okrągłą liczbę klastrów i zobacz, co z tego wyjdzie. Nie martw się jeszcze, czy to *właściwa* liczba — to problem na następną lekcję."

## Cel lekcji

Uzasadnić biznesowo sens segmentacji, a następnie dopasować pierwszy model `KMeans` na czterech przeskalowanych cechach Aurora Stream przy dowolnie wybranym `k`.

## Pytanie analityczne dnia

Jeśli podzielisz subskrybentów na kilka grup wyłącznie na podstawie ich zachowania podczas oglądania, czy otrzymasz grupy różniące się znacząco wielkością — i czy samo to mówi coś wartego działania?

## Co dostajesz

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-3
- `task.py` — dwie funkcje do zaimplementowania: `load_scaled_features`, `fit_kmeans`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

- Wczytaj ponownie przeskalowaną tabelę per subskrybent.
- Dopasuj `fit_kmeans` z domyślnym `k=4` i sprawdź wynikową bezwładność (inertia).
- Zobacz, ilu subskrybentów trafiło do każdego z czterech klastrów.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

Jedno zdanie: jeden z czterech klastrów jest dużo mniejszy od pozostałych. Co warto by sprawdzić, zanim zarekomendujesz Aurora Stream zbudowanie wokół niego oferty retencyjnej?

## Refleksja

Mentor pyta: na razie `k=4` zostało wybrane bez żadnego rzeczywistego uzasadnienia — to po prostu okrągła liczba. Co to oznacza dla rekomendacji biznesowej, jeśli „segmenty”, które zaraz opiszesz, zależą od liczby, której nikt jeszcze nie obronił?

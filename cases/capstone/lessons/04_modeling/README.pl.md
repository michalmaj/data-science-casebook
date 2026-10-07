# Lekcja 4 — Modelowanie

**Szacowany czas:** 55-65 min

## Decyzja do podjęcia

Tu ścieżka faktycznie się rozdziela. Regresja, klasyfikacja, klasteryzacja — cokolwiek wymaga wybrany zbiór danych, dopasuj najpierw model bazowy. Jeśli nie da się go pobić, nie ma jeszcze modelu — jest zbieg okoliczności.

Podział poniżej używa tego samego sposobu co w Lekcji 2 (i w Lekcji 3, dla dwóch ścieżek predykcyjnych) — ta lekcja nie wprowadza nowego podziału, tylko ponownie wykorzystuje ten, na którym opierały się już kroki jakości danych i eksploracji.

## Masz do dyspozycji

- `task.py` — siedem funkcji: `load_dataset` (bez czyszczenia, zastępuje starą `load_clean_dataset`), `split_dataset`, `impute_missing`, `scale_features` (standaryzuje cechy — zdecyduj samodzielnie, czy wybrana technika tego wymaga, i uzasadnij to w notatkach; zwraca też dopasowany scaler), oraz po jednej funkcji dopasowującej na technikę: `fit_regression_baseline_and_model`, `fit_classification_baseline_and_model`, `fit_clustering_model` (użyj tylko tej, która pasuje do wybranego zbioru).
- W notebooku: ustaw `DATASET_NAME`, uruchom komórkę, która wczytuje, dzieli, imputuje i (dla klasteryzacji) skaluje, a potem dopasowuje model. Porównaj wynik z modelem bazowym.

## Uzasadnij

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Od tej lekcji te testy sprawdzają zarówno strukturę/rozsądność, jak i dokładne wartości dla sugerowanych zestawów cech — potwierdzają, że generyczne funkcje działają poprawnie, nie że konkretny wybór cech jest najlepszy. Nie ma jednego poprawnego modelu, gdy cechy wybiera się samodzielnie, i te testy tego wyboru nie oceniają.

Dwa do trzech zdań: używając wybranego zestawu cech (sugerowanego albo własnego), o ile lepszy jest model od modelu bazowego, i czy ta różnica jest wystarczająco duża, żeby miała znaczenie dla pytania z Lekcji 1? Na ścieżce klasteryzacji dopisz też jedno zdanie uzasadniające decyzję o skalowaniu cech przed dopasowaniem (albo o jej braku). I: model, który dobrze dopasowuje się do danych treningowych, niekoniecznie zadziała na nowych danych. Co wzbudziłoby podejrzenie, że model po prostu zapamiętuje swój zbiór treningowy, zamiast uczyć się czegoś rzeczywistego?

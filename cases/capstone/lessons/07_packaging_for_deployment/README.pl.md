# Lekcja 7 (Opcjonalna) — Pakowanie preprocessingu jako Pipeline

**Szacowany czas:** 40-55 min

## Decyzja do podjęcia

Ta lekcja nie jest oceniana — potraktuj ją jako rundę bonusową. Sześć lekcji temu wybrano zbiór danych z kolumną lub dwiema, których wcześniejsze lekcje nigdy nie pozwoliły użyć. Użyjmy jednej naprawdę i spakujmy cały krok preprocessingu tak, jak przekazałoby się go komuś innemu, zamiast trzech funkcji, które trzeba wywołać w dokładnie właściwej kolejności.

## Masz do dyspozycji

- `task.py` — dwie funkcje odtworzone z Lekcji 4-6 (`load_dataset`, `split_dataset`), plus siedem nowych: `build_preprocessor` (wspólny budowniczy `ColumnTransformer`), po jednej funkcji `build_and_fit_*_pipeline` na typ problemu, i po jednej `evaluate_pipeline_*` na typ problemu.
- W notebooku: ustaw `DATASET_NAME`, uruchom komórkę dyspozycyjną — wczytuje, dzieli, buduje `Pipeline` łączący `ColumnTransformer` z modelem, dopasowuje i ocenia. Porównaj wynik do tego z Lekcji 6 — zobacz notatkę w notebooku o tym, dlaczego mogła zmienić się więcej niż jedna rzecz naraz.

## Uzasadnij

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Podobnie jak w Lekcjach 4-6, te sprawdzenia weryfikują dokładne wartości dla sugerowanych zestawów cech — nie mogą powiedzieć, czy dodanie kategorycznej kolumny było dobrym wyborem analitycznym, tylko że kod `Pipeline`/`ColumnTransformer` działa poprawnie.

Brak zadania — lekcja opcjonalna i nieoceniana. Dla ćwiczenia: dwa-trzy zdania o tym, czy dodana kategoryczna kolumna faktycznie pomogła modelowi, w komórce "Your notes". I: `ColumnTransformer` pozwolił potraktować kolumny numeryczne i kategoryczne różnie w jednym obiekcie. Co poszłoby nie tak przy próbie dopasowania `StandardScaler` bezpośrednio do kolumny kategorycznej, zamiast skierować ją do `OneHotEncoder`?

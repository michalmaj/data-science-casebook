# Lekcja 7 (Opcjonalna) — Pakowanie preprocessingu jako Pipeline

**Szacowany czas:** 40-55 min

## Efekty uczenia się

- Będziesz umieć zastąpić ręczną sekwencję imputacja→skalowanie→dopasowanie jednym dopasowanym `sklearn.pipeline.Pipeline`.
- Będziesz umieć użyć `ColumnTransformer`, żeby wprowadzić kategoryczną kolumnę, którą Twój dataset zawsze miał, ale nigdy nie użyłeś/nie użyłaś jej jako cechy, i sprawdzić, czy faktycznie pomaga.

## Głos mentora

"Ta lekcja nie jest oceniana — potraktuj ją jako rundę bonusową. Sześć lekcji
temu wybrałeś/wybrałaś dataset z kolumną lub dwiema, których wcześniejsze
lekcje nigdy nie pozwoliły Ci użyć. Użyjmy jednej naprawdę i spakujmy cały
krok preprocessingu tak, jak przekazałbyś/przekazałabyś go komuś innemu,
zamiast trzech funkcji, które trzeba wywołać w dokładnie właściwej
kolejności."

## Cel lekcji

Zastąpić ręczną sekwencję `impute_missing` -> `scale_features` -> `fit_*` z
Lekcji 4-6 jednym dopasowanym `sklearn.pipeline.Pipeline`, i użyć
`sklearn.compose.ColumnTransformer`, żeby wprowadzić kategoryczną kolumnę,
którą Twój dataset zawsze miał, ale nigdy nie użyłeś/nie użyłaś jej jako
cechy.

## Pytanie analityczne dnia

Czy spakowanie preprocessingu w jeden obiekt zmienia Twoje wyniki — i czy
faktyczne użycie kategorycznej kolumny, którą oferuje Twój dataset, pomaga,
szkodzi, czy nic nie zmienia?

## Co dostajesz

- Ten sam dataset, który wybrałeś/wybrałaś w Lekcji 1
- `task.py` — dwie funkcje odtworzone z Lekcji 4-6 (`load_dataset`,
  `split_dataset`), plus siedem nowych: `build_preprocessor` (wspólny
  budowniczy `ColumnTransformer`), po jednej funkcji `build_and_fit_*_pipeline`
  na typ problemu, i po jednej `evaluate_pipeline_*` na typ problemu (użyj
  tylko tych pasujących do Twojego datasetu)
- `lesson.ipynb` — notebook, w którym zbudujesz i ocenisz swój pipeline

## Praca w notebooku

- Ustaw `DATASET_NAME` na dataset, który wybrałeś/wybrałaś w Lekcji 1.
- Uruchom komórkę dyspozycyjną — wczytuje, dzieli (poza klasteryzacją, która
  nigdy się nie dzieli), buduje `Pipeline` łączący `ColumnTransformer` z
  Twoim modelem, dopasowuje go i ocenia, wszystko w jednym miejscu.
- Porównaj wynik do tego, co dostałeś/dostałaś w Lekcji 6 — zobacz notatkę w
  notebooku o tym, dlaczego mogła zmienić się więcej niż jedna rzecz naraz.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Podobnie jak
w Lekcjach 4-6, te sprawdzenia weryfikują dokładne wartości dla
sugerowanych zestawów cech — nie mogą powiedzieć, czy dodanie kategorycznej
kolumny Twojego datasetu było dobrym wyborem analitycznym, tylko że Twój kod
`Pipeline`/`ColumnTransformer` działa poprawnie.

## Zadanie domowe

Brak — ta lekcja jest opcjonalna i nieoceniana. Jeśli chcesz ćwiczenia: dwa-
trzy zdania o tym, czy dodana przez Ciebie kategoryczna kolumna faktycznie
pomogła Twojemu modelowi, w komórce "Your notes".

## Refleksja

Mentor pyta: `ColumnTransformer` pozwolił Ci potraktować kolumny numeryczne i
kategoryczne różnie w jednym obiekcie. Co poszłoby nie tak, gdybyś spróbował/
spróbowała dopasować `StandardScaler` bezpośrednio do kolumny kategorycznej
zamiast skierować ją do `OneHotEncoder`?

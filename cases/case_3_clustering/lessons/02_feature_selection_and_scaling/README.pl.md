# Lekcja 2 — Dobór i skalowanie cech

**Szacowany czas:** 40-50 min

## Po co to robimy

Liczba sesji waha się od 0 do 65, minuty oglądania od 0 do tysięcy, staż w setkach dni. Wrzuć to prosto do algorytmu opartego na odległości, a staż zdominuje wszystko inne. Trzeba to naprawić, zanim cokolwiek pogrupujemy.

Pytanie na dziś: które z cech subskrybentów Aurora Stream faktycznie należą do modelu grupowania, i co się z nimi dzieje, gdy wszystkie znajdą się na tej samej skali?

## Co masz zrobić

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcji 1.
- W `task.py` zaimplementuj `load_subscriber_features`, `scale_features`.
- W notebooku: wczytaj ponownie tabelę per subskrybent, przeskaluj cztery cechy behawioralne. Potwierdź, że przeskalowane kolumny mają średnią 0 i odchylenie standardowe 1.

## Na co zwrócić uwagę

Cecha z największym surowym zakresem wygrywa obliczenie odległości, nie ta z największym znaczeniem biznesowym — chyba że wszystkie są na tej samej skali. To właśnie robi skalowanie: nie poprawia znaczenia cech, tylko usuwa przewagę wynikającą wyłącznie z jednostek.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Jedno zdanie: dlaczego `plan_tier` i `country` nie zostały uwzględnione w `scale_features`? I: `tenure_days` waha się od 35 do 895 — prawie 25-krotnie. `session_count` waha się od 0 do 65. Przed skalowaniem, która z tych dwóch cech zdominowałaby obliczenie odległości, i mniej więcej o ile?

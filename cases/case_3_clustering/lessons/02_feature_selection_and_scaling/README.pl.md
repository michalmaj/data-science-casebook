# Lekcja 2 — Dobór i skalowanie cech

**Szacowany czas:** 40-50 min

## Efekty uczenia się

- Będziesz umieć zdecydować, które kolumny faktycznie opisują zachowanie, wg którego chcesz segmentować, a które nie należą do modelu.
- Będziesz umieć przeskalować cechy tak, żeby żadna z nich nie zdominowała algorytmu opartego na odległości tylko przez swoje surowe jednostki.

## Głos mentora

"Liczba sesji waha się od 0 do 65, minuty oglądania od 0 do tysięcy, staż w setkach dni. Wrzuć to prosto do algorytmu opartego na odległości, a staż zdominuje wszystko inne. Napraw to, zanim cokolwiek pogrupujesz."

## Cel lekcji

Zdecydować, które kolumny faktycznie opisują zachowanie oglądania, i przeskalować je tak, żeby żadna pojedyncza cecha nie dominowała obliczeń odległości.

## Pytanie analityczne dnia

Które z cech subskrybentów Aurora Stream faktycznie należą do modelu grupowania, i co się z nimi dzieje, gdy wszystkie znajdą się na tej samej skali?

## Co dostajesz

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcji 1
- `task.py` — dwie funkcje do zaimplementowania: `load_subscriber_features`, `scale_features`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

- Wczytaj ponownie tabelę per subskrybent.
- Przeskaluj cztery cechy behawioralne.
- Potwierdź, że przeskalowane kolumny faktycznie mają średnią 0 i odchylenie standardowe 1.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

Jedno zdanie: dlaczego `plan_tier` i `country` nie zostały uwzględnione w `scale_features`?

## Refleksja

Mentor pyta: `tenure_days` waha się od 35 do 895 — prawie 25-krotnie. `session_count` waha się od 0 do 65. Przed skalowaniem, która z tych dwóch cech zdominowałaby obliczenie odległości, i mniej więcej o ile?

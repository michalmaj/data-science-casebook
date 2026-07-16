# Lekcja 7 — Korelacja vs. predykcja vs. przyczynowość

**Szacowany czas:** 35-45 min

## Efekty uczenia się

- Będziesz umieć ponownie dopasować model na różnych podzestawach cech, żeby sprawdzić, czy historia współczynnika przetrwa dodanie skorelowanych zmiennych.
- Będziesz umieć odróżnić współczynnik, który możesz interpretować przyczynowo, od takiego, którego wolno Ci użyć tylko do predykcji.
- Będziesz umieć zdecydować, na podstawie konkretnego testu, a nie intuicji, które wnioski są bezpieczne do przekazania klientowi jako rekomendacja przyczynowa.

## Głos mentora

"Znalazłeś/znalazłaś to, co koreluje z opóźnieniem, i to, co poprawia predykcję. Żadne z tych dwóch nie mówi Ci, co *zmienić*, żeby naprawić opóźnienie. To trzy różne pytania, a TransLine zaraz zada Ci to trzecie — bo to jedyne, na które faktycznie mogą coś poradzić."

## Cel lekcji

Nauczyć się konkretnego sposobu sprawdzania, czy historia stojąca za współczynnikiem jest wiarygodna — przez sprawdzenie, czy przetrwa dodanie innych, skorelowanych zmiennych do modelu.

## Pytanie analityczne dnia

Którym współczynnikom modelu możesz zaufać na tyle, żeby zbudować na nich rekomendację, a których w ogóle nie masz prawa interpretować?

## Co dostajesz

- Te same podzielone dane co w Lekcji 5-6 (odtworzone tutaj przez `load_shipments`, `split_shipments`, `impute_driver_experience`)
- `task.py` — dwie nowe funkcje: `fit_model_on` (trenowanie na dowolnym zestawie cech, nie tylko stałym) i `coefficient_for` (odczyt współczynnika konkretnej cechy)
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Porównaj współczynnik `num_stops` wytrenowany samodzielnie vs. razem z innymi cechami — zauważ, jak mało się zmienia.
4. Porównaj współczynnik `distance_km` wytrenowany samodzielnie vs. razem z `planned_duration_min` — zauważ, jak bardzo się zmienia, i dlaczego (sprawdź ich korelację).
5. Przeczytaj komórki dyskusyjne i zastanów się, na które czynniki TransLine mogłoby realnie wpłynąć.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` wybierz jeden czynnik i oddziel to, co faktycznie wiesz (skorelowany? predykcyjny?), od tego, czego się tylko domyślasz (przyczynowy? możliwy do zaadresowania?).

## Refleksja

Mentor pyta: współczynnik `num_stops` był stabilny w różnych zestawach cech, co jest dobrym znakiem — ale sama stabilność to wciąż nie dowód przyczynowości. Jaki jest konkretny sposób, w jaki `num_stops` mógłby być proxy dla czegoś innego, zamiast bezpośrednią przyczyną opóźnienia?

# Lekcja 7 — Korelacja vs. predykcja vs. przyczynowość

**Szacowany czas:** 35-45 min

## Po co to robimy

Już wiadomo, co koreluje z opóźnieniem i co poprawia predykcję. Żadne z tych dwóch nie mówi, co *zmienić*, żeby naprawić opóźnienie. To trzy różne pytania, a TransLine zaraz zada to trzecie — bo to jedyne, na które może coś poradzić.

Pytanie na dziś: którym współczynnikom modelu można zaufać na tyle, żeby zbudować na nich rekomendację, a których nie wolno w ogóle interpretować?

## Co masz zrobić

- Te same podzielone dane co w Lekcji 3 i to samo podejście do dopasowania modelu co w Lekcji 5 (odtworzone tutaj przez `load_shipments`, `split_shipments`, `impute_driver_experience`).
- W `task.py` zaimplementuj dwie nowe funkcje: `fit_model_on` (trenowanie na dowolnym zestawie cech, nie tylko stałym) i `coefficient_for` (odczyt współczynnika konkretnej cechy).
- W notebooku: porównaj współczynnik `num_stops` wytrenowany samodzielnie vs. razem z innymi cechami — zauważ, jak mało się zmienia. Porównaj współczynnik `distance_km` wytrenowany samodzielnie vs. razem z `planned_duration_min` — zauważ, jak bardzo się zmienia, i sprawdź ich korelację, żeby zrozumieć czemu.

## Na co zwrócić uwagę

Konkretny sposób sprawdzenia, czy historia za współczynnikiem jest wiarygodna: sprawdzić, czy przetrwa dodanie innych, skorelowanych zmiennych do modelu. Współczynnik, który się nie zmienia, zasługuje na więcej zaufania niż ten, który skacze w zależności od tego, co jeszcze jest w modelu — ale stabilność współczynnika to wciąż nie dowód przyczynowości, tylko argument za tym, że warto go dalej sprawdzać.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" wybierz jeden czynnik i oddziel to, co wiesz na pewno (skorelowany? predykcyjny?), od tego, czego się tylko domyślasz (przyczynowy? możliwy do zaadresowania?). I: współczynnik `num_stops` był stabilny w różnych zestawach cech, co jest dobrym znakiem — jaki jest konkretny sposób, w jaki `num_stops` mógłby być proxy dla czegoś innego, zamiast bezpośrednią przyczyną opóźnienia?

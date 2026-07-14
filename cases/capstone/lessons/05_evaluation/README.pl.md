# Lekcja 5 — Ewaluacja

## Głos mentora

"Lekcja 4 pokazała Ci tylko, jak model radzi sobie z danymi, które już widział. To nie jest ewaluacja, to próba generalna. Teraz sprawdzisz, czy faktycznie się czegoś nauczył."

## Cel lekcji

Ocenić Twój baseline i model z Lekcji 4 na danych testowych, których model nigdy nie widział podczas dopasowywania — używając metryki faktycznie pasującej do Twojego typu problemu.

## Pytanie analityczne dnia

Czy wynik Twojego modelu na zbiorze testowym nadal pokonuje baseline, tak jak jego wynik na zbiorze treningowym w Lekcji 4?

## Co dostajesz

- Ten sam zbiór danych, który wybrałeś/wybrałaś w Lekcji 1
- `task.py` — siedem funkcji z Lekcji 4, odtworzonych, plus cztery nowe: `evaluate_regression`, `evaluate_classification`, `evaluate_clustering`, `cluster_stability` (użyj tylko tych, które pasują do Twojego zbioru)
- `lesson.ipynb` — notebook, w którym uruchomisz cały swój pipeline i go ocenisz

## Praca w notebooku

- Uruchom tylko komórkę pasującą do typu problemu Twojego zbioru — wczytuje, dzieli, imputuje, dopasowuje i ocenia w jednym miejscu (komórka klasteryzacji dodatkowo skaluje cechy przed dopasowaniem).
- Porównaj wynik na zbiorze testowym z tym, co zobaczyłeś/zobaczyłaś w Lekcji 4.
- Zdecyduj, czy model jest wystarczająco dobry, żeby na jego podstawie działać.

**Uwaga o ocenie klasteryzacji:** w przeciwieństwie do regresji i klasyfikacji, klasteryzacja nie jest tutaj oceniana na zbiorze testowym, którego model nie widział — silhouette score z `evaluate_clustering` jest liczony na tych samych danych, na których model był dopasowany, co jest standardem dla oceny *jakości* klastrów (zgodnie z podejściem Case 3). Komórka klasteryzacji uruchamia też `cluster_stability`, która sprawdza coś, co zbiór testowy daje regresji/klasyfikacji za darmo: czy wynik utrzymałby się na innej próbce. Ponowne dopasowanie na powtarzanych podpróbkach i porównanie przypisań klastrów przez Adjusted Rand Index (ARI — 1,0 oznacza identyczne, blisko 0 oznacza praktycznie losowe) mówi Ci, czy Twoje segmenty są prawdziwe, czy są artefaktem akurat tego zbioru danych.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Te testy sprawdzają liczby ewaluacji dla sugerowanych zestawów cech — nie mogą powiedzieć Ci, czy Twój model jest wystarczająco dobry dla Twojego faktycznego pytania z Lekcji 1.

## Zadanie domowe

Dwa do trzech zdań: czy faktycznie zarekomendowałbyś/zarekomendowałabyś ten model swojemu klientowi z Lekcji 1 w obecnej formie, czy wymaga jeszcze pracy? Bądź konkretny/konkretna co do tego, co mówi Ci wynik ewaluacji.

## Refleksja

Mentor pyta: dla klasyfikacji i regresji masz teraz zarówno wynik na zbiorze treningowym (Lekcja 4), jak i na zbiorze testowym (ta lekcja). Gdyby te dwie liczby opowiadały bardzo różne historie, co mówiłoby to o Twoim modelu — i której liczbie ufałbyś/ufałabyś bardziej, i dlaczego?

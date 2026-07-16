# Lekcja 5 — Wybór k: porównanie rozwiązań

**Szacowany czas:** 40-50 min

## Efekty uczenia się

- Będziesz umieć porównać rozwiązania `KMeans` dla różnych k, używając zarówno inercji (metoda łokcia), jak i silhouette score.
- Będziesz umieć poradzić sobie z sytuacją, gdy dwie standardowe metryki doboru modelu są ze sobą sprzeczne, i zdecydować, która z nich faktycznie powinna kierować wyborem.

## Głos mentora

"k=4 z Lekcji 4 było zgadywanką i mówiłem Ci to już wtedy. Teraz naprawdę porównajmy rozwiązania. Dopasuj KMeans dla różnych wartości k, spójrz na inertia tak, jak chce tego metoda łokcia, a potem spójrz na silhouette score. Nie zdziw się, jeśli nie wskażą tej samej odpowiedzi."

## Cel lekcji

Porównać rozwiązania `KMeans` dla różnych wartości k, używając dwóch metryk — inertia (metoda łokcia) i silhouette score — i sprawdzić, czy zgadzają się co do "najlepszego" k.

## Pytanie analityczne dnia

Czy łokieć na wykresie inertia i szczyt silhouette score wskazują tę samą liczbę klastrów — a jeśli nie, która metryka powinna faktycznie kierować decyzją?

## Co dostajesz

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-4
- `task.py` — dwie funkcje do zaimplementowania: `load_scaled_features`, `cluster_metrics_by_k`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

- Wczytaj ponownie przeskalowaną tabelę per subskrybent.
- Policz `cluster_metrics_by_k` dla k od 2 do 8.
- Porównaj, gdzie krzywa inertia się załamuje, z tym, które k ma najwyższy silhouette score.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

Jedno zdanie: najwyższy silhouette score należy do mniejszego k niż zgadywanka z Lekcji 4 (k=4). Co powiedziałbyś/powiedziałabyś Aurora Stream o poleganiu na jednej metryce przy wyborze "właściwej" liczby segmentów?

## Refleksja

Mentor pyta: inertia spada gładko w całym zakresie k=2 do 8, bez jednego wyraźnego łokcia — samo inertia broni niemal każdego k. Silhouette score za to wyraźnie osiąga szczyt przy jednej wartości. Co to oznacza dla rekomendacji biznesowej, gdy dwie "standardowe" metody wyboru k nie są ze sobą zgodne?

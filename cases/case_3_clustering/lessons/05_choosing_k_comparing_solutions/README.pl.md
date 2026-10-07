# Lekcja 5 — Wybór k: porównanie rozwiązań

**Szacowany czas:** 40-50 min

## Po co to robimy

k=4 z Lekcji 4 było zgadywanką. Teraz porównajmy rozwiązania naprawdę: dopasujmy KMeans dla różnych wartości k, spójrzmy na inertia tak, jak chce tego metoda łokcia, a potem na silhouette score. Nie ma gwarancji, że wskażą tę samą odpowiedź.

Pytanie na dziś: czy łokieć na wykresie inertia i szczyt silhouette score wskazują tę samą liczbę klastrów — a jeśli nie, która metryka powinna kierować decyzją?

## Co masz zrobić

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-4.
- W `task.py` zaimplementuj `load_scaled_features`, `cluster_metrics_by_k`, `compare_feature_sets`.
- W notebooku: policz `cluster_metrics_by_k` dla k od 2 do 8, porównaj gdzie krzywa inertia się załamuje z tym, które k ma najwyższy silhouette score. Odpal `compare_feature_sets` przy k=2 i jeszcze raz przy k=4, używając `REDUCED_FEATURE_COLUMNS` (tylko `total_minutes_watched` i `tenure_days`) wobec pełnego czterocechowego zestawu — sprawdź, czy zgłoszona segmentacja zależy od tego, jakie kolumny podano KMeans.

## Szczyt silhouette to nie czysta lista rankingowa, i nie jest jedynym wyborem, który się liczy

Silhouette score osiąga wyraźny szczyt przy k=2 — to jest prawdziwe i warte traktowania na serio. Ale to nie jest lista rankingowa, do której można się wycofać o jeden krok, jeśli nie ufasz wynikowi na szczycie: k=3 do k=8 wahają się między ~0,44 i ~0,47 bez konsekwentnego porządku (k=3 bije k=4, k=4 przegrywa z k=5 i k=6, k=6 bije k=7 i k=8) — nie ma tam czystego "drugiego miejsca". Silhouette porównał rozwiązania, które faktycznie dopasowano, w geometrii zdefiniowanej przez te cztery cechy; nie przeskanował każdej możliwej liczby segmentów i nie uszeregował ich.

Ta "geometria zdefiniowana przez cztery cechy" ma większe znaczenie, niż mogłoby się wydawać. `compare_feature_sets` dopasowuje to samo k na pełnym `FEATURE_COLUMNS` i na `REDUCED_FEATURE_COLUMNS` — jeden reprezentatywny sygnał zaangażowania (`total_minutes_watched`) plus `tenure_days`, odrzucając `session_count` i dokładnie wyliczony `avg_minutes_per_session` (Lekcja 3). Przy k=2 oba zestawy cech zgadzają się całkowicie (`ari = 1,0`) — co uspokaja, ale nie dlatego, że k=2 jest jakoś odporne na wybór cech. Przy k=4 nie zgadzają się (`ari ≈ 0,977`): kilku subskrybentów trafia do innych klastrów w zależności od użytych kolumn. A silhouette zredukowanego zestawu jest nawet wyższe niż pełnego przy k=4 (0,560 wobec 0,444) — mniejsza liczba mniej redundantnych cech może wyglądać czyściej według tej metryki. Część tej różnicy to znana właściwość samego silhouette, nie tylko redundancji: silhouette bywa wyższe w przestrzeniach o mniejszej liczbie wymiarów, więc silhouette liczone na 2 i na 4 cechach nie da się porównywać wprost, jeden do jednego. Tak czy inaczej, to powód, by nie przeceniać jednej liczby silhouette. To, jakie cechy podaje się KMeans, jest częścią definiowania segmentacji, tak jak k — nie wstępnym szczegółem do odhaczenia przed "prawdziwą" decyzją.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Jedno zdanie: najwyższy silhouette score należy do mniejszego k niż zgadywanka z Lekcji 4 (k=4). Co warto powiedzieć Aurora Stream o poleganiu na jednej metryce przy wyborze "właściwej" liczby segmentów? Dodaj drugie zdanie: czy porównanie zestawów cech przy k=2 i k=4 zmienia tę odpowiedź? I: inertia spada gładko w całym zakresie k=2 do 8, bez jednego wyraźnego łokcia — samo inertia broni niemal każdego k. Silhouette score za to wyraźnie osiąga szczyt przy jednej wartości. Co to oznacza dla rekomendacji biznesowej, gdy dwie "standardowe" metody wyboru k nie są ze sobą zgodne?

# Lekcja 5 — Wybór k: porównanie rozwiązań

**Szacowany czas:** 40-50 min

## Efekty uczenia się

- Będziesz umieć porównać rozwiązania `KMeans` dla różnych k, używając zarówno inercji (metoda łokcia), jak i silhouette score.
- Będziesz umieć poradzić sobie z sytuacją, gdy dwie standardowe metryki doboru modelu są ze sobą sprzeczne, i zdecydować, która z nich faktycznie powinna kierować wyborem.
- Będziesz umieć wyjaśnić, czemu ani łokieć inertia, ani szczyt silhouette nie są wyrocznią co do tego, "ile segmentów naprawdę istnieje" — oba tylko porównują konkretne dopasowane rozwiązania, w geometrii zdefiniowanej przez wybrane cechy.
- Będziesz umieć pokazać, w praktyce, że rozwiązanie klasteryzacji zależy od tego, jakie cechy zakodowano w metryce odległości — nie tylko od k.

## Głos mentora

"k=4 z Lekcji 4 było zgadywanką i mówiłem Ci to już wtedy. Teraz naprawdę porównajmy rozwiązania. Dopasuj KMeans dla różnych wartości k, spójrz na inertia tak, jak chce tego metoda łokcia, a potem spójrz na silhouette score. Nie zdziw się, jeśli nie wskażą tej samej odpowiedzi."

## Cel lekcji

Porównać rozwiązania `KMeans` dla różnych wartości k, używając dwóch metryk — inertia (metoda łokcia) i silhouette score — i sprawdzić, czy zgadzają się co do "najlepszego" k.

## Pytanie analityczne dnia

Czy łokieć na wykresie inertia i szczyt silhouette score wskazują tę samą liczbę klastrów — a jeśli nie, która metryka powinna faktycznie kierować decyzją?

## Co dostajesz

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-4
- `task.py` — trzy funkcje do zaimplementowania: `load_scaled_features`, `cluster_metrics_by_k`, `compare_feature_sets`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

- Wczytaj ponownie przeskalowaną tabelę per subskrybent.
- Policz `cluster_metrics_by_k` dla k od 2 do 8.
- Porównaj, gdzie krzywa inertia się załamuje, z tym, które k ma najwyższy silhouette score.
- Odpal `compare_feature_sets` przy k=2 i jeszcze raz przy k=4, używając `REDUCED_FEATURE_COLUMNS` (tylko `total_minutes_watched` i `tenure_days`) wobec pełnego czterocechowego zestawu — sprawdź, czy segmentacja, którą zgłosiłbyś/zgłosiłabyś, faktycznie zależy od tego, jakie kolumny podałeś/podałaś KMeans.

## Szczyt silhouette to nie czysta lista rankingowa, i nie jest jedynym wyborem, który się liczy

Silhouette score osiąga wyraźny szczyt przy k=2 — to jest prawdziwe i warte traktowania na serio. Ale to nie jest lista rankingowa, do której można się wycofać o jeden krok, jeśli nie ufasz wynikowi na szczycie: k=3 do k=8 wahają się między ~0,44 i ~0,47 bez konsekwentnego porządku (k=3 bije k=4, k=4 przegrywa z k=5 i k=6, k=6 bije k=7 i k=8) — nie ma tam czystego "drugiego miejsca". Silhouette porównał rozwiązania, które faktycznie dopasowałeś/dopasowałaś, w geometrii zdefiniowanej przez te cztery cechy; nie przeskanował każdej możliwej liczby segmentów i nie uszeregował ich.

Ta "geometria zdefiniowana przez cztery cechy" ma większe znaczenie, niż mogłoby się wydawać. `compare_feature_sets` dopasowuje to samo k na pełnym `FEATURE_COLUMNS` i na `REDUCED_FEATURE_COLUMNS` — jeden reprezentatywny sygnał zaangażowania (`total_minutes_watched`) plus `tenure_days`, odrzucając `session_count` i dokładnie wyliczony `avg_minutes_per_session` (Lekcja 3). Przy k=2 oba zestawy cech zgadzają się całkowicie (`ari = 1,0`) — co uspokaja, ale nie dlatego, że k=2 jest jakoś odporne na wybór cech. Przy k=4 nie zgadzają się (`ari ≈ 0,977`): kilku subskrybentów trafia do innych klastrów w zależności od użytych kolumn. A silhouette zredukowanego zestawu jest nawet wyższe niż pełnego przy k=4 (0,560 wobec 0,444) — mniejsza liczba mniej redundantnych cech może wyglądać czyściej według tej metryki. Część tej różnicy to znana właściwość samego silhouette, nie tylko redundancji: silhouette bywa wyższe w przestrzeniach o mniejszej liczbie wymiarów, więc silhouette liczone na 2 i na 4 cechach nie da się porównywać wprost, jeden do jednego. Tak czy inaczej, to powód, by nie przeceniać jednej liczby silhouette. To, jakie cechy podajesz, jest częścią definiowania segmentacji, tak jak k — nie wstępnym szczegółem do odhaczenia przed "prawdziwą" decyzją.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

Jedno zdanie: najwyższy silhouette score należy do mniejszego k niż zgadywanka z Lekcji 4 (k=4). Co powiedziałbyś/powiedziałabyś Aurora Stream o poleganiu na jednej metryce przy wyborze "właściwej" liczby segmentów? Dodaj drugie zdanie: czy porównanie zestawów cech przy k=2 i k=4 zmienia Twoją odpowiedź?

## Refleksja

Mentor pyta: inertia spada gładko w całym zakresie k=2 do 8, bez jednego wyraźnego łokcia — samo inertia broni niemal każdego k. Silhouette score za to wyraźnie osiąga szczyt przy jednej wartości. Co to oznacza dla rekomendacji biznesowej, gdy dwie "standardowe" metody wyboru k nie są ze sobą zgodne?

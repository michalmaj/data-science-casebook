# Lekcja 6 — Interpretacja i nazywanie segmentów

## Głos mentora

"Lekcja 5 nie stworzyła tylko szumu — silhouette score wyraźnie wskazał k=2. Przestańmy więc porównywać rozwiązania i rzeczywiście zinterpretujmy jedno z nich. Dopasuj je, zobacz, co odróżnia dwa klastry, i nadaj im nazwy, których faktycznie użyłby ktoś z biznesu."

## Cel lekcji

Policzyć profile cech per klaster dla rozwiązania k=2 wskazanego przez Lekcję 5 i przełożyć wynik na biznesowo zrozumiałe nazwy segmentów.

## Pytanie analityczne dnia

Co właściwie odróżnia dwa segmenty Aurora Stream i jak nazwałbyś/nazwałabyś każdy z nich?

## Co dostajesz

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-5
- `task.py` — dwie funkcje do zaimplementowania: `load_scaled_features`, `segment_profiles`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

- Wczytaj ponownie przeskalowaną tabelę per subskrybent.
- Policz `segment_profiles` dla rozwiązania k=2.
- Porównaj trzy kolumny intensywności oglądania oraz tenure_days między dwoma klastrami.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

Jedno zdanie: jeden segment jest mały i wyraźnie wysoko zaangażowany, drugi duży i wyraźnie nisko zaangażowany, a staż (tenure) prawie się między nimi nie różni. Jak nazwałbyś/nazwałabyś te dwa segmenty i co powiedziałbyś/powiedziałabyś Aurora Stream, żeby robili inaczej dla każdego z nich?

## Refleksja

Mentor pyta: ten podział na dwa klastry to tak naprawdę tylko "poziom zaangażowania" — tenure_days, plan_tier i country nie odegrały żadnej roli w rozdzieleniu grup, bo klasteryzacja widziała wyłącznie cztery przeskalowane cechy liczbowe. Na jakie realne różnice między subskrybentami ta segmentacja może być całkowicie ślepa?

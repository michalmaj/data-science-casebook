# Lekcja 6 — Interpretacja i nazywanie segmentów

**Szacowany czas:** 45-60 min

## Po co to robimy

Lekcja 5 nie stworzyła tylko szumu — spośród porównanych rozwiązań k=2 wypadło jako mocny kandydat: najlepszy silhouette score, do tego odporny, bo utrzymał się nawet po zamianie redundantnych cech engagement. To wystarczający powód, żeby przestać porównywać i rzeczywiście zinterpretować jedno rozwiązanie. Dopasujmy je, zobaczmy, co odróżnia dwa klastry, i nadajmy im nazwy, których faktycznie użyłby ktoś z biznesu.

Pytanie na dziś: co właściwie odróżnia dwa segmenty Aurora Stream, i jakie nazwy warto im dać?

## Co masz zrobić

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-5.
- W `task.py` zaimplementuj `load_scaled_features`, `segment_profiles`.
- W notebooku: wczytaj ponownie przeskalowaną tabelę per subskrybent, policz `segment_profiles` dla rozwiązania k=2 (mocnego kandydata spośród rozwiązań porównanych w Lekcji 5). Porównaj trzy kolumny intensywności oglądania oraz `tenure_days` między dwoma klastrami. Sprawdź, czy poziom planu lub kraj pokrywają się z klastrami, mimo że klasteryzacja nigdy ich nie widziała.

## Na co zwrócić uwagę

Zgodność z poziomem planu czy krajem, jeśli się pojawi, jest sugestywna, nie jest potwierdzeniem — klasteryzacja nigdy nie widziała tych kolumn, więc pokrycie się z nimi mówi coś o tym, co segmenty mogą reprezentować, ale nie dowodzi, że segmenty są "prawdziwe" w jakimś głębszym sensie.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Jedno zdanie: jeden segment jest mały i wyraźnie wysoko zaangażowany, drugi duży i wyraźnie nisko zaangażowany, a staż (tenure) prawie się między nimi nie różni. Jakie nazwy warto dać tym dwóm segmentom, i co warto powiedzieć Aurora Stream o tym, co robić inaczej dla każdego z nich? I: ten podział na dwa klastry to tak naprawdę tylko "poziom zaangażowania" — `tenure_days`, `plan_tier` i `country` nie odegrały żadnej roli w rozdzieleniu grup, bo klasteryzacja widziała wyłącznie cztery przeskalowane cechy liczbowe. Na jakie realne różnice między subskrybentami ta segmentacja może być całkowicie ślepa?

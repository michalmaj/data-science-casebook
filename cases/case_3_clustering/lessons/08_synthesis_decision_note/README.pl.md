# Lekcja 8 — Synteza: Notatka decyzyjna

**Szacowany czas:** 45-60 min

## Po co to robimy

Siedem lekcji kodu, a zespół retencji Aurora Stream nigdy nie przeczyta ani linijki. Przeczyta to, co napiszesz dzisiaj. Redundantne cechy, dowolna pierwsza próba, niezgodność metryk, profile segmentów, sprawdzenie stabilności — wszystko to ma znaczenie tylko wtedy, gdy potrafisz to powiedzieć na tyle jasno, żeby ktoś, kto nigdy nie dopasowywał modelu KMeans, mógł na tym działać.

Pytanie na dziś: mając to wszystko, co teraz wiadomo, co Aurora Stream powinno zrobić dla każdego segmentu subskrybentów — i jak bardzo powinno być tego pewne?

## Co masz zrobić

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-7.
- W `task.py` zaimplementuj `load_scaled_features` (odtworzona z Lekcji 1-2) i jedną nową funkcję, `final_segment_table`, która zestawia obok siebie profile cech, wielkości i udziały w bazie subskrybentów dla obu segmentów.
- W notebooku: odpal komórkę kodu, żeby wygenerować finalną tabelę segmentów, a potem wypełnij siedem sekcji notatki decyzyjnej pod nią, prostym językiem, wykorzystując wiedzę z Lekcji 1-7. Nie ma osobnego zadania domowego — kompletna notatka decyzyjna jest deliverable'em całego Case'u 3. Dla dodatkowego ćwiczenia: skompresuj całą notatkę do trzyzdaniowego podsumowania wykonawczego, jakby zespół retencji miał tylko trzydzieści sekund.

## Na co zwrócić uwagę

Notatka ma być tak pewna, jak faktycznie pozwalają na to dowody — nie bardziej. Segmentacja to robocza hipoteza do sprawdzenia, nie odkryty fakt o populacji subskrybentów; rekomendacja ma to odzwierciedlać, nie przedstawiać k=2 jako ostatecznie potwierdzonej liczby "prawdziwych" grup.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Sprawdzają one liczby w tabeli segmentów — nie mogą ocenić treści notatki decyzyjnej, która jest oceniana pod kątem komunikacji i interpretacji (zobacz [`ASSESSMENT_RUBRIC.pl.md`](../../../../ASSESSMENT_RUBRIC.pl.md) oraz [`exemplar_decision_note.pl.md`](exemplar_decision_note.pl.md) tej lekcji po wzorcową odpowiedź).

Którą sekcję warto zostawić, a którą wyciąć, żeby notatka zmieściła się na jednym slajdzie? Co ten wybór mówi o tym, co naprawdę ma znaczenie dla Aurora Stream?

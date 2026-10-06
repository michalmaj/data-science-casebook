# Lekcja 8 — Synteza: Notatka decyzyjna

**Szacowany czas:** 40-50 min

## Po co to robimy

Siedem lekcji kodu, a menedżer operacyjny Meridian Outlet nigdy nie przeczyta ani linijki. Przeczyta to, co napiszesz dzisiaj. Model bazowy, model, kompromis progu, to, jak bardzo ufać przedziałom ryzyka — wszystko to ma znaczenie tylko wtedy, gdy potrafisz to powiedzieć na tyle jasno, żeby ktoś, kto nigdy nie widział p-value, mógł na tym działać.

Pytanie na dziś: mając to wszystko, co teraz wiadomo, co Meridian Outlet powinno zrobić — i jak bardzo powinno być tego pewne?

## Co masz zrobić

- Te same wyczyszczone, podzielone dane i model co w Lekcjach 5-7 (odtworzone tutaj przez `load_and_merge_orders`, `split_orders`, `fit_classifier`).
- W `task.py` zaimplementuj jedną nową funkcję, `final_scorecard` — zestawia obok siebie każdy predyktor zbudowany w tym case'ie (model bazowy większościowy, model przy domyślnym progu, model przy wybranym progu) na tych samych danych testowych.
- W notebooku: odpal komórkę kodu, żeby wygenerować scorecard, a potem wypełnij siedem sekcji notatki decyzyjnej pod nią, prostym językiem, wykorzystując to, czego nauczyłeś się w Lekcjach 1-7. Nie ma osobnego zadania domowego — kompletna notatka decyzyjna jest deliverable'em całego Case'u 2. Dla dodatkowego ćwiczenia: skompresuj całą notatkę do trzyzdaniowego podsumowania wykonawczego, jakby menedżer operacyjny miał tylko trzydzieści sekund.

## Na co zwrócić uwagę

Notatka ma być tak pewna, jak faktycznie pozwalają na to dowody — nie bardziej. Narzędzie oparte na prawdopodobieństwie nie jest certyfikatem; rekomendacja ma dać jedną konkretną akcję, nie powtórzenie liczby accuracy czy F1.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Sprawdzają one liczby w scorecardzie — nie mogą ocenić treści notatki decyzyjnej, która jest oceniana pod kątem komunikacji i interpretacji (zobacz [`ASSESSMENT_RUBRIC.pl.md`](../../../../ASSESSMENT_RUBRIC.pl.md) oraz [`exemplar_decision_note.pl.md`](exemplar_decision_note.pl.md) tej lekcji po wzorcową odpowiedź).

Którą sekcję warto zostawić, a którą wyciąć, żeby notatka zmieściła się na jednym slajdzie? Co ten wybór mówi o tym, co naprawdę ma znaczenie dla Meridian Outlet?

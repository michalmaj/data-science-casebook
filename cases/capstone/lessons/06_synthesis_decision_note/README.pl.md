# Lekcja 6 — Synteza: Notatka decyzyjna

**Szacowany czas:** 60-75 min

## Decyzja do podjęcia

Pięć lekcji kodu, a klient nigdy nie przeczyta ani linijki. Przeczyta to, co napiszesz dzisiaj. Model bazowy, model, to, jak dobrze poradził sobie na danych, których nigdy nie widział — wszystko to ma znaczenie tylko wtedy, gdy potrafisz to powiedzieć na tyle jasno, żeby ktoś, kto nigdy nie dopasowywał modelu, mógł na tej podstawie działać.

Mając to wszystko, co teraz wiadomo: co klient powinien zrobić — i jak bardzo powinien być tego pewien?

## Masz do dyspozycji

- `task.py` — jedenaście funkcji z Lekcji 4-5, odtworzonych (`evaluate_classification` przyjmuje opcjonalny `threshold`), plus trzy nowe: `final_regression_scorecard`, `final_classification_scorecard` (też przyjmuje `threshold` — podaj ten, który wybrano w Lekcji 5), `final_clustering_summary`.
- W notebooku: wygeneruj scorecard albo podsumowanie segmentów (dla ścieżki LendWell ustaw `CHOSEN_THRESHOLD` na wartość wybraną w Lekcji 5, nie domyślnie na 0,5), a potem wypełnij siedem sekcji notatki decyzyjnej, wykorzystując wiedzę z Lekcji 1-5. Nie ma osobnego zadania domowego — kompletna notatka decyzyjna jest deliverable'em dla całego capstone'u.

## Uzasadnij

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Te testy sprawdzają liczby w scorecardzie i podsumowaniu segmentów — nie mogą ocenić treści notatki decyzyjnej, która jest oceniana pod kątem komunikacji i interpretacji (zobacz [`ASSESSMENT_RUBRIC.pl.md`](../../../../ASSESSMENT_RUBRIC.pl.md) oraz [`exemplar_decision_note.pl.md`](exemplar_decision_note.pl.md) tej lekcji po wzorcową odpowiedź).

Jeśli chcesz dodatkowe ćwiczenie: skompresuj całą notatkę decyzyjną do trzech zdań podsumowania wykonawczego, jakby klient miał tylko trzydzieści sekund. I: którą sekcję notatki warto zostawić, a którą wyciąć, żeby zmieściła się na jednym slajdzie — i co ten wybór mówi o tym, co faktycznie ma znaczenie dla klienta?

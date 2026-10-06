# Lekcja 8 — Synteza: Notatka decyzyjna

**Szacowany czas:** 40-50 min

## Po co to robimy

Siedem lekcji kodu, a kierownik operacyjny TransLine nigdy nie przeczyta z niego ani linii. Przeczyta to, co napiszesz dzisiaj. Model bazowy, model, ślepy punkt, co jest możliwe do zaadresowania, a co nie — wszystko to ma znaczenie tylko wtedy, gdy potrafisz to powiedzieć wystarczająco prosto, żeby ktoś, kto nigdy nie widział p-value, mógł na tej podstawie działać.

Pytanie na dziś: mając całą tę wiedzę, co TransLine powinno zrobić — i jak bardzo powinno być tego pewne?

## Co masz zrobić

- Te same podzielone dane co w Lekcji 3 i ten sam model co w Lekcjach 5-7 (odtworzone tutaj przez `load_shipments`, `split_shipments`, `impute_driver_experience`, `fit_model`).
- W `task.py` zaimplementuj jedną nową funkcję, `final_scorecard` — zestawia obok siebie każdy predyktor zbudowany w tym case'ie (model bazowy zero, model bazowy średnia, model) na tych samych danych testowych.
- W notebooku: odpal komórkę z kodem, żeby wygenerować tabelę wyników, a potem wypełnij siedem sekcji notatki decyzyjnej pod nią, prostym językiem, korzystając z tego, czego nauczyłeś się w Lekcjach 1-7. Nie ma osobnego zadania domowego — kompletna notatka decyzyjna jest deliverable dla całego Case'u 1. Jeśli chcesz dodatkowe ćwiczenie: skompresuj całą notatkę do trzech zdań podsumowania wykonawczego, jakby kierownik operacyjny miał tylko trzydzieści sekund.

## Na co zwrócić uwagę

Notatka ma być tak pewna, jak faktycznie pozwalają na to dowody — nie bardziej. Jeśli jakaś cecha (np. `weather`) nigdy nie trafiła do modelu, to ograniczenie notatki, nie coś, co można przemilczeć. Rekomendacja ma dać jedną konkretną akcję, nie powtórzenie liczby MAE.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

To sprawdza liczby w tabeli wyników — nie może sprawdzić Twojej notatki decyzyjnej, która jest oceniana pod kątem komunikacji i interpretacji (zobacz [`ASSESSMENT_RUBRIC.pl.md`](../../../../ASSESSMENT_RUBRIC.pl.md) oraz [`exemplar_decision_note.pl.md`](exemplar_decision_note.pl.md) tej lekcji po wzorcową odpowiedź).

Którą sekcję warto zostawić, a którą wyciąć, żeby notatka zmieściła się na jednym slajdzie? Co ten wybór mówi o tym, co ma znaczenie dla TransLine?

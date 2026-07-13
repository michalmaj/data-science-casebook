# Lekcja 8 — Synteza: Notatka decyzyjna

## Głos mentora

"Siedem lekcji kodu, a kierownik operacyjny TransLine nigdy nie przeczyta z niego ani linii. Przeczyta to, co napiszesz dzisiaj. Wszystko, co znalazłeś/znalazłaś — model bazowy, model, ślepy punkt, co jest możliwe do zaadresowania, a co nie — ma znaczenie tylko wtedy, gdy potrafisz to powiedzieć wystarczająco prosto, żeby ktoś, kto nigdy nie widział p-value, mógł na tej podstawie działać."

## Cel lekcji

Złożyć wszystko z Lekcji 1-7 w notatkę decyzyjną, którą TransLine mogłoby faktycznie otrzymać i na podstawie której mogłoby działać.

## Pytanie analityczne dnia

Mając całą tę wiedzę, co TransLine powinno faktycznie zrobić — i jak bardzo powinno być tego pewne?

## Co dostajesz

- Te same podzielone dane i model co w Lekcji 5-7 (odtworzone tutaj przez `load_shipments`, `split_shipments`, `impute_driver_experience`, `fit_model`)
- `task.py` — jedna nowa funkcja, `final_scorecard`, która zestawia obok siebie każdy predyktor zbudowany w tym case'ie (model bazowy zero, model bazowy średnia, model) na tych samych danych testowych
- `lesson.ipynb` — tym razem większość notebooka to sam szablon notatki decyzyjnej, nie kod

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal komórkę z kodem, żeby wygenerować tabelę wyników.
3. Wypełnij każdą z siedmiu sekcji notatki decyzyjnej pod nią, prostym językiem, korzystając z tego, czego nauczyłeś/nauczyłaś się w Lekcjach 1-7.
4. Nie ma osobnego zadania domowego w tej lekcji — kompletna notatka decyzyjna jest deliverable dla całego Case'u 1.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. To sprawdza liczby w tabeli wyników — nie może sprawdzić Twojej notatki decyzyjnej, która jest oceniana pod kątem komunikacji i interpretacji (zobacz [`ASSESSMENT_RUBRIC.pl.md`](../../../../ASSESSMENT_RUBRIC.pl.md) oraz [`exemplar_decision_note.pl.md`](exemplar_decision_note.pl.md) tej lekcji po wzorcową odpowiedź).

## Zadanie domowe

Brak osobnego — ale jeśli chcesz dodatkowe ćwiczenie, spróbuj skompresować całą swoją notatkę decyzyjną do trzech zdań podsumowania wykonawczego, jakby kierownik operacyjny miał tylko trzydzieści sekund.

## Refleksja

Mentor pyta: gdybyś musiał/musiała wyciąć jedną sekcję swojej notatki decyzyjnej, żeby zmieścić się na jednym slajdzie, którą byś zostawił/zostawiła, a którą wyciął/wycięła — i co ten wybór mówi o tym, co faktycznie ma znaczenie dla TransLine?

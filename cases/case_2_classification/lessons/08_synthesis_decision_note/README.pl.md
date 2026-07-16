# Lekcja 8 — Synteza: Notatka decyzyjna

**Szacowany czas:** 40-50 min

## Efekty uczenia się

- Będziesz umieć złożyć modele, baseline'y i decyzję o progu z całego case'u w jedną tabelę porównawczą.
- Będziesz umieć napisać notatkę decyzyjną, która uczciwie podaje rekomendację i poziom pewności, nie sprzedając narzędzia opartego na prawdopodobieństwie jako pewności.
- Będziesz umieć zdecydować, co Meridian Outlet powinno faktycznie zrobić na podstawie wszystkiego, co znaleziono w całym case'ie, nie tylko tego, co zwraca model.

## Głos mentora

"Siedem lekcji kodu, a menedżer operacyjny Meridian Outlet nigdy nie przeczyta ani linijki. Przeczyta to, co napiszesz dzisiaj. Wszystko, co znalazłeś/znalazłaś — baseline, model, kompromis progu, jak bardzo ufać przedziałom ryzyka — ma znaczenie tylko wtedy, gdy potrafisz to powiedzieć na tyle jasno, żeby ktoś, kto nigdy nie widział p-value, mógł na tym działać."

## Cel lekcji

Zebrać wszystko z Lekcji 1-7 w notatkę decyzyjną, którą Meridian Outlet mogłoby naprawdę otrzymać i na jej podstawie działać.

## Pytanie analityczne dnia

Mając to wszystko, co teraz wiesz, co Meridian Outlet powinno faktycznie zrobić — i jak bardzo powinno być tego pewne?

## Co dostajesz

- Te same wyczyszczone, podzielone dane i model co w Lekcjach 5-7 (odtworzone tutaj przez `load_and_merge_orders`, `split_orders`, `fit_classifier`)
- `task.py` — jedna nowa funkcja, `final_scorecard`, która zestawia obok siebie każdy predyktor zbudowany w tym case'ie (baseline większościowy, model przy domyślnym progu, model przy wybranym progu) na tych samych danych testowych
- `lesson.ipynb` — tym razem większość notebooka to sam szablon notatki decyzyjnej, nie kod

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal komórkę kodu, żeby wygenerować scorecard.
3. Uzupełnij każdą z siedmiu sekcji notatki decyzyjnej poniżej, prostym językiem, wykorzystując to, czego nauczyłeś/nauczyłaś się w Lekcjach 1-7.
4. Tym razem nie ma osobnego zadania domowego — ukończona notatka decyzyjna jest deliverable'em całego Case'u 2.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Sprawdzają one liczby w scorecardzie — nie mogą ocenić treści Twojej notatki decyzyjnej, która jest oceniana pod kątem komunikacji i interpretacji (zobacz [`ASSESSMENT_RUBRIC.pl.md`](../../../../ASSESSMENT_RUBRIC.pl.md) oraz [`exemplar_decision_note.pl.md`](exemplar_decision_note.pl.md) tej lekcji po wzorcową odpowiedź).

## Zadanie domowe

Brak osobnego — ale jeśli chcesz dodatkowego ćwiczenia, spróbuj skompresować całą swoją notatkę decyzyjną do trzyzdaniowego podsumowania wykonawczego, tak jakby menedżer operacyjny miał tylko trzydzieści sekund.

## Refleksja

Mentor pyta: gdybyś musiał/musiała wyciąć jedną sekcję swojej notatki decyzyjnej, żeby zmieściła się na jednym slajdzie, którą byś zostawił/zostawiła, a którą wyciął/wycięła — i co ten wybór mówi o tym, co naprawdę ma znaczenie dla Meridian Outlet?

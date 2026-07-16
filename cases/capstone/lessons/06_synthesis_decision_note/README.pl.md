# Lekcja 6 — Synteza: Notatka decyzyjna

**Szacowany czas:** 60-75 min

## Efekty uczenia się

- Będziesz umieć złożyć baseline, model i wyniki ewaluacji z Twojego własnego case'u w jedną tabelę, w formacie pasującym do Twojego typu problemu.
- Będziesz umieć napisać notatkę decyzyjną dla klienta wybranego w Lekcji 1, uczciwie podając rekomendację i poziom pewności.
- Będziesz umieć zdecydować, co Twój własny klient powinien faktycznie zrobić, mając za sobą samodzielne zbudowanie i obronienie każdego kroku analizy.

## Głos mentora

"Pięć lekcji kodu, a Twój klient nigdy nie przeczyta ani linijki. Przeczyta to, co dziś napiszesz. Wszystko, co znalazłeś/znalazłaś — baseline, model, to, jak dobrze poradził sobie na danych, których nigdy nie widział — ma znaczenie tylko wtedy, gdy potrafisz to powiedzieć na tyle jasno, żeby ktoś, kto nigdy nie dopasowywał modelu, mógł na tej podstawie działać."

## Cel lekcji

Zebrać wszystko z Lekcji 1-5 w notatkę decyzyjną, którą Twój klient z Lekcji 1 mógłby faktycznie otrzymać i na jej podstawie działać.

## Pytanie analityczne dnia

Mając całą tę wiedzę, co Twój klient powinien faktycznie zrobić — i jak bardzo powinien być tego pewien?

## Co dostajesz

- Ten sam zbiór danych, który wybrałeś/wybrałaś w Lekcji 1
- `task.py` — jedenaście funkcji z Lekcji 4-5, odtworzonych, plus trzy nowe: `final_regression_scorecard`, `final_classification_scorecard`, `final_clustering_summary` (użyj tylko tej, która pasuje do Twojego zbioru)
- `lesson.ipynb` — tym razem większość notebooka to sam szablon notatki decyzyjnej, nie kod

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Gdy `task.py` będzie kompletny, uruchom tylko komórkę kodu pasującą do typu problemu Twojego zbioru, żeby wygenerować swój scorecard albo podsumowanie segmentów.
3. Wypełnij każdą z siedmiu sekcji notatki decyzyjnej poniżej, prostym językiem, wykorzystując to, czego nauczyłeś/nauczyłaś się w Lekcjach 1-5.
4. W tej lekcji nie ma osobnego zadania domowego — ukończona notatka decyzyjna jest deliverable'em dla całego capstone'u.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Te testy sprawdzają liczby w scorecardzie i podsumowaniu segmentów — nie mogą ocenić tego, co napiszesz w notatce decyzyjnej, co jest oceniane pod kątem komunikacji i interpretacji (zobacz [`ASSESSMENT_RUBRIC.pl.md`](../../../../ASSESSMENT_RUBRIC.pl.md) oraz [`exemplar_decision_note.pl.md`](exemplar_decision_note.pl.md) tej lekcji po wzorcową odpowiedź).

## Zadanie domowe

Brak osobnego — ale jeśli chcesz dodatkowe ćwiczenie, spróbuj skompresować całą swoją notatkę decyzyjną do trzech zdań podsumowania wykonawczego, jakby Twój klient miał tylko trzydzieści sekund.

## Refleksja

Mentor pyta: gdybyś musiał/musiała wyciąć jedną sekcję swojej notatki decyzyjnej, żeby zmieściła się na jednym slajdzie, którą byś zostawił/zostawiła, a którą wyciął/wycięła — i co ten wybór mówi o tym, co faktycznie liczy się dla Twojego klienta?

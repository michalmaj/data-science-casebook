# Lekcja 8 — Synteza: Notatka decyzyjna

**Szacowany czas:** 45-60 min

## Efekty uczenia się

- Będziesz umieć złożyć wnioski o zbędnych cechach, rozbieżności metryk, profile segmentów i wynik sprawdzenia stabilności w jedną notatkę decyzyjną.
- Będziesz umieć zarekomendować działanie dla konkretnego segmentu, jasno mówiąc, co klasteryzacja może, a czego nie może potwierdzić jako dowód.
- Będziesz umieć zdecydować, co Aurora Stream powinno faktycznie zrobić dla każdego segmentu i jak pewni powinni być każdej rekomendacji.

## Głos mentora

"Siedem lekcji kodu, a zespół retencji Aurora Stream nigdy nie przeczyta ani linijki. Przeczyta to, co napiszesz dzisiaj. Wszystko, co znalazłeś/znalazłaś — redundantne cechy, dowolna pierwsza próba, niezgodność metryk, profile segmentów, sprawdzenie stabilności — ma znaczenie tylko wtedy, gdy potrafisz to powiedzieć na tyle jasno, żeby ktoś, kto nigdy nie dopasowywał modelu KMeans, mógł na tym działać."

## Cel lekcji

Zebrać wszystko z Lekcji 1-7 w notatkę decyzyjną, którą Aurora Stream mogłoby naprawdę otrzymać i na jej podstawie działać.

## Pytanie analityczne dnia

Mając to wszystko, co teraz wiesz, co Aurora Stream powinno faktycznie zrobić dla każdego segmentu subskrybentów — i jak bardzo powinno być tego pewne?

## Co dostajesz

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-7
- `task.py` — dwie funkcje: `load_scaled_features` (odtworzona z Lekcji 1-2) i jedna nowa funkcja, `final_segment_table`, która zestawia obok siebie profile cech, wielkości i udziały w bazie subskrybentów dla obu segmentów
- `lesson.ipynb` — tym razem większość notebooka to sam szablon notatki decyzyjnej, nie kod

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal komórkę kodu, żeby wygenerować finalną tabelę segmentów.
3. Uzupełnij każdą z siedmiu sekcji notatki decyzyjnej poniżej, prostym językiem, wykorzystując to, czego nauczyłeś/nauczyłaś się w Lekcjach 1-7.
4. Tym razem nie ma osobnego zadania domowego — ukończona notatka decyzyjna jest deliverable'em całego Case'u 3.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Sprawdzają one liczby w tabeli segmentów — nie mogą ocenić treści Twojej notatki decyzyjnej, która jest oceniana pod kątem komunikacji i interpretacji (zobacz [`ASSESSMENT_RUBRIC.pl.md`](../../../../ASSESSMENT_RUBRIC.pl.md) oraz [`exemplar_decision_note.pl.md`](exemplar_decision_note.pl.md) tej lekcji po wzorcową odpowiedź).

## Zadanie domowe

Brak osobnego — ale jeśli chcesz dodatkowego ćwiczenia, spróbuj skompresować całą swoją notatkę decyzyjną do trzyzdaniowego podsumowania wykonawczego, tak jakby zespół retencji miał tylko trzydzieści sekund.

## Refleksja

Mentor pyta: gdybyś musiał/musiała wyciąć jedną sekcję swojej notatki decyzyjnej, żeby zmieściła się na jednym slajdzie, którą byś zostawił/zostawiła, a którą wyciął/wycięła — i co ten wybór mówi o tym, co naprawdę ma znaczenie dla Aurora Stream?

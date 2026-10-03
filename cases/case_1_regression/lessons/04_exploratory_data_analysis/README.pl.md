# Lekcja 3 — Eksploracyjna analiza danych

**Szacowany czas:** 30-40 min

## Efekty uczenia się

- Będziesz umieć policzyć i odczytać macierz korelacji, żeby znaleźć kolumny numeryczne faktycznie powiązane z targetem.
- Będziesz umieć porównać średnie w grupach, żeby wykryć wpływ zmiennej kategorycznej na target.
- Będziesz umieć rozpoznać, kiedy silnie skorelowana kolumna i tak nie nadaje się do użycia, bo nie byłaby znana w momencie predykcji.

## Głos mentora

"Dane są już czyste — dobrze. Nie sięgaj jeszcze po model. Najpierw popatrz. Połowę tego, co 'odkryjesz' modelując za wcześnie, widać już na macierzy korelacji i wykresie słupkowym, a patrzenie jest dużo tańsze niż dopasowywanie modelu."

## Cel lekcji

Sprawdzić, które kolumny faktycznie zmieniają się razem z `delay_minutes`, używając korelacji i porównań grupowych — i zauważyć, gdzie sama korelacja wprowadza w błąd.

## Pytanie analityczne dnia

Z tego, co TransLine zapisało, co naprawdę przewiduje opóźnienie przesyłki, a co tylko wygląda, jakby powinno?

## Co dostajesz

- Wyczyszczone dane z Lekcji 2 (odtworzone tutaj przez `load_clean_shipments`)
- `task.py` — cztery funkcje do zaimplementowania: `load_clean_shipments`, `correlation_matrix`, `correlation_with_target`, `mean_delay_by_weather`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę, w tym Twoje pierwsze wykresy

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Zobacz histogramy — coś skośnego albo zaskakującego?
4. Zobacz macierz korelacji — która kolumna numeryczna ma najsilniejszy związek z `delay_minutes`?
5. Porównaj korelację `num_stops` i `actual_duration_min` z celem — jedna to prawdziwy sygnał, druga jest zwodnicza. Ustal, czemu.
6. Zobacz wykres słupkowy pogody — zauważ, że nigdy nie pojawiła się w macierzy korelacji. To też jedyna kolumna, którą kierownik operacyjny TransLine już w Lekcji 1 oznaczył jako niemożliwą do poznania, zanim przesyłka wyjedzie z magazynu — miej obie te rzeczy na uwadze przy zadaniu domowym poniżej.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` wypisz kolumny, które weźmiesz do modelowania w następnej lekcji, i te, które odpuścisz — z jednym zdaniem uzasadnienia dla każdej.

## Refleksja

Mentor pyta: `actual_duration_min` jest *zdefiniowane* jako `planned_duration_min + delay_minutes`, a jednak jego korelacja z `delay_minutes` jest bliska zeru. Jeśli kolumna może być matematycznie związana z Twoim celem i mimo to wykazywać słabą korelację, co to mówi o ufaniu samej macierzy korelacji?

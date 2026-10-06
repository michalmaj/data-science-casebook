# Lekcja 4 — Eksploracyjna analiza danych

**Szacowany czas:** 30-40 min

## Po co to robimy

Dane są już podzielone — dobrze. Nie sięgaj jeszcze po model. Najpierw popatrz, wyłącznie na wiersze treningowe. Połowę tego, co "odkryjesz" modelując za wcześnie, widać już na macierzy korelacji i wykresie słupkowym, a patrzenie jest dużo tańsze niż dopasowywanie modelu.

Pytanie na dziś: z tego, co TransLine zapisało, co naprawdę przewiduje opóźnienie przesyłki, a co tylko wygląda, jakby powinno — oceniając wyłącznie na wierszach, na które wolno nam patrzeć?

## Co masz zrobić

- Podzielone dane z Lekcji 3 (odtworzone tutaj przez `load_shipments`, `split_shipments`, `impute_driver_experience`).
- W `task.py` zaimplementuj sześć funkcji: `load_shipments`, `split_shipments`, `impute_driver_experience`, `correlation_matrix`, `correlation_with_target`, `mean_delay_by_weather`.
- W notebooku: zobacz histogramy, macierz korelacji (która kolumna numeryczna ma najsilniejszy związek z `delay_minutes`?), i porównaj korelację `num_stops` i `actual_duration_min` z celem — jedna to prawdziwy sygnał, druga jest zwodnicza. Ustal, czemu.

## Na co zwrócić uwagę

Wykres słupkowy pogody nigdy nie pojawia się w macierzy korelacji, bo `weather` jest kategoryczna — ale to też jedyna kolumna, którą kierownik operacyjny TransLine już w Lekcji 1 oznaczył jako niemożliwą do poznania, zanim przesyłka wyjedzie z magazynu. Miej obie te rzeczy na uwadze przy zadaniu poniżej.

`test_df` jest tworzony przez `split_shipments`, ale nigdzie dalej w tym notebooku nie jest używany — to jest celowe, nie przeoczenie.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" wypisz kolumny, które weźmiesz do modelowania w następnej lekcji, i te, które odpuścisz — z jednym zdaniem uzasadnienia dla każdej. I: `actual_duration_min` jest *zdefiniowane* jako `planned_duration_min + delay_minutes`, a jednak jego korelacja z `delay_minutes` jest bliska zeru. Jeśli kolumna może być matematycznie związana z celem i mimo to wykazywać słabą korelację — co to mówi o ufaniu samej macierzy korelacji?

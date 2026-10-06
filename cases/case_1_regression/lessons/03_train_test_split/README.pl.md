# Lekcja 3 — Podział train/test i zapieczętowana koperta

**Szacowany czas:** 30-40 min

## Po co to robimy

Zanim zbadasz w tych danych cokolwiek więcej, zbiór testowy trzeba włożyć do zapieczętowanej koperty. Nie metaforycznie — naprawdę przestać patrzeć na te wiersze. Każda decyzja od tego momentu — co z czym koreluje, co liczy się jako sygnał, jaka powinna być zgadywanka modelu bazowego — zapada wyłącznie na wierszach treningowych. Kopertę otwiera się dokładnie raz, na końcu, żeby sprawdzić, czy to wszystko zadziałało.

Pytanie na dziś: gdy już wydzielimy dane, na których uczciwie przetestujemy wynik, co właściwie zostaje do eksploracji i budowania — i co się stanie, jeśli tę granicę przekroczymy?

## Co masz zrobić

- Dane z Lekcji 2 (odtworzone tutaj przez `load_shipments`).
- W `task.py` zaimplementuj `load_shipments`, `split_shipments`, `impute_driver_experience`.
- W notebooku: potwierdź, że podział się zgadza (394 + 99 = 493). Wywołaj `impute_driver_experience` zaraz po podziale i zauważ, że liczy wartość uzupełniającą wyłącznie ze zbioru treningowego, a potem stosuje tę samą wartość do zbioru treningowego i testowego. Każda kolejna lekcja w tym case'ie wykorzystuje dokładnie ten sam podział i tę samą imputację — ten sam `RANDOM_STATE`, te same wiersze.

## Na co zwrócić uwagę

`test_df` w tej lekcji nie jest dotykany poza zliczeniem brakujących wartości i uzupełnieniem ich liczbą wyliczoną z treningu. Uzupełnienie braków w zbiorze testowym statystyką z treningu jest bezpieczne — ale czemu? I czemu liczenie tej samej statystyki z samego zbioru testowego już by bezpieczne nie było?

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" porównaj medianę z całego zbioru z medianą tylko ze zbioru treningowego i zapisz, czemu różnica o 1 rok w wartości uzupełnianej ma znaczenie dla uczciwej ewaluacji.

# Lekcja 3 — Podział train/test i zapieczętowana koperta

**Szacowany czas:** 30-40 min

## Efekty uczenia się

- Będziesz umieć wyjaśnić, czemu zbiór testowy musi zostać wydzielony zanim jakakolwiek eksploracja, selekcja cech czy statystyka (np. mediana do imputacji) dotknie danych.
- Będziesz umieć podzielić zbiór danych w sposób powtarzalny za pomocą `train_test_split` i zachować stabilny podział między uruchomieniami.
- Będziesz umieć policzyć statystykę do imputacji wyłącznie ze zbioru treningowego i zastosować ją, bez zmian, do zbioru testowego.

## Głos mentora

"Zanim zbadasz w tych danych cokolwiek więcej, włóż zbiór testowy do zapieczętowanej koperty. Nie metaforycznie — naprawdę przestań patrzeć na te wiersze. Każda decyzja od tego momentu — co z czym koreluje, co liczy się jako sygnał, jaka powinna być zgadywanka 'modelu bazowego' — zapada wyłącznie na wierszach treningowych. Kopertę otwierasz dokładnie raz, na końcu, by sprawdzić, czy to wszystko zadziałało."

## Cel lekcji

Podzielić wyczyszczone dane o przesyłkach na zbiór treningowy i testowy, i wykonać ostatni pozostały krok czyszczenia — imputację `driver_experience_years` — poprawnie, wyłącznie na danych treningowych.

## Pytanie analityczne dnia

Gdy już wydzielimy dane, na których uczciwie przetestujemy wynik, co właściwie zostaje do eksploracji i budowania — i co się stanie, jeśli tę granicę przekroczymy?

## Co dostajesz

- Dane z Lekcji 2 (odtworzone tutaj przez `load_shipments`)
- `task.py` — trzy funkcje do zaimplementowania: `load_shipments`, `split_shipments`, `impute_driver_experience`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Potwierdź, że podział się zgadza: 394 + 99 = 493.
4. Wywołaj `impute_driver_experience` zaraz po podziale — zauważ, że liczy wartość uzupełniającą wyłącznie z `train_df`, a potem stosuje tę samą wartość do `train_df` i `test_df`.
5. Każda kolejna lekcja w tym case'ie (od 4 wzwyż) wykorzystuje dokładnie ten sam podział i tę samą imputację — ten sam `RANDOM_STATE`, te same wiersze treningowe i testowe.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` odpowiedz na pytanie o medianę z całego zbioru kontra medianę tylko z treningu, i czemu różnica o 1 minutę w wartości uzupełnianej ma znaczenie dla uczciwej ewaluacji.

## Refleksja

Mentor pyta: `test_df` w tej lekcji nie jest w ogóle dotykany poza zliczeniem brakujących wartości i uzupełnieniem ich liczbą *wyliczoną z treningu*. Czemu uzupełnienie braków w teście statystyką z treningu jest wciąż bezpieczne, podczas gdy liczenie tej statystyki z samego testu by nie było?

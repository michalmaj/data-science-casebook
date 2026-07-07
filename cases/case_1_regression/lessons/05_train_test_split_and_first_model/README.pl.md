# Lekcja 5 — Podział na train/test i pierwszy model regresji

## Głos mentora

"To pierwszy model, który musi naprawdę zapracować na swoje miejsce. Nie wobec zgadywanki na danych, które zapamiętał — wobec modelu bazowego z Lekcji 4, na przesyłkach, których nigdy nie widział. Jeśli przeskoczysz podział i oceniasz go na tych samych danych, na których trenował, nie mierzysz skuteczności — mierzysz zapamiętywanie."

## Cel lekcji

Wytrenować prawdziwy model regresji z właściwym, wydzielonym zbiorem testowym i udowodnić — liczbami, nie intuicją — że pobija sprawiedliwy model bazowy.

## Pytanie analityczne dnia

Czy regresja liniowa na cechach, które Lekcja 3 oznaczyła jako prawdziwy sygnał, faktycznie przewiduje opóźnienie przesyłki lepiej niż najlepsza naiwna zgadywanka TransLine?

## Co dostajesz

- Wyczyszczone dane z Lekcji 2-4 (odtworzone tutaj przez `load_clean_shipments`)
- `task.py` — cztery funkcje do zaimplementowania: `load_clean_shipments`, `split_shipments`, `fit_model`, `predict_delay`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Potwierdź, że podział się zgadza: 394 + 99 = 493.
4. Porównaj MAE/RMSE modelu na zbiorze testowym ze sprawiedliwym modelem bazowym (średnia z treningu zastosowana do testu, nie średnia z całego zbioru z Lekcji 4).
5. Zobacz współczynniki modelu — czy ich znaki zgadzają się z tym, co sugerowały korelacje z Lekcji 3?

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz, o ile (w minutach MAE) model pobija sprawiedliwy model bazowy, i wymień jedną rzecz, którą wypróbowałbyś/wypróbowałabyś dalej, żeby go ulepszyć.

## Refleksja

Mentor pyta: czemu ta lekcja liczy średnią modelu bazowego tylko ze zbioru treningowego, a nie ponownie wykorzystuje średnią z Lekcji 4 (liczoną z całego zbioru)? Co poszłoby źle, gdybyś użył/użyła średniej z całego zbioru jako "sprawiedliwego" modelu bazowego tutaj?

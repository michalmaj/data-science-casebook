# Lekcja 5 — Podział na train/test i pierwszy model regresji

**Szacowany czas:** 35-45 min

## Efekty uczenia się

- Będziesz umieć wyjaśnić, dlaczego podział train/test musi nastąpić zanim policzona zostanie jakakolwiek statystyka (np. mediana do imputacji) z danych.
- Będziesz umieć dopasować model bazowy i pierwszy model `LinearRegression`, i odczytać wynikowe MAE jako "lepiej/gorzej niż zawsze przewidywanie średniej", nie jako abstrakcyjną liczbę.
- Będziesz umieć wskazać, które korelacje kandydujących cech z targetem są wystarczająco silne, by nazwać je "realnym sygnałem", a nie szumem.

## Głos mentora

"To pierwszy model, który musi naprawdę zapracować na swoje miejsce. Nie wobec zgadywanki na danych, które zapamiętał — wobec modelu bazowego z Lekcji 4, na przesyłkach, których nigdy nie widział. Jeśli przeskoczysz podział i oceniasz go na tych samych danych, na których trenował, nie mierzysz skuteczności — mierzysz zapamiętywanie."

## Cel lekcji

Wytrenować prawdziwy model regresji z właściwym, wydzielonym zbiorem testowym i udowodnić — liczbami, nie intuicją — że pobija sprawiedliwy model bazowy.

## Pytanie analityczne dnia

Czy regresja liniowa na czterech cechach liczbowych, które zbadała Lekcja 3, faktycznie przewiduje opóźnienie przesyłki lepiej niż najlepsza naiwna zgadywanka TransLine — mimo że tylko jedna z nich korelowała silnie samodzielnie?

## Co dostajesz

- Dane z Lekcji 2-4 (odtworzone tutaj przez `load_shipments`)
- `task.py` — pięć funkcji do zaimplementowania: `load_shipments`, `split_shipments`, `impute_driver_experience`, `fit_model`, `predict_delay`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Potwierdź, że podział się zgadza: 394 + 99 = 493.
4. Wywołaj `impute_driver_experience` zaraz po podziale — zauważ, że liczy wartość uzupełniającą wyłącznie z `train_df`, a potem stosuje tę samą wartość do `train_df` i `test_df`. To naprawa prawdziwego błędu, który ten kurs kiedyś miał: liczenie mediany przed podziałem pozwalało odrobinie informacji ze zbioru testowego przeciekać do treningu.
5. Porównaj MAE/RMSE modelu na zbiorze testowym ze sprawiedliwym modelem bazowym (średnia z treningu zastosowana do testu, nie średnia z całego zbioru z Lekcji 4).
6. Zobacz współczynniki modelu — czy ich znaki zgadzają się z tym, co sugerowały korelacje z Lekcji 3?

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

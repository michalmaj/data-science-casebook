# Lekcja 5 — Model bazowy i pierwszy model

**Szacowany czas:** 45-55 min

## Efekty uczenia się

- Będziesz umieć zbudować naiwny model bazowy, ocenić go najpierw w próbie treningowej, by zbudować intuicję MAE/RMSE, a potem ocenić jego (i prawdziwego modelu) wynik uczciwie, na wydzielonych danych testowych.
- Będziesz umieć policzyć MAE i RMSE ręcznie i wyjaśnić, co każda z tych miar inaczej karze.
- Będziesz umieć dopasować pierwszy model `LinearRegression` i pokazać, liczbami, że pobija on zarówno naiwną zgadywankę, jak i przekłada się na coś, czym TransLine może działać, w minutach.

## Głos mentora

"Zanim zbudujesz coś sprytnego, odpowiedz na to: jaka jest najgłupsza możliwa zgadywanka, i jak bardzo się myli? Potem — i tylko potem — zbuduj prawdziwy model i udowodnij, że przeskakuje tę poprzeczkę na przesyłkach, których nigdy nie widział. Nie wobec zgadywanki na danych, które zapamiętał. Jeśli przeskoczysz podział i oceniasz go na tych samych danych, na których trenował, nie mierzysz skuteczności — mierzysz zapamiętywanie."

## Cel lekcji

Ustalić sprawiedliwy model bazowy z danych treningowych, a potem dopasować pierwszy model regresji i udowodnić — liczbami, nie intuicją — że pobija ten model bazowy na wydzielonych danych.

## Pytanie analityczne dnia

Jeśli TransLine nie miałoby żadnego modelu i po prostu zgadywało tę samą liczbę każdy raz, jak bardzo by się myliło — i czy prawdziwa regresja liniowa na czterech cechach, które zbadała Lekcja 4, faktycznie radzi sobie lepiej, na przesyłkach, których nigdy nie widziała?

## Co dostajesz

- Podzielone i uzupełnione dane z Lekcji 3 (odtworzone tutaj przez `load_shipments`, `split_shipments`, `impute_driver_experience`)
- `task.py` — dziewięć funkcji do zaimplementowania: `load_shipments`, `split_shipments`, `impute_driver_experience`, `predict_zero_baseline`, `predict_mean_baseline`, `mean_absolute_error`, `root_mean_squared_error`, `fit_model`, `predict_delay`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Porównaj MAE obu modeli bazowych w próbie treningowej — która naiwna zgadywanka jest faktycznie mniej błędna?
4. Zauważ, że `predict_mean_baseline` przyjmuje dwa argumenty: wywołaj ją z `(train_df, train_df)` dla sprawdzenia w próbie, i z `(train_df, test_df)` dla sprawiedliwego porównania później — sama średnia zawsze pochodzi z `train_df`.
5. Potwierdź, że model pobija sprawiedliwy model bazowy na średniej, który z kolei pobija model bazowy na zerze, na wydzielonym zbiorze testowym.
6. Zobacz współczynniki modelu — czy ich znaki zgadzają się z tym, co sugerowały korelacje z Lekcji 4?

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz, o ile (w minutach MAE) model pobija sprawiedliwy model bazowy, i wymień jedną rzecz, którą wypróbowałbyś/wypróbowałabyś dalej, żeby go ulepszyć.

## Refleksja

Mentor pyta: ta lekcja liczy wartość modelu bazowego na średniej z `train_df` w obu wywołaniach `predict_mean_baseline` — nawet tym ocenianym względem `test_df`. Czemu to wciąż jest uczciwe, podczas gdy liczenie `correlation_with_target` na `test_df` by nie było?

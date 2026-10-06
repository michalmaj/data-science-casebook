# Lekcja 5 — Model bazowy i pierwszy model

**Szacowany czas:** 45-55 min

## Po co to robimy

Zanim zbudujesz coś sprytnego, odpowiedz na to: jaka jest najgłupsza możliwa zgadywanka, i jak bardzo się myli? Potem — i tylko potem — zbuduj prawdziwy model i udowodnij, że przeskakuje tę poprzeczkę na przesyłkach, których nigdy nie widział. Nie wobec zgadywanki na danych, które zapamiętał: jeśli ocenisz model na tych samych danych, na których trenował, nie mierzysz skuteczności — mierzysz zapamiętywanie.

Pytanie na dziś: jeśli TransLine nie miałoby żadnego modelu i po prostu zgadywało tę samą liczbę każdy raz, jak bardzo by się myliło — i czy prawdziwa regresja liniowa na czterech cechach z Lekcji 4 radzi sobie lepiej, na przesyłkach, których nigdy nie widziała?

## Co masz zrobić

- Podzielone i uzupełnione dane z Lekcji 3 (odtworzone tutaj przez `load_shipments`, `split_shipments`, `impute_driver_experience`).
- W `task.py` zaimplementuj dziewięć funkcji: `load_shipments`, `split_shipments`, `impute_driver_experience`, `predict_zero_baseline`, `predict_mean_baseline`, `mean_absolute_error`, `root_mean_squared_error`, `fit_model`, `predict_delay`.
- W notebooku: porównaj MAE obu modeli bazowych na zbiorze treningowym — która naiwna zgadywanka jest mniej błędna? `predict_mean_baseline` przyjmuje dwa argumenty: wywołaj ją z `(train_df, train_df)` dla sprawdzenia w próbie i z `(train_df, test_df)` dla sprawiedliwego porównania później — sama średnia zawsze pochodzi z `train_df`. Potwierdź, że model pobija sprawiedliwy model bazowy na średniej, który z kolei pobija model bazowy na zerze, na zbiorze testowym. Zobacz współczynniki modelu — czy ich znaki zgadzają się z korelacjami z Lekcji 4?

## Na co zwrócić uwagę

Ta lekcja liczy wartość modelu bazowego na średniej z `train_df` w obu wywołaniach `predict_mean_baseline` — nawet tym ocenianym względem `test_df`. To wciąż jest uczciwe, bo średnia jest tylko *stosowana* do zbioru testowego, nie wyliczona z niego — tak samo jak imputacja w Lekcji 3. Liczenie `correlation_with_target` na `test_df` by już nie było bezpieczne, bo tam sam zbiór testowy byłby źródłem statystyki, nie jej odbiorcą.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" napisz, o ile (w minutach MAE) model pobija sprawiedliwy model bazowy, i zanotuj, co trzeba by zrobić, żeby wprowadzić do modelu `weather` — która miała realny wpływ w Lekcji 4, ale nie jest w `FEATURE_COLUMNS`. To pytanie do refleksji, nie kolejny krok do wykonania: uczciwe dodanie cechy po zobaczeniu wyniku na teście wymaga nowego podziału na świeżych danych, a nie potajemnego przeuczenia i ponownej oceny na tym samym `test_df`.

# Lekcja 6 — Dobór progu i wybór metryki

**Szacowany czas:** 40-50 min

## Po co to robimy

Widzieliśmy, jak model przypisuje prawdziwe prawdopodobieństwa, ale domyślny próg to wszystko ukrywał. Teraz wybieramy próg sami — i zobaczymy dokładnie, co tracimy za każdym razem, gdy go obniżamy.

Obniżamy próg decyzyjny poniżej 0,5 i obserwujemy, jak precision, recall i F1 zmieniają się względem siebie — łącząc każdy wybór z realnym kosztem biznesowym.

Każdy podział w tej lekcji (`train_df`/`test_df`, potem `fit_df`/`val_df`) to podział wierszowy z Lekcji 5, celowo: ta lekcja dostraja model pod scenariusz A (jak dobrze model ocenia kolejne zamówienia klientów, których Meridian Outlet już zna), nie scenariusz B (zupełnie nowi klienci) — zobacz Lekcję 5 po wyjaśnienie tego rozróżnienia, jeśli jeszcze nie jest jasne.

Pytanie na dziś: ile precision Meridian Outlet jest skłonny poświęcić, żeby złapać więcej rzeczywistych zwrotów — i gdzie sensownie postawić tę granicę?

## Co masz zrobić

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-5.
- W `task.py` zaimplementuj sześć funkcji: `load_and_merge_orders`, `split_orders`, `split_for_validation`, `fit_classifier`, `predict_at_threshold`, `classification_metrics`.
- W notebooku:
  1. Potwierdź, że `split_orders`/`fit_classifier` odtwarzają dokładnie ten sam model co w Lekcji 5.
  2. Wywołaj `split_for_validation` na `train_df`, żeby wydzielić `fit_df`/`val_df` — progi porównasz na `val_df`, nie na `test_df`.
  3. Wywołaj `predict_at_threshold` przy 0,5, 0,3 i 0,2 na `val_df` — obserwuj, jak rośnie liczba oflagowanych zamówień.
  4. Wywołaj `classification_metrics` przy każdym progu na `val_df` — obserwuj, jak rośnie recall i jak zmienia się precision.
  5. Połącz dwa rodzaje błędów z tym, co naprawdę oznaczają: fałszywy alarm (FP) niesłusznie flaguje dobre zamówienie, a przeoczony przypadek (FN) pozwala prawdziwemu zwrotowi przejść bez flagi.
  6. W ostatniej komórce doucz model na pełnym `train_df` i sprawdź wybrany próg na `test_df` — jedyny raz, kiedy ta lekcja go dotyka, i w zasadzie pierwszy raz w całym tym case'ie, kiedy `test_df` jest użyty do oceny modelu (Lekcja 5 zerknęła na `test_df` raz, ale tylko żeby zliczyć nakładanie się klientów z `train_df` — fakt o strukturze podziału, nie liczba o skuteczności). W tym momencie cechy, model i próg są już ustalone — żadna liczba z `test_df` nie może już nic z tego zmienić.

## Na co zwrócić uwagę

To jest pierwszy moment w całym tym case'ie, w którym `test_df` faktycznie ocenia model — nie liczy nakładania klientów, nie sprawdza struktury, tylko mierzy skuteczność. Dzieje się to na samym końcu, dopiero gdy cechy, model i próg są już zamknięte.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" wybierz próg, który warto polecić Meridian Outlet, i uzasadnij go kosztem fałszywego alarmu w porównaniu z kosztem przeoczonego przypadku. I: liczby ze zbioru walidacyjnego przewidywały, jak zachowa się próg 0,2 — w ostatniej komórce pojawia się prawdziwy wynik na `test_df`. Wypada on blisko tego, co przewidziała walidacja, czy przesuwa się dość mocno? Co powiedziałaby duża różnica między nimi — i dlaczego bezpieczniej jest się o tym dowiedzieć *po* wybraniu progu, a nie w trakcie jego wybierania?

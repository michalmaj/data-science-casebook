# Lekcja 6 — Dobór progu i wybór metryki

## Głos mentora

"Widziałeś/widziałaś, jak model przypisuje prawdziwe prawdopodobieństwa, ale domyślny próg to wszystko ukrywał. Teraz sam/sama wybierzesz próg — i zobaczysz dokładnie, co tracisz za każdym razem, gdy go obniżasz."

## Cel lekcji

Obniżyć próg decyzyjny poniżej 0.5 i zobaczyć, jak precision, recall i F1 zmieniają się względem siebie — łącząc każdy wybór z realnym kosztem biznesowym.

## Pytanie analityczne dnia

Ile precision Meridian Outlet jest skłonny poświęcić, żeby złapać więcej rzeczywistych zwrotów — i gdzie sensownie postawić tę granicę?

## Co dostajesz

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-5
- `task.py` — pięć funkcji do zaimplementowania: `load_and_merge_orders`, `split_orders`, `fit_classifier`, `predict_at_threshold`, `classification_metrics`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Potwierdź, że `split_orders`/`fit_classifier` odtwarzają dokładnie ten sam model co w Lekcji 5.
4. Wywołaj `predict_at_threshold` przy 0.5, 0.3 i 0.2 — obserwuj, jak rośnie liczba oflagowanych zamówień.
5. Wywołaj `classification_metrics` przy każdym progu — obserwuj, jak rośnie recall i jak zmienia się precision.
6. Połącz dwa rodzaje błędów z tym, co naprawdę oznaczają: fałszywy alarm (FP) niesłusznie flaguje dobre zamówienie, a przeoczony przypadek (FN) pozwala prawdziwemu zwrotowi przejść bez flagi.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania: wybierz próg, który faktycznie poleciłbyś/poleciłabyś Meridian Outlet, i uzasadnij go kosztem fałszywego alarmu w porównaniu z kosztem przeoczonego przypadku.

## Refleksja

Mentor pyta: przy progu 0.2 model wciąż przeocza 9 z 20 rzeczywistych zwrotów i niesłusznie flaguje 34 dobre zamówienia na każde 11 trafionych. Czy dla Meridian Outlet ważniejsze jest optymalizowanie precision czy recall — i czy ta odpowiedź zależy od tego, co dzieje się *po* oflagowaniu (człowiek to sprawdza, czy zamówienie zostaje automatycznie zablokowane)?

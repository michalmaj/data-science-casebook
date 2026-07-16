# Lekcja 4 — Biznesowy sens błędu i model bazowy

**Szacowany czas:** 35-45 min

## Efekty uczenia się

- Będziesz umieć zbudować naiwną predykcję bazową i traktować ją jako poprzeczkę, którą musi przeskoczyć każdy realny model.
- Będziesz umieć policzyć MAE i RMSE oraz wyjaśnić, co każda z tych miar inaczej karze.
- Będziesz umieć przełożyć abstrakcyjny wynik błędu na to, co faktycznie znaczy dla klienta, w realnych jednostkach.

## Głos mentora

"Zanim zbudujesz coś sprytnego, odpowiedz na to: jaka jest najgłupsza możliwa zgadywanka, i jak bardzo się myli? Jeśli to przeskoczysz, nie będziesz mieć sposobu, żeby sprawdzić, czy model z następnej lekcji jest naprawdę dobry — 'lepszy niż nic' to nie to samo, co 'wystarczająco dobry, żeby wdrożyć'."

## Cel lekcji

Ustalić bazowy punkt odniesienia, z którego TransLine mogłoby korzystać już dziś, i zmierzyć precyzyjnie, jak bardzo się myli — w minutach, nie w abstrakcyjnych wskaźnikach błędu.

## Pytanie analityczne dnia

Jeśli TransLine nie miałoby żadnego modelu i po prostu zgadywało tę samą liczbę każdy raz, jaka powinna być ta liczba, i jak bardzo typowo by się myliło?

## Co dostajesz

- Wyczyszczone dane z Lekcji 2-3 (odtworzone tutaj przez `load_clean_shipments`)
- `task.py` — pięć funkcji do zaimplementowania: `load_clean_shipments`, `predict_mean_baseline`, `predict_zero_baseline`, `mean_absolute_error`, `root_mean_squared_error`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Porównaj MAE obu modeli bazowych — która naiwna zgadywanka jest faktycznie mniej błędna średnio?
4. Porównaj MAE i RMSE dla tego samego modelu bazowego — czemu to różne liczby dla tych samych predykcji?

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz jednozdaniową odpowiedź na pytanie kierownika operacyjnego, plus notatkę, jaki wynik MAE musi pobić każdy Twój przyszły model, żeby było warto go wdrożyć.

## Refleksja

Mentor pyta: RMSE modelu bazowego opartego na średniej wychodzi równe odchyleniu standardowemu `delay_minutes`. Czemu to musi być prawda, i co to mówi o tym, co RMSE naprawdę mierzy?

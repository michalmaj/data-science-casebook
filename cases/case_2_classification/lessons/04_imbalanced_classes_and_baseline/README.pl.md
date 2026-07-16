# Lekcja 4 — Niezbalansowane klasy i baseline

**Szacowany czas:** 35-45 min

## Efekty uczenia się

- Będziesz umieć zbudować baseline przewidujący klasę większościową i zobaczyć, dlaczego jego nagłówkowa dokładność może wprowadzać w błąd.
- Będziesz umieć policzyć macierz pomyłek i odczytać z niej to, co ukrywa pojedynczy wynik dokładności.
- Będziesz umieć wyjaśnić, dlaczego model "dokładny w 86%", który nie wyłapuje ani jednego prawdziwego przypadku, wcale nie jest użyteczny.

## Głos mentora

"W poprzedniej lekcji pytałem, jaką dokładność (accuracy) osiągnąłby model, który zawsze przewiduje 'brak zwrotu' — pewnie zgadłeś/zgadłaś coś bliskiego 86%. Teraz zbuduj ten baseline naprawdę i sprawdź dokładnie, w których zamówieniach się myli."

## Cel lekcji

Zbudować najprostszy możliwy klasyfikator — zawsze przewidujący klasę większościową — i zobaczyć, dlaczego sama liczba accuracy potrafi ukryć model, który nie łapie ani jednego prawdziwego zwrotu.

## Pytanie analityczne dnia

Jeśli baseline ignorujący wszystkie cechy osiąga już 86% accuracy, co właściwie musiałby zrobić prawdziwy klasyfikator, żeby udowodnić Meridian Outlet swoją użyteczność?

## Co dostajesz

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-3
- `task.py` — cztery funkcje do zaimplementowania: `load_and_merge_orders`, `predict_majority_baseline`, `accuracy`, `confusion_counts`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Spójrz na `predict_majority_baseline(df)` — potwierdź, że przewiduje dokładnie tę samą wartość dla każdego zamówienia.
4. Sprawdź `accuracy(...)` — potwierdź, że niemal pokrywa się z `class_balance` z Lekcji 3.
5. Spójrz na `confusion_counts(...)` — zwróć uwagę na `tp` i `fn`: baseline nie łapie ani jednego prawdziwego zwrotu.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania: skoro w tej macierzy pomyłek `tp=0`, a `fn=98`, dlaczego 86% accuracy jest mylącą liczbą nagłówkową w kontekście prawdziwego problemu Meridian Outlet — łapania zwrotów, zanim towar zostanie wysłany?

## Refleksja

Mentor pyta: jeśli prawdziwym celem Meridian Outlet jest złapanie jak największej liczby zwrotów, zanim zamówienie zostanie wysłane, czy model, który ma 86% accuracy, ale nigdy nie przewiduje ani jednego zwrotu, jest bezużyteczny, wręcz szkodliwy, czy coś pomiędzy? Co byś im powiedział/powiedziała, gdyby to był jedyny model, jaki masz?

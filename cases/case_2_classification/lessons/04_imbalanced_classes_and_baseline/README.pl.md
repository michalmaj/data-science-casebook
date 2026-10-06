# Lekcja 4 — Niezbalansowane klasy i model bazowy

**Szacowany czas:** 35-45 min

## Po co to robimy

W poprzedniej lekcji pytaliśmy, jaką dokładność (accuracy) osiągnąłby model, który zawsze przewiduje "brak zwrotu" — pewnie wyszło coś bliskiego 86%. Teraz budujemy ten model bazowy naprawdę i sprawdzamy dokładnie, w których zamówieniach się myli.

Pytanie na dziś: jeśli model bazowy ignorujący wszystkie cechy osiąga już 86% accuracy, co właściwie musiałby zrobić prawdziwy klasyfikator, żeby udowodnić Meridian Outlet swoją użyteczność?

## Co masz zrobić

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-3.
- W `task.py` zaimplementuj cztery funkcje: `load_and_merge_orders`, `predict_majority_baseline`, `accuracy`, `confusion_counts`.
- W notebooku: sprawdź `predict_majority_baseline(df)` — potwierdź, że przewiduje dokładnie tę samą wartość dla każdego zamówienia. Sprawdź `accuracy(...)` — potwierdź, że dokładnie pokrywa się z `class_balance` z Lekcji 3 (dokładność modelu bazowego klasy większościowej to z definicji udział tej klasy). Sprawdź `confusion_counts(...)` — zwróć uwagę na `tp` i `fn`: model bazowy nie łapie ani jednego prawdziwego zwrotu.

## Na co zwrócić uwagę

Macierz pomyłek pokazuje coś, co pojedyncza liczba accuracy chowa: `tp=0` i `fn=98` oznaczają, że ten model bazowy nigdy — ani razu — nie przewiduje zwrotu, mimo 86% "dokładności".

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" napisz: skoro `tp=0`, a `fn=98`, dlaczego 86% accuracy jest mylącą liczbą nagłówkową w kontekście prawdziwego problemu Meridian Outlet — łapania zwrotów, zanim towar zostanie wysłany? I: jeśli prawdziwym celem Meridian Outlet jest złapanie jak największej liczby zwrotów zanim zamówienie zostanie wysłane, czy model z 86% accuracy, który nigdy nie przewiduje ani jednego zwrotu, jest bezużyteczny, wręcz szkodliwy, czy coś pomiędzy? Co warto by im powiedzieć, gdyby to był jedyny dostępny model?

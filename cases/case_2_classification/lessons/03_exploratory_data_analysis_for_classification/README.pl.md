# Lekcja 3 — Eksploracyjna analiza danych do klasyfikacji

## Głos mentora

"Masz już połączone dane — teraz prawdziwe pytanie: które z tych sygnałów naprawdę warto wykorzystać przy budowie modelu, a które tylko wyglądają ciekawie? Zanim dotkniesz jakiegokolwiek klasyfikatora, wyrób sobie pogląd na to, co przewiduje zwrot, a co nie."

## Cel lekcji

Zbadać połączone dane zamówień Meridian Outlet, żeby znaleźć czynniki faktycznie powiązane ze zwrotem, i uczciwie ocenić, jak rzadkie są zwroty w ogóle.

## Pytanie analityczne dnia

Jak bardzo niezbalansowane są zwroty Meridian Outlet, i które zarejestrowane czynniki — kategoria produktu, rabat czy własna historia zwrotów klienta — faktycznie mają znaczenie?

## Co dostajesz

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-2
- `task.py` — cztery funkcje do zaimplementowania: `load_and_merge_orders`, `class_balance`, `return_rate_by_category`, `correlation_with_return`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Spójrz na `class_balance(df)` — zauważ, jak rzadkie są w rzeczywistości zwroty.
4. Spójrz na `return_rate_by_category(df)` — która kategoria zwraca się najczęściej, a która najrzadziej?
5. Porównaj `correlation_with_return` dla `discount_percent`, `previous_returns_count` i `account_age_days` — który z nich jest najsilniejszym sygnałem liczbowym?

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania: skoro zwroty są tak rzadkie, co jest nie tak z ocenianiem przyszłego klasyfikatora wyłącznie na podstawie accuracy?

## Refleksja

Mentor pyta: jeśli 14% zamówień jest zwracanych, jaką dokładność (accuracy) osiągnąłby model, który zawsze przewiduje "brak zwrotu", nie patrząc na żadną cechę? Czy nazwałbyś/nazwałabyś to dobrym modelem?

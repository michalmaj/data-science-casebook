# Lekcja 3 — Eksploracyjna analiza danych do klasyfikacji

**Szacowany czas:** 35-45 min

## Po co to robimy

Dane są już połączone — teraz prawdziwe pytanie: które sygnały naprawdę warto wykorzystać przy budowie modelu, a które tylko wyglądają ciekawie? Zanim dotkniemy jakiegokolwiek klasyfikatora, wyrabiamy sobie pogląd, co przewiduje zwrot, a co nie.

Pytanie na dziś: jak bardzo niezbalansowane są zwroty Meridian Outlet, i które zarejestrowane czynniki — kategoria produktu, rabat czy własna historia zwrotów klienta — faktycznie mają znaczenie?

## Co masz zrobić

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-2.
- W `task.py` zaimplementuj cztery funkcje: `load_and_merge_orders`, `class_balance`, `return_rate_by_category`, `correlation_with_return`.
- W notebooku: sprawdź `class_balance(df)` — jak rzadkie są w rzeczywistości zwroty. Sprawdź `return_rate_by_category(df)` — która kategoria zwraca się najczęściej, a która najrzadziej. Porównaj `correlation_with_return` dla `discount_percent`, `previous_returns_count` i `account_age_days` — który z nich jest najsilniejszym sygnałem liczbowym.

## Na co zwrócić uwagę

Przy tak niezbalansowanym targecie intuicja z regresji nie przenosi się bezpośrednio: wysoka korelacja i wysoka accuracy mogą znaczyć coś zupełnie innego niż się wydaje, gdy jedna klasa dominuje liczebnie. To temat kolejnej lekcji — tutaj wystarczy zobaczyć, jak rzadkie są zwroty.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" napisz: skoro zwroty są tak rzadkie, co jest nie tak z ocenianiem przyszłego klasyfikatora wyłącznie na podstawie accuracy? I: jeśli 14% zamówień jest zwracanych, jaką dokładność (accuracy) osiągnąłby model, który zawsze przewiduje "brak zwrotu", nie patrząc na żadną cechę? Czy to byłby dobry model?

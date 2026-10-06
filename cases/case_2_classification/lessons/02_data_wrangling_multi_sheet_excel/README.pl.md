# Lekcja 2 — Porządkowanie danych: wielo-arkuszowy Excel

**Szacowany czas:** 35-45 min

## Po co to robimy

W surowym wczytaniu z Lekcji 1 były dwa wiersze za dużo — to wiersz tytułowy i prawdziwy nagłówek, oba wczytane jako dane. Dziś naprawiamy to porządnie, a przy okazji trafiamy na podobny bałagan w arkuszu Customers: ten sam pomysł, inne przebranie.

Pytanie na dziś: gdy oba arkusze są już poprawnie wczytane i połączone, jak dokładnie wygląda pojedynczy, kompletny wiersz danych zamówienia Meridian Outlet?

## Co masz zrobić

- Ten sam plik `data/orders.xlsx` co w Lekcji 1.
- W `task.py` zaimplementuj `load_customers`, `load_and_merge_orders`.
- W notebooku: wczytaj arkusz Customers i potwierdź, że jego kolumna id pasuje teraz do `customer_id` z Orders. Wczytaj i połącz arkusz Orders — sprawdź kształt i nazwy kolumn w porównaniu z surowym wczytaniem z Lekcji 1. Potwierdź, że połączona tabela nie ma braków danych i ma tę samą ~14% stopę zwrotów, jakiej można się spodziewać po Lekcji 1.

## Na co zwrócić uwagę

Kolejność ma znaczenie: nazwę niespójnej kolumny trzeba ujednolicić *przed* połączeniem arkuszy, nie po. Połączenie po kolumnach o różnych nazwach po prostu nie znajdzie dopasowania.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" napisz: co poszłoby nie tak, gdyby połączenie obu arkuszy nastąpiło przed zmianą nazwy niespójnej kolumny? I: liczba wierszy spadła z 702 do 700 przez pominięcie dokładnie dwóch wierszy nad prawdziwym nagłówkiem — gdyby narzędzie eksportujące Meridian Outlet kiedyś dodało drugą pustą linię przed tytułem, co po cichu przestałoby działać w tym kodzie, i jak dałoby się to zauważyć, zanim spowodowałoby to realny błąd?

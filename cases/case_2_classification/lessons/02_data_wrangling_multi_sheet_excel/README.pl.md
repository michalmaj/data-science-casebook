# Lekcja 2 — Porządkowanie danych: wielo-arkuszowy Excel

## Głos mentora

"Zauważyłeś/zauważyłaś, że surowe wczytanie miało dwa wiersze za dużo — to wiersz tytułowy i prawdziwy nagłówek, oba wczytane jako dane. Dziś naprawiasz to porządnie, a przy okazji spotkasz podobny bałagan w arkuszu Customers: ten sam pomysł, inne przebranie."

## Cel lekcji

Wczytać oba arkusze `orders.xlsx` z ich prawdziwymi nagłówkami, ujednolicić niespójną nazwę kolumny z id klienta i połączyć je w jedną tabelę na poziomie zamówienia, gotową do analizy.

## Pytanie analityczne dnia

Gdy oba arkusze są już poprawnie wczytane i połączone, jak dokładnie wygląda pojedynczy, kompletny wiersz danych zamówienia Meridian Outlet?

## Co dostajesz

- Ten sam plik `data/orders.xlsx` co w Lekcji 1
- `task.py` — dwie funkcje do zaimplementowania: `load_customers`, `load_and_merge_orders`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Wczytaj arkusz Customers i potwierdź, że jego kolumna id pasuje teraz do `customer_id` z Orders.
4. Wczytaj i połącz arkusz Orders — sprawdź kształt i nazwy kolumn w porównaniu z tym, co widziałeś/widziałaś przy surowym wczytaniu w Lekcji 1.
5. Potwierdź, że połączona tabela nie ma braków danych i ma tę samą ~14% stopę zwrotów, jakiej można się spodziewać po Lekcji 1.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania: co poszłoby nie tak, gdybyś połączył/połączyła oba arkusze przed zmianą nazwy niespójnej kolumny, i dlaczego?

## Refleksja

Mentor pyta: zeszliście z 702 do 700 wierszy, pomijając dokładnie dwa wiersze nad prawdziwym nagłówkiem. Gdyby narzędzie eksportujące Meridian Outlet kiedyś dodało drugą pustą linię przed tytułem, co po cichu przestałoby działać w Twoim kodzie — i jak zauważyłbyś/zauważyłabyś to, zanim spowodowałoby to realny błąd?

# Lekcja 5 — Podział na train/test i pierwszy klasyfikator

**Szacowany czas:** 35-45 min

## Efekty uczenia się

- Będziesz umieć poprawnie podzielić dane do klasyfikacji, zachowując balans klas między train a test.
- Będziesz umieć dopasować klasyfikator `LogisticRegression` i ocenić jego predykcje przy domyślnym progu 0,5.
- Będziesz umieć porównać wskaźnik wykrywalności realnego klasyfikatora z baseline'em klasy większościowej, nie tylko jego surową dokładność.
- Będziesz umieć rozróżnić dwa różne pytania o "czy to się generalizuje?" — do kolejnych zamówień znanych klientów, czy do zupełnie nowych klientów — i wybrać to, które odpowiada scenariuszowi biznesowemu.

## Głos mentora

"Zbudowałeś/zbudowałaś baseline, który nigdy nie złapał ani jednego zwrotu. Teraz dopasuj prawdziwy model na trzech numerycznych sygnałach z Lekcji 3 — rabat, historia zwrotów, wiek konta — i sprawdź, czy prawdziwy klasyfikator radzi sobie lepiej przy tym samym progu 0.5."

## Cel lekcji

Poprawnie podzielić dane Meridian Outlet, dopasować prawdziwy klasyfikator `LogisticRegression` na trzech numerycznych sygnałach z Lekcji 3, i ocenić jego predykcje przy domyślnym progu 0.5.

Lekcja 3 pokazała też, że `product_category` to najsilniejszy sygnał, jaki znalazłeś/znalazłaś — zwroty w kategorii clothing na poziomie ~20% wobec 7% dla home_goods. Świadomie pomijamy ją tutaj w `FEATURE_COLUMNS`: kategoria wymaga dodatkowego kroku kodowania, zanim model może jej użyć, a to wykracza poza zakres tego case'u. Jeśli chcesz zobaczyć ten krok, opcjonalna Lekcja 7 Projektu końcowego przeprowadza przez to z użyciem `ColumnTransformer`.

## Pytanie analityczne dnia

Czy prawdziwy klasyfikator, wytrenowany na prawdziwych cechach, faktycznie łapie więcej zwrotów niż baseline większościowy — przynajmniej przy domyślnym progu?

## "Nowe dane" znaczą tu dwie różne rzeczy

`split_orders` powyżej wydziela zbiór testowy — ale *czego* właściwie testuje generalizację? Przy 264 klientach i 700 zamówieniach większość klientów (78%) złożyła więcej niż jedno zamówienie, a prosty losowy podział nie wie o tym nic: całkiem możliwe (i, jak zobaczysz, faktycznie się zdarza), że pierwsze zamówienie klienta X trafia do `train_df`, a jego drugie zamówienie do `test_df`. Ten wiersz testowy nie pochodzi od klienta, którego model nigdy nie spotkał — to *nowe zamówienie* od klienta, którego już ma w swojej bazie.

To realne, przydatne pytanie — "czy ten model działa na kolejnym zamówieniu klienta, którego już znamy?" — ale to inne pytanie niż "czy ten model działa na kliencie, którego nigdy wcześniej nie widzieliśmy?". Oba są uzasadnione; które z nich ma znaczenie, zależy całkowicie od tego, jak Meridian Outlet faktycznie będzie używać modelu. Jeśli system ocenia każde przychodzące zamówienie niezależnie od tego, czy to klient powracający, realistyczny jest scenariusz A (znani klienci). Jeśli Meridian Outlet konkretnie chce wiedzieć, jak model radzi sobie z zupełnie nowymi rejestracjami, to scenariusz B.

**Główny workflow tego case'u — każdy podział od tego miejsca do Lekcji 8 — odpowiada na scenariusz A: czy model działa na kolejnych zamówieniach klientów już obecnych w danych treningowych?** To zgadza się z faktycznym zleceniem Meridian Outlet ("które zamówienia są ryzykowne", nie "którzy nowi klienci są ryzykowni") i to właśnie robi już poprawnie, dla tego pytania, zwykły `split_orders` powyżej.

Żeby zobaczyć scenariusz B, podziel dane po kliencie, a nie po wierszu, tak żeby żaden klient nie wystąpił po obu stronach:

```python
from task import split_orders_by_customer

group_train_df, group_test_df = split_orders_by_customer(df)
```

Konkretny przykład: klientka `CUST-0231` — nazwiemy ją Anna — złożyła 7 zamówień. W podziale wierszowym 5 z nich trafia do `train_df`, a 2 do `test_df`: model nie spotyka w `test_df` kogoś zupełnie nieznanego, tylko jest sprawdzany na dwóch kolejnych zamówieniach osoby, którą już częściowo poznał — tak samo jak sprawdzilibyśmy, czy lojalna klientka z długą historią zamówień ma sensownie ocenione swoje kolejne zamówienia. W podziale po kliencie Anna trafia w całości na jedną stronę; nie ma "Anny, częściowo znanej".

| | Podział wierszowy (główny, scenariusz A) | Podział po kliencie (scenariusz B) |
|---|---:|---:|
| Wiersze / klienci w treningu | 560 / 248 | 577 / 211 |
| Wiersze / klienci w teście | 140 / 106 | 123 / 53 |
| Klienci obecni w obu zbiorach | 90 | 0 |
| % wierszy testowych, których klient jest też w treningu | 86,4% | 0% |
| Macierz pomyłek na teście przy progu 0,5 | `[[119, 1], [20, 0]]` | `[[108, 0], [15, 0]]` |
| ROC-AUC na teście | 0,643 | 0,672 |

Zauważ, że wyniki obu podziałów są *bliskie*, nie dramatycznie różne, a AUC podziału po kliencie jest tu nawet nieco wyższe — odwrotnie niż mogłoby się wydawać, gdyby podziały grupowe były po prostu "trudniejsze". Nie czytaj tego jako dowodu, że któryś podział jest błędny. Trzy powody, czemu to porównanie nie jest tak dramatyczne, jak mogłoby być: zbiory testowe są małe (140 i 123 wiersze, tylko 20 i 15 zwrotów odpowiednio — co daje dużo miejsca, by wynik jednego podziału się wahał); podział po kliencie nie jest stratyfikowany, więc jego stopy zwrotów train/test (14,38% / 12,20%) rozjeżdżają się bardziej niż w podziale wierszowym (13,93% / 14,29%); a `previous_returns_count`/`account_age_days` to stałe atrybuty przypisane każdemu klientowi niezależnie od jego zamówień (zobacz `data/generate.py` — są losowane, zanim istnieje jakiekolwiek zamówienie), nie bieżąca suma budowana z historii zamówień tego klienta. Gdyby cecha była czymś w stylu "stopa zwrotów tego klienta policzona z jego dotychczasowych zamówień", różnica między podziałem wierszowym a grupowym miałaby dużo większe znaczenie, bo podział wierszowy mógłby wtedy pozwolić przyszłym zamówieniom klienta po cichu wpływać na cechę opisującą jego przeszłość.

## Co dostajesz

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-4
- `task.py` — pięć funkcji do zaimplementowania: `load_and_merge_orders`, `split_orders`, `split_orders_by_customer`, `fit_classifier`, `predict_return`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Sprawdź `split_orders(df)` — potwierdź rozmiary zbioru treningowego i testowego, oraz że oba zachowują podobną stopę zwrotów.
4. Odpal `split_orders_by_customer` i porównaj jego statystyki nakładania się klientów z `split_orders` — potwierdź zero nakładania dla podziału grupowego wobec 90 klientów dla podziału wierszowego.
5. Dopasuj model i spójrz na jego współczynniki.
6. Wykonaj predykcję na zbiorze testowym i sprawdź macierz pomyłek — porównaj `tp` z baseline'em z Lekcji 4.
7. Spójrz na rzeczywiste przewidywane prawdopodobieństwa, nie tylko na etykiety 0/1.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania: biorąc pod uwagę zakres prawdopodobieństw, jaki zaobserwowałeś/zaobserwowałaś — czy ten model jest naprawdę bezużyteczny, czy 0.5 to po prostu zły próg dla problemu Meridian Outlet? Ta sama komórka pyta też, czemu wyniki podziału wierszowego i grupowego wyszły bliskie, a nie dramatycznie różne — odpowiedz też na to.

## Refleksja

Mentor pyta: model przypisał niektórym zamówieniom aż ~54% prawdopodobieństwa, a mimo to jego macierz pomyłek przy progu 0.5 wygląda niemal identycznie jak baseline z Lekcji 4. Jeśli prawdziwym priorytetem Meridian Outlet jest łapanie zwrotów, jak myślisz, co stanie się z macierzą pomyłek, gdy obniżysz próg decyzyjny z 0.5 do np. 0.3? Nie musisz tego jeszcze liczyć — to temat następnej lekcji.

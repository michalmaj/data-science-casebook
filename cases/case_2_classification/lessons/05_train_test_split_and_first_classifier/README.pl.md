# Lekcja 5 — Podział na train/test i pierwszy klasyfikator

**Szacowany czas:** 35-45 min

## Efekty uczenia się

- Będziesz umieć poprawnie podzielić dane do klasyfikacji, zachowując balans klas między train a test.
- Będziesz umieć dopasować klasyfikator `LogisticRegression` i ocenić jego predykcje przy domyślnym progu 0,5.
- Będziesz umieć porównać wskaźnik wykrywalności realnego klasyfikatora z baseline'em klasy większościowej, nie tylko jego surową dokładność.
- Będziesz umieć rozróżnić dwa różne pytania o "czy to się generalizuje?" — do kolejnych zamówień znanych klientów, czy do zupełnie nowych klientów — i wybrać to, które odpowiada scenariuszowi biznesowemu.
- Będziesz umieć wyjaśnić, czemu zbiór testowy zostaje zamknięty, dopóki model, jego cechy i próg decyzyjny nie są już ustalone — i pokazać problem progu 0,5 bez otwierania go zbyt wcześnie.

## Głos mentora

"Zbudowałeś/zbudowałaś baseline, który nigdy nie złapał ani jednego zwrotu. Teraz dopasuj prawdziwy model na trzech numerycznych sygnałach z Lekcji 3 — rabat, historia zwrotów, wiek konta — i sprawdź, czy prawdziwy klasyfikator radzi sobie lepiej przy tym samym progu 0.5."

## Cel lekcji

Poprawnie podzielić dane Meridian Outlet, dopasować prawdziwy klasyfikator `LogisticRegression` na trzech numerycznych sygnałach z Lekcji 3, i sprawdzić, co domyślny próg 0,5 z nim robi — bez otwierania `test_df`, żeby się tego dowiedzieć. `test_df` powstaje w tej lekcji i zostaje odłożony; otwieramy go znowu dopiero w Lekcji 6, po tym, jak próg zostanie faktycznie wybrany.

Lekcja 3 pokazała też, że `product_category` to najsilniejszy sygnał, jaki znalazłeś/znalazłaś — zwroty w kategorii clothing na poziomie ~20% wobec 7% dla home_goods. Świadomie pomijamy ją tutaj w `FEATURE_COLUMNS`: kategoria wymaga dodatkowego kroku kodowania, zanim model może jej użyć, a to wykracza poza zakres tego case'u. Jeśli chcesz zobaczyć ten krok, opcjonalna Lekcja 7 Projektu końcowego przeprowadza przez to z użyciem `ColumnTransformer`.

## Pytanie analityczne dnia

Czy prawdziwy klasyfikator, wytrenowany na prawdziwych cechach, faktycznie łapie więcej zwrotów niż baseline większościowy — przynajmniej przy domyślnym progu?

## Co dostajesz

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-4
- `task.py` — pięć funkcji do zaimplementowania: `load_and_merge_orders`, `split_orders`, `split_orders_by_customer`, `fit_classifier`, `predict_return`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Sprawdź `split_orders(df)` — potwierdź rozmiary zbioru treningowego i testowego, oraz że oba zachowują podobną stopę zwrotów.
4. Sprawdź nakładanie się klientów między `train_df` i `test_df` — to fakt o strukturze podziału, nie spojrzenie na wynik modelu, więc można to zrobić już teraz.
5. Dopasuj model i spójrz na jego współczynniki.
6. Wykonaj predykcję *w próbie treningowej*, na samym `train_df` — nie na `test_df` — i sprawdź macierz pomyłek. Porównaj `tp` z baseline'em z Lekcji 4.
7. Spójrz na rzeczywiste przewidywane prawdopodobieństwa (wciąż w próbie treningowej), nie tylko na etykiety 0/1.
8. Odpal `split_orders_by_customer` na `train_df` (nie na całym `df`) i porównaj go z dodatkowym podziałem wierszowym `train_df` — potwierdź zero nakładania dla podziału grupowego wobec realnego nakładania dla podziału wierszowego, a potem porównaj oba na ich własnym, wydzielonym fragmencie walidacyjnym.

## "Nowe dane" znaczą tu dwie różne rzeczy — a zbiór testowy zostaje zamknięty w obu przypadkach

`split_orders` (krok 3 powyżej) wydziela zbiór testowy — ale *czego* właściwie testuje generalizację? Przy 264 klientach i 700 zamówieniach większość klientów (78%) złożyła więcej niż jedno zamówienie, a prosty losowy podział nie wie o tym nic: całkiem możliwe (i, jak pokazał krok 4, faktycznie się zdarza), że pierwsze zamówienie klienta X trafia do `train_df`, a jego drugie zamówienie do `test_df`. Ten wiersz testowy nie pochodzi od klienta, którego model nigdy nie spotkał — to *nowe zamówienie* od klienta, którego już ma w swojej bazie.

To realne, przydatne pytanie — "czy ten model działa na kolejnym zamówieniu klienta, którego już znamy?" — ale to inne pytanie niż "czy ten model działa na kliencie, którego nigdy wcześniej nie widzieliśmy?". Oba są uzasadnione; które z nich ma znaczenie, zależy całkowicie od tego, jak Meridian Outlet faktycznie będzie używać modelu. Jeśli system ocenia każde przychodzące zamówienie niezależnie od tego, czy to klient powracający, realistyczny jest scenariusz A (znani klienci). Jeśli Meridian Outlet konkretnie chce wiedzieć, jak model radzi sobie z zupełnie nowymi rejestracjami, to scenariusz B.

**Główny workflow tego case'u — każdy podział od tego miejsca do Lekcji 8 — odpowiada na scenariusz A: czy model działa na kolejnych zamówieniach klientów już obecnych w danych treningowych?** To zgadza się z faktycznym zleceniem Meridian Outlet ("które zamówienia są ryzykowne", nie "którzy nowi klienci są ryzykowni") i to właśnie robi już poprawnie, dla tego pytania, zwykły `split_orders`.

Zobaczenie tego rozróżnienia nie wymaga jednak otwierania `test_df`. Krok 8 odpowiada na nie inaczej: `split_orders_by_customer` (scenariusz B) jest porównywany z *drugim* podziałem wierszowym (scenariusz A) — oba zastosowane do `train_df`, dając parę `fit`/`val` każdy, tego samego rodzaju podział, jaki Lekcja 6 wykorzysta na serio. **`val_df` tutaj to próbna kopia `test_df`, nie sam `test_df`** — służy do wypróbowywania rzeczy (porównywania podziałów, sprawdzania progu), zanim coś zostanie ustalone na stałe; `test_df` służy do potwierdzenia decyzji, która już została podjęta. Wyniki walidacyjne mogą wpływać na to, co zdecydujesz dalej (który podział wybrać, jaki próg wybrać w Lekcji 6); wyniki testowe, gdy już na nie spojrzysz, są ostatnim słowem — nie ma już nic "dalej" do zdecydowania.

Konkretny przykład: klientka `CUST-0231` — nazwiemy ją Anna — ma 5 zamówień w `train_df` (kolejne 2 jej zamówienia trafiły do `test_df`, nietknięte, jeszcze przy głównym podziale). W podziale wierszowym `fit`/`val` 2 z jej 5 zamówień trafiają do `fit_df`, a 3 do `val_df`: model nie spotyka w `val_df` kogoś zupełnie nieznanego, tylko jest sprawdzany na kolejnych zamówieniach osoby, którą już częściowo poznał. W podziale po kliencie wszystkie 5 zamówień Anny trafia na tę samą stronę; nie ma "Anny, częściowo znanej".

| | Podział wierszowy (główny, scenariusz A) | Podział po kliencie (scenariusz B) |
|---|---:|---:|
| Wiersze / klienci w `fit` | 448 / 234 | 451 / 198 |
| Wiersze / klienci w `val` | 112 / 91 | 109 / 50 |
| Klienci obecni w `fit` i `val` | 77 | 0 |
| Macierz pomyłek na `val` przy progu 0,5 | `[[96, 0], [16, 0]]` | `[[93, 0], [16, 0]]` |
| ROC-AUC na `val` (pole pod krzywą ROC — porównanie jakości rankingu niezależne od progu; 0,5 to przypadek, 1,0 to idealny model) | 0,553 | 0,606 |

Zauważ, że wyniki obu podziałów są *bliskie*, nie dramatycznie różne, choć AUC podziału po kliencie jest tu nieco wyższe — nie czytaj tego jako dowodu, że któryś podział jest błędny. Trzy powody, czemu to porównanie nie jest tak dramatyczne, jak mogłoby być: te fragmenty walidacyjne są małe (112 i 109 wierszy, tylko 16 zwrotów w każdym — co daje dużo miejsca, by wynik jednego podziału się wahał); podział po kliencie nie jest stratyfikowany, więc jego własny balans klas rozjeżdża się trochę bardziej od `train_df` niż w podziale wierszowym; a `previous_returns_count`/`account_age_days` to stałe atrybuty przypisane każdemu klientowi niezależnie od jego zamówień (zobacz `data/generate.py` — są losowane, zanim istnieje jakiekolwiek zamówienie), nie bieżąca suma budowana z historii zamówień tego klienta. Gdyby cecha była czymś w stylu "stopa zwrotów tego klienta policzona z jego dotychczasowych zamówień", różnica między podziałem wierszowym a grupowym miałaby dużo większe znaczenie, bo podział wierszowy mógłby wtedy pozwolić przyszłym zamówieniom klienta po cichu wpływać na cechę opisującą jego przeszłość.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania: biorąc pod uwagę zakres prawdopodobieństw, jaki zaobserwowałeś/zaobserwowałaś — czy ten model jest naprawdę bezużyteczny, czy 0.5 to po prostu zły próg dla problemu Meridian Outlet? Ta sama komórka pyta też, czemu wyniki podziału wierszowego i grupowego wyszły bliskie, a nie dramatycznie różne — odpowiedz też na to.

## Refleksja

Mentor pyta: nawet w próbie treningowej model przypisał niektórym zamówieniom aż ~40% prawdopodobieństwa, a mimo to jego macierz pomyłek przy progu 0.5 wygląda niemal identycznie jak baseline z Lekcji 4. Jeśli prawdziwym priorytetem Meridian Outlet jest łapanie zwrotów, jak myślisz, co stanie się z macierzą pomyłek, gdy obniżysz próg decyzyjny z 0.5 do np. 0.3? Nie musisz tego jeszcze liczyć — to temat następnej lekcji.

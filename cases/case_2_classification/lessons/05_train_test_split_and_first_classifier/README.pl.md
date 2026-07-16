# Lekcja 5 — Podział na train/test i pierwszy klasyfikator

**Szacowany czas:** 35-45 min

## Efekty uczenia się

- Będziesz umieć poprawnie podzielić dane do klasyfikacji, zachowując balans klas między train a test.
- Będziesz umieć dopasować klasyfikator `LogisticRegression` i ocenić jego predykcje przy domyślnym progu 0,5.
- Będziesz umieć porównać wskaźnik wykrywalności realnego klasyfikatora z baseline'em klasy większościowej, nie tylko jego surową dokładność.

## Głos mentora

"Zbudowałeś/zbudowałaś baseline, który nigdy nie złapał ani jednego zwrotu. Teraz dopasuj prawdziwy model na sygnałach znalezionych w Lekcji 3 — rabat, historia zwrotów, wiek konta — i sprawdź, czy prawdziwy klasyfikator radzi sobie lepiej przy tym samym progu 0.5."

## Cel lekcji

Poprawnie podzielić dane Meridian Outlet, dopasować prawdziwy klasyfikator `LogisticRegression` na sygnałach znalezionych w Lekcji 3, i ocenić jego predykcje przy domyślnym progu 0.5.

## Pytanie analityczne dnia

Czy prawdziwy klasyfikator, wytrenowany na prawdziwych cechach, faktycznie łapie więcej zwrotów niż baseline większościowy — przynajmniej przy domyślnym progu?

## Co dostajesz

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-4
- `task.py` — cztery funkcje do zaimplementowania: `load_and_merge_orders`, `split_orders`, `fit_classifier`, `predict_return`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Sprawdź `split_orders(df)` — potwierdź rozmiary zbioru treningowego i testowego, oraz że oba zachowują podobną stopę zwrotów.
4. Dopasuj model i spójrz na jego współczynniki.
5. Wykonaj predykcję na zbiorze testowym i sprawdź macierz pomyłek — porównaj `tp` z baseline'em z Lekcji 4.
6. Spójrz na rzeczywiste przewidywane prawdopodobieństwa, nie tylko na etykiety 0/1.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania: biorąc pod uwagę zakres prawdopodobieństw, jaki zaobserwowałeś/zaobserwowałaś — czy ten model jest naprawdę bezużyteczny, czy 0.5 to po prostu zły próg dla problemu Meridian Outlet?

## Refleksja

Mentor pyta: model przypisał niektórym zamówieniom aż ~54% prawdopodobieństwa, a mimo to jego macierz pomyłek przy progu 0.5 wygląda niemal identycznie jak baseline z Lekcji 4. Jeśli prawdziwym priorytetem Meridian Outlet jest łapanie zwrotów, jak myślisz, co stanie się z macierzą pomyłek, gdy obniżysz próg decyzyjny z 0.5 do np. 0.3? Nie musisz tego jeszcze liczyć — to temat następnej lekcji.

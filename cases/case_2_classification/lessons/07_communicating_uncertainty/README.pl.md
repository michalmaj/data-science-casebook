# Lekcja 7 — Komunikowanie niepewności

**Szacowany czas:** 45-55 min

## Efekty uczenia się

- Będziesz umieć zamienić przewidywane prawdopodobieństwo w zrozumiały poziom ryzyka, na którym mógłby oprzeć się zespół nietechniczny.
- Będziesz umieć zbudować raport ryzyka per zamówienie w kształcie, w jakim faktycznie użyłby go zespół operacyjny.
- Będziesz umieć sprawdzić, czy poziomy ryzyka naprawdę odzwierciedlają ryzyko wyniku, czy tylko wyglądają uporządkowanie bez bycia skalibrowanymi.

## Głos mentora

"Wybrałeś/wybrałaś próg — teraz wyobraź sobie, że dajesz Meridian Outlet arkusz surowych prawdopodobieństw. Nikt w operacjach nie chce czytać '0.34'. Zamień tę liczbę w coś, na czym człowiek może się oprzeć."

## Cel lekcji

Przetłumaczyć przewidywane przez model prawdopodobieństwa na prostą kategorię ryzyka i zbudować raport, z którego naprawdę korzystałby zespół operacyjny Meridian Outlet — a potem sprawdzić, czy te kategorie faktycznie odzwierciedlają ryzyko.

## Pytanie analityczne dnia

Gdy już podzielisz zamówienia na ryzyko Low/Medium/High, czy te kategorie faktycznie śledzą prawdziwe ryzyko zwrotu — czy tylko wyglądają schludnie?

## Co dostajesz

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-6
- `task.py` — siedem funkcji do zaimplementowania: `load_and_merge_orders`, `split_orders`, `fit_classifier`, `risk_tier`, `risk_report`, plus dwie kolejne — `tier_summary` i `brier_score` — które sprawdzają, czy przewidywane prawdopodobieństwa w przedziałach są rzeczywiście wiarygodne, a nie tylko poprawnie uporządkowane
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Odtwórz dokładnie ten sam podział i model co w Lekcjach 5-6.
4. Wypróbuj `risk_tier` na kilku przykładowych prawdopodobieństwach.
5. Zbuduj pełny `risk_report` dla zbioru testowego.
6. Sprawdź rzeczywistą stopę zwrotów w każdym przedziale — czy rośnie od Low do High tak, jak byś się spodziewał/spodziewała?
7. Wywołaj `tier_summary` i porównaj *przewidywane* prawdopodobieństwo każdego przedziału z jego *rzeczywistą* stopą — dobrze skalibrowany model powinien mieć te liczby bliskie sobie.
8. Wywołaj `brier_score` i porównaj go z wynikiem dla baseline'u, który zawsze przewiduje bazową stopę zbioru treningowego — czy ten model jest faktycznie lepiej skalibrowany niż nicnierobienie, czy tylko lepszy w sortowaniu zamówień wg ryzyka?

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania: opisz, co zaobserwowałeś/zaobserwowałaś, sprawdzając rzeczywistą stopę zwrotów wg przedziału, i co `tier_summary`/`brier_score` powiedziały Ci o kalibracji — czy przewidywane prawdopodobieństwo przedziału High zgadzało się z jego rzeczywistą stopą? Jeśli nie, czy ufałbyś/ufałabyś pojedynczej predykcji z przedziału High bez zastrzeżeń?

## Refleksja

Mentor pyta: obserwowana stopa zwrotów w przedziale High (ok. 17,6%) jest w tym zbiorze testowym w rzeczywistości nieco *niższa* niż w przedziale Medium (ok. 22,7%), mimo że "High" powinno oznaczać wyższe ryzyko — a `tier_summary` pokazuje, że to nie tylko dziwna kolejność: przewidywana średnia w przedziale High to ok. 38,3%, ponad dwa razy więcej niż to, co faktycznie się wydarzyło. Skoro w tym przedziale jest tylko 17 zamówień, czy to realny problem z kalibracją, czy po prostu szum wynikający z małej próbki? `CalibratedClassifierCV` ze scikit-learn to standardowe narzędzie do naprawiania takiej luki — sięgnąłbyś/sięgnęłabyś po nie tutaj, czy najpierw chciałbyś/chciałabyś więcej danych? Jak przekazałbyś/przekazałabyś tę niuansową informację Meridian Outlet, zamiast prezentować przedziały albo surowe prawdopodobieństwa jako bardziej precyzyjne, niż naprawdę są?

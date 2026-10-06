# Lekcja 7 — Komunikowanie niepewności

**Szacowany czas:** 45-55 min

## Po co to robimy

Próg jest już wybrany — teraz wyobraź sobie, że dajesz Meridian Outlet arkusz surowych prawdopodobieństw. Nikt w operacjach nie chce czytać "0,34". Trzeba zamienić tę liczbę w coś, na czym człowiek może się oprzeć.

Pytanie na dziś: gdy już podzielimy zamówienia na ryzyko Low/Medium/High, czy te kategorie śledzą prawdziwe ryzyko zwrotu — czy tylko wyglądają schludnie?

## Co masz zrobić

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-6.
- W `task.py` zaimplementuj siedem funkcji: `load_and_merge_orders`, `split_orders`, `fit_classifier`, `risk_tier`, `risk_report`, plus dwie kolejne — `tier_summary` i `brier_score` — które sprawdzają, czy przewidywane prawdopodobieństwa w przedziałach są rzeczywiście wiarygodne, a nie tylko poprawnie uporządkowane.
- W notebooku: odtwórz dokładnie ten sam podział i model co w Lekcjach 5-6. Wypróbuj `risk_tier` na kilku przykładowych prawdopodobieństwach. Zbuduj pełny `risk_report` dla zbioru testowego. Sprawdź rzeczywistą stopę zwrotów w każdym przedziale — czy rośnie od Low do High, jak można by się spodziewać? Wywołaj `tier_summary` i porównaj *przewidywane* prawdopodobieństwo każdego przedziału z jego *rzeczywistą* stopą — dobrze skalibrowany model powinien mieć te liczby bliskie sobie. Wywołaj `brier_score` i porównaj go z wynikiem dla modelu bazowego, który zawsze przewiduje bazową stopę zbioru treningowego.

## Na co zwrócić uwagę

Dobre sortowanie według ryzyka i dobra kalibracja to dwie różne rzeczy. Model może poprawnie uporządkować zamówienia od najmniej do najbardziej ryzykownego, a mimo to jego przewidywane prawdopodobieństwa mogą się mijać z rzeczywistymi stopami zwrotu w danym przedziale — `tier_summary` i `brier_score` sprawdzają właśnie to drugie, nie pierwsze.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" opisz, co widać po sprawdzeniu rzeczywistej stopy zwrotów wg przedziału, i co `tier_summary`/`brier_score` powiedziały o kalibracji — zgadzało się przewidywane prawdopodobieństwo przedziału High z jego rzeczywistą stopą? Jeśli nie, czy warto ufać pojedynczej predykcji z przedziału High bez zastrzeżeń? I: obserwowana stopa zwrotów w przedziale High (ok. 17,6%) jest w tym zbiorze testowym w rzeczywistości nieco *niższa* niż w przedziale Medium (ok. 22,7%), mimo że "High" powinno oznaczać wyższe ryzyko — a `tier_summary` pokazuje, że to nie tylko dziwna kolejność: przewidywana średnia w przedziale High to ok. 38,3%, ponad dwa razy więcej niż to, co faktycznie się wydarzyło. Skoro w tym przedziale jest tylko 17 zamówień, czy to realny problem z kalibracją, czy po prostu szum wynikający z małej próbki? `CalibratedClassifierCV` ze scikit-learn to standardowe narzędzie do naprawiania takiej luki — warto po nie sięgnąć tutaj, czy lepiej najpierw zebrać więcej danych? Jak przekazać tę niuansową informację Meridian Outlet, zamiast prezentować przedziały albo surowe prawdopodobieństwa jako bardziej precyzyjne, niż naprawdę są?

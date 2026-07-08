# Lekcja 7 — Komunikowanie niepewności

## Głos mentora

"Wybrałeś/wybrałaś próg — teraz wyobraź sobie, że dajesz Meridian Outlet arkusz surowych prawdopodobieństw. Nikt w operacjach nie chce czytać '0.34'. Zamień tę liczbę w coś, na czym człowiek może się oprzeć."

## Cel lekcji

Przetłumaczyć przewidywane przez model prawdopodobieństwa na prostą kategorię ryzyka i zbudować raport, z którego naprawdę korzystałby zespół operacyjny Meridian Outlet — a potem sprawdzić, czy te kategorie faktycznie odzwierciedlają ryzyko.

## Pytanie analityczne dnia

Gdy już podzielisz zamówienia na ryzyko Low/Medium/High, czy te kategorie faktycznie śledzą prawdziwe ryzyko zwrotu — czy tylko wyglądają schludnie?

## Co dostajesz

- Ten sam plik `data/orders.xlsx` co w Lekcjach 1-6
- `task.py` — pięć funkcji do zaimplementowania: `load_and_merge_orders`, `split_orders`, `fit_classifier`, `risk_tier`, `risk_report`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Odtwórz dokładnie ten sam podział i model co w Lekcjach 5-6.
4. Wypróbuj `risk_tier` na kilku przykładowych prawdopodobieństwach.
5. Zbuduj pełny `risk_report` dla zbioru testowego.
6. Sprawdź rzeczywistą stopę zwrotów w każdym przedziale — czy rośnie od Low do High tak, jak byś się spodziewał/spodziewała?

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania: opisz, co zaobserwowałeś/zaobserwowałaś, sprawdzając rzeczywistą stopę zwrotów wg przedziału — czy wyglądało to tak, jak się spodziewałeś/spodziewałaś? Jeśli nie, co Twoim zdaniem to tłumaczy?

## Refleksja

Mentor pyta: obserwowana stopa zwrotów w przedziale High (ok. 17,6%) jest w tym zbiorze testowym w rzeczywistości nieco *niższa* niż w przedziale Medium (ok. 22,7%), mimo że "High" powinno oznaczać wyższe ryzyko. Skoro w tym przedziale jest tylko 17 zamówień, czy to realny problem z kategoriami ryzyka, czy po prostu szum wynikający z małej próbki? Jak przekazałbyś/przekazałabyś tę niuansową informację Meridian Outlet, zamiast prezentować przedziały jako idealnie uporządkowaną skalę ryzyka?

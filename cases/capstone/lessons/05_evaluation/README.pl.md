# Lekcja 5 — Ewaluacja

**Szacowany czas:** 65-85 min

## Decyzja do podjęcia

Lekcja 4 pokazała tylko, jak model radzi sobie z danymi, które już widział. To nie jest ewaluacja, to próba generalna. Teraz trzeba sprawdzić, czy model faktycznie się czegoś nauczył — i zdecydować, czy wynik jest wystarczająco dobry, żeby na jego podstawie działać.

## Masz do dyspozycji

- `task.py` — siedem funkcji z Lekcji 4, odtworzonych, plus sześć nowych: `evaluate_regression`, `evaluate_classification` (przyjmuje opcjonalny `threshold`), `evaluate_clustering`, `cluster_stability`, oraz — nowość w tej lekcji — `split_for_validation` i `metrics_at_threshold` (tylko klasyfikacja), `cluster_metrics_by_k` (tylko klasteryzacja).
- W notebooku: uruchom komórkę pasującą do typu problemu — wczytuje, dzieli, imputuje, dopasowuje i ocenia w jednym miejscu. Porównaj wynik na zbiorze testowym z Lekcją 4 i zdecyduj, czy model jest wystarczająco dobry, żeby na jego podstawie działać.

## Zanim zdecydujesz

**Ocena klasteryzacji:** w przeciwieństwie do regresji i klasyfikacji, klasteryzacja nie jest tutaj oceniana na zbiorze testowym, którego model nie widział — silhouette score z `evaluate_clustering` jest liczony na tych samych danych, na których model był dopasowany, co jest standardem dla oceny *jakości* klastrów (zgodnie z podejściem Case 3). Komórka klasteryzacji uruchamia też `cluster_stability`, która sprawdza coś, co zbiór testowy daje regresji/klasyfikacji za darmo: czy wynik utrzymałby się na innej próbce. Ponowne dopasowanie na powtarzanych podpróbkach i porównanie przypisań klastrów przez Adjusted Rand Index (ARI — 1,0 oznacza identyczne, blisko 0 oznacza praktycznie losowe) mówi, czy segmenty są prawdziwe, czy są artefaktem akurat tego zbioru danych. To sprawdza wrażliwość na *to, które wiersze trafiają do próbki*, nie na losową inicjalizację KMeans — to dwa różne pytania, a `cluster_stability` testuje tylko pierwsze z nich.

**Wybór progu klasyfikacji:** domyślny `threshold=0,5` w `fit_classification_baseline_and_model` i `evaluate_classification` to wartość domyślna, nie wyrok. Zanim dotkniesz `test_df`, wydziel parę `fit_df`/`val_df` z `train_df` za pomocą `split_for_validation`, dopasuj na `fit_df` i porównaj kilka kandydujących progów za pomocą `metrics_at_threshold` na `val_df`. Dla sugerowanego zestawu cech LendWell, progi między 0,2 a 0,6 wymieniają precyzję na recall — niższy próg wychwytuje więcej pożyczek, które faktycznie kończą się defaultem, kosztem oznaczenia większej liczby pożyczek, które by go nie miały. Który kompromis jest właściwy, zależy od tego, który błąd kosztuje klienta więcej: zaakceptowanie pożyczki, która zdefoltuje, czy odrzucenie wnioskodawcy, który by ją spłacił. Wybierz próg na `val_df`, a potem — i tylko potem — wywołaj `evaluate_classification(..., threshold=wybrany_próg)` na `test_df` po prawdziwą liczbę.

**Wybór k dla klasteryzacji:** sugerowane `k=3` w `fit_clustering_model` to punkt wyjścia, nie odpowiedź. `cluster_metrics_by_k` raportuje inercję i silhouette dla zakresu wartości k — spójrz na obie, plus na sprawdzenie `cluster_stability` powyżej, zanim zdecydujesz. Te metryki nie będą się automatycznie zgadzać (niższy silhouette dla jednego k nie sprawia, że k z wyższym silhouette jest "tą" poprawną liczbą segmentów) — właściwe k zależy też od tego, czy wynikające z niego grupy mają rozmiar i kształt, na którym klient mógłby działać.

## Uzasadnij

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Te testy sprawdzają liczby ewaluacji dla sugerowanych zestawów cech — nie mogą powiedzieć, czy model jest wystarczająco dobry dla konkretnego pytania z Lekcji 1.

Dwa do trzech zdań: czy ten model warto polecić klientowi z Lekcji 1 w obecnej formie, czy wymaga jeszcze pracy? Bądź konkretny co do tego, co mówi wynik ewaluacji. Na ścieżce klasyfikacji podaj wybrany próg i uzasadnienie; na ścieżce klasteryzacji — wybrane k i uzasadnienie. I: dla klasyfikacji i regresji są teraz dwa wyniki — na zbiorze treningowym (Lekcja 4) i na zbiorze testowym (ta lekcja). Gdyby te dwie liczby opowiadały bardzo różne historie, co mówiłoby to o modelu — i której liczbie warto ufać bardziej, i dlaczego?

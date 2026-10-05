# Lekcja 5 — Ewaluacja

**Szacowany czas:** 65-85 min

## Efekty uczenia się

- Będziesz umieć ocenić swój model z Lekcji 4 na wydzielonych danych testowych, używając metryki faktycznie pasującej do Twojego typu problemu.
- Będziesz umieć sprawdzić stabilność rozwiązania klasteryzacyjnego przez resampling zamiast wydzielonego splitu, i wyjaśnić, dlaczego to właściwy zamiennik, gdy nie ma targetu do wydzielenia.
- Będziesz umieć stwierdzić, czy wynik Twojego modelu na zbiorze testowym nadal przebija baseline, tak jak robił to jego wynik na zbiorze treningowym.
- Będziesz umieć wybrać próg klasyfikacji na splicie walidacyjnym — nie na `test_df` i nie domyślnie — i uzasadnić go tym, który błąd kosztuje Twojego klienta więcej.
- Będziesz umieć porównać wartości k dla problemu klasteryzacji, używając więcej niż jednej metryki, zamiast ufać jednej zaszytej na sztywno wartości domyślnej.

## Głos mentora

"Lekcja 4 pokazała Ci tylko, jak model radzi sobie z danymi, które już widział. To nie jest ewaluacja, to próba generalna. Teraz sprawdzisz, czy faktycznie się czegoś nauczył."

## Cel lekcji

Ocenić Twój baseline i model z Lekcji 4 na danych testowych, których model nigdy nie widział podczas dopasowywania — używając metryki faktycznie pasującej do Twojego typu problemu.

## Pytanie analityczne dnia

Czy wynik Twojego modelu na zbiorze testowym nadal pokonuje baseline, tak jak jego wynik na zbiorze treningowym w Lekcji 4?

## Co dostajesz

- Ten sam zbiór danych, który wybrałeś/wybrałaś w Lekcji 1
- `task.py` — siedem funkcji z Lekcji 4, odtworzonych, plus sześć nowych: `evaluate_regression`, `evaluate_classification` (przyjmuje teraz opcjonalny `threshold`), `evaluate_clustering`, `cluster_stability`, oraz — nowość w tej lekcji — `split_for_validation` i `metrics_at_threshold` (tylko klasyfikacja), `cluster_metrics_by_k` (tylko klasteryzacja). Użyj tylko tych, które pasują do Twojego zbioru.
- `lesson.ipynb` — notebook, w którym uruchomisz cały swój pipeline i go ocenisz

## Praca w notebooku

- Uruchom tylko komórkę pasującą do typu problemu Twojego zbioru — wczytuje, dzieli, imputuje, dopasowuje i ocenia w jednym miejscu (komórka klasteryzacji dodatkowo skaluje cechy przed dopasowaniem).
- Porównaj wynik na zbiorze testowym z tym, co zobaczyłeś/zobaczyłaś w Lekcji 4.
- Zdecyduj, czy model jest wystarczająco dobry, żeby na jego podstawie działać.

**Uwaga o ocenie klasteryzacji:** w przeciwieństwie do regresji i klasyfikacji, klasteryzacja nie jest tutaj oceniana na zbiorze testowym, którego model nie widział — silhouette score z `evaluate_clustering` jest liczony na tych samych danych, na których model był dopasowany, co jest standardem dla oceny *jakości* klastrów (zgodnie z podejściem Case 3). Komórka klasteryzacji uruchamia też `cluster_stability`, która sprawdza coś, co zbiór testowy daje regresji/klasyfikacji za darmo: czy wynik utrzymałby się na innej próbce. Ponowne dopasowanie na powtarzanych podpróbkach i porównanie przypisań klastrów przez Adjusted Rand Index (ARI — 1,0 oznacza identyczne, blisko 0 oznacza praktycznie losowe) mówi Ci, czy Twoje segmenty są prawdziwe, czy są artefaktem akurat tego zbioru danych. To sprawdza wrażliwość na *to, które wiersze trafiają do próbki*, nie na losową inicjalizację KMeans — to dwa różne pytania, a `cluster_stability` testuje tylko pierwsze z nich (zawsze dopasowuje z tym samym `random_state`).

**Uwaga o wyborze progu klasyfikacji:** domyślny `threshold=0.5` w `fit_classification_baseline_and_model` i `evaluate_classification` to wartość domyślna, nie wyrok. Zanim dotkniesz `test_df`, wydziel parę `fit_df`/`val_df` z `train_df` za pomocą `split_for_validation`, dopasuj na `fit_df` i porównaj kilka kandydujących progów za pomocą `metrics_at_threshold` na `val_df`. Dla sugerowanego zestawu cech LendWell, progi między 0,2 a 0,6 wymieniają precyzję na recall — niższy próg wychwytuje więcej pożyczek, które faktycznie kończą się defaultem, kosztem oznaczenia większej liczby pożyczek, które by go nie miały. Który kompromis jest właściwy, zależy od tego, który błąd kosztuje Twojego klienta więcej: zaakceptowanie pożyczki, która zdefoltuje, czy odrzucenie wnioskodawcy, który by ją spłacił. Wybierz próg na `val_df`, a potem — i tylko potem — wywołaj `evaluate_classification(..., threshold=twój_wybór)` na `test_df` po swoją prawdziwą liczbę.

**Uwaga o wyborze k dla klasteryzacji:** sugerowane `k=3` w `fit_clustering_model` to punkt wyjścia, nie odpowiedź. `cluster_metrics_by_k` raportuje inercję i silhouette dla zakresu wartości k — spójrz na obie, plus na sprawdzenie `cluster_stability` powyżej, zanim zdecydujesz. Te metryki nie będą się automatycznie zgadzać (niższy silhouette dla jednego k nie sprawia, że k z wyższym silhouette jest "tą" poprawną liczbą segmentów) — właściwe k zależy też od tego, czy wynikające z niego grupy mają rozmiar i kształt, na którym Twój klient mógłby działać.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Te testy sprawdzają liczby ewaluacji dla sugerowanych zestawów cech — nie mogą powiedzieć Ci, czy Twój model jest wystarczająco dobry dla Twojego faktycznego pytania z Lekcji 1.

## Zadanie domowe

Dwa do trzech zdań: czy faktycznie zarekomendowałbyś/zarekomendowałabyś ten model swojemu klientowi z Lekcji 1 w obecnej formie, czy wymaga jeszcze pracy? Bądź konkretny/konkretna co do tego, co mówi Ci wynik ewaluacji. Jeśli jesteś na ścieżce klasyfikacji, podaj wybrany próg i czemu go wybrałeś/wybrałaś; jeśli na ścieżce klasteryzacji — podaj wybrane k i czemu.

## Refleksja

Mentor pyta: dla klasyfikacji i regresji masz teraz zarówno wynik na zbiorze treningowym (Lekcja 4), jak i na zbiorze testowym (ta lekcja). Gdyby te dwie liczby opowiadały bardzo różne historie, co mówiłoby to o Twoim modelu — i której liczbie ufałbyś/ufałabyś bardziej, i dlaczego?

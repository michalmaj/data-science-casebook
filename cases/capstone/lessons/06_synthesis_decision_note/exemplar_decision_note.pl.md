# Wzorcowa notatka decyzyjna — Capstone (ścieżka regresji)

*To jest wzorcowa odpowiedź dla jednej ścieżki capstone'u (regresja, Riverside Community Clinic), napisana po ukończeniu wszystkich 6 lekcji. Nie czytaj jej przed napisaniem własnej — sensem tego ćwiczenia jest dojście do tych wniosków samodzielnie; ten plik istnieje, żebyś mógł/mogła porównać swoje rozumowanie z dobrą odpowiedzią później, nie żeby go skopiować. Jeśli wybrałeś/aś inny zbiór (klasyfikacja albo klasteryzacja), ta notatka pokazuje format i głębię, jakiej oczekujemy — nie konkretną treść dla Twojego zbioru.*

## 1. Pytanie biznesowe

Czy Riverside Community Clinic może przewidzieć, jak długo pacjent będzie czekał, na podstawie informacji dostępnych przy rejestracji — ile pacjentów jest przed nim w kolejce, ilu pracowników jest na zmianie, pora dnia i wiek pacjenta — na tyle precyzyjnie, żeby dać pacjentom bardziej uczciwe oszacowanie czasu oczekiwania niż płaska średnia dla całej kliniki?

## 2. Podejście

Wczytałem/am dane kliniki, podzieliłem/am je 80/20 na train/test, a następnie zaimputowałem/am niewielką liczbę brakujących wartości `staff_on_duty` medianą policzoną wyłącznie ze zbioru treningowego (zastosowaną do obu zbiorów). Kolumna `department` też ma braki, ale nie użyłem/am jej jako cechy, więc nigdy nie została zaimputowana. Porównałem/am baseline średniej (zawsze przewiduj średni czas oczekiwania ze zbioru treningowego) z regresją liniową dopasowaną na `num_patients_ahead`, `staff_on_duty`, `hour_of_day` i `patient_age`, przewidującą `wait_time_minutes`.

## 3. Wyniki

| Predyktor | MAE (min) |
|---|---:|
| Baseline (średni czas oczekiwania) | 18,57 |
| Model liniowy | 10,60 |

Błąd modelu na zbiorze testowym (10,60 minuty) jest zbliżony do jego błędu treningowego z Lekcji 4, co jest dobrym znakiem — oznacza to, że model generalizuje na pacjentów, których nigdy nie widział podczas dopasowania, nie tylko na tych, na których był trenowany.

## 4. Wybór modelu i pewność

To, że MAE na zbiorze testowym (10,60) i MAE treningowe z Lekcji 4 mieszczą się w tym samym zakresie — zamiast błędu testowego dramatycznie gorszego — jest tym, co uzasadnia zaufanie do tego modelu, nie sama surowa liczba MAE w izolacji. Model, który świetnie wygląda na danych treningowych, ale rozpada się na zbiorze testowym, zapamiętywałby dane, nie uczyłby się z nich; ten model tego nie robi.

## 5. Interpretacja

Średni błąd ~10,6 minuty oznacza, że klinika może teraz dać pacjentom spersonalizowane oszacowanie, które zwykle mieści się w granicach ok. 10,6 minuty od prawdy — realna poprawa względem obecnego płaskiego baseline'u, który zawsze mówi każdemu pacjentowi ok. 41,5 minuty i myli się średnio o ok. 18,6 minuty. To wystarczająco precyzyjne, żeby było użyteczne do ustawiania oczekiwań, ale nie na tyle precyzyjne, żeby obiecywać dokładny czas konkretnemu pacjentowi.

## 6. Ograniczenia

- (Rozwiązane) We wcześniejszych wersjach tej analizy brakujące wartości `staff_on_duty` były imputowane statystykami z całego zbioru danych, przed podziałem train/test — niewielka ilość informacji ze zbioru testowego technicznie przeciekała do tych wartości uzupełniających. Zostało to naprawione: wartość uzupełniająca (mediana) jest teraz liczona wyłącznie ze zbioru treningowego i stosowana do obu zbiorów.
- Model użył tylko jednego podziału train/test z jednym seedem losowym; inny podział mógłby dać nieco inne MAE, a ta analiza nie kwantyfikuje, o ile ta liczba mogłaby się przesunąć.

## 7. Rekomendacja

Użyć modelu, żeby dawać pacjentom spersonalizowane oszacowanie czasu oczekiwania przy rejestracji zamiast obecnej płaskiej średniej — to realna, zweryfikowana na zbiorze testowym poprawa (18,57 → 10,60 minuty MAE). Nie traktować 10,60 minuty jako dokładnej obietnicy dla konkretnego pacjenta; formułować to jako "zwykle w granicach ok. 10 minut od tego oszacowania".

---

## Dlaczego to dobra odpowiedź

Ta notatka zasługuje na "Wzorowy" w **Poprawności modelowania/oceny**, ponieważ sekcja 4 wprost sprawdza spójność train-vs-test jako podstawę zaufania, zamiast raportować MAE testowe tak, jakby pojedyncza liczba sama się uzasadniała — a także dlatego, że leżący u podstaw pipeline dopasowuje imputację wyłącznie na zbiorze treningowym, nigdy nie pozwalając informacji ze zbioru testowego wpływać na preprocessing. Zasługuje na "Wzorowy" w **Interpretacji i ograniczeniach**, nazywając realne, konkretne ograniczenie (jeden podział train/test z jednym seedem losowym) i jasno stwierdzając, że ta analiza nie kwantyfikuje, o ile mogłoby się przesunąć raportowane MAE przy innym podziale — to konkretne, sprawdzalne stwierdzenie, a nie ogólnikowe zastrzeżenie.

# Projekt końcowy — Wybierz swoje zlecenie

Każdy poprzedni case mówił Ci, kim jest klient, czego chce i mniej więcej co zbudować. Tym razem wybierasz sam/sama.

## Menu

Trzech potencjalnych klientów, każdy z lekkim briefem. Wybierz jednego — będziesz z nim pracować przez wszystkie sześć lekcji projektu końcowego.

### Riverside Community Clinic (`clinic_wait_times.csv`)

"Pacjenci ciągle mówią nam, że czekanie wydaje się nieskończone, ale tak naprawdę nie wiemy, co na to wpływa ani jak ustawiać oczekiwania."

### LendWell Financial (`lendwell_loan_default.csv`)

"Zatwierdzamy pożyczki bez systematycznego sposobu oceny ryzyka, i zaczyna nas to kosztować."

### Northfield Retail Group (`retail_store_segments.csv`)

"Nasze sklepy nie są takie same, ale w planowaniu regionalnym traktujemy je tak samo. Podejrzewamy, że istnieją tu naturalne grupy — po prostu nie wiemy, jakie."

Żaden z tych briefów nie mówi Ci, jaka jest zmienna celu, metryka sukcesu ani dokładne pytanie do odpowiedzi. To Twoje zadanie, zaczynając od Lekcji 1.

## Co jest inne w projekcie końcowym

- **Wybierasz zbiór danych.** Kod w każdej lekcji działa generycznie dla wszystkich trzech, więc niezależnie od wyboru, dostępne narzędzia będą działać.
- **Sam/sama definiujesz problem.** Lekcja 1 to moment, w którym zamieniasz niejasną skargę klienta w konkretne, mierzalne pytanie analityczne.
- **Self-checki są luźniejsze.** `check.py` w tych lekcjach sprawdza strukturę i rozsądność (czy Twoja funkcja zwraca odpowiedni kształt, czy model ma `.predict()`, czy metryka mieści się w sensownym zakresie) — nie konkretne liczby, bo nie ma tu jednej poprawnej odpowiedzi.

## Format danych

Zwykłe CSV, jeden plik na klienta, generowany przez `data/generate.py`.

## Ocenianie

Ta sama rubryka co w każdym case'ie w tym repozytorium (zobacz `do_poczytania.txt`): definicja problemu 15%, rozpoznanie/jakość danych 15%, eksploracja/uzasadnienie 20%, poprawność modelowania/oceny 20%, interpretacja/ograniczenia 15%, komunikacja 10%, czytelność/powtarzalność 5% — zastosowana do Twojej finalnej notatki decyzyjnej (Lekcja 6).

Lekcje znajdują się w `lessons/`, ponumerowane w kolejności, w jakiej należy przez nie przechodzić.

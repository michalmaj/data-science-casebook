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

Jest też opcjonalna, nieoceniana Lekcja 7 po sześciu podstawowych lekcjach, pokazująca, jak spakować preprocessing w `Pipeline`/`ColumnTransformer` pod kątem wdrożenia.

## Co jest inne w projekcie końcowym

- **Wybierasz zbiór danych.** Kod w każdej lekcji działa generycznie dla wszystkich trzech, więc niezależnie od wyboru, dostępne narzędzia będą działać.
- **Sam/sama definiujesz problem.** Lekcja 1 to moment, w którym zamieniasz niejasną skargę klienta w konkretne, mierzalne pytanie analityczne.
- **Self-checki sprawdzają poprawność Twojego kodu, nie Twoich wyborów analitycznych.** `check.py` w Lekcjach 1-3 sprawdza strukturę i rozsądność (czy czyszczenie usuwa każdą lukę, czy liczby korelacji są poprawnie policzone), ale nie potrafi ocenić, czy wybór zbioru danych albo pytania jest dobry. `check.py` w Lekcjach 4-6 idzie dalej i sprawdza też dokładne wartości — ale tylko dla sugerowanego zestawu cech, żeby potwierdzić, że Twoje generyczne funkcje działają poprawnie. Żaden z tych checkerów nie powie Ci, czy Twój model, cechy albo rekomendacja są właściwym wyborem dla Twojego własnego pytania z Lekcji 1.

## Format danych

Zwykłe CSV, jeden plik na klienta, generowany przez `data/generate.py`.

## Ocenianie

Ta sama rubryka co w każdym case'ie w tym repozytorium (zobacz [`ASSESSMENT_RUBRIC.pl.md`](../../ASSESSMENT_RUBRIC.pl.md)): definicja problemu 15%, rozpoznanie/jakość danych 15%, eksploracja/uzasadnienie 20%, poprawność modelowania/oceny 20%, interpretacja/ograniczenia 15%, komunikacja 10%, czytelność/powtarzalność 5% — zastosowana do Twojej finalnej notatki decyzyjnej (Lekcja 6). Zobacz [`lessons/06_synthesis_decision_note/exemplar_decision_note.pl.md`](lessons/06_synthesis_decision_note/exemplar_decision_note.pl.md) po wzorcową odpowiedź.

Lekcje znajdują się w `lessons/`, ponumerowane w kolejności, w jakiej należy przez nie przechodzić.

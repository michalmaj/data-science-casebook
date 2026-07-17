# Dziennik zmian

Wszystkie znaczące zmiany w tym projekcie są dokumentowane w tym pliku.

Format oparty jest na [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
a projekt stosuje się do [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-07-17

### Dodano

- **Szkielet kursu**: `uv` + `pyproject.toml`, `ruff`, `pytest`, GitHub Actions CI, konwencja dwujęzycznych plików Markdown (#1)
- **Case 1 — Regresja** (opóźnienia dostaw TransLine, 8 lekcji): Lekcja 1 Definiowanie pytania (#1), Lekcja 2 Jakość danych i czyszczenie (#2), Lekcja 3 Eksploracyjna analiza danych (#3), Lekcja 4 Biznesowe znaczenie błędu i baseline (#4), Lekcja 5 Podział trenujący/testowy i pierwszy model (#5), Lekcja 6 Interpretacja reszt (#6), Lekcja 7 Korelacja vs. predykcja vs. przyczynowość (#7), Lekcja 8 Synteza — notatka decyzyjna (#8)
- **Case 2 — Klasyfikacja** (zwroty w Meridian Outlet, 8 lekcji): Lekcja 1 Definiowanie pytania (#9), Lekcja 2 Porządkowanie danych — wieloarkuszowy Excel (#10), Lekcja 3 Eksploracyjna analiza danych dla klasyfikacji (#11), Lekcja 4 Niezbalansowane klasy i baseline (#12), Lekcja 5 Podział trenujący/testowy i pierwszy klasyfikator (#13), Lekcja 6 Wybór progu i miary (#14), Lekcja 7 Komunikowanie niepewności (#15), Lekcja 8 Synteza — notatka decyzyjna (#16)
- **Case 3 — Klasteryzacja** (segmentacja subskrybentów Aurora Stream, 8 lekcji): Lekcja 1 Definiowanie pytania (#17), Lekcja 2 Wybór i skalowanie cech (#18), Lekcja 3 Eksploracyjna analiza danych dla klasteryzacji (#19), Lekcja 4 Po co segmentować? Pierwsza próba KMeans (#20), Lekcja 5 Wybór k — porównanie rozwiązań (#21), Lekcja 6 Interpretacja i nazywanie segmentów (#22), Lekcja 7 Stabilność segmentów i ryzyko nadinterpretacji (#23), Lekcja 8 Synteza — notatka decyzyjna (#24)
- **Capstone** (zlecenie wybrane przez studenta, 6 lekcji): generator danych + Lekcja 1 Definiowanie pytania (#25), Lekcja 2 Przygotowanie danych (#26), Lekcja 3 Eksploracja (#27), Lekcja 4 Modelowanie (#28), Lekcja 5 Ewaluacja (#29), Lekcja 6 Synteza — notatka decyzyjna (#30)
- **`ASSESSMENT_RUBRIC.pl.md`**: rubryka oceniania z 7 kryteriami i 4 poziomami, do której odwołuje się notatka decyzyjna każdego case'u (#32)
- **Metodologia preprocessingu Capstone** — dostosowanie `impute_missing`/`split_dataset`/ewaluacji klasteryzacji do konwencji Case 3: `impute_missing` ograniczone do `feature_columns`, stratyfikowany split klasyfikacji, `cluster_stability` przeniesiony z Case 3, scaler zwracany z `scale_features` (#39)
- **Lekcja 7 Capstone (opcjonalna, nieoceniana)** — pakowanie preprocessingu jako `sklearn.pipeline.Pipeline`/`ColumnTransformer`, wprowadzająca kolumnę kategoryczną, którą każda ścieżka datasetu miała, ale nigdy nie użyła jako cechy (#42)
- **Kalibracja w Lekcji 7 Case 2** — `tier_summary`/`brier_score`, rozszerzenie istniejącej lekcji o poziomach ryzyka o sprawdzenie, czy przewidywane prawdopodobieństwa są faktycznie skalibrowane, nie tylko poprawnie uporządkowane (#43)
- **`tools/run_notebooks.py`** i nowy job CI `notebooks` — wykonuje każdy notebook lekcji przeciw wzorcowemu rozwiązaniu (wszystkie 3 gałęzie datasetów dla 4 wielościeżkowych notebooków Capstone), zamykając lukę, w której CI nigdy faktycznie nie uruchamiało notebooka (#45)
- **Lekcja 8 Capstone (opcjonalna, nieoceniana, tylko ścieżka LendWell)** — wyjaśnialność modelu per wnioskodawca i zbiorczo (`reason_codes`, `reason_code_frequency`), zamykająca się pytaniami refleksyjnymi o tym, czego wyjaśnialność nie może powiedzieć bez danych demograficznych (#46)
- **Efekty uczenia się i szacowany czas** dodane do wszystkich 32 README lekcji (#48)
- **`INSTRUCTOR_GUIDE.md`** — struktura i kolejność kursu, typowe błędy studentów wyciągnięte z własnej historii poprawek tego projektu, i towarzysz do czytania rubryki oceniania (#49)

### Naprawiono

- **Cztery błędy metodologiczne (P0) znalezione przez zewnętrzny audyt**, wszystkie dotyczące wycieku danych lub nieskalowanych cech trafiających do modelu przed/bez właściwej obróbki: próg klasyfikacji dobierany przez patrzenie na wyniki zbioru testowego zamiast splitu walidacyjnego (Case 2, #33); statystyka imputacji liczona z całego datasetu, zanim istniał podział train/test (Case 1, #34); ten sam wyciek plus `KMeans` dopasowany na nieprzeskalowanych cechach (Capstone, #35)
- **CI nigdy nie uruchamiało się przy pushu taga wersji**, rozwiązywało zależności bez przypięcia, i nie ograniczało liczby wątków BLAS/OpenMP (~34s → ~3,3s czasu testów po poprawce) (#36)
- **Profile klastrów raportowane w jednostkach przeskalowanych/z-score** zamiast rzeczywistych jednostek w notatkach decyzyjnych Case 3 i Capstone — cofnięcie wcześniejszej decyzji projektowej po tym, jak dwa niezależne audyty flagowały ten sam problem czytelności (#40)
- **Brief Case 1 nigdy nie ujawniał, że `weather` nie jest znana w momencie predykcji** aż do pięciu lekcji po tym, jak student po raz pierwszy widzi tę kolumnę jako pozornie użyteczną (#41)
- **Osiem miejsc w Case 1/2/3**, gdzie interpretacja w exemplarzu lub README wykraczała poza to, co faktycznie potwierdzała analiza — porównanie współczynników regresji między cechami o różnej skali bez zastrzeżenia o jednostkach, twierdzenie o "dolnej granicy", które było odwrotnością prawdy dla większości danych, próg operacyjny rekomendowany bez sprawdzenia precision/recall, mylenie stabilności klastrów z wrażliwością na inicjalizację K-means, i więcej (#44)
- **Dwie kolejne instancje tej samej kruchości** — testy `check.py` asercjonujące właściwość klastra względem konkretnego numeru etykiety KMeans, dla którego sklearn nie gwarantuje kolejności między wersjami — znalezione i naprawione po tym, jak pierwsze podejście z #47 je przeoczyło, zamykając tę klasę błędu w całym repo (#51)

### Zmieniono

- **Dokumentacja onboardingowa** (główny `README.md`, `CONTRIBUTING.md`) przepisana pod kątem nowego kontrybutora: instrukcje instalacji wyłącznie przez `uv`, poprawione twierdzenia o tym, jak ściśle `check.py` weryfikuje dokładne wartości, przeetykietowanie poziomu prowadzenia per case (#37)
- **Wszystkie 30 oryginalnych plików `lesson.ipynb`** zyskało komórkę `%load_ext autoreload`; trzy komórki "only" per dataset w Capstone skonsolidowane w jedną komórkę z dyspozycją po `DATASET_NAME`; zaszyty na sztywno próg w Lekcji 6 Case 2 stał się jawną zmienną `CHOSEN_THRESHOLD` (#38)
- **`tools/check_bilingual_pairs.py`** sprawdza teraz też strukturalną zgodność poziomów nagłówków EN/PL, nie tylko istnienie pliku siostrzanego (#47)
- **Dwie asercje `check.py` w Case 2** poprawione: nadużycie w sformułowaniu o tym, które sygnały z Lekcji 3 faktycznie trafiają do modelu, oraz exemplarz cytujący wyłącznie metryki progu ze zbioru testowego bez ujawnienia słabszych liczb ze zbioru walidacyjnego, które ten próg wybrały (#50)

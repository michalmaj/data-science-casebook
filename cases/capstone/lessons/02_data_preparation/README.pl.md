# Lekcja 2 — Przygotowanie danych

**Szacowany czas:** 45-55 min

## Decyzja do podjęcia

Cokolwiek brakowało w Lekcji 1, nie zaklejaj tego byle jak. Zdecyduj świadomie, co wypełnienie tych luk zakłada o danych, których nie masz, i uzasadnij ten wybór — zamiast stosować medianę/modę mechanicznie tylko dlatego, że zadziałała w poprzednim case'ie.

## Masz do dyspozycji

- Ten sam zbiór danych wybrany w Lekcji 1.
- `task.py` — pięć funkcji: `load_dataset` i `missing_value_counts` (odtworzone z Lekcji 1), `clean_dataset` (czyszczenie całego zbioru — właściwy wybór dla ścieżki klasteryzacji, która nie ma podziału train/test do ochrony), plus `split_dataset` i `impute_missing` dla dwóch pozostałych ścieżek.
- W notebooku: wczytaj zbiór i sprawdź braki przed czyszczeniem. Jeśli wybrano `clinic_wait_times` lub `lendwell_loan_default`: podziel na `train_df`/`test_df`, potem imputuj, używając tylko statystyk z `train_df`. Jeśli wybrano `retail_store_segments`: tutaj nie ma podziału do ochrony — uruchom `clean_dataset` na całym zbiorze.

## Zanim zdecydujesz

Jeśli zbiór ma target, który próbujesz przewidzieć, podział train/test musi nastąpić przed policzeniem jakiejkolwiek wartości wypełniającej braki — nie po. Dla zbioru bez targetu (klasteryzacja) ten problem w ogóle nie istnieje.

## Uzasadnij

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Te testy sprawdzają, czy `clean_dataset`, `split_dataset` i `impute_missing` robią to, co obiecują — nie mogą ocenić, czy wypełnianie medianą/modą, albo sam podział train/test, był *właściwą* decyzją dla konkretnego zbioru.

Dwa do trzech zdań: wybierz jedną kolumnę z brakującymi wartościami. Jaki realny powód mógł wyjaśniać ten brak — i czy wypełnianie medianą/modą dobrze czy źle radzi sobie z tym powodem? I: `clean_dataset`/`impute_missing` traktują każdą brakującą wartość w kolumnie tak samo, niezależnie od zbioru danych. Jakie jest ryzyko stosowania jednej generycznej strategii czyszczenia do bardzo różnych rodzajów danych — i jest kolumna, dla której warto by uzasadnić inne podejście?

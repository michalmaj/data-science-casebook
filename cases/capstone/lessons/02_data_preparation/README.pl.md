# Lekcja 2 — Przygotowanie danych

**Szacowany czas:** 45-55 min

## Efekty uczenia się

- Będziesz umieć uogólnić strategię czyszczenia, która działa niezależnie od tego, które kolumny w Twoim własnym datasetcie akurat mają braki.
- Będziesz umieć uzasadnić konkretną decyzję o imputacji jako odpowiednią dla Twoich danych, zamiast stosować ją mechanicznie tylko dlatego, że zadziałała w poprzednim case'ie.
- Będziesz umieć wyjaśnić, czemu dla zbioru z targetem, który próbujesz przewidzieć, podział train/test musi nastąpić przed policzeniem jakiejkolwiek wartości wypełniającej braki — nie po.

## Głos mentora

"Cokolwiek brakowało w Lekcji 1, nie zaklejaj tego byle jak. Zdecyduj świadomie, co wypełnienie tych luk zakłada o danych, których nie masz — i bądź gotowy/gotowa obronić ten wybór."

## Cel lekcji

Ocenić jakość danych i wyczyścić zbiór wybrany w Lekcji 1, używając strategii, która działa niezależnie od tego, które kolumny akurat mają luki.

## Pytanie analityczne dnia

Które kolumny w Twoim zbiorze mają brakujące wartości i czy wypełnienie ich medianą/modą jest tutaj faktycznie uzasadnionym wyborem?

## Co dostajesz

- Ten sam zbiór danych, który wybrałeś/wybrałaś w Lekcji 1
- `task.py` — pięć funkcji: `load_dataset` i `missing_value_counts` (odtworzone z Lekcji 1), `clean_dataset` (czyszczenie całego zbioru — właściwy wybór dla ścieżki klasteryzacji, która nie ma podziału train/test do ochrony), plus `split_dataset` i `impute_missing` dla dwóch pozostałych ścieżek. Jeśli Twój zbiór ma target, który próbujesz przewidzieć, Twój podział train/test następuje *tutaj* — przed policzeniem jakiejkolwiek statystyki (mediany, mody) z danych, które później trafią do Twojego zbioru testowego.
- `lesson.ipynb` — notebook, w którym sprawdzisz jakość i wyczyścisz dane

## Praca w notebooku

- Wczytaj swój zbiór danych i sprawdź braki przed czyszczeniem — to jest takie samo niezależnie od zbioru.
- Jeśli wybrałeś/wybrałaś `clinic_wait_times` lub `lendwell_loan_default`: najpierw podziel na `train_df`/`test_df`, potem imputuj, używając tylko statystyk z `train_df`. Potwierdź, że po tym nic nie brakuje w żadnej z ramek.
- Jeśli wybrałeś/wybrałaś `retail_store_segments`: tutaj nie ma podziału do ochrony — uruchom `clean_dataset` na całym zbiorze, tak jak wcześniej.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Te testy sprawdzają, czy `clean_dataset`, `split_dataset` i `impute_missing` robią to, co obiecują (luki faktycznie wypełnione, train/test faktycznie rozłączne, wartości wypełniające faktycznie policzone tylko z train) — nie mogą ocenić, czy wypełnianie medianą/modą, albo sam podział train/test, był *właściwą* decyzją dla Twojego konkretnego zbioru.

## Zadanie domowe

Dwa do trzech zdań: wybierz jedną kolumnę, która miała brakujące wartości w Twoim zbiorze. Jaki realny powód mógł wyjaśniać brak tej wartości — i czy wypełnianie medianą/modą dobrze czy źle radzi sobie z tym powodem?

## Refleksja

Mentor pyta: `clean_dataset`/`impute_missing` traktują każdą brakującą wartość w kolumnie tak samo (mediana albo moda), niezależnie od zbioru danych. Jakie jest ryzyko stosowania jednej generycznej strategii czyszczenia do bardzo różnych rodzajów danych — i czy jest kolumna w Twoim zbiorze, dla której uzasadniłbyś/uzasadniłabyś inne podejście?

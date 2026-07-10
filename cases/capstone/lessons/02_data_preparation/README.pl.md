# Lekcja 2 — Przygotowanie danych

## Głos mentora

"Cokolwiek brakowało w Lekcji 1, nie zaklejaj tego byle jak. Zdecyduj świadomie, co wypełnienie tych luk zakłada o danych, których nie masz — i bądź gotowy/gotowa obronić ten wybór."

## Cel lekcji

Ocenić jakość danych i wyczyścić zbiór wybrany w Lekcji 1, używając strategii, która działa niezależnie od tego, które kolumny akurat mają luki.

## Pytanie analityczne dnia

Które kolumny w Twoim zbiorze mają brakujące wartości i czy wypełnienie ich medianą/modą jest tutaj faktycznie uzasadnionym wyborem?

## Co dostajesz

- Ten sam zbiór danych, który wybrałeś/wybrałaś w Lekcji 1
- `task.py` — trzy funkcje: `load_dataset` i `missing_value_counts` (odtworzone z Lekcji 1) oraz jedna nowa funkcja, `clean_dataset`
- `lesson.ipynb` — notebook, w którym sprawdzisz jakość i wyczyścisz dane

## Praca w notebooku

- Wczytaj swój zbiór danych i sprawdź braki przed czyszczeniem.
- Uruchom `clean_dataset` i potwierdź, że po nim nic nie brakuje.
- Zanotuj, czy wypełnianie medianą/modą jest rozsądne dla Twoich konkretnych kolumn.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Te testy sprawdzają, czy `clean_dataset` faktycznie usuwa każdą lukę dla wszystkich trzech zbiorów z menu — nie mogą ocenić, czy wypełnianie medianą/modą było *właściwą* decyzją dla Twojego konkretnego zbioru.

## Zadanie domowe

Dwa do trzech zdań: wybierz jedną kolumnę, która miała brakujące wartości w Twoim zbiorze. Jaki realny powód mógł wyjaśniać brak tej wartości — i czy wypełnianie medianą/modą dobrze czy źle radzi sobie z tym powodem?

## Refleksja

Mentor pyta: `clean_dataset` traktuje każdą brakującą wartość tak samo, niezależnie od zbioru danych. Jakie jest ryzyko stosowania jednej generycznej strategii czyszczenia do bardzo różnych rodzajów danych?

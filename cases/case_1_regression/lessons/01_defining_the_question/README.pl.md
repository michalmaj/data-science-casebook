# Lekcja 1 — Definiowanie pytania

**Szacowany czas:** 25-35 min

## Po co to robimy

Kierownik operacyjny TransLine powiedział tylko: "przesyłki się opóźniają, załatwcie to". To nie jest jeszcze pytanie, na które da się odpowiedzieć danymi. Zanim dotkniesz modelu, trzeba zamienić tę skargę w coś konkretnego i sprawdzalnego — i rzucić pierwsze, krytyczne spojrzenie na dane, które dostałeś.

Jedna rzecz z tego samego spotkania: cokolwiek zbudujemy, musi działać w momencie, gdy przesyłka wyjeżdża z magazynu, nie na podstawie informacji poznanych później (np. pogoda, w jaką przesyłka trafiła). Miej to z tyłu głowy już teraz.

Pytanie na dziś: mając dane o przesyłkach TransLine, co dokładnie powinniśmy przewidywać — i czy dane są na tyle wiarygodne, żeby zacząć?

## Jak tu pracujemy

To pierwsza lekcja, więc kilka słów o tym, jak jest zbudowana każda — to się nie zmieni w kolejnych siedmiu.

- **Edytujesz tylko `task.py`.** Trzy funkcje, każda z docstringiem `TODO` opisującym, co ma robić: `load_shipments`, `target_column_name`, `missing_value_counts`. Nic innego w tej lekcji nie wymaga zmian.
- **Nie dotykasz `check.py`.** To zestaw testów `pytest`, który sprawdza Twoje funkcje. Z katalogu tej lekcji uruchom `uv run pytest` — `5 passed` oznacza, że wszystkie trzy funkcje działają zgodnie z opisem; każdy `FAILED` wskaże, która funkcja i dlaczego (czytaj komunikat błędu, zwykle mówi dokładnie, czego test oczekiwał).
- **`solution.py` to koło ratunkowe, nie pierwszy krok.** Zawiera referencyjną implementację. Zajrzyj do niego, gdy naprawdę się zablokujesz po własnej próbie — nie przed nią. Rozwiązanie zadania polega na dojściu do niego samodzielnie.
- **`lesson.ipynb` to miejsce, gdzie uruchamiasz swój kod i piszesz interpretację.** Otwórz notebook *po* tym, jak `task.py` przechodzi testy — tam zobaczysz dane, wygenerujesz pierwsze statystyki i zapiszesz wnioski w komórce "Your notes".
- **Lekcja jest skończona, gdy:** `uv run pytest` daje `5 passed`, a w `lesson.ipynb` masz wypełnioną komórkę z notatkami o tym, które kolumny wyglądają wiarygodnie i co warto by zapytać klienta. Potem przejdź do kolejnego katalogu lekcji w porządku numerycznym — `02_data_quality_and_cleaning/` — tak samo przy każdej następnej lekcji.

## Co masz zrobić

- `data/transport_delays.csv` — 500 przesyłek, wygenerowane przez `data/generate.py`.
- W `task.py` zaimplementuj `load_shipments`, `target_column_name`, `missing_value_counts`.
- W notebooku: zobacz `df.describe()`, potwierdź, która kolumna odpowiada na pytanie TransLine, zanotuj uzasadnienie wyboru, a potem sprawdź `missing_value_counts(df)` i zapisz, które kolumny mają braki i ile.

## Na co zwrócić uwagę

Dwie kolumny mają braki danych. To, co z nimi zrobić, zależy od tego, o którą kolumnę chodzi — nie ma jednej uniwersalnej reguły ("usuń wiersz" albo "uzupełnij średnią") ani dla wszystkich kolumn, ani dla wszystkich case'ów. Lekcja 2 zajmie się tym konkretnie; tutaj wystarczy zauważyć braki i zacząć się zastanawiać, co każdy z nich oznacza.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

W komórce "Your notes" odpowiedz krótko: gdyby trzeba było wrócić do kierownika operacyjnego z jednym pytaniem doprecyzowującym przed jakimkolwiek modelowaniem — jakie by to było pytanie? I: dla dwóch kolumn z brakami — usunąć te wiersze, uzupełnić je, czy najpierw zapytać klienta? Czy odpowiedź zależy od tego, o którą kolumnę chodzi?

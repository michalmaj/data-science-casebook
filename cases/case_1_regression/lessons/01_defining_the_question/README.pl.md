# Lekcja 1 — Definiowanie pytania

**Szacowany czas:** 25-35 min

## Efekty uczenia się

- Będziesz umieć zamienić niejasną skargę klienta w konkretne, testowalne pytanie analityczne.
- Będziesz umieć dostrzec ryzyko wycieku danych ukryte już w samym briefie, zanim napiszesz jakikolwiek kod.
- Będziesz umieć odczytać liczbę braków danych i zacząć rozumować, co brak w każdej kolumnie faktycznie oznacza.

## Głos mentora

"Witaj na pokładzie. Kierownik operacyjny TransLine właśnie powiedział mi — cytuję — 'przesyłki się opóźniają, załatwcie to'. To nie jest jeszcze pytanie, na które możemy odpowiedzieć danymi. Zanim dotkniesz jakiegokolwiek modelu, musisz zamienić tę skargę w coś wystarczająco konkretnego, żeby dało się to sprawdzić. Jeszcze jedno z tego spotkania: cokolwiek zbudujemy, musi działać w momencie, gdy przesyłka wyjeżdża z magazynu — nie na podstawie informacji, które poznajemy dopiero później, jak pogoda, w jaką przesyłka faktycznie trafiła w trasie. Miej to z tyłu głowy, poznając dane."

## Cel lekcji

Zamienić niejasną skargę TransLine w konkretne, mierzalne pytanie analityczne i rzucić pierwsze, krytyczne spojrzenie na dane, które dostałeś/dostałaś.

## Pytanie analityczne dnia

Mając dane o przesyłkach zebrane przez TransLine, co dokładnie powinniśmy przewidywać i czy możemy na tyle zaufać danym, żeby zacząć?

## Co dostajesz

- `data/transport_delays.csv` (500 przesyłek, wygenerowanych przez `data/generate.py` w katalogu case'u)
- `task.py` — trzy funkcje do zaimplementowania: `load_shipments`, `target_column_name`, `missing_value_counts`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

1. Otwórz `lesson.ipynb`.
2. Po uzupełnieniu `task.py` odpal notebook od góry do dołu.
3. Zobacz `df.describe()` — które kolumny mają sens jako predyktory, a które wyglądają podejrzanie?
4. Potwierdź, która kolumna faktycznie odpowiada na prawdziwe pytanie TransLine, i zapisz, czemu ją wybrałeś/wybrałaś.
5. Sprawdź `missing_value_counts(df)` — zanotuj, które kolumny mają braki i ile.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

W komórce "Your notes" w `lesson.ipynb` napisz dwa-trzy zdania: gdybyś musiał/musiała wrócić do kierownika operacyjnego TransLine z jednym pytaniem doprecyzowującym przed jakimkolwiek modelowaniem, jakie by to było pytanie i czemu?

## Refleksja

Mentor pyta: dwie kolumny mają braki danych. Usunąłbyś/usunęłabyś te wiersze, uzupełnił/uzupełniła je, czy najpierw zapytał/zapytała klienta — i czy odpowiedź zależy od tego, o którą kolumnę chodzi?

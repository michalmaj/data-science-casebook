# Lekcja 1 — Definiowanie pytania

**Szacowany czas:** 35-45 min

## Efekty uczenia się

- Będziesz umieć napisać SQL, który złączy i zagreguje znormalizowane tabele w jedną tabelę wiersz-na-podmiot, gotową do analizy.
- Będziesz umieć sformułować pytanie analityczne do klasteryzacji, gdzie nie ma kolumny celu, względem której sprawdziłbyś swoją pracę.

## Głos mentora

"Nowy case, nowy format — tym razem SQLite. Dwie tabele, żadnych sztuczek z bałaganem w Excelu, tylko prawdziwy SQL. Zobacz kształt danych, a potem zbuduj tabelę, na której naprawdę będziesz pracować."

## Cel lekcji

Rzucić pierwsze spojrzenie na dane subskrybentów Aurora Stream i napisać SQL, który zamienia dwie znormalizowane tabele w jedną tabelę per subskrybent, gotową do grupowania.

## Pytanie analityczne dnia

Jak dokładnie wygląda pojedynczy, kompletny wiersz zachowania subskrybenta, gdy surowe logi sesji Aurora Stream zostaną połączone i zagregowane?

## Co dostajesz

- `data/aurora_stream.sqlite` — dwie tabele, `subscribers` i `sessions`
- `task.py` — dwie funkcje do zaimplementowania: `list_tables`, `load_subscriber_features`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

- Wypisz tabele.
- Wczytaj połączoną tabelę cech per subskrybent.
- Zauważ, którzy subskrybenci mają zero sesji — zdecyduj, co to oznacza.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

Jedno zdanie: co poszłoby nie tak, gdybyś użył/użyła INNER JOIN zamiast LEFT JOIN?

## Refleksja

Mentor pyta: dwóch subskrybentów ma zero sesji. Czy są kandydatami do segmentu "widmo", czy powinni zostać całkowicie wykluczeni z analizy? Nie ma jednej słusznej odpowiedzi — po prostu bądź gotowy/gotowa jej bronić.

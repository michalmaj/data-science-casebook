# Lekcja 1 — Definiowanie pytania

**Szacowany czas:** 35-45 min

## Po co to robimy

Nowy case, nowy format — tym razem SQLite. Dwie tabele, żadnych sztuczek z bałaganem w Excelu, tylko prawdziwy SQL. Zobaczmy kształt danych, a potem zbudujmy tabelę, na której naprawdę będziemy pracować.

Pytanie na dziś: jak dokładnie wygląda pojedynczy, kompletny wiersz zachowania subskrybenta, gdy surowe logi sesji Aurora Stream zostaną połączone i zagregowane?

## Co masz zrobić

- `data/aurora_stream.sqlite` — dwie tabele, `subscribers` i `sessions`.
- W `task.py` zaimplementuj `list_tables`, `load_subscriber_features`.
- W notebooku: wypisz tabele, wczytaj połączoną tabelę cech per subskrybent. Zobacz, którzy subskrybenci mają zero sesji — zdecyduj, co to oznacza.

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Jedno zdanie: co poszłoby nie tak, gdyby zamiast LEFT JOIN użyć INNER JOIN? I: dwóch subskrybentów ma zero sesji. Są kandydatami do segmentu "widmo", czy powinni zostać całkowicie wykluczeni z analizy? Nie ma jednej słusznej odpowiedzi — po prostu zapisz uzasadnienie.

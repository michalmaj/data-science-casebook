# Lekcja 3 — Eksploracyjna analiza danych do grupowania

**Szacowany czas:** 35-45 min

## Po co to robimy

Tym razem żadnej kolumny celu — nic do przewidzenia, nic, z czym można by porównać korelacje. Zobaczmy, jak te cztery cechy odnoszą się do siebie nawzajem, zanim zdecydujemy, co właściwie będzie grupował KMeans.

Pytanie na dziś: czy te cztery cechy faktycznie niosą cztery różne sygnały, czy niektóre z nich opowiadają tę samą historię?

## Co masz zrobić

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-2.
- W `task.py` zaimplementuj `load_scaled_features`, `feature_correlations`.
- W notebooku: wczytaj ponownie przeskalowaną tabelę per subskrybent, policz macierz korelacji między czterema cechami. Przyjrzyj się konkretnie `tenure_days` — jak odnosi się do pozostałych trzech?

## Jedna z tych trzech to nie tylko korelacja

Zobacz, jak faktycznie liczony jest `avg_minutes_per_session` — to samo zapytanie SQL, które używa każda lekcja, wyciąga `AVG(minutes_watched)` obok `SUM(minutes_watched)` i `COUNT(...)` z tych samych wierszy. Dla każdego subskrybenta, który zalogował przynajmniej jedną sesję, to dokładny iloraz dwóch innych (`total_minutes_watched / session_count`), nie niezależnie zmierzony sygnał, który przypadkiem porusza się razem z nimi. Grupowanie na tych trzech plus `tenure_days` to nie grupowanie na czterech niezależnych wymiarach z silną relacją między trzema — to bliżej dwóch niezależnych wymiarów, gdzie wymiar zaangażowania widokowego jest liczony w odległości euklidesowej niemal trzy razy (potwierdza to szybkie PCA na czterech przeskalowanych cechach: jeden komponent wyjaśnia ok. 73% wariancji, a wszystkie trzy kolumny dotyczące oglądania mają na niego niemal identyczny wkład).

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Jedno zdanie: trzy cechy korelują ze sobą powyżej 0,9. Co to sugeruje co do liczby faktycznie różnych sygnałów, które masz? I: `session_count`, `total_minutes_watched` i `avg_minutes_per_session` korelują ze sobą powyżej 0,94, podczas gdy `tenure_days` prawie z nimi nie koreluje (wszystkie poniżej 0,1). Gdyby trzeba było opisać subskrybentów Aurora Stream za pomocą tylko dwóch liczb zamiast czterech, które dwie warto by wybrać, i dlaczego?

# Lekcja 3 — Eksploracyjna analiza danych do grupowania

**Szacowany czas:** 35-45 min

## Efekty uczenia się

- Będziesz umieć sprawdzić korelacje między cechami, gdy nie ma targetu, względem którego mógłbyś je zweryfikować.
- Będziesz umieć rozpoznać, kiedy kilka cech niesie w dużej mierze ten sam sygnał — w tym kiedy jedna jest dokładną funkcją wyliczoną z innych, nie tylko z nimi skorelowaną — i wyciągnąć z tego wnioski przed klasteryzacją na nich wszystkich.

## Głos mentora

"Tym razem żadnej kolumny celu — nic do przewidzenia, nic, z czym można by porównać korelacje. Po prostu spójrz, jak te cztery cechy odnoszą się do siebie nawzajem, zanim zdecydujesz, co właściwie będzie grupował KMeans."

## Cel lekcji

Poszukać struktury wśród czterech przeskalowanych cech Aurora Stream przed jakimkolwiek grupowaniem — zaczynając od tego, jak bardzo są ze sobą skorelowane.

## Pytanie analityczne dnia

Czy te cztery cechy faktycznie niosą cztery różne sygnały, czy niektóre z nich opowiadają tę samą historię?

## Co dostajesz

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-2
- `task.py` — dwie funkcje do zaimplementowania: `load_scaled_features`, `feature_correlations`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

- Wczytaj ponownie przeskalowaną tabelę per subskrybent.
- Policz macierz korelacji między czterema cechami.
- Przyjrzyj się konkretnie `tenure_days` — jak odnosi się do pozostałych trzech?

## Jedna z tych trzech to nie tylko korelacja

Zobacz, jak faktycznie liczony jest `avg_minutes_per_session` — to samo zapytanie SQL, które używa każda lekcja, wyciąga `AVG(minutes_watched)` obok `SUM(minutes_watched)` i `COUNT(...)` z tych samych wierszy. Dla każdego subskrybenta, który zalogował przynajmniej jedną sesję, to dokładny iloraz dwóch innych (`total_minutes_watched / session_count`), nie niezależnie zmierzony sygnał, który przypadkiem porusza się razem z nimi. Grupowanie na tych trzech plus `tenure_days` to nie grupowanie na czterech niezależnych wymiarach z silną relacją między trzema — to bliżej dwóch niezależnych wymiarów, gdzie wymiar zaangażowania widokowego jest liczony w odległości euklidesowej niemal trzy razy (potwierdza to szybkie PCA na czterech przeskalowanych cechach: jeden komponent wyjaśnia ok. 73% wariancji, a wszystkie trzy kolumny dotyczące oglądania mają na niego niemal identyczny wkład).

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

Jedno zdanie: trzy cechy korelują ze sobą powyżej 0.9. Co to sugeruje co do liczby faktycznie różnych sygnałów, które masz?

## Refleksja

Mentor pyta: `session_count`, `total_minutes_watched` i `avg_minutes_per_session` korelują ze sobą powyżej 0.94, podczas gdy `tenure_days` prawie z nimi nie koreluje (wszystkie poniżej 0.1). Gdybyś musiał/musiała opisać subskrybentów Aurora Stream za pomocą tylko dwóch liczb zamiast czterech, które dwie byś wybrał/wybrała, i dlaczego?

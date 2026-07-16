# Lekcja 3 — Eksploracja

**Szacowany czas:** 40-50 min

## Efekty uczenia się

- Będziesz umieć zbadać relacje między cechami numerycznymi w wybranym przez siebie datasetcie, bez wcześniejszej lekcji wskazującej istotne kolumny.
- Będziesz umieć wyrobić sobie wstępny, oparty na dowodach pogląd na to, które cechy Twojego datasetu prawdopodobnie mają znaczenie dla Twojego własnego pytania z Lekcji 1.

## Głos mentora

"Zanim cokolwiek dopasujesz, zobacz, co faktycznie jest w danych. Niektóre cechy okażą się bardzo ważne dla Twojego pytania, inne prawie wcale — i chcesz wiedzieć, które są które, zanim zbudujesz model wokół niewłaściwych."

## Cel lekcji

Zbadać, jak liczbowe cechy w Twoim wybranym zbiorze danych odnoszą się do siebie nawzajem, i zacząć wyrabiać sobie zdanie, które z nich prawdopodobnie mają znaczenie dla Twojego pytania z Lekcji 1.

## Pytanie analityczne dnia

Które liczbowe cechy Twojego zbioru danych wyglądają na najbardziej powiązane ze sobą — i z tym, co próbujesz przewidzieć lub zrozumieć?

## Co dostajesz

- Ten sam zbiór danych, który wybrałeś/wybrałaś w Lekcji 1
- `task.py` — dwie funkcje: `load_clean_dataset` (Lekcje 1-2 połączone) i jedna nowa funkcja, `numeric_correlations`
- `lesson.ipynb` — notebook, w którym przeprowadzisz eksplorację

## Praca w notebooku

- Wczytaj i wyczyść swój zbiór danych w jednym kroku.
- Policz macierz korelacji cech liczbowych.
- Posortuj zależności, żeby zobaczyć, które wyróżniają się na plus lub na minus.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Te testy sprawdzają same liczby korelacji — nie mogą powiedzieć Ci, które zależności faktycznie mają znaczenie dla Twojego konkretnego pytania.

## Zadanie domowe

Dwa do trzech zdań: na podstawie tego, co znalazłeś/znalazłaś, która cecha najbardziej Cię przekonuje, że pomoże odpowiedzieć na Twoje pytanie z Lekcji 1, a którą kusi Cię pominąć? Co mogłoby pójść nie tak przy takiej ocenie?

## Refleksja

Mentor pyta: silna korelacja między dwiema cechami nie mówi Ci, która z nich (jeśli w ogóle którakolwiek) jest tą faktycznie wartą zbudowania wokół niej analizy. Co musiałbyś/musiałabyś sprawdzić, zanim to zdecydujesz?

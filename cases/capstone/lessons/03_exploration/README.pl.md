# Lekcja 3 — Eksploracja

**Szacowany czas:** 45-55 min

## Efekty uczenia się

- Będziesz umieć zbadać relacje między cechami numerycznymi w wybranym przez siebie datasetcie, bez wcześniejszej lekcji wskazującej istotne kolumny.
- Będziesz umieć wyrobić sobie wstępny, oparty na dowodach pogląd na to, które cechy Twojego datasetu prawdopodobnie mają znaczenie dla Twojego własnego pytania z Lekcji 1.
- Będziesz umieć wyjaśnić, czemu dla zbioru z targetem, zbadanie związku cechy z targetem mówi Ci coś uczciwego tylko wtedy, gdy liczysz je wyłącznie na `train_df`.

## Głos mentora

"Zanim cokolwiek dopasujesz, zobacz, co faktycznie jest w danych. Niektóre cechy okażą się bardzo ważne dla Twojego pytania, inne prawie wcale — i chcesz wiedzieć, które są które, zanim zbudujesz model wokół niewłaściwych."

## Cel lekcji

Zbadać, jak liczbowe cechy w Twoim wybranym zbiorze danych odnoszą się do siebie nawzajem, i zacząć wyrabiać sobie zdanie, które z nich prawdopodobnie mają znaczenie dla Twojego pytania z Lekcji 1.

## Pytanie analityczne dnia

Które liczbowe cechy Twojego zbioru danych wyglądają na najbardziej powiązane ze sobą — i z tym, co próbujesz przewidzieć lub zrozumieć?

## Co dostajesz

- Ten sam zbiór danych, który wybrałeś/wybrałaś w Lekcji 1
- `task.py` — cztery funkcje: `load_dataset`, `split_dataset`, `impute_missing` (dla dwóch ścieżek predykcyjnych — badasz relacje tylko na `train_df`, ten sam podział i sposób wypełniania co w Lekcji 2), `load_clean_dataset` (Lekcje 1-2 połączone, dla ścieżki segmentacji, która nie ma podziału do ochrony) oraz `numeric_correlations`, używana przez obie ścieżki
- `lesson.ipynb` — notebook, w którym przeprowadzisz eksplorację

Jeśli Twoja ścieżka ma target, który próbujesz przewidzieć, eksploracja w tej lekcji — włącznie z korelacją cechy z targetem — patrzy wyłącznie na `train_df`. Zobaczenie, jak cecha wiąże się z targetem, używając wierszy, które później trafią do Twojego zbioru testowego, to właśnie ten typ podglądu, przez który oryginalny krok EDA w Case 1 wyciekał informację, zanim naprawił to PR #55 — ta lekcja nie powtarza tego błędu.

## Praca w notebooku

- Jeśli wybrałeś/wybrałaś `clinic_wait_times` lub `lendwell_loan_default`: najpierw podziel (ten sam sposób co w Lekcji 2), imputuj `train_df`/`test_df`, potem policz macierz korelacji tylko na `train_df`.
- Jeśli wybrałeś/wybrałaś `retail_store_segments`: wczytaj i wyczyść cały zbiór w jednym kroku, tak jak wcześniej — tutaj nie ma podziału do ochrony dla problemu segmentacji.
- Posortuj zależności, żeby zobaczyć, które wyróżniają się na plus lub na minus.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Te testy sprawdzają same liczby korelacji, oraz to, że dwie ścieżki predykcyjne liczą je wyłącznie na `train_df` — nie mogą powiedzieć Ci, które zależności faktycznie mają znaczenie dla Twojego konkretnego pytania.

## Zadanie domowe

Dwa do trzech zdań: na podstawie tego, co znalazłeś/znalazłaś, która cecha najbardziej Cię przekonuje, że pomoże odpowiedzieć na Twoje pytanie z Lekcji 1, a którą kusi Cię pominąć? Co mogłoby pójść nie tak przy takiej ocenie?

## Refleksja

Mentor pyta: silna korelacja między dwiema cechami nie mówi Ci, która z nich (jeśli w ogóle którakolwiek) jest tą faktycznie wartą zbudowania wokół niej analizy. Co musiałbyś/musiałabyś sprawdzić, zanim to zdecydujesz?

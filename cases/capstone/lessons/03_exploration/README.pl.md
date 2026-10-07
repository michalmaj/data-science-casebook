# Lekcja 3 — Eksploracja

**Szacowany czas:** 45-55 min

## Decyzja do podjęcia

Zanim cokolwiek dopasujesz, zobacz, co faktycznie jest w danych. Zbadaj relacje między cechami numerycznymi w wybranym zbiorze — bez wcześniejszej lekcji wskazującej istotne kolumny — i wyrób sobie wstępny, oparty na dowodach pogląd, które z nich prawdopodobnie mają znaczenie dla pytania z Lekcji 1.

## Masz do dyspozycji

- `task.py` — cztery funkcje: `load_dataset`, `split_dataset`, `impute_missing` (dla dwóch ścieżek predykcyjnych — relacje badane tylko na `train_df`, ten sam podział i sposób wypełniania co w Lekcji 2), `load_clean_dataset` (Lekcje 1-2 połączone, dla ścieżki segmentacji, która nie ma podziału do ochrony) oraz `numeric_correlations`, używana przez obie ścieżki.
- W notebooku: dla `clinic_wait_times` lub `lendwell_loan_default` — podziel (ten sam sposób co w Lekcji 2), imputuj, policz macierz korelacji tylko na `train_df`. Dla `retail_store_segments` — wczytaj i wyczyść cały zbiór w jednym kroku. Posortuj zależności, żeby zobaczyć, które wyróżniają się na plus lub na minus.

## Zanim zdecydujesz

Jeśli ścieżka ma target, eksploracja — włącznie z korelacją cechy z targetem — patrzy wyłącznie na `train_df`. Zobaczenie, jak cecha wiąże się z targetem, używając wierszy, które później trafią do zbioru testowego, to właśnie ten typ podglądu, przez który oryginalny krok EDA w Case 1 wyciekał informację, zanim naprawił to PR #55.

## Uzasadnij

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Te testy sprawdzają same liczby korelacji, oraz to, że dwie ścieżki predykcyjne liczą je wyłącznie na `train_df` — nie mogą powiedzieć, które zależności faktycznie mają znaczenie dla konkretnego pytania.

Dwa do trzech zdań: na podstawie znalezionych wyników, która cecha najbardziej przekonuje, że pomoże odpowiedzieć na pytanie z Lekcji 1, a którą kusi pominąć? Co mogłoby pójść nie tak przy takiej ocenie? I: silna korelacja między dwiema cechami nie mówi, która z nich (jeśli którakolwiek) jest tą faktycznie wartą zbudowania wokół niej analizy. Co warto by sprawdzić, zanim to zdecydujesz?

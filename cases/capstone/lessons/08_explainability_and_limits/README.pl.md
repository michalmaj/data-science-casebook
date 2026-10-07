# Lekcja 8 (Opcjonalna, tylko LendWell) — Wyjaśnialność i granice

**Szacowany czas:** 45-55 min

## Decyzja do podjęcia

Lekcja 7 spakowała ten model pod kątem wdrożenia. Ta pyta o to, czego faktycznie wymaga *odpowiedzialne* wdrożenie — na jedynej ścieżce, gdzie błędna odpowiedź ma przy sobie realny wynik dla konkretnej osoby. Lekcja dotyczy tylko sytuacji, gdy w Lekcji 1 wybrano LendWell — dwie pozostałe ścieżki nie mają takiej decyzji do wyjaśnienia.

## Masz do dyspozycji

- `lendwell_loan_default.csv` — tym razem bez wyboru zbioru danych, ta lekcja dotyczy wyłącznie LendWell.
- `task.py` — pięć funkcji odtworzonych z Lekcji 4 (`load_dataset`, `split_dataset`, `impute_missing`, `scale_features`, `fit_classification_baseline_and_model`), plus dwie nowe: `reason_codes` i `reason_code_frequency`.
- W notebooku: uruchom komórkę przygotowawczą (ta sama sekwencja co Lekcje 4-6, ale skalowanie teraz stosuje się też przed dopasowaniem klasyfikatora — zobacz notatkę w notebooku, dlaczego). Wywołaj `reason_codes` na realnym wnioskodawcy, któremu model by odmówił, i odczytaj trzy najważniejsze cechy stojące za tą decyzją. Wywołaj `reason_code_frequency` na całym zbiorze testowym — zobacz, która cecha pojawia się w niemal każdej odmowie.

## Uzasadnij

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Podobnie jak w Lekcjach 4-7, te sprawdzenia weryfikują dokładne wartości — potwierdzają, że kod `reason_codes`/`reason_code_frequency` działa poprawnie, nie że model bazowy czy zestaw cech są właściwym wyborem.

Brak zadania — lekcja opcjonalna i nieoceniana. Pięć pytań, bez kodu — napisz dwa-trzy zdania o tym, które najbardziej Cię interesuje, w komórce "Your notes":

1. Ten zbiór danych nie ma żadnych kolumn demograficznych. Czego byłoby trzeba — i kto musiałby to dać — żeby faktycznie sprawdzić, czy ten model odrzuca niektóre grupy wnioskodawców nieproporcjonalnie często?
2. `debt_to_income_ratio` pojawia się w top-3 powodów dla każdego bez wyjątku odrzuconego wniosku w zbiorze testowym. Czy to czyni tę cechę uczciwą podstawą decyzji kredytowej, czerwoną flagą, że może zastępować coś innego, czy jedno i drugie — i jak dałoby się to odróżnić?
3. Fałszywie pozytywne (odmowa kredytu komuś, kto by go spłacił) i fałszywie negatywne (akceptacja kredytu, który nie zostanie spłacony) nie kosztują LendWell — ani wnioskodawcy — tyle samo. Kto ponosi każdy z tych rodzajów błędu, i czy powinno to zmienić, gdzie ustawiony jest próg decyzyjny?
4. `reason_codes` daje technicznie poprawną odpowiedź. Czy lista nazw cech i podpisanych liczb to faktycznie coś, co odrzucony wnioskodawca mógłby zrozumieć jako "dlaczego"? Co warto by zmienić w tym wyniku, gdyby musiała go przeczytać prawdziwa osoba?
5. Czy każda predykcja tego modelu powinna iść prosto do decyzji, czy są wnioskodawcy — np. ci blisko granicy decyzyjnej modelu — gdzie przed finalną odpowiedzią powinien na nich spojrzeć człowiek?

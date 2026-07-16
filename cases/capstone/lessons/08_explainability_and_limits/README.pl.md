# Lekcja 8 (Opcjonalna, tylko LendWell) — Wyjaśnialność i granice

## Głos mentora

"Lekcja 7 spakowała ten model pod kątem wdrożenia. Ta pyta o to, czego
faktycznie wymaga *odpowiedzialne* wdrożenie — na jedynej ścieżce, gdzie
błędna odpowiedź ma przy sobie realny wynik dla konkretnej osoby. Ta lekcja
dotyczy tylko sytuacji, gdy wybrałeś/wybrałaś LendWell w Lekcji 1 — dwie
pozostałe ścieżki nie mają takiej decyzji do wyjaśnienia."

## Cel lekcji

Zaimplementować `reason_codes` i `reason_code_frequency`, a potem użyć ich
na zbiorze testowym, żeby zobaczyć, co faktycznie napędza odmowy tego
modelu — i gdzie to wyjaśnienie się kończy.

## Pytanie analityczne dnia

Gdy ten model odmawia wnioskodawcy, jaki podaje powód — i jak często ten
sam powód stoi za każdą pojedynczą odmową?

## Co dostajesz

- `lendwell_loan_default.csv` — tym razem bez wyboru datasetu, ta lekcja
  dotyczy wyłącznie LendWell
- `task.py` — pięć funkcji odtworzonych z Lekcji 4 (`load_dataset`,
  `split_dataset`, `impute_missing`, `scale_features`,
  `fit_classification_baseline_and_model`), plus dwie nowe:
  `reason_codes` i `reason_code_frequency`
- `lesson.ipynb` — notebook, w którym dopasujesz model i sprawdzisz jego
  powody

## Praca w notebooku

- Uruchom komórkę przygotowawczą — wczytuje, dzieli, imputuje, skaluje i
  dopasowuje, tę samą sekwencję co Lekcje 4-6, poza tym, że skalowanie
  teraz stosuje się też przed dopasowaniem klasyfikatora (zobacz notatkę w
  notebooku, dlaczego).
- Wywołaj `reason_codes` na realnym wnioskodawcy, któremu Twój model by
  odmówił, i odczytaj trzy najważniejsze cechy stojące za tą decyzją.
- Wywołaj `reason_code_frequency` na całym zbiorze testowym — zobacz, która
  cecha pojawia się w niemal każdej odmowie.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny. Podobnie
jak w Lekcjach 4-7, te sprawdzenia weryfikują dokładne wartości — potwierdzają,
że Twój kod `reason_codes`/`reason_code_frequency` działa poprawnie, nie że
model bazowy czy zestaw cech są właściwym wyborem.

## Zadanie domowe

Brak — ta lekcja jest opcjonalna i nieoceniana.

## Refleksja

Mentor pyta, pięć pytań, bez kodu — napisz dwa-trzy zdania o tym, które Cię
najbardziej interesuje, w komórce "Your notes":

1. Ten dataset nie ma żadnych kolumn demograficznych. Czego potrzebowałbyś/
   potrzebowałabyś — i kto musiałby Ci to dać — żeby faktycznie sprawdzić,
   czy ten model odrzuca niektóre grupy wnioskodawców nieproporcjonalnie
   często?
2. `debt_to_income_ratio` pojawia się w top-3 powodów dla każdego bez
   wyjątku odrzuconego wniosku w zbiorze testowym. Czy to czyni tę cechę
   uczciwą podstawą decyzji kredytowej, czerwoną flagą, że może zastępować
   coś innego, czy jedno i drugie — i jak byś to odróżnił/odróżniła?
3. Fałszywie pozytywne (odmowa kredytu komuś, kto by go spłacił) i
   fałszywie negatywne (akceptacja kredytu, który nie zostanie spłacony)
   nie kosztują LendWell — ani wnioskodawcy — tyle samo. Kto ponosi każdy
   z tych rodzajów błędu, i czy powinno to zmienić, gdzie ustawiasz próg
   decyzyjny?
4. `reason_codes` daje Ci technicznie poprawną odpowiedź. Czy lista nazw
   cech i podpisanych liczb to faktycznie coś, co odrzucony wnioskodawca
   mógłby zrozumieć jako "dlaczego"? Co zmieniłbyś/zmieniłabyś w tym
   wyniku, gdyby musiała go przeczytać prawdziwa osoba?
5. Czy chciałbyś/chciałabyś, żeby każda predykcja tego modelu szła prosto
   do decyzji, czy są wnioskodawcy — np. ci blisko granicy decyzyjnej
   modelu — gdzie zanim odpowiedź stanie się ostateczna, powinien na nich
   spojrzeć człowiek?

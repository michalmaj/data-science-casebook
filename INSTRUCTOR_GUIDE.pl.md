# Przewodnik dla instruktora

To materiał towarzyszący dla każdego, kto prowadzi ten kurs jako zajęcia, kohortę albo mentoring jeden na jeden — nie dla studentów przechodzących przez kurs samodzielnie (oni powinni zacząć od głównego [`README.md`](README.md)). Obejmuje to, jak cztery case'y się ze sobą łączą, błędy, które studenci faktycznie popełniają (wyciągnięte z historii tego kursu, nie hipotetyczne), i jak w praktyce czytać [`ASSESSMENT_RUBRIC.pl.md`](ASSESSMENT_RUBRIC.pl.md).

## 1. Struktura kursu i kolejność

Cztery case'y, każdy pełny cykl analityczny, z malejącym poziomem prowadzenia — ta tabela odpowiada tabeli z głównego README:

| Case | Prowadzenie | Lekcje | Szacowany czas |
|---|---|---:|---:|
| Case 1 — Regresja | Intensywnie prowadzony | 8 | 275-355 min (~4,5-6 godz.) |
| Case 2 — Klasyfikacja | Prowadzony | 8 | 290-370 min (~5-6 godz.) |
| Case 3 — Klasteryzacja | Prowadzony, mniejsze wsparcie interpretacyjne | 8 | 330-420 min (~5,5-7 godz.) |
| Projekt końcowy (wymagane) | Prowadzony projekt końcowy (ograniczony wybór) | 6 | 295-365 min (~5-6 godz.) |
| Projekt końcowy (opcjonalne) | Nieoceniane, Lekcja 7 wszystkie ścieżki / Lekcja 8 tylko LendWell | 2 | ~85-110 min (~1,5-2 godz.) |

**Suma dla 30 wymaganych lekcji: mniej więcej 1190-1510 minut (~20-25 godzin).** Dodając dwie opcjonalne lekcje projektu końcowego, to bliżej 1275-1620 minut (~21-27 godzin). To te same edytorskie szacunki z README każdej lekcji — nie zmierzone, tylko zsumowane.

**Rekomendowana kolejność: Case 1 → Case 2 → Case 3 → Projekt końcowy**, zgodnie z kolejnością wymienioną w głównym README. Każdy case usuwa jakieś wsparcie, na którym opierał się poprzedni:

- **Case 1 (regresja)** to najprostszy punkt wejścia — etykietowany target, prosty podział train/test, i pierwsze miejsce, gdzie studenci spotykają wyciek danych i porównanie z baseline. Warto tu ugruntować tę dyscyplinę, bo każdy kolejny case ją zakłada.
- **Case 2 (klasyfikacja)** zachowuje etykietowany target, ale dodaje dwie rzeczy, których nie potrzebował Case 1: niezbalansowaną klasę i próg decyzyjny, który trzeba świadomie dobrać (z własnym splitem walidacyjnym), zamiast zostawiać domyślne 0,5.
- **Case 3 (klasteryzacja)** całkowicie usuwa etykietowany target — nie ma względem czego sprawdzać predykcji, więc "czy to dobre?" trzeba odpowiedzieć innymi narzędziami (silhouette score, stabilność przy resamplingu) i dużo większym osądem interpretacyjnym. To też miejsce, gdzie studenci po raz pierwszy spotykają ryzyko nadinterpretacji wzorca, którego dane faktycznie nie potwierdzają.
- **Projekt końcowy** usuwa narzucony brief. Student wybiera dataset, target, technikę i pytanie — i musi połączyć wszystko z pierwszych trzech case'ów bez podpowiedzi, które narzędzie pasuje. To jedyny case, gdzie "czy dobrze wybrał/wybrała" samo w sobie jest częścią oceny.

Nie pomijaj case'u ani nie zmieniaj tej kolejności, oczekując tego samego efektu — specyficzny dla Case 3 osąd klasteryzacyjny i dyscyplina doboru progu z Case 2 to dokładnie te umiejętności, które Projekt końcowy zakłada jako już zbudowane.

## 2. Typowe błędy studentów, per case

To realne błędy — własny materiał referencyjny tego kursu miał każdy z nich w pewnym momencie, złapany albo przez zewnętrzny audyt, albo przez późniejsze self-review, i naprawiony w śledzonym PR-ze. Są tu wymienione, bo błąd wart naprawienia w materiale referencyjnym to dokładnie ten rodzaj błędu, który prawdopodobnie popełni też student.

### Wyciek danych przed podziałem train/test (Case 1, Projekt końcowy)

**Jak to wygląda:** Student liczy statystykę — medianę do imputacji brakujących wartości, w realnym wcześniejszym błędzie tego kursu — z *całego* datasetu, a dopiero potem dzieli na train/test. Oba splity kończą na dotknięte tą samą "wyciekłą" statystyką.

**Dlaczego to błąd:** Zbiór testowy ma symulować dane, których model nigdy nie widział. Jeśli statystyka preprocessingu została policzona z użyciem wierszy ze zbioru testowego, to zbiór testowy już wyciekł informację do treningu, nawet jeśli model nigdy nie zobaczył surowych wierszy testowych. Ewaluacja jest teraz optymistyczna w sposób, który nie powtórzy się produkcyjnie.

**Jak to wyglądało w tym kursie:** `load_clean_shipments` w Case 1 liczyło medianę `driver_experience_years` z całego datasetu, zanim jakikolwiek split w ogóle istniał (naprawione w PR #34). `load_clean_dataset` w Projekcie końcowym robiło to samo generycznie dla dowolnej kolumny z brakami (naprawione w PR #35, ten sam wzorzec błędu).

**Co by to złapało:** Kryterium 4 rubryki (Poprawność modelowania/oceny) — poziom "Rozwijający się" explicite wymienia "preprocessing dopasowany przed splitem". Przy ocenianiu ręcznym bez uruchamiania `check.py`: sprawdź, czy funkcje `impute_*`/`scale_*` przyjmują `train_df` i `test_df` jako osobne argumenty i liczą statystyki wyłącznie z `train_df`.

### Dopasowanie KMeans na nieprzeskalowanych cechach (Projekt końcowy)

**Jak to wygląda:** Student dopasowuje `KMeans` bezpośrednio na surowych kolumnach cech, bez wcześniejszej standaryzacji.

**Dlaczego to błąd:** KMeans mierzy odległość bezpośrednio na wartościach cech. Kolumna rzędu dziesiątek tysięcy (np. przychód) zdominuje obliczenie odległości nad kolumną będącą małym ułamkiem dziesiętnym (np. wskaźnik zwrotów), niezależnie od tego, która z nich faktycznie sensownie rozdziela dane — klasteryzacja kończy napędzana jednostkami, nie sygnałem.

**Jak to wyglądało w tym kursie:** `fit_clustering_model` w Projekcie końcowym dopasowywało się bezpośrednio na surowych cechach; wynikowe klastry były zdominowane przez tę surową kolumnę, która akurat miała największą skalę (naprawione w tym samym PR #35 co wyciek danych powyżej — oba błędy żyły w tym samym pliku).

**Co by to złapało:** Znów kryterium 4 rubryki (poziom "Niewystarczający": brak baseline'u, brak ewaluacji na wydzielonych danych, albo — przez analogię — metodologicznie niepoprawny fit). Ręcznie: sprawdź, czy `StandardScaler` (lub odpowiednik) jest zastosowany przed `KMeans.fit`, nie po.

### Dobór progu decyzyjnego przez patrzenie na wyniki zbioru testowego (Case 2)

**Jak to wygląda:** Student porównuje precision/recall klasyfikatora dla kilku kandydujących progów (0,5, 0,3, 0,2...) bezpośrednio na zbiorze testowym, a potem wybiera ten próg, który tam wygląda najlepiej.

**Dlaczego to błąd:** To wyciek przez decyzję, nie przez preprocessing — zbiór testowy ma być dotknięty dokładnie raz, do finalnej, już podjętej ewaluacji. Porównanie progów na nim i wybranie zwycięzcy sprawia, że wynik "testowy" już nie odzwierciedla, jak model radziłby sobie na faktycznie niewidzianych danych — próg został dopasowany do zbioru testowego tak samo pewnie, jak byłby dopasowany parametr modelu.

**Jak to wyglądało w tym kursie:** Lekcja 6 Case 2 pierwotnie porównywała progi 0,5/0,3/0,2 bezpośrednio na zbiorze testowym i wybierała 0,2 na tej podstawie (naprawione w PR #33) — naprawa wydziela split walidacyjny z danych treningowych specjalnie do porównań progów, dotykając zbioru testowego tylko raz, na końcu, z już wybranym progiem.

**Co by to złapało:** Kryterium 4 rubryki — poziom "Dobry" explicite dopuszcza tę lukę ("walidacja decyzji strojenia... może zostać pominięta"), ale "Wzorowy" wymaga "braku decyzji dopasowania czy strojenia podjętych na danych testowych". Ręcznie: zapytaj konkretnie, jak wybrano próg, i czy ta decyzja użyła tych samych danych co finalna raportowana metryka.

### Nadinterpretacja wniosków (Case 1, Case 2, Case 3)

Cztery powiązane wzorce, wszystkie realne, wszystkie złapane w tym samym audycie i naprawione w jednym PR-ze (#44):

- **Porównanie surowych współczynników regresji między cechami o różnej skali** bez zaznaczenia, że nie są na porównywalnych jednostkach (współczynnik 6,9 dla cechy w zakresie 0-10 nie jest w żadnym sensownym znaczeniu "większy" niż -2,3 dla cechy w zakresie 0-1000) — Case 1.
- **Twierdzenie, że model ma jednolite obciążenie predykcji** ("model niedoszacowuje opóźnień") bez sprawdzenia, czy to prawda w każdej podgrupie, czy tylko w niektórych — model Case 1 faktycznie PRZEszacowywał opóźnienie w czystej pogodzie (70% przesyłek), a niedoszacowywał w deszczu/śniegu; bezwarunkowe stwierdzenie było odwrotne dla większości przypadków.
- **Rekomendowanie progu operacyjnego** (np. "oznacz wszystko powyżej 20 minut") **bez sprawdzenia jego precision/recall** — próg może brzmieć rozsądnie i wciąż oznaczać głównie fałszywe alarmy.
- **Mylenie stabilności klastrów opartej na resamplingu z wrażliwością na inicjalizację K-means** — test stabilności, który zmienia tylko *próbkę* (trzymając `random_state` na stałe), nic nie mówi o tym, czy inna losowa inicjalizacja znalazłaby te same klastry. To różne pytania z różnymi odpowiedziami.

**Dlaczego warto na to uważać:** żadne z nich nie jest "błędnym kodem" — `check.py` nie złapie żadnego z nich, bo wszystkie liczby są policzone poprawnie. Problem leży całkowicie w tym, co te liczby rzekomo znaczą. To dokładnie terytorium kryterium 5 rubryki (Interpretacja i ograniczenia).

**Co by to złapało:** Kryterium 5 rubryki — poziom "Niewystarczający": "analiza przedstawiona jako bardziej pewna, niż wspierają to dowody". Ręcznie: dla każdego stwierdzenia w sekcji "Interpretacja" lub "Rekomendacja" zapytaj "co musiałoby być prawdą, a nie zostało faktycznie sprawdzone, żeby to stwierdzenie było fałszywe?"

## 3. Jak czytać rubrykę

[`ASSESSMENT_RUBRIC.pl.md`](ASSESSMENT_RUBRIC.pl.md) już definiuje wszystkich 7 kryteriów z jednozdaniową definicją Wzorowy/Dobry/Rozwijający się/Niewystarczający dla każdego — ta sekcja tego nie powtarza, dodaje praktyczny osąd, przed którym faktycznie stoi oceniający na granicy Wzorowy/Dobry, i wskazuje na przepracowany przykład.

1. **Definicja problemu/pytania (15%)** — praktyczny sygnał: Dobry podaje pytanie; Wzorowy dodatkowo mówi, co jest explicite poza zakresem. Jeśli praca nigdy nie mówi, na co *nie* odpowiada, to co najwyżej Dobry, choćby samo pytanie było bardzo ostre. Zobacz wzorcową notatkę Case 1, "1. Business question".
2. **Rozpoznanie/jakość danych (15%)** — praktyczny sygnał: czy praca wspomina o problemach, których *nie* znalazła, tak samo jak o tych, które znalazła? Wzorowy explicite wyklucza wyciek danych i niezbalansowanie nawet, gdy żadne z nich nie występuje w wybranym datasetcie, a nie tylko obsługuje problemy, które akurat istnieją. Zobacz wzorcową notatkę Case 2, "2. Approach" (niezbalansowanie jest sprawdzone i nazwane, zanim stanie się centralnym tematem case'u).
3. **Eksploracja i uzasadnienie decyzji (20%)** — praktyczny sygnał: czy da się prześledzić *każdą* decyzję modelową do konkretnej liczby lub wykresu z eksploracji, czy tylko większość? Jedna niewyjaśniona decyzja (dlaczego ten zestaw cech, dlaczego to k) obniża pracę z Wzorowej do Dobrej, nawet jeśli reszta jest szczelna. Zobacz wzorcową notatkę Case 3, "2. Approach" i "4. Choosing k and checking stability" razem — wybór k jest explicite prześledzony do konkretnego porównania silhouette, nie stwierdzony bez uzasadnienia.
4. **Poprawność modelowania/oceny (20%)** — praktyczny sygnał omówiony w Sekcji 2 powyżej: Dobry dopuszcza lukę w splicie walidacyjnym dla decyzji strojenia; Wzorowy nie. To kryterium najbardziej bezpośrednio sprawdzalne wynikiem `check.py`, ale `check.py` nie zweryfikuje *rozumowania* stojącego za wyborem progu czy splitu — tylko że kod działa poprawnie. Zobacz wzorcową notatkę Case 2, "4. Threshold and metric choice".
5. **Interpretacja i ograniczenia (15%)** — praktyczny sygnał: czy podane ograniczenia są specyficzne dla *tej* analizy, czy pasowałyby do dowolnej analizy dowolnego datasetu ("więcej danych by pomogło")? Generyczne ograniczenia czytają się jak ćwiczenie z odhaczania checkboxów, nie jak realna interpretacja. Zobacz wzorcową notatkę Case 1, "6. Limitations" — każde ograniczenie nazywa konkretną, sprawdzalną konsekwencję dla rekomendacji, nie mgliste zastrzeżenie.
6. **Komunikacja (10%)** — praktyczny sygnał: przeczytaj tylko sekcję "Rekomendacja" w oderwaniu od reszty. Czy interesariusz bez żadnego backgroundu data science mógłby na jej podstawie działać, nie czytając niczego więcej? Jeśli zrozumienie wymaga liczb z sekcji "Wyniki", to Dobry, nie Wzorowy. Zobacz sekcję "7. Recommendation" dowolnej wzorcowej notatki.
7. **Czytelność/powtarzalność (5%)** — kryterium o najniższej wadze, ale najszybsze do sprawdzenia: uruchom notebook od góry do dołu, zanim przeczytasz choć słowo analizy. Jeśli nie odpali się czysto, nic innego w pracy nie da się zweryfikować jako zadeklarowane — to kryterium jest bramką do zaufania reszcie oceny, nie tylko swoimi własnymi 5%.

Każda wzorcowa notatka decyzyjna kończy się sekcją "Why this is a strong answer", która explicite wiąże swoje wybory z konkretnymi kryteriami rubryki — przeczytaj najpierw tę sekcję, jeśli chcesz najszybszej orientacji, jak "Wzorowy" wygląda w głosie danego case'u, a potem sprawdzaj realną pracę kryterium po kryterium, zamiast próbować trzymać wszystkie 7 w głowie dosłownie.

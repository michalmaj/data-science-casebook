# Wzorcowa notatka decyzyjna — Case 1 (TransLine)

*To jest wzorcowa odpowiedź, napisana po ukończeniu całego Case'u 1. Nie czytaj jej przed napisaniem własnej — sensem tego ćwiczenia jest dojście do tych wniosków samodzielnie; ten plik istnieje, żebyś mógł/mogła porównać swoje rozumowanie z dobrą odpowiedzią później, nie żeby go skopiować.*

## 1. Pytanie biznesowe

Czy możemy przewidzieć, o ile minut opóźni się dostawa TransLine, na podstawie informacji dostępnych zanim kierowca wyjedzie — dystansu, liczby przystanków, doświadczenia kierowcy i wieku pojazdu — na tyle dokładnie, żeby pokonać proste założenie "średniego opóźnienia", tak żeby dyspozytornia mogła oznaczyć dostawy wysokiego ryzyka zanim się opóźnią?

## 2. Podejście

Użyłem/am oczyszczonych danych o dostawach TransLine (`distance_km`, `num_stops`, `driver_experience_years`, `vehicle_age_years` jako cechy, `delay_minutes` jako cel), podzieliłem/am 80/20 na train/test z ustalonym seedem. Porównałem/am dwa baseline'y — zawsze przewidujący 0 minut opóźnienia i zawsze przewidujący średnie opóźnienie ze zbioru treningowego — z regresją liniową dopasowaną na czterech cechach. Wszystkie trzy zostały ocenione na tym samym odłożonym zbiorze testowym.

## 3. Wyniki

| Predyktor | MAE (min) | RMSE (min) |
|---|---:|---:|
| Baseline zerowy | 16,80 | 20,50 |
| Baseline średniej | 12,08 | 15,19 |
| Model liniowy | 10,21 | 12,80 |

Model liniowy pokonuje baseline średniej o ok. 1,9 minuty MAE — realna poprawa, ale nie dramatyczna.

## 4. Czego model nie widzi

`weather` (pogoda) nie jest w zestawie cech, mimo że wcześniejsza eksploracja pokazała jej realny związek z opóźnieniem. Model został celowo zbudowany bez niej — w tym ćwiczeniu systemy dyspozytorskie mają dostęp tylko do czterech powyższych cech w momencie predykcji — co oznacza, że reszty modelu będą systematycznie większe w dni ze złą pogodą. To nie jest błąd modelu; to znana, nazwana luka między tym, co model widzi, a tym, co faktycznie napędza opóźnienie.

## 5. Co jest faktycznie do zastosowania

Średni błąd 10,21 minuty jest wystarczająco mały, żeby był użyteczny do triażu (oznacz dostawy przewidziane na >20 minut opóźnienia do uwagi dyspozytora), ale zbyt duży, żeby obiecywać klientom wąskie okno dostawy. Cechy, które najbardziej wpływają na predykcje modelu, to `distance_km` i `num_stops` — obie znane już zanim dostawa wyjedzie z magazynu, czyli dokładnie wtedy, kiedy TransLine potrzebuje tego oszacowania.

## 6. Ograniczenia

- Model nie ma dostępu do pogody, o której wiemy, że wpływa na opóźnienie — więc jego błędy będą gorsze konkretnie w dni złej pogody, nie tylko średnio większe.
- Model liniowy zakłada, że wpływ każdej cechy jest addytywny i stały; jeśli np. dodatkowe przystanki mają większe znaczenie na już długich trasach, ten model tego nie uchwyci.

## 7. Rekomendacja

Wdrożyć model liniowy jako flagę do triażu, nie jako obietnicę czasu dostawy dla klienta: każda dostawa przewidziana na ponad 20 minut opóźnienia trafia do uwagi dyspozytora zanim się opóźni. Nie używać go do podawania klientom okien czasowych dostawy, dopóki pogoda nie zostanie dodana jako cecha — do tego czasu traktować jego oszacowanie jako dolną granicę prawdopodobnego opóźnienia, nie jako sufit.

---

## Dlaczego to dobra odpowiedź

Ta notatka zasługuje na "Wzorowy" w kryterium **Poprawność modelowania/oceny**, ponieważ każda liczba w tabeli Wyników pochodzi z tego samego odłożonego zbioru testowego, a dwa baseline'y sprawiają, że faktyczny wkład modelu ("1,9 minuty lepiej niż samo zgadywanie średniej") jest czytelny, zamiast ukryty za jedną efektowną liczbą. Zasługuje na "Wzorowy" w **Interpretacji i ograniczeniach**, ponieważ sekcja 4 nie mówi tylko "model ma ograniczenia" — nazywa konkretnie pogodę, wyjaśnia *dlaczego* została wykluczona (dostępność cech w momencie predykcji, nie przeoczenie), i przewiduje *jak* ta luka objawi się w błędach (gorzej konkretnie w dni złej pogody). Sekcja 7 zasługuje na "Wzorowy" w **Komunikacji**, bo rekomendacja to konkretna granica zastosowania ("flaga do triażu, nie obietnica dla klienta"), a nie powtórzenie liczby MAE.

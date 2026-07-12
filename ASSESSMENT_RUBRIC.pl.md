# Rubryka oceny

Każdy case w tym kursie kończy się notatką decyzyjną — pisemnym argumentem za tym, co interesariusz powinien zrobić, opartym na Twojej analizie. `check.py` może zweryfikować, że Twój kod produkuje poprawne liczby; nie może zweryfikować, czy Twoja rekomendacja jest uczciwa, dobrze uargumentowana i faktycznie użyteczna. Do tego służy ta rubryka.

## Wagi

| Kryterium | Waga |
|---|---:|
| Definicja problemu/pytania | 15% |
| Rozpoznanie/jakość danych | 15% |
| Eksploracja i uzasadnienie decyzji | 20% |
| Poprawność modelowania/oceny | 20% |
| Interpretacja i ograniczenia | 15% |
| Komunikacja | 10% |
| Czytelność/powtarzalność | 5% |

## Kryteria szczegółowo

Każde kryterium jest oceniane na jednym z czterech poziomów: **Wzorowy**, **Dobry**, **Rozwijający się**, **Niewystarczający**.

### 1. Definicja problemu/pytania (15%)

- **Wzorowy:** Formułuje konkretne, mierzalne, falsyfikowalne pytanie analityczne bezpośrednio powiązane z realną decyzją interesariusza; jawnie oddziela to, co jest w zakresie, od tego, co nie jest.
- **Dobry:** Formułuje jasne pytanie analityczne powiązane z potrzebą interesariusza, choć granice zakresu są dorozumiane, a nie wprost wskazane.
- **Rozwijający się:** Pytanie jest obecne, ale niejasne — powtarza brief bez wyostrzenia go do czegoś mierzalnego.
- **Niewystarczający:** Brak jasnego pytania, albo pytanie nie przekłada się na żadną decyzję, którą interesariusz mógłby faktycznie podjąć.

### 2. Rozpoznanie/jakość danych (15%)

- **Wzorowy:** Identyfikuje każdy problem jakościowy (braki danych, ryzyko wycieku, niezbalansowanie klas, niezgodność skal) zanim dotknie modelu, i uzasadnia każdą decyzję dotyczącą jego obsługi.
- **Dobry:** Identyfikuje główne problemy jakościowe i obsługuje je w rozsądny sposób, z krótkim uzasadnieniem.
- **Rozwijający się:** Obsługuje problemy jakościowe mechanicznie ("uzupełnij braki") bez wyjaśnienia dlaczego, albo bez sprawdzenia wycieku danych.
- **Niewystarczający:** Problemy jakościowe są pominięte, zignorowane lub wprowadzone (np. użycie informacji dostępnej dopiero po zdarzeniu jako cechy).

### 3. Eksploracja i uzasadnienie decyzji (20%)

- **Wzorowy:** Każda decyzja modelowa (wybór cech, strategia podziału, preprocessing) jest wyraźnie powiązana z konkretnym wnioskiem z eksploracji.
- **Dobry:** Eksploracja jest obecna i w większości informuje decyzje, z kilkoma wyborami pozostawionymi bez wyjaśnienia.
- **Rozwijający się:** Eksploracja się odbywa, ale sprawia wrażenie oderwanej od decyzji, które po niej następują.
- **Niewystarczający:** Niewiele lub żadnej eksploracji; decyzje wydają się dowolne.

### 4. Poprawność modelowania/oceny (20%)

- **Wzorowy:** Poprawna dyscyplina train/validation/test przez całość (brak wycieku danych, żadna decyzja dopasowania ani strojenia nie jest podejmowana na podstawie danych testowych); baseline obecny; metryka dopasowana do pytania biznesowego.
- **Dobry:** Podział train/test jest poprawny, baseline obecny, ale walidacja do decyzji strojenia (np. progu klasyfikacji) bywa pomijana.
- **Rozwijający się:** Model jest dopasowany i oceniony, ale z luką metodologiczną (np. preprocessing dopasowany przed podziałem, próg strojony na podstawie wyników na zbiorze testowym).
- **Niewystarczający:** Brak baseline'u, brak oceny na danych odłożonych, albo wynik na zbiorze treningowym przedstawiony tak, jakby był generalizacją.

### 5. Interpretacja i ograniczenia (15%)

- **Wzorowy:** Odróżnia korelację od przyczynowości tam, gdzie to istotne; podaje co najmniej dwa konkretne, specyficzne dla tego case'a ograniczenia i ich praktyczną konsekwencję dla rekomendacji.
- **Dobry:** Podaje ograniczenia, choć część z nich jest ogólnikowa ("więcej danych by pomogło"), a nie specyficzna dla tej analizy.
- **Rozwijający się:** Interpretacja powtarza liczby, nie mówiąc, co one oznaczają dla decyzji, o którą chodzi.
- **Niewystarczający:** Brak podanych ograniczeń, albo analiza jest przedstawiona jako bardziej pewna, niż pozwalają na to dowody.

### 6. Komunikacja (10%)

- **Wzorowy:** Nietechniczny interesariusz mógłby przeczytać notatkę decyzyjną i działać na jej podstawie bez potrzeby zaglądania do kodu.
- **Dobry:** W większości prosty język, z kilkoma niewyjaśnionymi terminami technicznymi.
- **Rozwijający się:** Napisana dla czytelnika, który już zna metodę (np. "R² wyniosło 0,6") bez przełożenia na język biznesowy.
- **Niewystarczający:** Notatka decyzyjna jest opisem wykonanych kroków, nie rekomendacją.

### 7. Czytelność/powtarzalność (5%)

- **Wzorowy:** Notebook uruchamia się od góry do dołu bez żadnych ręcznych kroków; kod jest na tyle czytelny, że osoba oceniająca nie potrzebuje obecności studenta, żeby go zrozumieć.
- **Dobry:** Notebook uruchamia się z niewielką ręczną interwencją (np. trzeba najpierw ustawić zmienną).
- **Rozwijający się:** Notebook w większości się uruchamia, ale ma co najmniej jedną zepsutą komórkę albo zależność w złej kolejności.
- **Niewystarczający:** Notebook się nie uruchamia, albo kod jest na tyle nieczytelny, że nie da się zweryfikować poprawności.

## Checklista samooceny

Przejdź przez to, zanim uznasz notatkę decyzyjną za gotową:

- [ ] Moje pytanie analityczne jest na tyle konkretne, że ktoś mógłby je obalić.
- [ ] Sprawdziłem/am wyciek danych — żadna informacja ze zbioru testowego nie wpłynęła na preprocessing, wybór cech ani strojenie.
- [ ] Mam baseline, a mój model faktycznie go pokonuje na danych odłożonych, nie treningowych.
- [ ] Każda liczba w mojej sekcji "Wyniki" pochodzi z danych, których mój model nigdy nie widział podczas dopasowania ani strojenia.
- [ ] Podałem/am co najmniej dwa realne, specyficzne dla tego case'a ograniczenia — nie ogólnikowe.
- [ ] Mógłbym/mogłabym przekazać tę notatkę komuś, kto nigdy nie otworzył notebooka, i ta osoba wiedziałaby, co robić.
- [ ] Mój notebook uruchamia się od góry do dołu bez błędów, w kolejności, bez ręcznych kroków, o których zapomniałem/am napisać.
- [ ] Jeśli ktoś zapyta "jak bardzo jesteś pewien/pewna?", mam konkretną odpowiedź, nie tylko metrykę.

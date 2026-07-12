# Wzorcowa notatka decyzyjna — Case 2 (Meridian Outlet)

*To jest wzorcowa odpowiedź, napisana po ukończeniu całego Case'u 2. Nie czytaj jej przed napisaniem własnej — sensem tego ćwiczenia jest dojście do tych wniosków samodzielnie; ten plik istnieje, żebyś mógł/mogła porównać swoje rozumowanie z dobrą odpowiedzią później, nie żeby go skopiować.*

## 1. Pytanie biznesowe

Czy możemy zidentyfikować, przed wysyłką lub krótko po niej, które zamówienia w sklepie internetowym Meridian Outlet są narażone na zwrot — na tyle precyzyjnie, żeby oznaczenie zamówień wysokiego ryzyka do ręcznej weryfikacji wychwytywało znacząco więcej zwrotów niż losowa weryfikacja, bez zalewania zespołu operacyjnego fałszywymi alarmami?

## 2. Podejście

Wczytałem/am i połączyłem/am arkusze Orders i Customers Meridian (`discount_percent`, `previous_returns_count`, `account_age_days` jako cechy, `is_returned` jako cel), podzieliłem/am 80/20 ze stratyfikacją względem celu, żeby zachować ok. 14% stopę zwrotów w obu zbiorach, i dopasowałem/am regresję logistyczną na treningowym. Porównałem/am baseline większościowy (zawsze przewiduj "nie zwrócone") z modelem przy trzech progach — 0,5 (domyślny), 0,3 i 0,2 — porównanych na odłożonym zbiorze walidacyjnym, a następnie potwierdzonych raz na zbiorze testowym przy wybranym progu.

## 3. Wyniki

| Predyktor | Precision | Recall | F1 |
|---|---:|---:|---:|
| Baseline większościowy | 0,000 | 0,000 | 0,000 |
| Model @ próg 0,5 | 0,000 | 0,000 | 0,000 |
| Model @ próg 0,2 | 0,244 | 0,550 | 0,338 |

Przy domyślnym progu 0,5 model oznacza tylko 1 z 140 zamówień testowych — w praktyce nigdy nie przewiduje "zwrócone", funkcjonalnie identyczny z baseline'em większościowym. Obniżenie progu do 0,2 jest tym, co faktycznie czyni model użytecznym: wychwytuje 55% prawdziwych zwrotów, kosztem tego, że ok. 3 na 4 oznaczone zamówienia okazują się w porządku.

## 4. Wybór progu i metryki

Recall ma tu większe znaczenie niż precision: przeoczony zwrot kosztuje Meridian Outlet pełny cykl zwrotu pieniędzy, podczas gdy fałszywy alarm kosztuje tylko kilka minut sprawdzenia przez recenzenta zamówienia, które okazuje się w porządku. Dlatego wybrano 0,2 zamiast 0,5 czy 0,3 — to próg spośród testowanych, który znacząco podnosi recall bez zapadania się precision niemal do zera.

## 5. Komunikowanie ryzyka

"55% recall przy 24% precision" oznacza: spośród każdych 100 zamówień naprawdę zmierzających ku zwrotowi, ten system wychwytuje do weryfikacji ok. 55 z nich — a spośród każdych 4 oznaczonych zamówień, tylko 1 faktycznie wróci. To realny filtr, nie rzut monetą (baseline większościowy wychwytuje 0), ale nie jest to pewny wynik ryzyka dla pojedynczego zamówienia — traktuj oznaczenie jako "warte drugiego spojrzenia", nie "to zamówienie zostanie zwrócone".

## 6. Ograniczenia

- (Naprawione w Lekcji 6 poprzez wprowadzenie splitu walidacyjnego — zostawione tutaj jako przypomnienie, na co uważać.) Wcześniejsze wersje tej lekcji wybierały próg 0,2 przez bezpośrednie porównanie precision/recall na zbiorze testowym, co ponownie wykorzystywałoby go do decyzji strojenia. Lekcja 6 porównuje teraz progi na osobnym, odłożonym zbiorze walidacyjnym i dotyka zbioru testowego dokładnie raz, dla finalnej liczby raportowanej powyżej — więc to ograniczenie już nie dotyczy tej analizy, ale to dokładnie ten błąd, na który warto uważać we własnej pracy.
- Przy zaledwie 98 zwróconych zamówieniach w całym zbiorze (i 20 w zbiorze testowym), powyższe oszacowania precision/recall mają realny szum próbkowania — kilka zamówień idących w drugą stronę przesunęłoby te liczby nietrywialnie.

## 7. Rekomendacja

Wdrożyć model przy progu 0,2 jako flagę do ręcznej weryfikacji, nie jako system automatycznego odrzucania — oznaczać ~32% zamówień, które model wybiera, do weryfikacji przed lub krótko po wysyłce. Te liczby już odzwierciedlają wybór progu oparty na walidacji z Lekcji 6 oraz pojedyncze, prawdziwe sprawdzenie na zbiorze testowym, więc można ich bezpiecznie użyć do decyzji o zasobach (np. "potrzebujemy N recenzentów") bez dodatkowych zastrzeżeń.

---

## Dlaczego to dobra odpowiedź

Ta notatka zasługuje na "Wzorowy" w **Poprawności modelowania/oceny**, porównując progi na odłożonym zbiorze walidacyjnym i dotykając zbioru testowego dokładnie raz, dla finalnej liczby — dokładnie taką dyscyplinę opisuje poziom Wzorowy w rubryce, zamiast ponownie wykorzystywać zbiór testowy do decyzji strojenia. Zasługuje na "Wzorowy" w **Komunikacji** w sekcji 5, przekładając "55% recall, 24% precision" na konkretne stwierdzenie "1 na 4 oznaczone zamówienia jest prawdziwe", na podstawie którego nietechniczny interesariusz może działać.

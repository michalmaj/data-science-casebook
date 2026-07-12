# Wzorcowa notatka decyzyjna — Case 3 (Aurora Stream)

*To jest wzorcowa odpowiedź, napisana po ukończeniu całego Case'u 3. Nie czytaj jej przed napisaniem własnej — sensem tego ćwiczenia jest dojście do tych wniosków samodzielnie; ten plik istnieje, żebyś mógł/mogła porównać swoje rozumowanie z dobrą odpowiedzią później, nie żeby go skopiować.*

## 1. Pytanie biznesowe

Czy baza subskrybentów Aurora Stream faktycznie dzieli się na odrębne grupy behawioralne — poza poziomami planów, które już śledzimy — które uzasadniałyby różne oferty retencyjne, czy "jedna oferta dla wszystkich" to już właściwa decyzja?

## 2. Podejście

Wyciągnąłem/am cztery cechy zaangażowania/stażu na subskrybenta (`session_count`, `total_minutes_watched`, `avg_minutes_per_session`, `tenure_days`) przez SQL, ustandaryzowałem/am je `StandardScaler`, i dopasowałem/am KMeans dla kilku wartości k. Porównałem/am inertia i silhouette score dla różnych k, sprawdziłem/am stabilność przypisań do klastrów przy resamplingu, i zdecydowałem/am się na k=2.

## 3. Wyniki (finalna tabela segmentów, k=2)

| Segment | Rozmiar | Udział | Uwagi |
|---|---:|---:|---|
| 0 | 219 | 73% | Poniżej średniego zaangażowania we wszystkich trzech cechach oglądania |
| 1 | 81 | 27% | Powyżej średniego zaangażowania we wszystkich trzech cechach oglądania |

## 4. Wybór k i sprawdzenie stabilności

Inertia i silhouette score nie zgadzały się co do jednego "najlepszego" k, więc decydującym czynnikiem była stabilność: ponowne uruchomienie KMeans dla pięciu różnych zresamplowanych seedów dało k=2 idealnie spójne przypisanie segmentów (ARI = 1,0 za każdym razem), co jest silniejszym praktycznym argumentem niż którakolwiek z metryk osobno — segmentacja, która się przetasowuje przy innym seedzie losowym, nie jest taką, na której zespół retencyjny Aurora Stream może zbudować trwałą ofertę.

## 5. Interpretacja segmentów

Dwa segmenty rozdzielają się niemal wyłącznie na zaangażowaniu w oglądanie — liczba sesji, łączne minuty oglądania i średnia długość sesji są wyższe w Segmencie 1 — podczas gdy staż, poziom planu i kraj nie różnią się znacząco między grupami. Mówiąc wprost: to nie jest "długoletni subskrybenci vs. nowi" ani "premium vs. podstawowy plan" — to faktycznie kwestia tego, ile ludzie oglądają, niezależnie od tego, jak długo są klientami czy ile płacą.

## 6. Ograniczenia

- Te profile segmentów są raportowane w ustandaryzowanych jednostkach (z-score), które są poprawne do dopasowania KMeans, ale nie są bezpośrednio zrozumiałe dla nietechnicznego interesariusza — "liczba sesji to 1,46 odchylenia standardowego powyżej średniej" trzeba przełożyć z powrotem na realne liczby sesji, zanim trafi przed zespół retencyjny Aurora Stream.
- Segment 1 (81 subskrybentów, 27% bazy) jest znacząco mniejszy niż Segment 0 — każda oferta retencyjna skierowana do niego będzie testowana na mniejszej populacji, więc wczesne odczyty jej skuteczności powinny być traktowane ostrożnie, dopóki nie zbierze się więcej danych.

## 7. Rekomendacja

Zbudować dwie ścieżki retencyjne zamiast jednej: ścieżkę "ponownego zaangażowania" dla Segmentu 0 (73% większość, obecnie niedostatecznie zaangażowana) skupioną na podniesieniu użycia, i ścieżkę "nagradzania wysokiego zaangażowania" dla Segmentu 1 (27% mniejszość) skupioną na retencji przez docenienie, nie ponowne zaangażowanie, skoro już intensywnie korzystają z produktu. Przed uruchomieniem którejkolwiek, przełożyć powyższe profile segmentów z z-score'ów na rzeczywiste liczby sesji i minuty oglądania, żeby zespół retencyjny mógł zweryfikować segmenty względem subskrybentów, których już zna.

---

## Dlaczego to dobra odpowiedź

Ta notatka zasługuje na "Wzorowy" w **Poprawności modelowania/oceny** (sekcja 4), ponieważ wybór k jest uzasadniony stabilnością przy resamplingu, nie tylko tym, które k dało najlepszą pojedynczą metrykę — a liczba ARI=1,0 jest podana precyzyjnie, nie ogólnikowo. Zasługuje na "Wzorowy" w **Interpretacji i ograniczeniach**, nazywając wprost lukę między z-score'ami a realnymi jednostkami jako konkretne, praktyczne ograniczenie (sekcja 6), zamiast zostawiać interesariuszowi dekodowanie ustandaryzowanych jednostek samodzielnie, i będąc konkretnym co do tego, które cechy faktycznie rozdzielają segmenty (sekcja 5), zamiast opisywać klastry tylko ich rozmiarem.

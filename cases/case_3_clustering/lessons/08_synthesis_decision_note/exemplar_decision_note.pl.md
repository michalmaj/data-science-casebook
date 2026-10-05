# Wzorcowa notatka decyzyjna — Case 3 (Aurora Stream)

*To jest wzorcowa odpowiedź, napisana po ukończeniu całego Case'u 3. Nie czytaj jej przed napisaniem własnej — sensem tego ćwiczenia jest dojście do tych wniosków samodzielnie; ten plik istnieje, żebyś mógł/mogła porównać swoje rozumowanie z dobrą odpowiedzią później, nie żeby go skopiować.*

## 1. Pytanie biznesowe

Czy baza subskrybentów Aurora Stream faktycznie dzieli się na odrębne grupy behawioralne — poza poziomami planów, które już śledzimy — które uzasadniałyby różne oferty retencyjne, czy "jedna oferta dla wszystkich" to już właściwa decyzja?

## 2. Podejście

Wyciągnąłem/am cztery cechy zaangażowania/stażu na subskrybenta (`session_count`, `total_minutes_watched`, `avg_minutes_per_session`, `tenure_days`) przez SQL, ustandaryzowałem/am je za pomocą `StandardScaler`, i dopasowałem/am KMeans dla kilku wartości k. Porównałem/am inertia i silhouette score dla różnych k, sprawdziłem/am stabilność przypisań do klastrów przy resamplingu i przy losowej inicjalizacji KMeans, sprawdziłem/am, jak bardzo wynik zależy od użytych cech (odporny przy k=2, mniej przy drobniejszym k), i zdecydowałem/am się na k=2.

## 3. Wyniki (finalna tabela segmentów, k=2)

| Segment | Rozmiar | Udział | Uwagi |
|---|---:|---:|---|
| 0 | 219 | 73% | Poniżej średniego zaangażowania we wszystkich trzech cechach oglądania |
| 1 | 81 | 27% | Powyżej średniego zaangażowania we wszystkich trzech cechach oglądania |

## 4. Wybór k i sprawdzenie stabilności

Inertia i silhouette score nie zgadzały się co do jednego "najlepszego" k — inertia nie ma wyraźnego łokcia w całym zakresie k=2 do 8, a silhouette osiąga szczyt przy k=2, ale nie uszeregowuje czysto resztę zakresu. k=2 jest najmocniejszym kandydatem na podstawie całego zestawu dowodów razem: najlepszy silhouette score z testowanych, idealna stabilność przy resamplingu (ARI = 1,0 dla pięciu przetasowanych seedów, najlepsza z testowanych k), brak wrażliwości na losową inicjalizację KMeans dla żadnego testowanego k, segmentacja, która przetrwała zamianę dwóch z trzech redundantnych cech zaangażowania na jedną reprezentatywną, i historia o dwóch segmentach wystarczająco prosta, żeby zespół retencyjny mógł na niej faktycznie działać. Żadne z tego nie dowodzi, że dwa segmenty to liczba, która "naprawdę" istnieje w bazie subskrybentów Aurora Stream — oznacza, że k=2 jest prostą, stabilną i interpretowalną segmentacją *roboczą*, którą warto potraktować jako hipotezę operacyjną do sprawdzenia, a nie odkrytym faktem o populacji.

## 5. Interpretacja segmentów

Dwa segmenty rozdzielają się niemal wyłącznie na zaangażowaniu w oglądanie — liczba sesji, łączne minuty oglądania i średnia długość sesji są wyższe w Segmencie 1 — podczas gdy staż, poziom planu i kraj nie różnią się znacząco między grupami. Mówiąc wprost: to nie jest "długoletni subskrybenci vs. nowi" ani "premium vs. podstawowy plan" — to faktycznie kwestia tego, ile ludzie oglądają, niezależnie od tego, jak długo są klientami czy ile płacą.

## 6. Ograniczenia

- (Rozwiązane) We wcześniejszych wersjach tej analizy profile segmentów były raportowane w ustandaryzowanych jednostkach (z-score) — poprawne do dopasowania KMeans, ale niezrozumiałe bezpośrednio dla nietechnicznego interesariusza. Zostało to naprawione: tabele segmentów klastrują na ustandaryzowanych cechach wewnętrznie, ale raportują rzeczywiste liczby sesji, minuty oglądania i staż każdego segmentu w oryginalnych jednostkach.
- Segment 1 (81 subskrybentów, 27% bazy) jest znacząco mniejszy niż Segment 0 — każda oferta retencyjna skierowana do niego będzie testowana na mniejszej populacji, więc wczesne odczyty jej skuteczności powinny być traktowane ostrożnie, dopóki nie zbierze się więcej danych.
- Ta analiza sprawdziła stabilność przy resamplingu i przy losowej inicjalizacji KMeans, ale nie stabilność w czasie — dane to jedno 90-dniowe zdjęcie czasowe, więc nie ma sposobu, by na tej podstawie samej stwierdzić, czy te same dwa segmenty pojawiłyby się znowu w następnym kwartale.
- Podział k=2 jest odporny na odrzucenie dwóch z trzech silnie skorelowanych cech zaangażowania (liczby sesji i dokładnie wyliczonej średniej liczby minut na sesję) — ale ta odporność nie utrzymuje się przy drobniejszych k, gdzie wybór cech widocznie zmienia, który subskrybent trafia do którego klastra. Traktuj k=2 jako naprawdę stabilny gruby podział, nie jako dowód, że jakakolwiek drobniejsza segmentacja tej populacji byłaby równie godna zaufania.

## 7. Rekomendacja

Zaproponować dwie ścieżki retencyjne jako hipotezę do przetestowania, nie jako gotowy plan: ścieżkę "ponownego zaangażowania" dla Segmentu 0 (73% większość, obecnie niedostatecznie zaangażowana) skupioną na podniesieniu użycia, i ścieżkę "nagradzania wysokiego zaangażowania" dla Segmentu 1 (27% mniejszość) skupioną na retencji przez docenienie, nie ponowne zaangażowanie, skoro już intensywnie korzystają z produktu. Klasteryzacja pokazuje, że te dwie grupy różnią się zaangażowaniem — nie mówi nic o tym, czy którakolwiek ścieżka faktycznie zmniejszy odpływ klientów, ani którzy subskrybenci są warci tej inwestycji. Przed zaangażowaniem budżetu w obie, zespół retencyjny powinien zweryfikować profile segmentów względem subskrybentów, których już zna, i uruchomić obie ścieżki jako kontrolowany test wobec grupy kontrolnej, zamiast wdrażać je od razu wszędzie.

---

## Dlaczego to dobra odpowiedź

Ta notatka zasługuje na "Wzorowy" w **Poprawności modelowania/oceny** (sekcja 4), ponieważ wybór k jest uzasadniony całym zestawem dowodów — silhouette, stabilność przy resamplingu, stabilność przy inicjalizacji, odporność na wybór cech — a nie jedną metryką, i ponieważ wyraźnie powstrzymuje się od nazwania k=2 "prawdziwą" liczbą segmentów. Zasługuje na "Wzorowy" w **Interpretacji i ograniczeniach**, nazywając realne, konkretne ograniczenia (sekcja 6) — mniejszy rozmiar Segmentu 1, co nie zostało sprawdzone (stabilność w czasie), i gdzie odporność wyniku k=2 się kończy (wrażliwość na wybór cech przy drobniejszym k) — zamiast ogólnikowych zastrzeżeń, i będąc konkretnym co do tego, które cechy faktycznie rozdzielają segmenty (sekcja 5), zamiast opisywać klastry tylko ich rozmiarem.

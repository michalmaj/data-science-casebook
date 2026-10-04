# Lekcja 7 — Stabilność segmentów i ryzyko nadinterpretacji

**Szacowany czas:** 50-60 min

## Efekty uczenia się

- Będziesz umieć przetestować stabilność rozwiązania klasteryzacyjnego, ponownie dopasowując je na powtarzanych losowych podpróbach i porównując etykiety adjusted Rand index.
- Będziesz umieć rozróżnić cztery różne rzeczy, które ludzie nazywają "stabilnością": wrażliwość na próbkowanie, wrażliwość na losową inicjalizację KMeans, wrażliwość na wybór cech i stabilność w czasie — i jasno powiedzieć, o których z nich dane z tej lekcji faktycznie mogą, a o których nie mogą, nic powiedzieć.
- Będziesz umieć porównać kilka sensownych kandydatów na k — nie tylko dwóch — jednocześnie pod kątem stabilności, silhouette i wielkości segmentów, zamiast szukać jednej liczby, która to rozstrzygnie.
- Będziesz umieć zdecydować, mając takie porównanie w ręku, czy segment jest wystarczająco solidny, żeby budować wokół niego strategię retencji.

## Głos mentora

"Segment, którego nie da się odtworzyć, nie jest segmentem, tylko szumem. Zanim powiesz Aurora Stream, żeby zbudowali strategię retencji wokół tych klastrów, sprawdź, czy w ogóle przetrwają ponowne policzenie — na nieco innej próbce subskrybentów, z innym losowym startem, i dla więcej niż tylko dwóch wartości k, które sprawdziłeś/sprawdziłaś do tej pory."

## Cel lekcji

Sprawdzić, jak bardzo zmieniają się etykiety k=2 przy ponownym dopasowaniu na powtarzanych 80% losowych podpróbkach i przy różnych losowych inicjalizacjach KMeans, a potem rozszerzyć porównanie na k=2 do k=5, tak żeby decyzja opierała się na zestawie właściwości dla kilku kandydatów, nie tylko na k=2 kontra k=4.

## Pytanie analityczne dnia

Gdybyś widział/widziała tylko 80% tych subskrybentów, czy znalazłbyś/znalazłabyś te same segmenty?

## Co dostajesz

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-6
- `task.py` — cztery funkcje do zaimplementowania: `load_scaled_features`, `subsample_stability`, `initialization_stability`, `stability_comparison_table`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

- Wczytaj ponownie przeskalowaną tabelę per subskrybent.
- Uruchom `subsample_stability` przy domyślnym k=2 i spójrz na wyniki zgodności.
- Uruchom ją ponownie dla k=4 i porównaj.
- Uruchom `initialization_stability` dla k=2, a potem dla k=3, 4 i 5 — sprawdź, czy któryś z nich jest wrażliwy na losowy start KMeans tak, jak mogą być wrażliwe na próbkowanie.
- Uruchom `stability_comparison_table` dla k=2, 3, 4, 5 i spójrz na silhouette, stabilność przy próbkowaniu i udział najmniejszego klastra jednocześnie.

## Cztery różne pytania nazywane "stabilnością"

Łatwo powiedzieć, że segmentacja jest "stabilna", jakby to był jeden fakt. Nie jest — to cztery osobne pytania, i dane z tej lekcji potrafią odpowiedzieć tylko na niektóre z nich:

1. **Stabilność przy próbkowaniu** (`subsample_stability`, powyżej): gdybyś widział/widziała tylko 80% tych subskrybentów, czy KMeans znalazłby te same grupy? To właśnie zmienia się między seedami tutaj — którzy subskrybenci są w próbce — podczas gdy sam KMeans zawsze działa z tym samym `random_state`.
2. **Stabilność przy inicjalizacji** (`initialization_stability`, nowość w tej lekcji): na *tych samych* pełnych danych, czy losowy punkt startowy KMeans zmienia odpowiedź? To naprawdę inna oś — segmentacja mogłaby być wrażliwa na jedną, a odporna na drugą. Dla tego zbioru danych wynik jest czysty i warto go przyjąć w prostej formie: każde k od 2 do 5 jest całkowicie stabilne wobec inicjalizacji (ARI = 1,0, każdy seed). To nie jest ślepy zaułek — mówi Ci, że jakiekolwiek różnice widoczne w silhouette czy stabilności przy próbkowaniu nie pochodzą z tego, że KMeans trafia w różne lokalne optima; pochodzą z danych i próbki, nie z losowości algorytmu.
3. **Wrażliwość na wybór cech** (`compare_feature_sets` z Lekcji 5): trzecia, osobna oś — czy wynik się zmienia, gdybyś zakodował/zakodowała inne kolumny w metryce odległości? Lekcja 5 pokazała, że k=2 jest na to odporne, a k=4 nie do końca.
4. **Stabilność w czasie**, o której dane z tej lekcji naprawdę nic nie mogą powiedzieć: `aurora_stream.sqlite` to jedno 90-dniowe zdjęcie czasowe. Nic tutaj nie mówi, czy te same dwa segmenty pojawiłyby się znowu w następnym kwartale — do tego potrzebne byłyby powtarzane zdjęcia w czasie, których ten case nie ma. Nie pozwól, żeby "stabilne przy próbkowaniu" po cichu zmieniło się w czyjejś głowie — włącznie z Twoją — w "stabilne w czasie".

## Porównywanie kandydatów, nie koronowanie zwycięzcy

`stability_comparison_table` stawia k=2 do k=5 jedno przy drugim pod kątem silhouette, najgorszego przypadku stabilności przy próbkowaniu i udziału najmniejszego klastra w całej bazie — tak żeby decyzja opierała się na zestawie właściwości, nie na tym, która pojedyncza liczba wygląda najlepiej:

| k | silhouette | stabilność przy próbkowaniu (min ARI) | udział najmniejszego klastra |
|---|---:|---:|---:|
| 2 | 0,605 | 1,000 | 27,0% |
| 3 | 0,472 | 0,986 | 27,0% |
| 4 | 0,444 | 0,971 | 12,7% |
| 5 | 0,464 | 0,987 | 12,7% |

k=2 prowadzi w silhouette i jest najbardziej stabilne przy próbkowaniu z tych czterech — a wszystkie są równie stabilne wobec inicjalizacji. Ta kombinacja, plus prostota historii o dwóch grupach, jest powodem, czemu k=2 jest roboczym wyborem tego case'u — nie dlatego, że jakiś pojedynczy wiersz czy kolumna to "ogłosiły". Jedno szczere zastrzeżenie: konkretne liczby stabilności przy próbkowaniu dla k=3/4/5 są trochę specyficzne dla tego, jak `subsample_stability` dokładnie losuje 80% podpróbkę — inna, równie uzasadniona metoda próbkowania mogłaby je trochę przesunąć. Idealna stabilność k=2 jest odporna niezależnie od tego; dokładny ranking między k=3/4/5 nie jest czymś, w co warto wczytywać się za dużo.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

Jedno zdanie: zgodność podpróbek dla k=2 jest idealna dla każdego seeda; dla k=4 jest wysoka, ale nie idealna, a oba są całkowicie stabilne wobec inicjalizacji. Co *różnica między tymi dwoma rodzajami stabilności* mówi Ci o tym, skąd właściwie bierze się dodatkowa kruchość k=4?

## Refleksja

Mentor pyta: idealna stabilność przy k=2 — zarówno przy próbkowaniu, jak i przy inicjalizacji — nie oznacza, że historia o dwóch segmentach jest tą "prawdziwą". Oznacza, że jest najbardziej odtwarzalnym kandydatem, jakiego przetestowałeś/przetestowałaś, na danych, które masz, pod sprawdzonymi zaburzeniami. Co jeszcze warto by sprawdzić, zanim uznasz "wysokie zaangażowanie kontra niskie zaangażowanie" za trwały fakt o subskrybentach Aurora Stream, a nie za zdjęcie jednego 90-dniowego okna czasowego?

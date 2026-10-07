# Lekcja 7 — Stabilność segmentów i ryzyko nadinterpretacji

**Szacowany czas:** 50-60 min

## Po co to robimy

Segment, którego nie da się odtworzyć, nie jest segmentem, tylko szumem. Zanim powiemy Aurora Stream, żeby zbudowali strategię retencji wokół tych klastrów, sprawdźmy, czy w ogóle przetrwają ponowne policzenie — na nieco innej próbce subskrybentów, z innym losowym startem, i dla więcej niż tylko dwóch wartości k sprawdzonych do tej pory.

Pytanie na dziś: widząc tylko 80% tych subskrybentów, czy dałoby się znaleźć te same segmenty?

## Co masz zrobić

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-6.
- W `task.py` zaimplementuj cztery funkcje: `load_scaled_features`, `subsample_stability`, `initialization_stability`, `stability_comparison_table`.
- W notebooku: wczytaj ponownie przeskalowaną tabelę per subskrybent. Uruchom `subsample_stability` przy domyślnym k=2 i spójrz na wyniki zgodności, potem ponownie dla k=4. Uruchom `initialization_stability` dla k=2, 3, 4 i 5 — sprawdź, czy któryś z nich jest wrażliwy na losowy start KMeans tak, jak mogą być wrażliwe na próbkowanie. Uruchom `stability_comparison_table` dla k=2, 3, 4, 5 i spójrz na silhouette, stabilność przy próbkowaniu i udział najmniejszego klastra jednocześnie.

## Cztery różne pytania nazywane "stabilnością"

Łatwo powiedzieć, że segmentacja jest "stabilna", jakby to był jeden fakt. Nie jest — to cztery osobne pytania, i dane z tej lekcji potrafią odpowiedzieć tylko na niektóre z nich:

1. **Stabilność przy próbkowaniu** (`subsample_stability`, powyżej): widząc tylko 80% tych subskrybentów, czy KMeans znalazłby te same grupy? To właśnie zmienia się między seedami tutaj — którzy subskrybenci są w próbce — podczas gdy sam KMeans zawsze działa z tym samym `random_state`.
2. **Stabilność przy inicjalizacji** (`initialization_stability`, nowość w tej lekcji): na *tych samych* pełnych danych, czy losowy punkt startowy KMeans zmienia odpowiedź? To naprawdę inna oś — segmentacja mogłaby być wrażliwa na jedną, a odporna na drugą. Dla tego zbioru danych wynik jest czysty i warto go przyjąć w prostej formie: każde k od 2 do 5 jest całkowicie stabilne wobec inicjalizacji (ARI = 1,0, każdy seed). To nie jest ślepy zaułek — mówi, że jakiekolwiek różnice widoczne w silhouette czy stabilności przy próbkowaniu nie pochodzą z tego, że KMeans trafia w różne lokalne optima; pochodzą z danych i próbki, nie z losowości algorytmu.
3. **Wrażliwość na wybór cech** (`compare_feature_sets` z Lekcji 5): trzecia, osobna oś — czy wynik się zmienia, gdyby w metryce odległości zakodowano inne kolumny? Lekcja 5 pokazała, że k=2 jest na to odporne, a k=4 nie do końca.
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

## Sprawdź się

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Jedno zdanie: zgodność podpróbek dla k=2 jest idealna dla każdego seeda; dla k=4 jest wysoka, ale nie idealna, a oba są całkowicie stabilne wobec inicjalizacji. Co *różnica między tymi dwoma rodzajami stabilności* mówi o tym, skąd właściwie bierze się dodatkowa kruchość k=4? I: idealna stabilność przy k=2 — zarówno przy próbkowaniu, jak i przy inicjalizacji — nie oznacza, że historia o dwóch segmentach jest tą "prawdziwą". Oznacza, że jest najbardziej odtwarzalnym kandydatem z przetestowanych, na danych, które są dostępne, pod sprawdzonymi zaburzeniami. Co jeszcze warto by sprawdzić, zanim "wysokie zaangażowanie kontra niskie zaangażowanie" uznane zostanie za trwały fakt o subskrybentach Aurora Stream, a nie za zdjęcie jednego 90-dniowego okna czasowego?

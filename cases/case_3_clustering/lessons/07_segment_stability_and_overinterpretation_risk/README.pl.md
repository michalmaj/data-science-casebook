# Lekcja 7 — Stabilność segmentów i ryzyko nadinterpretacji

## Głos mentora

"Segment, którego nie da się odtworzyć, nie jest segmentem, tylko szumem. Zanim powiesz Aurora Stream, żeby zbudowali strategię retencji wokół tych klastrów, sprawdź, czy w ogóle przetrwają ponowne policzenie na nieco innej próbce subskrybentów."

## Cel lekcji

Sprawdzić, jak bardzo zmieniają się etykiety rozwiązania k=2 przy ponownym dopasowaniu na powtarzanych 80% losowych podpróbkach, i porównać tę stabilność z k=4.

## Pytanie analityczne dnia

Gdybyś widział/widziała tylko 80% tych subskrybentów, czy znalazłbyś/znalazłabyś te same segmenty?

## Co dostajesz

- Ten sam plik `data/aurora_stream.sqlite` co w Lekcjach 1-6
- `task.py` — dwie funkcje do zaimplementowania: `load_scaled_features`, `subsample_stability`
- `lesson.ipynb` — notebook, w którym wykonasz właściwą pracę

## Praca w notebooku

- Wczytaj ponownie przeskalowaną tabelę per subskrybent.
- Uruchom `subsample_stability` przy domyślnym k=2 i spójrz na wyniki zgodności.
- Uruchom ją ponownie dla k=4 i porównaj.

## Self-check

Z katalogu tej lekcji odpal:

```bash
uv run pytest
```

Wszystkie testy powinny przejść, gdy `task.py` będzie kompletny.

## Zadanie domowe

Jedno zdanie: zgodność podpróbek dla k=2 jest idealna dla każdego seeda; dla k=4 jest wysoka, ale nie idealna. Co ta różnica mówi Ci o tym, ile zaufania dać drobniejszej segmentacji w porównaniu z bardziej ogólną?

## Refleksja

Mentor pyta: idealna stabilność przy k=2 nie oznacza, że historia o dwóch segmentach jest tą "prawdziwą" — oznacza tylko, że jest najbardziej odtwarzalna z tych, które przetestowałeś/przetestowałaś. Co jeszcze warto by sprawdzić, zanim uznasz "wysokie zaangażowanie kontra niskie zaangażowanie" za trwały fakt o subskrybentach Aurora Stream, a nie za zdjęcie jednego 90-dniowego okna czasowego?

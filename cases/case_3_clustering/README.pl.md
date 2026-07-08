# Case 3 — Grupowanie: Aurora Stream

**Klient:** Aurora Stream, serwis streamingowy oparty na subskrypcji.

**Zlecenie:** "Chcemy zrozumieć, jakich właściwie mamy subskrybentów, żeby dopasować oferty retencyjne zamiast traktować wszystkich tak samo."

**Format danych:** Baza SQLite (`data/aurora_stream.sqlite` — tabela `subscribers` i tabela `sessions`), generowana przez `data/generate.py`. Wyciągnięcie tabeli gotowej do analizy wymaga napisania SQL-a (JOIN i agregacji) — to główna nowa umiejętność techniczna tego case'u.

**Co zbudujesz w tym case'ie:** segmentację subskrybentów Aurora Stream na podstawie ich zachowania oglądania, przy użyciu `KMeans`, a także notatkę decyzyjną wyjaśniającą, jak wygląda każdy segment, jak stabilne są te segmenty, i co Aurora Stream powinno z tym zrobić.

Lekcje tego case'u znajdują się w `lessons/`, ponumerowane w kolejności, w jakiej należy przez nie przechodzić.

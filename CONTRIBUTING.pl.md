# Współtworzenie

Dzięki za rozważenie wkładu w `data-science-casebook`. Ten dokument opisuje konwencje, które nie są oczywiste po przeczytaniu pojedynczej lekcji. Jeśli prowadzisz ten kurs zamiast go współtworzyć, zobacz zamiast tego [`INSTRUCTOR_GUIDE.pl.md`](INSTRUCTOR_GUIDE.pl.md).

## Lokalny rozwój

Zainstaluj [uv](https://docs.astral.sh/uv/), a następnie:

```bash
uv sync --locked --all-groups
```

Przed pushem odtwórz to, co uruchamia CI (`.github/workflows/ci.yml`), w tej kolejności:

```bash
uv run --locked ruff check .
LESSON_MODULE=solution uv run --locked pytest
uv run --locked python tools/check_bilingual_pairs.py
```

`LESSON_MODULE=solution` mówi każdemu `check.py`, żeby testował `solution.py` (referencyjną odpowiedź) zamiast `task.py` (szkielet dla studenta, który ma nie przechodzić z `NotImplementedError`, dopóki nie zostanie uzupełniony) — tak CI weryfikuje, że referencyjne rozwiązania pozostają poprawne; to nie jest sposób, w jaki student sprawdza własną pracę.

## Dodawanie lekcji

Każda lekcja znajduje się w `cases/<case>/lessons/<NN_nazwa_lekcji>/` i potrzebuje dokładnie pięciu plików:

- `task.py` — szkielet dla studenta. Każde ciało funkcji to `raise NotImplementedError(...)`, z docstringiem wyjaśniającym co i dlaczego zaimplementować.
- `solution.py` — referencyjna implementacja. Te same sygnatury funkcji co `task.py`, prawdziwe ciała.
- `check.py` — self-check. Zobacz wzorzec ładowania modułu poniżej.
- `lesson.ipynb` — notebook, w którym student faktycznie pracuje, z wyczyszczonymi outputami komórek (zobacz "Higiena notebooków" poniżej).
- `README.md` i `README.pl.md` — brief lekcji, w obu językach.

Każdy `lesson.ipynb` zaczyna się od komórki `%load_ext autoreload` / `%autoreload 2` (zaraz po komórce markdown z wprowadzeniem) — to dzięki temu edycje `task.py` pojawiają się w działającym notebooku bez restartu kernela.

Każdy `README.md`/`README.pl.md` zaczyna się od linii `**Estimated time:** X-Y min` (`**Szacowany czas:**` po polsku) i sekcji `## Learning outcomes` (`## Efekty uczenia się`, 2-4 punkty, "Będziesz umieć...") zaraz po tytule, przed pierwszą sekcją lekcji (zazwyczaj "Mentor's note"). Zakres czasu to edytorska ocena, nie zmierzony fakt — oprzyj go na poziomie prowadzenia case'u i realnym obciążeniu implementacyjnym `task.py` tej lekcji, a każdy punkt efektów uczenia się uzasadnij tym, czego faktycznie uczą funkcje i pytanie analityczne tej konkretnej lekcji, nie generycznym wypełniaczem.

**Zasada samodzielności (self-containment)**: jeśli lekcja potrzebuje funkcji, którą zdefiniowała już wcześniejsza lekcja w tym samym case'ie (np. `load_dataset`, `split_dataset`), odtwórz ją bajt-w-bajt w `task.py`/`solution.py` nowej lekcji — nigdy nie importuj jej z modułu innej lekcji. Lekcje muszą dać się uruchomić i ocenić w izolacji; student przechodzący od razu do Lekcji 5 nie powinien potrzebować plików z Lekcji 3. Oznacza to, że pewne powtórzenia między lekcjami case'a są oczekiwane i celowe, nie błędem do posprzątania.

**Wzorzec ładowania modułu w `check.py`**: każdy `check.py` w tym repo używa tego samego boilerplate'u, żeby wczytać `task.py` albo `solution.py` w czasie działania:

```python
import importlib.util
import os
from pathlib import Path

_MODULE_NAME = os.environ.get("LESSON_MODULE", "task")
_LESSON_DIR = Path(__file__).parent
_MODULE_PATH = _LESSON_DIR / f"{_MODULE_NAME}.py"
_UNIQUE_NAME = f"lesson_{_LESSON_DIR.parent.parent.name}_{_LESSON_DIR.name}_{_MODULE_NAME}"

_spec = importlib.util.spec_from_file_location(_UNIQUE_NAME, _MODULE_PATH)
lesson = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(lesson)
```

Konstrukcja `_UNIQUE_NAME` ma znaczenie: wiele lekcji w wielu case'ach ma plik dosłownie nazwany `task.py`. Bez unikalnej nazwy modułu per katalog lekcji, cache `sys.modules` Pythona kolidowałby między nimi, gdy pytest zbiera całe repo w jednym uruchomieniu.

## Kontrakt dwujęzyczny

Każdy śledzony przez git plik `*.md` potrzebuje polskiego odpowiednika (`tools/check_bilingual_pairs.py` egzekwuje to w CI — bierze pod uwagę tylko pliki, które śledziłby git, więc nie dotyczy to plików gitignored). Angielski jest źródłem prawdy; kiedy edytujesz angielski plik Markdown, zaktualizuj jego polski odpowiednik w tym samym commicie. Jedynym wyjątkiem jest `do_poczytania.txt` (prywatne, gitignored notatki planistyczne, niewidoczne dla studentów).

Checker weryfikuje też strukturalną zgodność EN/PL: każda para musi mieć tę samą sekwencję poziomów nagłówków Markdown (`#`, `##`, `###`...). Porównuje wyłącznie strukturę, nie treść — więc dłuższe albo krótsze tłumaczenie nigdy nie zawiedzie sprawdzenia — ale dodanie, usunięcie albo przestawienie sekcji w jednym języku bez odzwierciedlenia tego w drugim już tak.

Kod, docstringi, komentarze i komunikaty commitów są wyłącznie po angielsku — również wewnątrz notebooków. Komórki markdown w `lesson.ipynb` są wyłącznie po angielsku, nawet w lekcjach, których `README.pl.md` jest po polsku; tylko brief jest dwujęzyczny, nie przestrzeń robocza.

## Regenerowanie danych case'a

Zbiór danych każdego case'a jest generowany przez `cases/<case>/data/generate.py`, z ustalonym seedem losowym — ponowne uruchomienie odtwarza dokładnie ten sam plik bajt-w-bajt (CSV/SQLite) albo semantycznie (Excel). Jeśli zmieniasz logikę generowania danych case'a (nowa kolumna, inny wzorzec braków, inna liczba wierszy), uruchom ponownie `generate.py`, a potem sprawdź każdy `check.py` w tym case'ie pod kątem wartości referencyjnych, które zakładały stare dane — zmiana schematu danych bardzo prawdopodobnie przesunie zahardkodowane liczby dalej w lekcjach.

## Higiena notebooków

Commituj pliki `lesson.ipynb` z wyczyszczonymi outputami i bez execution counts — świeży notebook, nie taki, który akurat uruchomiłeś/aś ostatnio. Jeśli iterowałeś/aś w Jupyterze, wyczyść wszystkie outputy ("Restart Kernel and Clear All Outputs" w Jupyterze, albo `jupyter nbconvert --clear-output --inplace lesson.ipynb`) przed commitem.

## Aktualizowanie wartości referencyjnych w `check.py`

`check.py` w tym repo celowo sprawdza dokładne wartości liczbowe w większości lekcji (nie tylko "kod działa bez błędu") — ta precyzja sprawia, że self-check lekcji jest wiarygodny. Jeśli uzasadniona zmiana w `solution.py` przesuwa policzoną liczbę (poprawka błędu, regeneracja danych, nowa cecha dodana do współdzielonej funkcji), nie zgaduj nowej wartości ani nie kopiuj jej z jednego, wyglądającego na zaufany, uruchomienia: napisz mały, jednorazowy skrypt, który niezależnie ją przelicza, potwierdź liczbę dwukrotnie, i dopiero wtedy zahardkoduj ją w asercji. Błędna zahardkodowana liczba, która akurat zgadza się z wadliwą implementacją, jest cichą luką w poprawności, dużo trudniejszą do zauważenia później niż test, który po prostu nie przechodzi.

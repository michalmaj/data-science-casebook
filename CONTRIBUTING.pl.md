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

Każdy `README.md`/`README.pl.md` zaczyna się od linii `**Estimated time:** X-Y min` (`**Szacowany czas:**` po polsku) i sekcji `## Learning outcomes` (`## Efekty uczenia się`, 2-4 punkty, "Będziesz umieć...") zaraz po tytule, przed pierwszą sekcją lekcji (zazwyczaj "Mentor's note"). Zakres czasu to edytorska ocena, nie zmierzony fakt — oprzyj go na poziomie prowadzenia case'u i realnym obciążeniu implementacyjnym `task.py` tej lekcji, a każdy punkt efektów uczenia się uzasadnij tym, czego uczą funkcje i pytanie analityczne tej konkretnej lekcji, nie generycznym wypełniaczem.

**Wyjątek pilotażowy:** lekcje Case 1-3 używają innej, prostszej struktury sekcji (`Po co to robimy` / `Co masz zrobić` / `Na co zwrócić uwagę` / `Sprawdź się`, zmiennej zależnie od lekcji, bez osobnych nagłówków "Efekty uczenia się" czy "Głos mentora") jako pilotażu UX — zobacz ich lekcje po wzorzec. Capstone używa własnego wariantu tego samego pomysłu (`Decyzja do podjęcia` / `Masz do dyspozycji` / `Zanim zdecydujesz` / `Uzasadnij`), żeby jego mniej prowadzący za rękę ton był faktycznie odczuwalny, nie tylko zadeklarowany — zobacz jego lekcje po ten konkretny wzorzec. To jest teraz kontrakt dla wszystkich czterech case'ów; szablon "Efekty uczenia się"/"Głos mentora" powyżej jest zachowany tu jako zapis wcześniejszej konwencji, nie coś do stosowania w nowych lekcjach.

**Zasady stylu polskiej prozy dla pilotażu** (stosuj przy pisaniu lub redagowaniu `README.pl.md` w tej strukturze): nie nadużywaj strony bezosobowej ("wykorzystano", "podzielono", "porównano") — brzmi jak sprawozdanie urzędowe, nie jak prowadzący na laboratorium; preferuj tryb rozkazujący ("Porównaj…", "Sprawdź…"), 1. osobę liczby mnogiej czasu teraźniejszego ("Sprawdzamy…", "Korzystamy…") albo neutralny czas teraźniejszy ("Model dostaje…"), zależnie od tego, czego faktycznie wymaga zdanie. Nigdy nie wracaj do domyślnej formy męskiej (odcinając "/zrobiłaś" z "zrobiłeś/zrobiłaś") tylko żeby ominąć problem formy dualnej — najpierw przebuduj zdanie: pytanie w bezokoliczniku ("Usunąć czy uzupełnić?"), czas teraźniejszy ("Widzisz już…"), bezosobowy modalny ("warto", "trzeba"), albo imiesłów zgadzający się z rzeczownikiem, nie z rodzajem studenta ("znaleziony sygnał"). W praktyce naturalne przeformułowanie da się znaleźć niemal zawsze; strona bezosobowa z pierwszego przejścia przez Case 1 wciąż jest poprawna dla formalnej sekcji "Podejście" w notatce decyzyjnej (ten rejestr faktycznie jej wymaga), ale nie dla prozy instruktażowej lekcji.

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

Kod, docstringi, komentarze i komunikaty commitów są wyłącznie po angielsku — również wewnątrz notebooków. Komórki markdown w `lesson.ipynb` są wyłącznie po angielsku, nawet w lekcjach, których `README.pl.md` jest po polsku; tylko brief jest dwujęzyczny, nie przestrzeń robocza. **Wyjątek pilotażowy:** każdy notebook lekcji w Case 1-3 i Capstone pilotuje dwujęzyczne *nagłówki sekcji* (`## First look / Pierwszy rzut oka`) — tylko krótkie nagłówki nawigacyjne dostają polski dopisek inline; jednoliniowe instrukcje, dłuższe akapity objaśniające i cały kod zostają wyłącznie po angielsku, i nie powstaje drugi plik notebooka. Główna narracja wciąż mieszka w `README.pl.md`, nie w notebooku. Nagłówki w Capstone są bardziej zadaniowe niż tutorialowe tam, gdzie to pasuje do treści (np. `## Decide what matters` zamiast `## Explore the data`) — zgodnie z decyzyjnym tonem jego lekcji, nie jako reguła do wymuszania wszędzie.

## Terminologia polska

Kilka terminów ustaliło się do jednej konsekwentnej formy we wszystkich czterech case'ach po finalnym przeglądzie słownika — nowa treść lekcji powinna z nimi być zgodna, nie wprowadzać wariantów:

- **baseline** → `model bazowy` (nigdy goły anglicyzm `baseline'u`/`baseline'em`)
- **feature** → `cecha`
- **target** → `zmienna celu` (we wcześniejszych case'ach spotykane też jako `kolumna celu`/`cel`; dla nowej treści preferowana jest `zmienna celu`)
- **decision threshold** → `próg decyzyjny` (nie `próg klasyfikacji`)
- **confusion matrix** → `macierz pomyłek`
- **precision / recall** → zostają po angielsku, konsekwentnie, nie tłumaczone na `precyzja`/`czułość` — to zgodne z dokładnymi nazwami metryk scikit-learn, które studenci widzą w kodzie i wyniku, oraz z konwencją polskiego pisarstwa o ML, które zwyczajowo zostawia te dwa terminy po angielsku nawet w polskiej prozie
- **accuracy** → gołe "accuracy" jest w porządku; jednorazowa glosa przy pierwszym wprowadzeniu (`dokładność (accuracy)`) również jest w porządku, bo w przeciwieństwie do precision/recall ten termin ma naprawdę naturalny polski odpowiednik w codziennym użyciu
- **silhouette** → zostaje po angielsku, nigdy nie tłumaczone
- **inertia** → glosowane raz przy pierwszym użyciu (`bezwładność (inertia)`), dalej po angielsku
- **cluster vs. segment** → `klaster` dla surowego wyniku algorytmu, `segment` gdy już zinterpretowany/nazwany jako biznesowa grupa — zachowaj to rozróżnienie
- **held-out** → `odłożony` (`zbiór odłożony`, `dane odłożone`)

Historyczne wpisy w `CHANGELOG.md`/`.pl.md` nie są przepisywane retroaktywnie, kiedy terminologia się zmienia — opisują to, co było prawdą w momencie, w którym zostały napisane.

## Regenerowanie danych case'a

Zbiór danych każdego case'a jest generowany przez `cases/<case>/data/generate.py`, z ustalonym seedem losowym — ponowne uruchomienie odtwarza dokładnie ten sam plik bajt-w-bajt (CSV/SQLite) albo semantycznie (Excel). Jeśli zmieniasz logikę generowania danych case'a (nowa kolumna, inny wzorzec braków, inna liczba wierszy), uruchom ponownie `generate.py`, a potem sprawdź każdy `check.py` w tym case'ie pod kątem wartości referencyjnych, które zakładały stare dane — zmiana schematu danych bardzo prawdopodobnie przesunie zahardkodowane liczby dalej w lekcjach.

## Higiena notebooków

Commituj pliki `lesson.ipynb` z wyczyszczonymi outputami i bez execution counts — świeży notebook, nie taki, który akurat uruchomiłeś/aś ostatnio. Jeśli iterowałeś/aś w Jupyterze, wyczyść wszystkie outputy ("Restart Kernel and Clear All Outputs" w Jupyterze, albo `jupyter nbconvert --clear-output --inplace lesson.ipynb`) przed commitem.

## Aktualizowanie wartości referencyjnych w `check.py`

`check.py` w tym repo celowo sprawdza dokładne wartości liczbowe w większości lekcji (nie tylko "kod działa bez błędu") — ta precyzja sprawia, że self-check lekcji jest wiarygodny. Jeśli uzasadniona zmiana w `solution.py` przesuwa policzoną liczbę (poprawka błędu, regeneracja danych, nowa cecha dodana do współdzielonej funkcji), nie zgaduj nowej wartości ani nie kopiuj jej z jednego, wyglądającego na zaufany, uruchomienia: napisz mały, jednorazowy skrypt, który niezależnie ją przelicza, potwierdź liczbę dwukrotnie, i dopiero wtedy zahardkoduj ją w asercji. Błędna zahardkodowana liczba, która akurat zgadza się z wadliwą implementacją, jest cichą luką w poprawności, dużo trudniejszą do zauważenia później niż test, który po prostu nie przechodzi.

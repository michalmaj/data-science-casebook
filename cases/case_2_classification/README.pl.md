# Case 2 — Klasyfikacja: Meridian Outlet

**Klient:** Meridian Outlet, wieloasortymentowy sklep e-commerce.

**Zlecenie:** "Zbyt dużo zamówień jest zwracanych. Chcemy wiedzieć, które zamówienia są ryzykowne, zanim je wyślemy."

**Format danych:** Dwuarkuszowy Excel (`data/orders.xlsx` — arkusz "Orders" i arkusz "Customers"), generowany przez `data/generate.py`.

**Co zbudujesz w tym case'ie:** model klasyfikacyjny szacujący ryzyko, że zamówienie zostanie zwrócone, na podstawie informacji dostępnych już w momencie zamówienia, a także notatkę decyzyjną wyjaśniającą, które czynniki mają znaczenie, jak bardzo być tego pewnym, i co Meridian Outlet powinno z tym zrobić.

**Co tu właściwie znaczy "nowe dane":** ten case ocenia model na *kolejnych zamówieniach klientów, których Meridian Outlet już ma w swojej bazie* — nie na zamówieniach klientów, których nigdy wcześniej nie widział. To dwa różne pytania z różnymi odpowiedziami; Lekcja 5 pokazuje dokładnie, jak i czemu.

Lekcje tego case'u znajdują się w `lessons/`, ponumerowane w kolejności, w jakiej należy przez nie przechodzić.

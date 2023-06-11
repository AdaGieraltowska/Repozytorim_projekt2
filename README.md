# Repozytorim_projekt2
### Wymagania 
- program QGIS wersja minimum 3.22
- python 3.9
- biblioteka PyQt5
- biblioteka qgis.core
- biblioteka qgis.utilis
- biblioteka qgis.PyQt

Program został napisany dla systemu operacyjnego Windows 10 i Windows 11
### Podstawowe funkcjonalności wtyczki  
Wtyczka oblicza różnice wysokości oraz pole powierzchni metodą Gaussa na podstawie współrzędnych zaznaczonych punktów. 
### Dodatkowe funkcjonalności
Wtyczka posiada dodatkowe funkcjonalności takie jak:
- Wyczyszczenie okna wynikowego.
- Zresetowanie zaznaczonch punktów na warstwie na żądanie użytkownika.
- Możliwość narysowania poligonu opartego na wybranych punktach na żądanie uzytkownika.
- Możliwość wgrania pliku .txt .csv do projektu.


### Opis interfejsu użytkownika
Wtyczka po uruchomieniu wygląda następująco i podzielony jest na dwie główne sekcje: lewą obsługującą obliczenie pola powierzchni oraz przewyższenia i prawą obsługującą importowanie pliku .txt .csv do projektu wraz z sepecyfikacjami dotyczącymi importu. 
<!--
<p align="center">
  <img src="https://i.imgur.com/d80RQHe.png" />
</p>
-->
<p align="center">
  <img src="https://i.imgur.com/NuLO186.png width="50%"" />
</p>

<p align="center">
  <img src="https://i.imgur.com/Jyh7B0k.png width="50%"" />
</p>

<p align="center">
  <img src="https://i.imgur.com/B0kfKbe.png width="50%"" />
</p>

Opcje interfejsu użytkownika:
- **1** -- wybór obliczenia przewyższenia pomiędzy punktami
- **2** -- wybór obliczenia pola powierzchni
    - **2a/2b/2c** -- wybór jednostki obliczonego pola 
    - **2d** -- wybór wyrysowania poligonu
- **3** -- wybór warstwy ,na której będą wykonywane operacje
    - **3a** -- wybór atrybutu dla którego ma zostać wykonana funkcjonalność
- **4** -- okno umożliwiające wybór punktów poprzez wskazanie indeks punktu
- **5** -- okno wynikowe
- **6** -- przycisk *"Odznacz"*
- **7** -- przycisk *"Wybierz punkty"*
- **8** -- przycisk *"Wyczyść"*
- **9** -- przycisk *"Oblicz"*
- **10** -- checkbox wskazujący układ współrzędnych importowanego punkt dla układu PL2000
    - **10a/10b/10c/10d** -- checkboxy definiujące strefe odwzorowawczą układu PL2000
- **11** -- checkbox wskazujący układ współrzędnych importowanego punkt dla układu PL1992
- **12** -- pole tekstowe umożliwiające podanie ścieżki dostępu do importowanego pliku
- **13** -- pole tekstowe umozliwiające podanie nazwy nowotworzonej warstwy projektu
- **14** -- przycisk *"Wczytaj"*

### Wybór punktów
Punkty dla których  mają zostac wykonane obliczenia można określić na 3 sposoby:
- **Metoda 1** poprzez **zaznaczenie ich numerow ID (4)**,w oknie znajdującym się po lewej stronie okna wynikowego
- **Metoda 2** poprzez naciśnięcie przycisku **Wybierz punkty (7)** ,ktory zminimalizuje okno wtyczki i pozwoli na wybór punktów na widocznej warstwie

Jeśli użytkownik korzysta z **obu metod jednocześnie** zalecane jest przed każdym kolejnym przeliczeniem, czy roznic wysokości,czy pola powierzchni, aby resetować wybrane obiekty na warstwie używając przycisku **Odznacz (6)**, ponieważ zaznaczane punkty poprzez numery ID nie są wyświetlane na warstwie jako wybrane, ale wtyczka je bierze pod uwagę.

### Wybór obliczeń i ich obsługa
<p align="center">
  <img src="https://i.imgur.com/8sLBPZb.png" />
</p>

Po zaznaczeniu **Różnica wysokości (1)** należy wybrać w pierwszej liście **warstwę (3)**, a w drugiej **nazwę atrybutu (3a)**, która zawiera wysokości punktów. 
Do wykonania tego obliczenia wymagany jest wybór 2 punktów, w innym przypadku zostanie zwrócony komunikat o nie spełnieniu tego warunku. 
Finalnie po użyciu przycisku **Oblicz (9)** w **oknie wynikowym (5)** zostanie wyświetlona wartość przewyższenia w kierunku głównym jak i w kierunku powrotnym. 

<p align="center">
  <img src="https://i.imgur.com/d2w7huc.png" />
</p>

Natomiast po zaznaczeniu **Pole powierzchni** (2) wyświetli się **wybór jednostek (2a, 2b, 2c)** w jakich ma być obliczone pole. Domyślną jednostką są metry kwadratowe.

<p align="center">
  <img src="https://i.imgur.com/Xp8TP5K.png" />
</p>

Pojawia się również dodatkowa opcja **rysowania poligonu (2d)** na żądanie uzytkownika opartego na zaznaczonych punktach. 
Następnie należy wybrać **warstwę (3)** oraz nacisnąć przycisk **Oblicz (9)**, czego następstwem będzie obliczenie pola oraz ewentualne utworzenie nowej warstwy z wrysowanym poligonem jeżeli użytkownik tego zażądał.
Finalnie w oknie wynikowym (5)pojawi się pole powierzchni obszaru rozpietego na wybranych punktach.

W celu obliczenia pola powierzchni wymagany jest wybór przynajmniej 3 punktów, jeśli liczba wybranych punktów jest mniejsza zostanie zwrócony komunikat informujący o nie spełnieniu tego warunku.
Algorytm wtyczki poprawnie oblicza polę powierzchni obszaru rozpiętego na 3 punktach. Problem powstaje kiedy użytkownik zażąda wyznaczenia pola o większej liczbie wierzchołków ,w przypadku błędnego rozwiązania zadania w oknie dialogowym (5) pojawia się stosowny komunikat.
<!--
**UWAGA**: W celu obliczenia pola powierzchni należy wybrać metodę 1 lub metodę 3 wyboru punktu ,czyli zaznaczenie punktów bezpośrednio na warstwie. Zastosowanie metody 2 zwraca błędny wynik na warstwach, których struktura tabeli atrybutów jest różna od struktur przedstawionych poniżej w **Obsługa pliku wewnątrz wtyczki.**.
-->


### Obsługa pliku wewnątrz wtyczki.
Możliwe jest także opracowanie pliku wewnątrz wtyczki. Wtyczka obsługuje pliki formatu *.txt* oraz *.csv* dla układu współrzednych PL-1992 oraz PL-2000.
W celu zaimportowania pliku należy zaznaczyć **układ współrzędnych (10/11)** w jakich wgrany ma być plik. Ponadto przy wyborze układu PL-2000, konieczne jest określenie strefy, w której znajdują się punkty poprzez zaznaczenie dostępnych do wyboru **stref (10a/10b/10c/10d)**. Następnie nalezy wskazać lokalizację pliku poprzez podanie **ścieżki dostępu (12)** lub naciśnięcia **[...]**, po którym pojawi się *Eksplorator plików* w celu wybrania pliku. Należy też **nazwać nowo tworzoną warstwę (13)** inaczej warstwa nie będzie miała nazwy. Przyciskiem **Wczytaj (14)** nalezy sfinalizować tą funkcjonalność.

Przykładowa struktura pliku:
1. **xy1992.txt** w układzie PL-1992
>1 239382.6473 644577.0195 100.00\
>2 243167.6185 645161.3032 101.00\
>3 247142.0552 644755.1646 102.00\
>4 250075.7519 644705.4659 103.00
2. **xy2000.txt** w układzie PL-2000
>1 5540883.974 7501304.251 100.00\
>2 5544653.338 7501989.823 101.00\
>3 5548638.675 7501690.090 102.00\
>4 5551573.724 7501718.971 103.00

W strukturze obu plików **.txt** układ kolumn jest rownoważny. Pierwsza kolumna stanowi numer punktu, druga współrzędną X [m], trzecia współrzędną Y [m], czwarta H [m] <!--w odpowiednim  układzie odniesienia wysokosci tj. PL1992 - PL-KRON86-NH, PL2000 - PL-EUFRV2007-NH. -->
Struktura plików **xy1992.csv** i **xy2000.csv** jest identyczna jak struktura plików z rozszerzeniem .txt opisanych powyżej.
### Obsługa dodatkowych funkcjonalności
Dodatkowe funkcjonalności umożliwiają:
- Wyczyszczenie okna wynikowego przy użyciu przycisku **Wyczyść (8)**
- Zresetowanie zaznaczonch punktów na warstwie oraz **zaznaczenych numerów ID (4)** w na żądanie użytkownika przy uzyciu przycisku **Odznacz (6)**
- Możliwość narysowania poligonu na żądanie uzytkownika. W tym celu nalezy zaznaczyć checkbox **Rysujj poligon (2d)**. Skutkiem działania tej funkcjonalności jest utworzenie nowej warstwy *'poligon'* w projekcie zawierającej poligon rozpoztarty na wybranych punkatch.
<!--
## Uwagi
W celu obliczenia przewyższenia nie ma zanaczenia jaka metoda zaznaczania punktow będzie wybrana, natomiast przy wyznaczeniu pola powierzchni zaleca się zaznaczanie punktów metodą 1 lub 3.

## Błędy rozwiązane
- Przy wyznaczaniu pola powierzchni algorytm wtyczki źle interpretuje punkty zaznaczone metoda 2. Aby zapewnic prawidłowość wyznaczenia pola należy postępowac zgodnie z schematem obsługi przedstawionym powyżej. Ponadto funkcjonalność wtyczki została ograniczona do mozliwości wyboru punktów metodą 1 oraz 3. 
-->
## Błędy nierozwiązane
- Przy wyborze warstwy z ogromną ilością obiektów istnieje prawdopodobieństwo krótkiego zawieszenia programu.
- Możliwa jest sytuacja kiedy poligon narysuje się w innym miejscu niż powinien, ponieważ przyjął inną wartość EPSG niż warstwa, na której jest rysowany. Zaleca się wtedy usunięcie poligonu i ponowne wczytanie warstwy, a w ostateczności zresetowanie wtyczki.
- W przypadku poligonów wklęsłych algorytm nie wrysuje ich poprawnie.
- Algorytm wtyczki oblicza pole powierzchni metodą Gaussa, zauważono jednak ,że dla niektórych poligonów niezachowuje on stałej skrętności przechodzenia na punkty po długościach boków tych poligonów, a zmienia ją w trakcie obliczania pola tzn. zaczyna obliczanie zgodnie z ruchem wskazówek zegara ,a następnie zmienia kierunek na przeciwny. Powiodło się jedynie częściowe wyeliminowanie tego błędu. W przypadku błędnego rozwiązania zadania algorytm zwróci stosowny komunikat na ten temat. Ponizej znajduje się przykład opisanej powyżej sytuacji ,kiedy algorytm poprawnie rozwiązuje zadanie oraz kiedy błędnie. 
Poprawne rozwiązanie: 

<p align="center">
  <img src="https://i.imgur.com/CKwXZ26.png" />
</p>

Niepoprawne rozwiązanie z zwizualizowaniem opisanego błędu: 

<p align="center">
  <img src="https://i.imgur.com/is47EGH.png" />
</p>

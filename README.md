# Repozytorim_projekt2
### Wymagania 
- program QGIS wersja minimum 3.22
- python 3.9
- biblioteka PyQt5
- biblioteka qgis.core
- biblioteka qgis.utilis
- biblioteka qgis.PyQt
- biblioteka numpy

Program został napisany dla systemu operacyjnego Windows 10 i Windows 11
### Podstawowe funkcjonalności wtyczki  
Wtyczka oblicza różnice wysokości oraz pole powierzchni metodą Gaussa na podstawie współrzędnych zaznaczonych punktów. 
### Dodatkowe funkcjonalności
Wtyczka posiada dodatkowe funkcjonalności takie jak:
1. Wyczyszczenie okna wynikowego.
2. Zresetowanie zaznaczonch punktów na warstwie na żądanie użytkownika.
3. Możliwość narysowania poligonu opartego w wybrane punkty na żądanie uzytkownika.
4. Możliwość wgrania pliku .txt do projektu.


### Opis interfejsu użytkownika
Wtyczka po uruchomieniu wygląda następująco:
![img](https://i.imgur.com/d80RQHe.png)
Interfejs wtyczki podzielony jest na dwie główne sekcje: lewą obsługującą obliczenie pola powierzchni oraz przewyższenia i prawą obsługującą importowanie pliku .txt do projektu wraz z sepecyfikacjami dotyczącymi importu.

![Imgur](https://i.imgur.com/NuLO186.png)

Opis interfejsu użytkownika:
- 1 --> wybór obliczenia przewyższenia pomiędzy punktami
- 2 --> wybór obliczenia pola powierzchni
- 2a/2b/2c --> wybór jednostki obliczonego pola 
- 2d --> wybór wyrysowania poligonu
- 3 --> wybór warstwy ,na której będą wykonywane operacje
- 3a --> wybór atrybutu dla którego ma zostać wykonana funkcjonalność
- 4 --> okno umożliwiające wybór punktów poprzez wskazanie indeks punktu
- 5 --> okno wynikowe
- 6 --> przycisk "Odznacz"
- 7 --> przycisk "Wybierz punkty"
- 8 --> przycisk "Wyczyść"
- 9 --> przycisk "Oblicz"
- 10 --> checkbox wskazujący układ współrzędnych importowanego punkt dla układu PL2000
- 10a/10b/10c/10d --> checkboxy definiujące strefe odwzorowawczą układu PL2000
- 11 --> checkbox wskazujący układ współrzędnych importowanego punkt dla układu PL1992
- 12 --> pole tekstowe umożliwiające podanie ścieżki dostępu do importowanego pliku
- 13 --> pole tekstowe umozliwiające podanie nazwy nowotworzonej warstwy projektu
- 14 --> przycisk "Wczytaj"

### Wybór punktów
Punkty dla których  mają zostac wykonane obliczenia można określić na 3 sposoby:
Metoda 1 przed uruchomieniem wtyczki lub w trakcie pracy z nią poprzez zaznaczenie punktów na widocznej warstwie,
Metoda 2 poprzez zaznaczenie ich numerow ID ,w oknie znajdującym się po lewej stronie okna wynikowego (4),
Metoda 3 poprzez naciśnięcie przycisku **Wybierz punkty** (7) ,ktory zminimalizuje okno wtyczki i pozwoli na wybór punktów na widocznej warstwie.

W trakcie pracy z wtyczką nie należy jednak zmieniać jednej uprzednio wybranej metody wprowadzania punktu. 

Zalecane jest przed każdym kolejnym przeliczeniem ,czy roznic wysokości ,czy pola powierzchni ,aby resetować wybrane obiekty na warstwie używając przycisku **Odznacz** (6).

### Wybór obliczeń i ich obsługa
![Imgur](https://i.imgur.com/8sLBPZb.png)
Po zaznaczeniu **Różnica wysokości**(1) należy wybrać w pierwszej liście (3) warstwę , a w drugiej(3a) nazwę atrybutu, która zawiera wysokości punktów. 
Do wykonania tego obliczenia wymagany jest wybór 2 punktów ,w innym przypadku zostanie zwrócony komunikat o nie spełnieniu tego warunku. 
Finalnie po użyciu przycisku **Oblicz** (9) w oknie wynikowym(5) zostanie wyświetlona wartość przewyższenia w kierunku głównym jak i w kierunku powrotnym. 
![Imgur](https://i.imgur.com/d2w7huc.png).

**Uwaga**: W celu obliczenia przewyższenia nie ma zanaczenia jaka metoda zaznaczania punktow będzie wybrana.


Natomiast po zaznaczeniu **Pole powierzchni** (2) wyświetli się wybór (2a,2b,2c) w jakich jednostkach ma być obliczone pole. Domyślną jednostką są metry kwadratowe.
![Imgur](https://i.imgur.com/Xp8TP5K.png). 
Pojawia się również dodatkowa opcja (2d), która narysuje poligon na żądanie uzytkownika oparty na zaznaczonych punktach. 
Następnie należy wybrać warstwę na ktorej znajdują się punkty z rozwijalnej listy(3) oraz nacisnąć przycisk **Oblicz** ,czego następstem będzie obliczenie pola oraz ewentualne utworzenie nowej warsty z wrysowanym poligonem jeżeli użytkownik tego zażądał.

Finalnie w oknie wynikowym (5)pojawi się pole powierzchni obszaru rozpietego na wybranych punktach.

**UWAGA**: W celu obliczenia pola powierzchni należy wybrać metodę 1 lub metodę 3 wyboru punktu ,czyli zaznaczenie punktów bezpośrednio na warstwie. Zastosowanie metody 2 zwraca błędny wynik na warstwach ,których struktura tabeli atrybutów jest różna od struktur przedstawionych poniżej w **Obsługa pliku wewnątrz wtyczki.**.



### Obsługa pliku wewnątrz wtyczki.
Możliwe jest także opracowanie pliku wewnątrz wtyczki. Wtyczka obsługuje pliki formatu .txt dla układu współrzednych PL-1992 oraz PL-2000.
W celu zaimportowania pliku należy zaznaczyć w jakim układzie współrzędnych wgrany ma być plik (10/11). Ponadto przy wyborze układu PL-2000 ,konieczne jest określenie strefy ,w której znajdują się punkty poprzez zaznaczenie dostępnych do wyboru stref (10a/10b/10c/10d). Następnie nalezy wskazać lokalizację pliku poprzez podanie ścieżki dostępu (12) ,oraz nazwać nowo tworzoną warstwę (13). Przyciskiem **Wczytaj** (14)nalezy sfinalizować tą funkcjonalność.

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

W strukturze obu plików układ kolumn jest rownoważny. Pierwsza kolumna stanowi numer punktu, druga współrzędną X [m], trzecia współrzędną Y[m] ,czwarta H[m] w odpowiednim  układzie odniesienia wysokosci tj. PL1992 --> PL-KRON86-NH, PL2000 --> PL-EUFRV2007-NH.

### Obsługa dodatkowych funkcjonalności
Dodatkowe funkcjonalności umożliwiają:
1. Wyczyszczenie okna wynikowego przy użyciu przycisku **Wyczyść**. Użycie skutkuje czym? jak ładnie to opisać
2. Zresetowanie zaznaczonch punktów na warstwie na żądanie użytkownika przy uzyciu przycisku **Odznacz**
3. Możliwość narysowania poligonu na żądanie uzytkownika. W tym celu nalezy zaznaczyć checbox **Rysujj poligon** jako aktywny. Skutkiem działania tej funkcjonalności jest utworzenie nowej warstwy 'poligon' w projekcie zawierającej poligon rozpoztarty na wybranych punkatch.



## Uwagi
W celu obliczenia przewyższenia nie ma zanaczenia jaka metoda zaznaczania punktow będzie wybrana, natomiast przy wyznaczeniu pola powierzchni zaleca się zaznaczanie punktów metodą 1 lub 3.

## Błędy rozwiązane
1. Przy wyznaczaniu pola powierzchni algorytm wtyczki źle interpretuje punkty zaznaczone metoda 2. Aby zapewnic prawidłowość wyznaczenia pola należy postępowac zgodnie z schematem obsługi przedstawionym powyżej. Ponadto funkcjonalność wtyczki została ograniczona do mozliwości wyboru punktów metodą 1 oraz 3. 

## Błędy nierozwiązane
1. Wtyczka nie działa poprawnie dla warstw zaimportowanych poprzez WFS oraz WMS. Zalecane jest ,aby struktura tabeli atrybutów była równoważna z strukturą przykładowych plików **xy1992.txt** oraz **xy2000.txt** opisanych w **Obsługa pliku wewnątrz wtyczki.**.

2. Algorytm wtyczki oblicza pole powierzchni metodą Gaussa ,jednak zauważono że dla niektórych poligonów niezachowuje on stałej skrętności przechodzenia na punkty po długościach boków tych poligonów ,a zmienia ją w trakcie obliczania pola tzn. zaczyna obliczanie zgodnie z ruchem wskazówek zegara ,a następnie zmienia kierunek na przeciwny. Powiązane może to być z indeksacją punktów po numerze ich numerach w zmiennej selected_features zastosowaną w funkcji oblicz. Powiodło się jedynie częściowe wyeliminowanie tego błędu. Ponizej znajduje się przykład opisanej powyżej sytuacji ,kiedy algorytm poprawnie rozwiązuje zadanie oraz kiedy błędnie
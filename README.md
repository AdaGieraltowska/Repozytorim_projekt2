# Repozytorim_projekt2
# Repozytorim_projekt2

# Repozytorim_projekt2
### Funkcjonalności wtyczki  
Wtyczka oblicza różnice wysokości oraz pole powierzchni na podstawie współrzędnych zaznaczonych punktów metodą Gaussa. Dodatkowo ma opcję wgrania pliku do projektu i rysowania poligonu na podstawie zaznaczonych punktów do obliczenia pola powierzchni.
### Wymagania 
- program QGIS wersja minimum 3.22
- python 3.9
- biblioteka PyQt5
- biblioteka qgis.core
- biblioteka qgis.utilis
- biblioteka qgis.PyQt

Program został napisany dla systemu operacyjnego Windows 10 i Windows 11

## Opis użycia programu
W zależności od potrzeb można wyrożnić 2 główne funkcjonalności wtyczki:
- Obliczanie przewyższenia
- Obliczenie pola powierzchni metodą Gaussa
### Ogólny wygląd
Wtyczka po uruchomieniu wygląda następująco:
![img](https://i.imgur.com/d80RQHe.png)
Po lewej stronie widoczny jest wybór jakie obliczenia ma wykonać wtyczka
### Wybór obliczeń
![Imgur](https://i.imgur.com/8sLBPZb.png)
Po zaznaczeniu **Różnica wysokości** trzeba wybrać w pierwszej liście warstwę , a w drugiej nazwę atrybutu, która zawiera wysokości punktów. 
![Imgur](https://i.imgur.com/Xp8TP5K.png). 
Do wykonania tego obliczenia wymagany jest wybór 2 punktów ,w innym przypadku zostanie zwrócony komunikat o nie spełnieniu tego warunku.


Finalnie w oknie dialogowym zostanie wyświetlona wartość przewyższenia w kierunku głównym jak i w kierunku powrotnym. 
![Imgur](https://i.imgur.com/d2w7huc.png)




Natomiast po zaznaczeniu **Pole powierzchni** wyświetli się wybór w jakich jednostkach ma być obliczone pole. Domyślną jednostką są metry kwadratowe. Pojawia się również dodatkowa opcja, która rysuje poligon dla zaznaczonych punktów.
### Wybór punktów
Punkty dla których  mają zostac wykonane obliczenia można określić na 3 sposoby:
1. przed uruchomieniem wtyczki poprzez zaznaczenie ich na widocznej warstwie,
2. poprzez zaznaczenie ich numerow ID ,w oknie znajdującym się po lewej stronie okna wynikowego,
3. poprzez naciśnięcie przycisku **Wybierz punkty** ,ktory zminimalizuje okno wtyczki i pozwoli na wybór punktów na widocznej warstwie.

W trakcie pracy z wtyczką należy jednak nie zmieniać jednej uprzednio wybranej metody wprowadzania punktu. 

Zalecane jest ,aby przed każdym kolejnym przeliczeniem ,czy roznic wysokości ,czy pola powierzchni resetować wybrane obiekty na warstwie używając przycisku **Odznacz**

### Wgrywanie pliku


### Pozostałe funkcje

## Opis przykładowych danych wgrania


## Błędy

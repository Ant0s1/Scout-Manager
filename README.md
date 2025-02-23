# Scout-Manager
POLISH

    Wprowadzenie

Program jest przeznaczony do zarządzania danymi harcerzy, drużyn, zbiórek oraz kalendarza zbiórek. Umożliwia dodawanie harcerzy do drużyn, przypisywanie zadań i ocen, a także zarządzanie zbiórkami. Wszystkie dane są przechowywane w odpowiednich obiektach i mogą być łatwo wyświetlane lub edytowane. 2. Struktura programu

Program składa się z kilku klas, które reprezentują różne elementy organizacyjne, takie jak harcerze, drużyny, zbiórki i kalendarz. 2.1 Klasa Harcerz

Klasa Harcerz przechowuje dane dotyczące harcerza: imię, nazwisko, stopień oraz listy zadań i ocen. Atrybuty:

imie: imię harcerza (typ: string).
nazwisko: nazwisko harcerza (typ: string).
stopien: stopień harcerza (typ: string).
zadania: lista zadań przypisanych harcerzowi (typ: lista).
oceny: lista ocen przypisanych harcerzowi (typ: lista).

Metody:

dodaj_zadanie(zadanie): Dodaje zadanie do listy zadań harcerza.
wykonane_zadania(): Zwraca listę zadań, które zostały wykonane (zadania mają atrybut wykonane).
dodaj_ocene(ocena): Dodaje ocenę do listy ocen harcerza.
__str__(): Zwraca reprezentację tekstową harcerza w formie "Imię Nazwisko - Stopień".

2.2 Klasa Druzyna

Klasa Druzyna reprezentuje drużynę harcerską i przechowuje listę jej członków. Atrybuty:

nazwa: nazwa drużyny (typ: string).
czlonkowie: lista członków drużyny (typ: lista obiektów typu Harcerz).

Metody:

dodaj_harcerza(harcerz): Dodaje harcerza do drużyny.
lista_harcerzy(): Zwraca listę nazwisk harcerzy w drużynie w postaci tekstowej.

2.3 Klasa Zbiorka

Klasa Zbiorka reprezentuje zbiórkę harcerską, zawierającą datę, temat oraz prowadzącego. Umożliwia również ocenianie harcerzy obecnych na zbiórce. Atrybuty:

data: data zbiórki (typ: string).
temat: temat zbiórki (typ: string).
prowadzacy: prowadzący zbiórkę (typ: string).
obecni: lista harcerzy obecnych na zbiórce (typ: lista obiektów typu Harcerz).
oceny: słownik ocen harcerzy obecnych na zbiórce (typ: słownik, klucz: obiekt Harcerz, wartość: ocena).

Metody:

dodaj_obecnego(harcerz): Dodaje harcerza do listy obecnych na zbiórce.
ocen_harcerza(harcerz, ocena): Przypisuje ocenę harcerzowi obecnemu na zbiórce.
lista_obecnych(): Zwraca listę nazwisk harcerzy obecnych na zbiórce w postaci tekstowej.

2.4 Klasa Kalendarz

Klasa Kalendarz umożliwia przechowywanie zbiórek w kalendarzu i ich wyświetlanie. Atrybuty:

zbiorki: lista wszystkich zbiórek (typ: lista obiektów typu Zbiorka).

Metody:

dodaj_zbiorke(zbiorka): Dodaje zbiórkę do kalendarza.
wyswietl_kalendarz(): Zwraca listę wszystkich zbiórek w kalendarzu w postaci tekstowej.

    Przykłady użycia

Poniżej przedstawiono przykłady użycia programu. 3.1 Tworzenie harcerzy

harcerz1 = Harcerz("Jan", "Kowalski", "Ochotnik") harcerz2 = Harcerz("Anna", "Nowak", "Młodzik")

Tworzenie dwóch obiektów Harcerz o imionach i nazwiskach oraz przypisanych stopniach. 3.2 Tworzenie drużyny i dodawanie harcerzy

druzyna = Druzyna("Orły") druzyna.dodaj_harcerza(harcerz1) druzyna.dodaj_harcerza(harcerz2)

Tworzenie obiektu Druzyna o nazwie "Orły" i dodawanie do niej harcerzy harcerz1 oraz harcerz2. 3.3 Tworzenie zbiórki, dodawanie obecnych i ocenianie

zbiorka = Zbiorka("2025-03-01", "Sztuka węzłów", "Druh Michał") zbiorka.dodaj_obecnego(harcerz1) zbiorka.dodaj_obecnego(harcerz2) zbiorka.ocen_harcerza(harcerz1, 5) zbiorka.ocen_harcerza(harcerz2, 4)

Tworzenie obiektu Zbiorka z datą, tematem i prowadzącym. Następnie dodawanie harcerzy do listy obecnych i ocenianie ich. 3.4 Tworzenie kalendarza i dodawanie zbiórek

kalendarz = Kalendarz() kalendarz.dodaj_zbiorke(zbiorka)

Tworzenie obiektu Kalendarz i dodawanie zbiórki do kalendarza. 3.5 Wyświetlanie danych

print("Lista harcerzy w drużynie:", druzyna.lista_harcerzy()) print("Obecni na zbiórce:", zbiorka.lista_obecnych()) print("Oceny harcerzy:", {str(h): h.oceny for h in zbiorka.obecni}) print("Kalendarz zbiórek:", kalendarz.wyswietl_kalendarz())

Wyświetlanie:

listy harcerzy w drużynie,
listy obecnych na zbiórce,
ocen harcerzy,
kalendarza zbiórek.

    Podsumowanie

Program umożliwia skuteczne zarządzanie informacjami o harcerzach, drużynach, zbiórkach i kalendarzach. Dzięki niemu można łatwo dodawać harcerzy, zarządzać zadaniami, ocenami i zbiórkami, co może być przydatne w organizacji działań harcerskich.

ENGLISH

    Introduction

The program is designed to manage data about scouts, teams, meetings, and meeting calendars. It allows adding scouts to teams, assigning tasks and grades, and managing meetings. All data is stored in relevant objects and can be easily displayed or edited. 2. Program Structure

The program consists of several classes that represent different organizational elements, such as scouts, teams, meetings, and calendars. 2.1 Harcerz Class

The Harcerz class stores data about a scout: first name, last name, rank, and lists of tasks and grades. Attributes:

imie: first name of the scout (type: string).
nazwisko: last name of the scout (type: string).
stopien: rank of the scout (type: string).
zadania: list of tasks assigned to the scout (type: list).
oceny: list of grades assigned to the scout (type: list).

Methods:

dodaj_zadanie(zadanie): Adds a task to the scout's task list.
wykonane_zadania(): Returns a list of tasks that have been completed (tasks have an attribute wykonane).
dodaj_ocene(ocena): Adds a grade to the scout's grade list.
__str__(): Returns the string representation of the scout in the format "First Name Last Name - Rank".

2.2 Druzyna Class

The Druzyna class represents a scout team and stores a list of its members. Attributes:

nazwa: name of the team (type: string).
czlonkowie: list of team members (type: list of Harcerz objects).

Methods:

dodaj_harcerza(harcerz): Adds a scout to the team.
lista_harcerzy(): Returns a list of scout names in the team in string format.

2.3 Zbiorka Class

The Zbiorka class represents a scout meeting, containing a date, topic, and leader. It also allows evaluating scouts present at the meeting. Attributes:

data: date of the meeting (type: string).
temat: topic of the meeting (type: string).
prowadzacy: leader of the meeting (type: string).
obecni: list of scouts present at the meeting (type: list of Harcerz objects).
oceny: dictionary of grades for scouts present at the meeting (type: dictionary, key: Harcerz object, value: grade).

Methods:

dodaj_obecnego(harcerz): Adds a scout to the list of those present at the meeting.
ocen_harcerza(harcerz, ocena): Assigns a grade to a scout present at the meeting.
lista_obecnych(): Returns a list of names of scouts present at the meeting in string format.

2.4 Kalendarz Class

The Kalendarz class allows storing meetings in the calendar and displaying them. Attributes:

zbiorki: list of all meetings (type: list of Zbiorka objects).

Methods:

dodaj_zbiorke(zbiorka): Adds a meeting to the calendar.
wyswietl_kalendarz(): Returns a list of all meetings in the calendar in string format.

    Example Usage

Below are examples of how to use the program. 3.1 Creating Scouts

harcerz1 = Harcerz("Jan", "Kowalski", "Ochotnik") harcerz2 = Harcerz("Anna", "Nowak", "Młodzik")

Creating two Harcerz objects with first names, last names, and assigned ranks. 3.2 Creating a Team and Adding Scouts

druzyna = Druzyna("Orły") druzyna.dodaj_harcerza(harcerz1) druzyna.dodaj_harcerza(harcerz2)

Creating a Druzyna object named "Orły" and adding scouts harcerz1 and harcerz2 to it. 3.3 Creating a Meeting, Adding Attendees, and Evaluating

zbiorka = Zbiorka("2025-03-01", "Knot Art", "Druh Michał") zbiorka.dodaj_obecnego(harcerz1) zbiorka.dodaj_obecnego(harcerz2) zbiorka.ocen_harcerza(harcerz1, 5) zbiorka.ocen_harcerza(harcerz2, 4)

Creating a Zbiorka object with a date, topic, and leader. Then, adding scouts to the list of attendees and assigning grades. 3.4 Creating a Calendar and Adding Meetings

kalendarz = Kalendarz() kalendarz.dodaj_zbiorke(zbiorka)

Creating a Kalendarz object and adding a meeting to the calendar. 3.5 Displaying Data

print("List of scouts in the team:", druzyna.lista_harcerzy()) print("Attendees at the meeting:", zbiorka.lista_obecnych()) print("Grades of scouts:", {str(h): h.oceny for h in zbiorka.obecni}) print("Meeting calendar:", kalendarz.wyswietl_kalendarz())

Displaying:

a list of scouts in the team,
a list of attendees at the meeting,
the grades of scouts,
the meeting calendar.

    Summary

The program allows effective management of information about scouts, teams, meetings, and calendars. With this tool, you can easily add scouts, manage tasks, grades, and meetings, which can be useful for organizing scout activities.

"""
Iris - perceptron training
"""

from Iris import Iris
from Perceptron import Perceptron


# Wprowadzanie danych przy odpaleniu programu z terminala

# import sys
#
# if len(sys.argv) != 4:
#     print('nieprawidlowa ilosc argumentow')
#     raise TypeError(f"nieprawidlowa ilosc argumentow\nwymagane: 4\notrzymane: {len(sys.argv)}")
#
# a = float(sys.argv[1])
# trainSet = sys.argv[2]
# testSet = sys.argv[3]


# Dane testowe

a = 0.5
trainSet = "Data/trainSet.txt"
testSet = "Data/testSet.txt"

accuracySet = "Data/accuracySet.txt"


# Metoda sprawdzajaca poprawnosc programu
def howaccurate(correctno, allno):
    return correctno/allno*100


# Metoda sortująca linie z pliku csv oraz tworzaca obiekt klasy Iris
def sortline(v_line):
    v_type = "default"
    info = v_line.split(",")
    wector = list()
    for i in range(len(info)):
        try:
            wector.append(float(info[i]))
        except ValueError:
            v_type = info[i]
    iris1 = Iris(wector, v_type)
    return iris1


# Metoda odczytujaca dane z podanego pliku i zapisujaca linie do listy, zwraca liste linii z pliku
def readfile(path):
    arr = list()
    ffile = open(path, 'r')
    for line in ffile:
        arr.append(sortline(line.replace("\n", "")))
    return arr


# Metoda, ktorej zadaniem jest podjecie decyzji co do typu Irysa,
# decyzja jest podejmowana na bazie zmiennej typu bool przekazanej jako parametr metody
def decision(isgood):
    if isgood:
        return "setosa"
    else:
        return "versicolor"


# Metoda, której zadaniem jest trenowanie perceptronu na bazie listy treningowej
# trening polega na sprawdzeniu czy metoda czynauczony zwraca wartosc 0 czy 1 i na tej podstawie przekazaniu
# tej wartosci do metody decyzyjnej
def train(perceptronn, v_trainlist):
    czydalejj = True
    while czydalejj:
        good, setosagood, versicolorgood = 0, 0, 0
        for trainiris in v_trainlist:
            v_type = trainiris.v_type
            parts = v_type.split("-")
            v_type = parts[1]
            czynauczon = perceptronn.czynauczony(trainiris.vector)
            # print(czynauczon)
            odp = decision(czynauczon)
            # print(f"{odp} == {v_type}")
            if odp == v_type:
                good += 1
                if odp == "setosa":
                    setosagood += 1
                elif odp == "versicolor":
                    versicolorgood += 1
            else:
                perceptronn.naucz(not czynauczon, czynauczon, trainiris.vector)
        accuracy = howaccurate(good, len(v_trainlist))
        print(f"Ogolna poprawnosc: {accuracy}%\n"
              f"Poprawnosc setosa: {howaccurate(setosagood, len(v_trainlist)/2)}%\n"
              f"Poprawnosc versicolor: {howaccurate(versicolorgood, len(v_trainlist)/2)}%")
        if accuracy > 99:
            czydalejj = False
        else:
            ask = input("powtorzyc nauczanie? (y/n)")
            if ask == "n":
                czydalejj = False


# Metoda, której zadaniem jest sprawdzenie na testowej liscie czy perceptron nauczyl sie
# rozpoznawac Irysy, drukujaca jego dokladnosc po przejsciu calej listy testowej
def test(perceptronn, v_testlist, v_accuracylist):
    good, setosagood, versicolorgood = 0, 0, 0
    for i in range(len(v_testlist)):
        czynauczon = perceptronn.czynauczony(v_testlist[i].vector)
        odp = decision(czynauczon)
        n_type = v_accuracylist[i].v_type
        parts = n_type.split("-")
        n_type = parts[1]
        if odp == n_type:
            good += 1
            if odp == "setosa":
                setosagood += 1
            elif odp == "versicolor":
                versicolorgood += 1
    accuracy = howaccurate(good, len(v_testlist))
    print(f"Ogolna poprawnosc: {accuracy}%\n"
          f"Poprawnosc setosa: {howaccurate(setosagood, len(v_testlist) / 2)}%\n"
          f"Poprawnosc versicolor: {howaccurate(versicolorgood, len(v_testlist) / 2)}%")


trainlist = readfile(trainSet)
testlist = readfile(testSet)
accuracylist = readfile(accuracySet)


print("\nWitamy w programie do rozpoznawania podgatunkow Irysow")
perceptron = Perceptron(len(trainlist[0].vector), a, 1, 2)
print(f"\n#######################\n\ttryb nauczania\n#######################\n")
train(perceptron, trainlist)
print("\nNauczanie zostało zakończone.")
print(f"\n#######################\n\ttryb testowania\n#######################\n")
test(perceptron, testlist, accuracylist)

czydalej = True
while czydalej:
    odpp = input("Czy chcesz przetestowac swojego irysa? (y/n)")
    if odpp == "y":
        vector = list()
        print("Wprowadz pojedynczo swoje dane:")
        for ii in range(len(perceptron.vectorwag)):
            wartosc = input("podaj wartosc: ")
            vector.append(float(wartosc))
        czynau = perceptron.czynauczony(vector)
        typ = decision(czynau)
        print(f"Podany podgatunek irysa to: {typ}")
    else:
        print("\nDziekujemy za skorzystanie z programu")
        czydalej = False

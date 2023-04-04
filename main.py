from Iris import Iris
from Perceptron import Perceptron

# import sys
#
# if len(sys.argv) != 4:
#     print('nieprawidlowa ilosc argumentow')
#     raise TypeError(f"nieprawidlowa ilosc argumentow\nwymagane: 4\notrzymane: {len(sys.argv)}")
#
# a = int(sys.argv[1])
# trainSet = sys.argv[2]
# testSet = sys.argv[3]


a = 0.5
trainSet = "Data/trainSet.txt"
testSet = "Data/testSet.txt"
accuracySet = "Data/accuracySet.txt"


def howaccurate(correctno, allno):
    return correctno/allno*100


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


def readfile(path):
    arr = list()
    ffile = open(path, 'r')
    for line in ffile:
        arr.append(sortline(line.replace("\n", "")))
    return arr


def decision(isgood):
    if isgood:
        return "setosa"
    else:
        return "versicolor"


def train(perceptronn, v_trainlist):
    czydalejj = True
    while czydalejj:
        good, setosagood, versicolorgood = 0, 0, 0
        for trainiris in v_trainlist:
            v_type = trainiris.v_type
            czynauczon = perceptronn.czynauczony(trainiris.vector)
            odp = decision(czynauczon)
            if odp == v_type:
                good += 1
                if odp == "setosa":
                    setosagood += 1
                elif odp == "versicolor":
                    versicolorgood += 1
            else:
                perceptronn.naucz(not czynauczon, czynauczon, trainiris.vector)
        accuracy = howaccurate(good, len(v_trainlist))
        print(f"Ogolna poprawnosc: {accuracy}\n"
              f"Poprawnosc setosa: {howaccurate(setosagood, len(v_trainlist)/2)}\n"
              f"Poprawnosc versicolor: {howaccurate(versicolorgood, len(v_trainlist)/2)}")
        if accuracy > 99:
            czydalejj = False
        else:
            ask = input("powtorzyc nauczanie? (y/n)")
            if ask == "n":
                czydalejj = False


def test(perceptronn, v_testlist, v_accuracylist):
    good, setosagood, versicolorgood = 0, 0, 0
    for i in range(len(v_testlist)):
        czynauczon = perceptronn.czynauczony(v_testlist[i].vector)
        odp = decision(czynauczon)
        if odp == v_accuracylist[i].v_type:
            good += 1
            if odp == "setosa":
                setosagood += 1
            elif odp == "versicolor":
                versicolorgood += 1
    accuracy = howaccurate(good, len(v_testlist))
    print(f"Ogolna poprawnosc: {accuracy}\n"
          f"Poprawnosc setosa: {howaccurate(setosagood, len(v_testlist) / 2)}\n"
          f"Poprawnosc versicolor: {howaccurate(versicolorgood, len(v_testlist) / 2)}")


trainlist = readfile(trainSet)
testlist = readfile(testSet)
accuracylist = readfile(accuracySet)

perceptron = Perceptron(len(trainlist[0].vector), a, 1, "default", 1)
train(perceptron, trainlist)
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
        print("Dziekuje za skorzystanie z programu")
        czydalej = False

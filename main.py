from Iris import Iris

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
    vector = list()
    for i in range(len(info)):
        try:
            vector.append(float(info[i]))
        except ValueError:
            v_type = info[i]
    iris1 = Iris(vector, v_type)
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


trainlist = readfile(trainSet)
testlist = readfile(testSet)
accuracylist = readfile(accuracySet)

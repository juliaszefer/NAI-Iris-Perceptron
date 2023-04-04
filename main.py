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


def howaccurate(correctno, allno):
    return correctno/allno*100


def sortline(v_line):
    info = v_line.split(",")
    vector = (info[0], info[1], info[2], info[3])
    if len(info) > 4:
        e = info[4]
        info_2 = e.split("-")
        v_type = info_2[1]
    else:
        v_type = "default"


def readfile(path):
    arr = list()
    ffile = open(path, 'r')
    for line in ffile:
        arr.append(sortline(line))
    return arr

from norm import minimum

fset1 = {(0, 0), (0.3, 1), (1, 2), (0.7, 3), (0.5, 4)}
fset2 = {(0.3, 0), (1, 1), (0.4, 2), (0.7, 5)}


def intersection(zbior1, zbior2, norma):
    print("set1: {}".format(zbior1))
    print("set2: {}".format(zbior2))
    z = set()  # creating empty set
    for x in zbior1:
        for y in zbior2:
            if x[1] == y[1]:
                z.add(norma(x, y))
    print("z: {}".format(z))

    for x in zbior1:
        contains = 0
        for y in z:
            if x[1] == y[1]:
                contains = 1
                print("contains")
        if contains == 0:
            minnorm = (0, x[1])  # TODO: change for proper norm
            print("add minnorm: {}".format(minnorm))
            z.add(minnorm)

    for x in zbior2:
        contains = 0
        for y in z:
            if x[1] == y[1]:
                contains = 1
                print("contains")
        if contains == 0:
            minnorm = (0, x[1])  # TODO: change for proper norm
            print("add minnorm: {}".format(minnorm))
            z.add(minnorm)
    print(z)

    # TODO: dodaj do zbioru elementy które nie są wspólne dla obu zbiorów


intersection(fset1, fset2, minimum)

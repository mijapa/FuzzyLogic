from norm import minimum

f_set_1 = {(0, 0), (0.3, 1), (1, 2), (0.7, 3), (0.5, 4)}
f_set_2 = {(0.3, 0), (1, 1), (0.4, 2), (0.7, 5)}


def intersection(set_1, set_2, norm):
    print("set1: {}".format(set_1))
    print("set2: {}".format(set_2))
    out_set = set()  # creating empty set
    for x in set_1:
        for y in set_2:
            if x[1] == y[1]:
                out_set.add(norm(x, y))
    print("z: {}".format(out_set))

    def lookForLeft(set, outSet):
        for x in set:
            contains = 0
            for y in outSet:
                if x[1] == y[1]:
                    contains = 1
                    print("contains")
            if contains == 0:
                minnorm = (0, x[1])  # TODO: change for proper norm
                print("add minnorm: {}".format(minnorm))
                outSet.add(minnorm)

    lookForLeft(set_1, out_set)
    lookForLeft(set_2, out_set)
    print(out_set)


intersection(f_set_1, f_set_2, minimum)

from norm import minimum

fnumber1 = {(0.3, 1), (1, 2)}
fnumber2 = {(1, 1)}


def addition(liczba1, liczba2, norma):
    z = set()
    for x in liczba1:
        for y in liczba2:
            print("x: {}".format(x))
            print("y: {}".format(y))
            print("suma: {}".format((norma(x, y)[0], x[1] + y[1])))
            z.add((norma(x, y)[0], x[1] + y[1]))
    # TODO: usuń ewentualne powtarzające się wartości
    print(z)


addition(fnumber1, fnumber2, minimum)

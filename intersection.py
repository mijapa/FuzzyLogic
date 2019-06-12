from norm import norma

fset1 = {(0.3, 1), (1, 2), (0.7, 3), (0.5, 4), (0, 0)}
fset2 = {(0.3, 0), (1, 1), (0.4, 2)}


def przeciecie(zbior1, zbior2, norma):
    z = set()  # creating empty set
    for x in zbior1:
        for y in zbior2:
            if x[1] == y[1]:
                z.add(norma(x, y))
    print(z)
    # TODO: dodaj do zbioru elementy które nie są wspólne dla obu zbiorów


przeciecie(fset1, fset2, norma)

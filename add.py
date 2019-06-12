from norm import minimum

f_number_1 = {(0.3, 1), (1, 2)}
f_number_2 = {(1, 1), (0.5, 2)}


def addition(number_1, number_2, norm):
    a_set = set()  # creating empty set
    for x in number_1:
        for y in number_2:
            print("x: {}".format(x))
            print("y: {}".format(y))
            print("suma: {}".format((norm(x, y)[0], x[1] + y[1])))
            a_set.add((norm(x, y)[0], x[1] + y[1]))

    print("a_set: {}".format(a_set))
    visited = set()
    b_set = set()
    for a, b in a_set:
        if not b in visited:
            visited.add(b)
            print("visited: {}".format(visited))
            b_set.add((a, b))
    print(b_set)

    for x in a_set:
        for y in b_set:
            if x[1] == y[1]:
                if x[0] > y[0]:
                    b_set.remove(y)
                    b_set.add(x)
    print(b_set)


addition(f_number_1, f_number_2, minimum)

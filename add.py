from norm import minimum

f_number_1 = {(0.3, 1), (1, 2)}
f_number_2 = {(1, 1), (0.5, 2)}


def addition(number_1, number_2, norm):
    a_set = set()  # creating empty set
    for x in number_1:
        for y in number_2:
            fuzzy_sum = (norm(x, y)[0], x[1] + y[1])
            print("x: {}, y: {}, fuzzy sum: {}".format(x, y, fuzzy_sum))
            a_set.add(fuzzy_sum)

    print("a_set before removing repetitions : {}".format(a_set))
    visited = set()
    b_set = set()
    for a, b in a_set:
        if not b in visited:
            visited.add(b)
            # print("visited: {}".format(visited))
            b_set.add((a, b))
    print("b_set before changing elements to upper bound: {}".format(b_set))

    for x in a_set:
        for y in b_set:
            if x[1] == y[1]:
                if x[0] > y[0]:  # upper bound
                    b_set.remove(y)
                    b_set.add(x)
    print("wynik: {}".format(b_set))


addition(f_number_1, f_number_2, minimum)

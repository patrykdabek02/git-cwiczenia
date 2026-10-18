# Zadanie 3: wyswietl tylko parzyste elementy
def print_even(nrs):
    for nr in nrs:
        if nr % 2 == 0:
            print(nr)


print_even(range(1, 11))

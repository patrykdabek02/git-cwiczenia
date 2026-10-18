# Zadanie 4: wyswietl co drugi element
def print_every_second(nrs):
    for i in range(0, len(nrs), 2):
        print(nrs[i])


print_every_second(range(1, 11))

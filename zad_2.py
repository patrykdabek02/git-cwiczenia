# Zadanie 2: pomnoz kazdy element listy przez 2 i zwroc nowa liste


# Wersja 1: petla for
def double_for(numbers):
    doubled = []
    for number in numbers:
        doubled.append(number * 2)
    return doubled


# Wersja 2: lista skladana
def double_comp(numbers):
    return [number * 2 for number in numbers]


numbers = [1, 2, 3, 4, 5]
print(double_for(numbers))
print(double_comp(numbers))

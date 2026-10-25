def czyZawiera(x: list[int], z: int) -> bool:
    return z in x


x = list(range(1, 10))
print(czyZawiera(x, 7))
print(czyZawiera(x, 15))

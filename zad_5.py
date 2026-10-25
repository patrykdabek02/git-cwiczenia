def czyZawiera(x: list, z: int) -> bool:
    return z in x


x = range(1, 10)
z = 7
print(czyZawiera(x, z))

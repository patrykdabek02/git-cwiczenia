def unique_cube_merge(a:list[int],b:list[int])->list[int]:
    c = a + b
    c=list(set(c))
    c=[x**3 for x in c]
    return c
a = [1,2,3,4,5]
b = [3,4,5,6,7]
c = unique_cube_merge(a, b)
print(c)
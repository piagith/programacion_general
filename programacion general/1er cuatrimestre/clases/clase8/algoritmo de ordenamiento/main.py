#bubble sort


def ord_burbujas(array):
    longitud = len(array)

    for i in range (longitud):
        for j in range(longitud - 1):
            print (array [i], array [j])


array = [8, 3, 1, 19, 14]
ord_burbujas(array)
print(array)

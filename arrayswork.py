import random


class Array:
    def ranarr(something,  count):
        arr = []
        for i in range(int(count)):
            arr.append(random.randint(10, 100))
        return arr;

    def rarmatrix(self, countrow, countcol):
        row = []
        collumn = []
        for i in range(int(countrow)):
            for j in range(int(countcol)):
                row.append(random.randint(0, 1000))

            collumn.append(row)

        return collumn

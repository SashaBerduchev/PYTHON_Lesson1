from math import factorial


class Factorial:

    def calFac(data, num):
        factorial = 1
        n = num

        for i in range(2, int(n) + 1):
            factorial *= i

        return factorial

    def calFacmath(data, num):
        res = factorial(int(num))
        return  res
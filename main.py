# This is a sample Python script.
import array

from Database import MSSQLConn
from MathWork.Factorial import Factorial
from arrayswork import Array


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

conn = MSSQLConn.MSSQLConnect()
name = input("Enter name: ")
print('Hellow ' + name)
lastname = input("Enter your family: ")
age = input('Enter your age: ')
Email = input("Enteryou email: ")
conn.setUser(name, lastname, age, Email)



conn.setName(name)


arrcount = input('Enter lengyh: ')
arrays = Array()
print("You put: " + arrcount);
arrres = arrays.ranarr(arrcount)
print(arrres)
print(len(arrres))
conn.setArray(name, lastname, Email, arrres)
col = input("Enter column: ")
row = input("Enter row: ")
matrix = arrays.rarmatrix(row, col)
print(matrix)
conn.setMatrix(name, col, row, matrix)
fac = input('Enter fac calc')
faccalc = Factorial()
res = faccalc.calFac(fac)
resmath = faccalc.calFacmath(fac)
print(res)
print(resmath)
conn.setFact(name, res)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

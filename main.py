# This is a sample Python script.
import array

from arrayswork import Array


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
name = input("Enter name: ")
print('Hellow ' + name)
arrcount = input('Enter lengyh: ')
arrays = Array()
print("You put: " + arrcount);
arrres = arrays.ranarr(arrcount)
print(arrres)

col = input("Enter column: ")
row = input("Enter row: ")
matrix = arrays.rarmatrix(row, col)
print(matrix)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
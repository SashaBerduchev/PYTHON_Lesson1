import pyodbc as pyodbc

class MSSQLConnect:


    def setName(self, Name):
        server = 'ALEXANDER'
        database = 'PYTHONLesson1'
        username = 'myusername'
        password = 'mypassword'
        cnxn = pyodbc.connect(
            'Driver={SQL Server};Server=' + server + ';Port=1433;Database=' + database + ';trusted_connection=yes')
        cursor = cnxn.cursor()
        print('conn_start')

        count = cursor.execute("""
        INSERT INTO Names (Name) 
        VALUES (?)""", Name).rowcount
        cnxn.commit()
        print('Rows inserted: ' + str(count))


    def setArray(self,Name, arr):
        server = 'ALEXANDER'
        database = 'PYTHONLesson1'
        username = 'myusername'
        password = 'mypassword'
        cnxn = pyodbc.connect(
            'Driver={SQL Server};Server=' + server + ';Port=1433;Database=' + database + ';trusted_connection=yes')
        cursor = cnxn.cursor()
        print('conn_start')

        for i in range(len(arr)):
            count = cursor.execute("""
            INSERT INTO Array (Name, ArrElem) 
            VALUES (?, ?)""", Name, arr[i]).rowcount
            print('Rows inserted: ' + str(count))
        cnxn.commit()





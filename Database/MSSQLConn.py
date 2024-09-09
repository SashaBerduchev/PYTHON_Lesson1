import pyodbc as pyodbc

class MSSQLConnect:

     
    def setUser(self, Name, LastName, Age, Email):
        server = 'ALEXANDER'
        database = 'PYTHONLesson1'
        username = 'myusername'
        password = 'mypassword'
        cnxn = pyodbc.connect(
            'Driver={SQL Server};Server=' + server + ';Port=1433;Database=' + database + ';trusted_connection=yes')
        cursor = cnxn.cursor()
        print('conn_start')

        count = cursor.execute("""
        INSERT INTO Users (Name, Sername, Age, Email)
        VALUES (?,?,?,?)""", Name, LastName, Age, Email).rowcount;
        print('Rows inserted: ' + str(count))
        cursor.commit()


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


    def setArray(self,Name, Sername, Email, arr):
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
            INSERT INTO Array (Name, ArrElem, Sername, Email) 
            VALUES (?, ?, ?, ?)""", Name, arr[i], Sername, Email).rowcount
            print('Rows inserted: ' + str(count))
        cnxn.commit()

    def setMatrix(self, Name, Sername, Email, col, row, matrix):
        server = 'ALEXANDER'
        database = 'PYTHONLesson1'
        username = 'sa'
        password = 'Sasha24'
        cnxn = pyodbc.connect(
            'Driver={SQL Server};Server=' + server + ';Port=1433;Database=' + database + ';trusted_connection=yes')
        cursor = cnxn.cursor()
        print('conn_start')

        for i in range(int(row)):
            for j in range(0, int(col)):
                count = cursor.execute("""
                    INSERT INTO Matrix (Name, ArrElem,Sername, Email) 
                    VALUES (?, ?, ?, ?)""", Name, float(matrix[i][j]), Sername, Email).rowcount
                print('Rows inserted: ' + str(count))
        cnxn.commit()




    def setFact(self, Name, fac):
        server = 'ALEXANDER'
        database = 'PYTHONLesson1'
        username = 'myusername'
        password = 'mypassword'
        cnxn = pyodbc.connect(
            'Driver={SQL Server};Server=' + server + ';Port=1433;Database=' + database + ';trusted_connection=yes')
        cursor = cnxn.cursor()
        print('conn_start')

        count = cursor.execute("""
        INSERT INTO Factorial (Name, Factorial) 
        VALUES (?, ?)""", Name, float(fac)).rowcount
        cnxn.commit()
        print('Rows inserted: ' + str(count))


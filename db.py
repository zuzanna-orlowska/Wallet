import sqlite3



def dbInit():
    global con
    global cur
    con = sqlite3.connect('wallet.db')
    cur = con.cursor()

def dbCreateTables():
    cur.execute("""CREATE TABLE Kategoria(
        ID integer primary key AUTOINCREMENT,
        Nazwa text)""")

    cur.execute("""CREATE TABLE Wydatki(
        ID integer primary key AUTOINCREMENT,
        Nazwa text,
        Kwota real,
        Kat_ID integer,
        Data text,
        foreign key(Kat_ID) references Kategoria(ID))""")

    cur.execute("""CREATE TABLE Budzet(
        ID integer primary key AUTOINCREMENT,
        Kat_ID integer,
        Kwota real,
        Data text,
        foreign key(Kat_ID) references Kategoria(ID))""")

def dbInitInsert():
    tasks = [("Opłaty konieczne",), ("Oszczędności",), ("Przyjemności",), ("Hobby",), ("Inwestycje",), ("Dla innych",)]
    sql = '''insert into Kategoria (Nazwa) values(?)'''

    for task in tasks:
        cur.execute(sql, task)
    con.commit()

def dbIncomeSplit(income):
    distributionPercentage = [0.35, 0.15, 0.3, 0.05, 0.1, 0.05]
    distributedIncome = []

    for item in distributionPercentage:
        distributedIncome.append(round(income*item, 2))


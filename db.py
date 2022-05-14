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

def dbTableInsert():
    task = [("Opłaty konieczne")]
    sql = '''insert into Kategoria (Nazwa)
        values(?)'''
    cur.execute(sql, task)
    con.commit()

    task2 = [("Oszczędności")]
    sql = '''insert into Kategoria (Nazwa)
            values(?)'''
    cur.execute(sql, task2)
    con.commit()
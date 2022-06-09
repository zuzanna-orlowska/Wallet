import sqlite3
from datetime import date
import config


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
    sql = '''insert into Kategoria (Nazwa) values(?)'''

    for name in config.categoryNames:
        cur.execute(sql, name)
    con.commit()

def dbIncomeSplit(income):
    distributionPercentage = [0.35, 0.15, 0.3, 0.05, 0.1, 0.05]
    distributedIncome = []

    for index, item in enumerate(distributionPercentage):
        distributedIncome.append([index+1, round(income*item, 2), str(date.today())])

    dbInsertBudget(distributedIncome)

def dbInsertBudget(distributedIncomes):
    sql = '''insert into Budzet (Kat_ID, Kwota, Data) values(?, ?, ?)'''

    for income in distributedIncomes:
        cur.execute(sql, income)
    con.commit()


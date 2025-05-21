import pandas as pd
import psycopg2

connection = psycopg2.connect(
host='loki',
port='5433',
user='postgres',
password='PG_root23@',
database='programmiersprachen'
)

# crs= connection.cursor()
# crs.execute('SELECT * FROM student')
# dta = crs.fetchall()
# print(dta)

class Student:
    

    def __init__(self, connection):
        self.con = connection
        self.con.autocommit = True
        self.crs = self.con.cursor()

    def insert(self, first:str, last:str, dob:str):
        qry = f"INSERT INTO student(FIRST, LAST, dob)"
        qry += f" VALUES ('{first}', '{last}', '{dob}')"
        qry += f" RETURNING (id)"
        self.crs.execute(qry)
        return self.crs.fetchone()[0]
    
    def select(self, where:str = ''):
        qry = f"SELECT * from student"
        self.crs.execute(qry)
        return self.crs.fetchall()
    
    def delete(self, id: int):
        qry = f"DELETE  from student WHERE id={id}"
        self.crs.execute(qry)
        return self.crs
    
s = Student(connection=connection)
# f = s.insert(first='Lilly', last='Tigger', dob='1903-01-02')
print(s.select())
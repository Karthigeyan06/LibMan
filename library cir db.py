import sqlite3
con=sqlite3.connect("library.db")
cr=con.cursor()
com="""CREATE TABLE CIRCBR(
SNO VARCHAR NOT NULL,
ROLLNO VARCHAR,
RDATE VARCHAR,
BDATE VARCHAR
);"""

cr.execute(com)
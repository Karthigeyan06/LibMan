import sqlite3
con=sqlite3.connect("library.db")
cr=con.cursor()
com="""CREATE TABLE BOOKMG(
SNO VARCHAR NOT NULL UNIQUE,
NAME CHAR,
AUTHOR CHAR,
QUANTITY INTEGER,
JOURNAL CHAR
);"""

cr.execute(com)
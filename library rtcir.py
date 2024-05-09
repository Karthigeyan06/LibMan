import sqlite3
con=sqlite3.connect("library.db")
cr=con.cursor()
com="""CREATE TABLE CIRCRT(
SNO VARCHAR NOT NULL,
ROLLNO VARCHAR,
RDATE VARCHAR,
DATE VARCHAR
);"""

cr.execute(com)
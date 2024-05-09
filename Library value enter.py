import sqlite3
con=sqlite3.connect("library.db")
cr=con.cursor()
cr.execute("INSERT INTO BOOKMG VALUES('LB1004', 'ELECTROMAGNETIC FIELDS', 'MEENAKUMARI',3 ,'EE')")

con.commit()
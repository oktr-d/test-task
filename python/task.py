import sqlite3
import random

connection = sqlite3.connect('example.db')
cursor = connection.cursor()
#Creating tables Table1 and Table2
#Structure: ID, number1, number2
cursor.execute('DROP TABLE IF EXISTS table1')
cursor.execute('CREATE TABLE table1(id INTEGER PRIMARY KEY, number1 INTEGER, number2 INTEGER)')
cursor.execute('DROP TABLE IF EXISTS table2')
cursor.execute('CREATE TABLE table2(id INTEGER PRIMARY KEY, number1 INTEGER, number2 INTEGER)')

min_num_rows = 3;
max_num_rows = 7;
max_number = 9;

#Filling in the tables randomly
num_rows = random.randint(min_num_rows, max_num_rows)
for i in xrange(0, num_rows):
    cursor.execute("INSERT INTO table1(number1, number2) VALUES (?, ?)", (random.randint(1, max_number), random.randint(1, max_number)))
    
num_rows = random.randint(min_num_rows, max_num_rows)
for i in xrange(0, num_rows):
    cursor.execute("INSERT INTO table2(number1, number2) VALUES (?, ?)", (random.randint(1, max_number), random.randint(1, max_number)))

connection.commit()


cursor.execute('SELECT * FROM table1')
print "Table1:"
for row in cursor.fetchall():
    print "ID: %d Numbers: (%d, %d)" % (row[0], row[1], row[2])

cursor.execute('SELECT * FROM table2')
print "\nTable2:"
for row in cursor.fetchall():
    print "ID: %d Numbers: (%d, %d)" % (row[0], row[1], row[2])

print "\nTable comparison:"

cursor.execute('SELECT number1, number2 FROM table1 INTERSECT SELECT number1, number2 FROM table2')
print "Table1 INTERSECT Table2:"
for row in cursor.fetchall():
    print "Numbers: (%d, %d)" % (row[0], row[1])
    
cursor.execute('SELECT number1, number2 FROM table1 EXCEPT SELECT number1, number2 FROM table2')
print "\nTable1 EXCEPT Table2:"
for row in cursor.fetchall():
    print "Numbers: (%d, %d)" % (row[0], row[1])
    
cursor.execute('SELECT number1, number2 FROM table2 EXCEPT SELECT number1, number2 FROM table1')
print "\nTable2 EXCEPT Table1:"
for row in cursor.fetchall():
    print "Numbers: (%d, %d)" % (row[0], row[1])        
    

#appending Table2 with Table1 data 
cursor.execute('INSERT INTO table2(number1, number2) SELECT number1, number2 FROM table1 EXCEPT SELECT number1, number2 FROM table2')
connection.commit()
print "\nUpdated Table2:"
cursor.execute('SELECT * FROM table2')
for row in cursor.fetchall():
    print "ID: %d Numbers: (%d, %d)" % (row[0], row[1], row[2])
    

connection.close()     
print "\nProcessed Successfully."
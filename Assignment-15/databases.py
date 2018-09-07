#Q.1- Write a python script to create a databse of students named Students.

import sqlite3
try:
    cons=sqlite3.connect('Students.db')
    print(cons)
except sqlite3.DatabaseError as e:
    if cons:
        print('Problem Occured') 
finally:
    cons.close()
    print('DATABASE CREATED')

#Q.2- Take students name and marks(between 0-100) as input from user 10 times using loops.
info=[]
for x in range(1,11):
   # print('Details of student {}'.format(x))
    info.append((input('Name:'),int(input('Marks:'))))

#Q.3- Add these values in two columns named "Name" and "Marks" with the appropriate data type.
                #Creating Table
import sqlite3
try:
    cons=sqlite3.connect('Students.db')
    cursor=cons.cursor()
    query='create table Students(name varchar(15),marks number(3) check (marks>=0 and marks<=100))'
    cursor.execute(query)
    print('TABLE CREATED')
    cons.commit()
except sqlite3.DatabaseError as e:
    if cons:
        cons.rollback()
        print('Problem Occured')
finally:
    if cursor:
        cursor.close()
    if cons:
        cons.close()
    print('DONE!')
                #Inserting Values
import sqlite3
try:
    cons=sqlite3.connect('Students.db')
    cursor=cons.cursor()
    query='insert into Students (name,marks) values (?,?)'
    cursor.executemany(query,info)
    cons.commit()
    print('VALUES INSERTED')
    quer="select * from Students"
    cursor.execute(quer)
    data=cursor.fetchall()
    for row in data:
        print("NAME:{} , MARKS:{}" .format(row[0],row[1]))
    cons.commit()
except sqlite3.DatabaseError as e:
    if cons:
        cons.rollback()
        print('Problem Occured')
finally:
    if cursor:
        cursor.close()
    if cons:
        cons.close()
    print('3rd DONE!')


#Q.4- Print the names of all the students who scored more than 80 marks.    
import sqlite3
try:
    cons=sqlite3.connect('Students.db')
    cursor=cons.cursor()
    query="select * from Students where marks > 80"
    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print("NAME:{} , MARKS:{}" .format(row[0],row[1]))
    cons.commit()
except sqlite3.DatabaseError as e:
    if cons:
        cons.rollback()
        print("Problem occured:",e)
finally:
    if cursor:
        cursor.close()
    if cons:
        cons.close()
    print("ALL DONE!")




















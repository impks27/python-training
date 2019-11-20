#DB connection. Setip xampp by downoading and launching mysql service
#mysql -u root
#create database
#use database

import pymysql
x=pymysql.connect('localhost','root','','wells')
y=x.cursor()
#s='create table xyz (eno integer, ename character(10))'
#y.execute(s)

#s='insert into xyz values(111, "pks")'
s='select * from xyz'
y.execute(s)
#x.commit()
p=y.fetchall()
for m in p:
    print (m)

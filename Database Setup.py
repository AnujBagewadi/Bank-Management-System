#To import MySql connector
import mysql.connector as a
con = a.connect(host='localhost',user='root',passwd='12345')

#To Create Database "Bank" and Table Account and Amount
c=con.cursor()
c.execute('drop database if exists bank')
c.execute('create database bank')
c.execute('use bank')
c.execute('''
create table account
(Name varchar(50) not null,
Account_no varchar(12) not null primary key,
Date_of_birth DATE not null,
Phone_no char(10) not null unique,
Address varchar(50) not null,
Email varchar(50) not null unique,
Opening_Balance double(9,2))''')

c.execute('''
create table amount
(Name varchar(50) not null,
Account_no varchar(12) not null,
Balance double(9,2) not null)''')
con.commit()
print('='*10,'DATABASE CREATED SUCCESSFULLY!!!','='*10,'\n')





#Import MySql connector
import mysql.connector as a
con = a.connect(host='localhost',user='root',passwd='12345',database= 'bank')

#To generate account number
list_acno=[]
def gen_acno():
    import random
    global list_acno
    s=''
    for i in range(10):
        x=str(random.randint(0,9))
        s+=x
    if s in list_acno:
        gen_acno()
    else:
        list_acno.append(s)
        return(s)


#To create a new account
def openacc():
    n=input('Enter Name : ')
    n=n.title()
    db= input('Enter Date Of Birth (YYYY/MM/DD) : ')
    p=int(input('Enter Phone Number : '))
    ad=input('Enter Full Address : ')
    e=input('Enter Email : ')
    ob=int(input('Enter Opening Balance : '))
    ac= gen_acno()
    data1=(n,ac,db,p,ad,e,ob)
    data2=(n,ac,ob)
    sql1='insert into account values(%s,%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    c= con.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    con.commit()
    print('\n'*2)
    print('*'*10,'Account created successfully!!!','*'*10,'\n'*2)
    print(' '*5,'Your account no. :',ac)
    main()

#To deposit money into existing account
def depoamo():
    am=int(input('Enter amount : '))
    ac=input('Enter account no. : ')
    a='select balance from amount where Account_no=%s'
    data = (ac,)
    c= con.cursor()
    c.execute(a,data)
    myresult= c.fetchone()
    tam= myresult[0] + am
    sql='update amount set balance = %s where Account_no =%s'
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print('Amount deposited successfully!!!')
    print('Your current balance is :',tam)
    main()

#To withdraw money from existing account
def witham():
    am=int(input('Enter amount : '))
    ac= input('Enter account no. : ')
    a='select balance from amount where Account_no=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    tam=myresult[0]-am
    sql='update amount set balance = %s where Account_no=%s'
    d=(tam,ac)
    c.execute(sql,d)
    con.commit()
    print('Amount withdrawn successfully!!!')
    print('Your current balance is :',tam)
    main()

#To check current balance from an existing account
def balance():
    ac=input('Enter account no : ')
    a='select balance from amount where Account_no =%s'
    data = (ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print('Your current balance is :',myresult[0])
    main()

#To display all the details of an account
def dispacc():
    ac=input('Enter account no : ')
    a='select* from account where Account_no=%s'
    data=(ac,)
    c=con.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print('='*10,'Account details','='*10,'\n')
    print('Name            :',myresult[0])
    print('Account no      :',myresult[1])
    print('Date of birth   :',myresult[2])
    print('Phone no        :',myresult[3])
    print('Address         :',myresult[4])
    print('Email           :',myresult[5])
    print('Opening Balance :',myresult[6])
    main()

#To close an account
def closeac():
    ac=input('Enter account no : ')
    sql1='delete from account where Account_no=%s'
    sql2='delete from amount where Account_no =%s'
    data=(ac,)
    c=con.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    con.commit()
    print('Your account has been closeded!!!')
    main()


#Main Menu
def main():
    print('\n','='*18,'DIGITO','='*18)
    print('''
            WELCOME TO DIGITO
    -------------------------------------        
    WHICH TASK WOULD YOU LIKE TO PERFORM?
    1. OPEN NEW ACCOUNT
    2. DEPOSIT AMOUNT
    3. WITHDRAW AMOUNT
    4. BALANCE ENQUIRY
    5. DISPLAY CUSTOMER DETAILS
    6. CLOSE AN ACCOUNT
    7. EXIT DIGITO
    ''')
    choice=input('Enter Task Number : ')
    print('\n','='*60)
    while True:
        if choice=='1':
            openacc()
        elif choice=='2':
            depoamo()
        elif choice=='3':
            witham()
        elif choice=='4':
            balance()
        elif choice=='5':
            dispacc()
        elif choice=='6':
            closeac()
        elif choice=='7':
            print('\n')
            print('>'*5,'DIGITO SHUTDOWN SUCCESSFULLY','<'*5,'\n')
            break
        else:
            print('Wrong choice!!!')
            main()
main()

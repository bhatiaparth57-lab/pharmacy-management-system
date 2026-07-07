import mysql.connector as m
con=m.connect(host='localhost',user='root',password='parth0011',database='pharmacyy')
c=con.cursor()
import time
import random as rd

# to insert a medicine
def insert_med():
    mID=int(input("Enter medicine id= "))
    n=input("enter medicine name: ")
    mf=input("enter manufacturer: ")
    dm=input("enter date of manufacture: ")
    de=input("enter date of expiry: ")
    qnt=input("enter quantity: ")
    price=input("enter price: ")
    q="insert into medical values({},'{}','{}','{}','{}',{},{})".format(mID,n,mf,dm,de,qnt,price)
    c.execute(q)
    con.commit()
    print("....medicine inserted....")



#to display medicine
def show_medicine():
    q="select * from medical"
    c.execute(q)
    r=c.fetchall()
    for i in r:
        print(i)

#to search a medicine

def search_med():
    med=int(input("medicine id:"))
    c.execute("select * from medical where m_id={}".format(med))
    k=c.fetchone()
    if k == None:
        print("No medicine available with this ID")
    else:
        t=PrettyTable(["m_id","m_name","m_manufacturer","m_mdate","m_expiry","m_qnt","m_price"])
        t.add_row([k[0],k[1],k[2],k[3],k[4],k[5],k[6]])
        print(t)
    
#to restock medicine

def restock():
    med_id=int(input("enter medicine id:"))
    qty=int(input("enter quantity to add:"))
    q="update medical set m_qnt= m_qnt+ %s where m_id=%s"
    d=(qty,med_id)
    c=con.cursor()
    c.execute(q,d)
    print("\n")
    print("+++"*10)
    print("medicine restocked....")
    print("+++"*10)
    print("\n")
    con.commit()
    
    
#to delete a medicine
def delmed():
    md=int(input("enter medicine id:"))
    c=con.cursor()
    q="delete from medical where m_id='%s'"% md
    c.execute(q)
    print("\nMedicine deleted........\n")
    print("----"*15)
    print("\n\n")
    con.commit()

#function for billing
def bill():
    bn=input("Enter bill no.: ")
    n=input("Enter customer's name: ")
    b=input("enter bill date(yyyy-mm-dd):")
    am=0
    med=""
    c=con.cursor()
    while True:
        mid=input("enter medicine id:")
        q="select * from medical where m_id='%s'"%mid
        c.execute(q)
        res=c.fetchone()
        if res==None:
            print("\nNo medicine available with this ID\n")
            print("$$$"*15)
        else:
            price=int(res[-2])
            med+=res[1]+""
            print("price of medicine is :",price)
            qty=int(input("enter the quantity to be purchased:"))
            bill=price*qty
            am+=bill
            print("amount for medicine:",am)
            ans=input("are there more medicine to be purchased:")
            if ans.lower()=="no":
                print("calculating your bill:")
                break
    print("total bill amount is:",am)
    q="insert into bill1 values(%s,%s,%s,%s,%s)"
    data=(bn,n,med,am,b)
    c.execute(q,data)
    con.commit()
    print(" ...bill generated.... \n\n")

while True:
    print("****"*15)
    print("\t\t\tDMS MEDICAL STORE")
    print("****"*15)
    print("\n")
    print("Press 1 - Add New medicine")
    print("Press 2 - Restock a medicine")
    print("Press 3 - Show all medicines")
    print("Press 4 - Delete a medicine")
    print("Press 5 - Billing")
    print("Press 6 - to exit")
    print("\n")
    choice=int(input("Enter your choice: "))
    if choice==1:
        insert_med()
    elif choice==2:
        restock()
    elif choice==3:
        show_medicine()
    elif choice==4:
        delmed()
    elif choice==5:
        bill()
    elif choice==6:
        print("\t\t Thanks for visiting!!")
        print("\t\t Have a good day!!!\n")
        print("-----"*10)
    else:
        print("Wrong choice")

            

    







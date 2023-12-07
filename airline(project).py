import os
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root", passwd="tcdav", database="airline")
mycursor=mydb.cursor()

def menu():
    
    
    print("****** Welcome to Airways Ticket Booking ********")
    print("-------------------------------------------------")
    print("         1: Create Data Table")
    print("         2: Book your Ticket")
    print("         3: Show all Tickets ")
    print("         4: Search Ticket")
    print("         5: Update Ticket")
    print("         6: Cancel Ticket")
    print("         7: Exit")
    print("-------------------------------------------------")
    print()


#              Create Data Table Function               
#-------------------------------------------------------
def CreateTable():
    
    try:
        
        
        mycursor.execute("CREATE TABLE Airways(\
                        ticket_no INT(10)  PRIMARY KEY,\
                        passenger_id INT(5),\
                        p_name VARCHAR(30),\
                        father_name VARCHAR(30),\
                        gender VARCHAR(1),\
                        dob DATE,\
                        address VARCHAR(40),\
                        doj DATE,\
                        source VARCHAR(10),\
                        destination VARCHAR(12),\
                        dep_time TIME,\
                        flight_name VARCHAR(25),\
                        class VARCHAR(20),\
                        amt float(10));")
        print("Table created successfully")
    except:
        
        

        print("Table Already Created.")
        r=input("Press any key to continue.....")


#                 Ticket Function               
#-------------------------------------------------------    
def ticket():
    
    
    

    print()
    print("----------------Data Entry----------------")

    
    
    tn=int(input("Enter Ticket Number")) 
    pid=int(input("Enter Passenger ID? "))
    pn=input("Enter Passenger Name ? ")
    fn=input("Enter Passenger's Father Name? ")
    gn=input("Enter Gender? ")
    dob=input("Enter DOB? ")
    add=input("Enter Address? ")
    doj=input("Enter DOJ?")
    sc=input("Enter Source?")
    des=input("Enter Destination?")
    dt=input("Enter Departure Time?")
    fln=input("Enter Flight Name?")
    cl=input("Enter Class?")
    amount=float(input("Enter Flight Charges?"))
    mycursor = mydb.cursor()
    sql =   "INSERT INTO Airways(ticket_no,passenger_id, p_name,father_name,gender,dob,address,doj,source,destination,dep_time\
    ,flight_name,class,amt)\
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    val = (tn,pid,pn,fn,gn,dob,add,doj,sc,des,dt,fln,cl,amount)
    mycursor.execute(sql, val)

    """mydb.commit()required to make the changes,
          otherwise no changes are made to the table."""

    mydb.commit()
    print(mycursor.rowcount, "Ticket booked successfully.")
    print()
    choice=input("Enter x or X for more Ticket? ")
  

#             Show All Ticket Function               
#-------------------------------------------------------   
def ShowAll():
    

    sql="select * from Airways  "
    mycursor.execute(sql)

    print()
    print()
    print("All Tickets")
    print()
    for row in mycursor:
        
        print(row)
    print()
    print(mycursor.rowcount, "recods found.")

    print()
    r=input("Press any key to continue.....")
   


#          Ticket Wise Search Function               
#------------------------------------------------------
def Searchticket():
    


    tn=input("Enter Ticket Number? ")
    sql = "SELECT * FROM Airways WHERE ticket_no=%s;"  
    val=(tn,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    if myresult != "":
        
        for x in myresult:
            print(x)
    else:
        
        print("Failed to get record from Server")

    r=input("Press any key to continue.....")
   

#               Update  Ticket Function               
#-------------------------------------------------------
def Updateticket():

    tn=int(input("Enter Ticket Number to be modified? "))
    doj=input("Enter DOJ")
    des=input("Enter Destination")
    pn=input("Enter name")
    cl=input("Enter Class")

    str="UPDATE Airways SET doj='{}',destination='{}',class='{}',p_name='{}' where ticket_no={}".format(doj,des,cl,pn,tn) 

    mycursor.execute(str)
    mydb.commit()    

    print()
    print(mycursor.rowcount, "record updated successfully.")
    print()
    r=input("Press any key to continue.....")

    
#               Cancel Ticket Function               
#-------------------------------------------------------
def Cancelticket():
    tn=int(input("Enter Ticket number to cancel ticket? "))
    str = "DELETE FROM Airways WHERE ticket_no={}".format(tn)
    mycursor.execute(str)

    print(mycursor.rowcount, "record(s) deleted")
    mydb.commit()

    print()
    r=input("Press any key to continue.....")

def clear():
    os.system('cls')
    menu()
programme='enter'    
while programme=="enter":
    
    menu()
    choice = int(input("     Please enter your choice: "))
    if choice == 1 :
           
        CreateTable()
        os.system('cls')
    elif choice == 2:
        ticket()
        os.system('cls')
        
    elif choice == 3:
        ShowAll()
        os.system('cls')
    elif choice == 4:
        Searchticket()
        os.system('cls')
    elif choice == 5:
        Updateticket()
        os.system('cls')
    elif choice == 6:
        Cancelticket()
        os.system('cls')
    elif choice == 7:
        mydb.close()
        os.system('cls')
        programme='exit'

    else:
        print("You must only select either 1 to 7")
        print("Please try again")
         


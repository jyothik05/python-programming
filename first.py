username=input("enter username:")
password=input("enter password:")
if(username=="admin"):
    if(password=="password"):
        print("login successfully")
        from_=input("enter the city:")
        to=input("enter the city:")
        sleeper=1
        ac=2
        luxury=3
        classes=int(input("enter the type of class:"))
        tickets=int(input("enter the no.of tickets:"))
        if(classes==1):
            if(tickets<=45):
                print("book the ticket")
            else:
                print("no seats are available")
        else:
            if(classes==2):
                if(tickets<=45):
                    print("book the ticket")
                else:
                    print("no seats are available")
                    if(classes==3):
                        if(tickets<=45):
                            print("book the tickets")
                        else:
                            print("no seats are available")
                    else:
                        print("no seats are available")
        for i in range(1,tickets+1):
            name=input("enter your name:")
            age=input("enter your age:")
            phno=input("enter your phone number:")
            seatno=input("enter the seat number:")
        print("proceed with the payment")
        payment=input(("do you want to pay?"))
        if(payment=="yes"):
            print("payment succesful!")
            print("your ticket is booked")
        else:
            print("payment failed")
        print("Thank you for using TSRTC")
    else:
        print("incorrect password")
else:
    if(username=="guest"):
        if(password=="password"):
            print("login successfully")
        else:
            print("incorrect password")
    else:
        print("unknown user")
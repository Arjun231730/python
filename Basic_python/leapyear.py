a=int(input("enter a year"))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("its a leap year")
        
    else:
        print("is a leap year")
else:
    print("not leap year")
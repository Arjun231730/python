a=int(input("what was the total bill?"))
b=int(input("how much tip percent u would like to give? 10,12,15"))
c=int(input("how much people u would like to split"))
tip=(b/100)*a
each=tip/c
print(f"each person should pay: ${round(each,2)}")
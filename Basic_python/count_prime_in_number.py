number=int(input("enter a number"))
count=0
prime=[int(d) for d in str(number)]
for i in prime:
    if i%2==1:
        count+=1
    else:
        count+=0
print(f"the number of prime digit are: {count}")
number=int(input("enter a number"))
even=[int(d) for d in str(number)if int(d)%2==0]
print(f"sum of even digit is: {sum(even)}")
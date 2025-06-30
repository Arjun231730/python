number=int(input("enter a number"))
odd=[int(d) for d in str(number)if int(d)%2==1]
print(f"sum of odd digit is: {sum(odd)}")
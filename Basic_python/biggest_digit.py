number=int(input("enter the number"))
biggest=0
while number > 0:
    digit=number%10
    if digit > biggest:
        biggest=digit
    number=number//10
print(biggest)                                                     
    
m=int(input("give the starting range"))
n=int(input("give the ending range"))
prime_number=[]
for i in range(m,n):
    for j in range(2,i):
        if i%j==0:
            break
        else:
            prime_number.append(i)
prime_number=sorted(prime_number)
    
       
print(set(prime_number))
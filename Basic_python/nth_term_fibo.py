n=int(input("enter the nth term"))
fib_list=[]
for i in range(1,n+1):
    if i==1 or i==2:
        fib_list.append(i)
    else:
        fib_list.append(fib_list[i-2]+fib_list[i-3])
print(fib_list)

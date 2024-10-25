n = 5
fibunacci = [0,1]
print(fibunacci[-2], ',', fibunacci[-1])
for _ in range (0,n-2):
    fib_number = fibunacci[-2]+fibunacci[-1]
    fibunacci.append(fib_number)
    print(fib_number,',', end ='')


a=0
b=1
fib=0
print(a)
print(b)
for _ in range (0,n-2):
    fib = a+b
    print(fib)
    a=b
    b=fib
    #prueba fubu
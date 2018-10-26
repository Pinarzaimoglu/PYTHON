fib1, fib2= 1,1

print(fib1)
print(fib2)

i=2

while i<=50 :
    fib1, fib2 = fib2, fib1+fib2
    print(fib2)
    i+=1


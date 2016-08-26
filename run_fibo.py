import fibo

i=0
while i < 40:
    print(str(i) + ": " + str(fibo.fib_rec(i)))
    i=i+1
#fib(1000) #NameError: name 'fib' is not defined
#fibo.fib(1000)
#print(fib2(1000))

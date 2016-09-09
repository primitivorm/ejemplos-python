import dis

# Fibonacci numbers module
def fibo_rec(n):
    if n < 2:
        return n
    return fibo_rec(n-1) + fibo_rec(n-2)

#dis.dis(fibo_rec)
x=fibo_rec(2)
print(x)
    
#def fib(n):    # Fibonacci series up to n
#    a, b = 0, 1
#    while b < n:
#        print(b)
#        a, b = b, a+b
#
#def fib2(n):   # Fibonacci series up to n
#    result = []
#    a, b = 0, 1
#    while b < n:
#        result.append(b)
#        a, b = b, a+b
#    return result

#fib(1000)
#print(fib2(1000))

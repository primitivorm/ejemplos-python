import dis

def f(a, b):
    return a + b

dis.dis(f)
f(1, 2)
#x = 1
#y = 2
#z = x + y
#print z

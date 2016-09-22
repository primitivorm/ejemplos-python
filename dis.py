import dis

def f(a, b):
    return a + b

dis.dis(f)
c = f(1, 2)
print c

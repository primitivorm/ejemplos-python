import dis

def f(a, b):
    return a + b

dis.dis(f)
f(1, 2)

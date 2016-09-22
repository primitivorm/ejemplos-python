##Cualquier cadena distinta de vacia es considerada verdadero
#s = "null"
#if s:
#    print("es verdadero")
#else:
#    print("es falso")
#
##Cualquier numero distinto de 0 es verdadero
#n = -5
#if n:
#    print("es verdadero")
#else:
#    print("es falso")
#
##True o False
#b = True
#if b:
#    print("es verdadero")
#else:
#    print("es falso")
#
##Si la lista esta vacia en considerado falso
#l = [1,2,3]
#if l:
#    print("es verdadero")
#else:
#    print("es falso")
#
##Si el diccionario esta vacio en considerado falso
#d = {"key": "value"}
#if d:
#    print("es verdadero")
#else:
#    print("es falso")
#
##n = -"1"   #  File "data_types.py", line 36, in <module> n = -"1" TypeError: bad operand type for unary -: 'str'
##print(n) 
##r = 1+"2"  #File "data_types.py", line 39, in <module> r = 1+"2" TypeError: unsupported operand type(s) for +: 'int' and 'str'
##print(r) 

if "1" > 1:
    print("es mayor")
else:
    print("es menor o igual")

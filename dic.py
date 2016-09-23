dic = { "Chilindrina": "Maria Antonieta de las Nieves",
     "El chavo del 8": "Roberto Gomez Bolanios",
     "Tres patines": "Leopoldo Fernandez" }

print(dic)

#cambiando un valor
dic["Chilindrina"] = "Maria Antonieta"
print("")
print(dic)

dic["ch"] = "Maria Antonieta"
print("")
print(dic)

ch = dic["ch"]
print("")
print(ch)

#ch = dic["ch2"]
#print("")
#print(ch)

numeros = {}
i = 0
while i <= 1000000:
    llave = str(i)
    numeros[llave] = i
    i=i+1

print(numeros["1000000"])


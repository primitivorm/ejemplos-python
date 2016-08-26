i = 0
lista = []
while i < 1000000:
    #print str(i)
    lista.append(i)
    i = i + 1
print("longitud: " + str(len(lista)))
""" 5           0 BUILD_LIST               0
              3 STORE_NAME               0 (lista)

  6           6 LOAD_CONST               0 (0)
              9 STORE_NAME               1 (i)

  7          12 SETUP_LOOP              39 (to 54)
        >>   15 LOAD_NAME                1 (i)
             18 LOAD_CONST               1 (1000000)
             21 COMPARE_OP               0 (<)
             24 POP_JUMP_IF_FALSE       53

  9          27 LOAD_NAME                0 (lista)
             30 LOAD_ATTR                2 (append)
             33 LOAD_NAME                1 (i)
             36 CALL_FUNCTION            1
             39 POP_TOP             

 10          40 LOAD_NAME                1 (i)
             43 LOAD_CONST               2 (1)
             46 BINARY_ADD          
             47 STORE_NAME               1 (i)
             50 JUMP_ABSOLUTE           15
        >>   53 POP_BLOCK           

 12     >>   54 LOAD_CONST               3 ('longitud: ')
             57 LOAD_NAME                3 (str)
             60 LOAD_NAME                4 (len)
             63 LOAD_NAME                0 (lista)
             66 CALL_FUNCTION            1
             69 CALL_FUNCTION            1
             72 BINARY_ADD          
             73 PRINT_ITEM          
             74 PRINT_NEWLINE       
             75 LOAD_CONST               4 (None)
             78 RETURN_VALUE        """

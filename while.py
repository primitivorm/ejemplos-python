#i = 0
#while i < 10:
#    print i
#    i = i + 1
#
#  1           0 LOAD_CONST               0 (0)
#              3 STORE_NAME               0 (i)
#
#  2           6 SETUP_LOOP              31 (to 40)
#        >>    9 LOAD_NAME                0 (i)
#             12 LOAD_CONST               1 (10)
#             15 COMPARE_OP               0 (<)
#             18 POP_JUMP_IF_FALSE       39
#
#  3          21 LOAD_NAME                0 (i)
#             24 PRINT_ITEM          
#             25 PRINT_NEWLINE       
#
#  4          26 LOAD_NAME                0 (i)
#             29 LOAD_CONST               2 (1)
#             32 BINARY_ADD          
#             33 STORE_NAME               0 (i)
#             36 JUMP_ABSOLUTE            9
#        >>   39 POP_BLOCK           
#        >>   40 LOAD_CONST               3 (None)
#             43 RETURN_VALUE        

i=1
while i<=10:
    j=1
    while j<=10:
        print i*j
        j=j+1
    i=i+1


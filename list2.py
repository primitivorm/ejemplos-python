aList = [123, 'xyz', 'zara', 'abc'];
#aList.appends( 2009 );    #AttributeError: 'list' object has no attribute 'appends'
aList.append( 2009 );
aList[0] = 321
print "Updated List : ", aList
print aList[1]
aList.append(2009)

list1, list2, list4 = [123, 'xyz'], [456, 'abc'], ['123', 'xyz']
print cmp(list1, list2)
print cmp(list2, list1)
list3 = list2 + [786];
print cmp(list2, list3)
print cmp(list1, list4)
print cmp([2, 'xyz'], [True, 'xyz'])


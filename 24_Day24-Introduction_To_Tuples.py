tup = (1,5,6,544,54,64,44, "Green", True)
# tup[0] = 90
print(type(tup), tup)
print(len(tup), tup)
print(tup[0])
print(tup[-1])
print(tup[2])
# print(tup[34])

if 544 in tup:
    print("Yes 554 is present in this tuple")

tup2 = tup[1:4]
print(tup2)
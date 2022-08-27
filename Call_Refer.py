'''a = 10
b = 10
c = a

print ("A id location is:", id(a))
print ("B id location is:", id(b))
print ("C id location is:", id(c))


a = 10
b = 20
c = a

print ("A id location is:", id(a))
print ("B id location is:", id(b))
print ("C id location is:", id(c))'''


l = [2,3,4]
l2 = l

print ("L Id location is:", id(l))
print ("L2 Id location is:", id(l2))


l = [2,3,4]

l2 = l.copy()
print (l.sort(reverse=True))

print ("L Id location is:", id(l),l)
print ("L2 Id location is:", id(l2), l2)
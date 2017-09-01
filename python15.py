import random

a = []
for i in range (100) :
	a.append(random.randint(1,100))

print("Random numbers:")
for i in range (100) :
	print(str(a[i])+" ", end=' ')

print("\n\nAscending order:")
a.sort()
for i in range (100) :
        print(str(a[i])+" ", end=' ')

print("\n\nDescending order:")
a.sort(reverse=True)
for i in range (100) :
        print(str(a[i])+" ", end=' ')

print("\n")

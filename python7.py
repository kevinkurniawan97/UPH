x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
z = int(input("Please enter a third integer: "))
if y > x:
	if z > y:
		print(z, "is greatest.")
	else:
		print(y, "is greatest.")
else:
	if z > x:
		print(z, "is greatest.")
	else:
		print(x, "is greatest.")
print("Done.")

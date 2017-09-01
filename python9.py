age = int(input("Please enter your age:"))
member = True
if age <= 15:
	member = False
if age >= 18:
	member = False
if member:
	print("You can join")
else:
	print("You can't join")

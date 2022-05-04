# Calculates if you can get into the mesuem for free, with a discount or need to pay full price

age = int(input("Please enter your age: "))
day = input("Please enter the day: ")
day = day.upper()

if (day == "MONDAY") or (day == "TUESDAY") or (day == "WEDNESDAY") or (day == "THURSDAY") or (day == "FRIDAY") or (day == "SATURDAY") or (day == "SUNDAY"):
	if (age <= 5) or (age >= 95):
		print("You can get in for free!")
	elif (age >= 12) and (age <= 21):
		print("You get a student discount!")
	elif (day == "TUESDAY"):
		print("Because it's tuesday you get a student discount!")
	elif (day == "THURSDAY"):
		print("Because it's thursday you get a student discount!")
	else:
		print("You need to pay full price")
else:
	print("Thats not a real day")
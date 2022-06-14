# If else
num1 = int(input("Enter Score: "))

if num1 >= 90:
   grade = "A"
elif num1 >= 80:
   grade = "B+"
elif num1 >= 70:
   grade = "B"
elif num1 >= 60:
   grade = "C+"
elif num1 >= 50:
   grade = "C"
elif num1 >= 40:
   grade = "D"
else:
   grade = "E"

print("Grade: %s" % grade)
# Comparison Operations

num1 = input("First number: ")
num2 = input("\nSecond number: ")

sum1 = float(num1) < float(num2)
print("The sum of {0} < {1} = {2}" .format(num1, num2, sum1))

sum2 = float(num1) > float(num2)
print("The sum of {0} > {1} = {2}" .format(num1, num2, sum2))

sum3 = float(num1) == float(num2)
print("The sum of {0} == {1} = {2}" .format(num1, num2, sum3))

sum4 = float(num1) != float(num2)
print("The sum of {0} != {1} = {2}" .format(num1, num2, sum4))

sum5 = float(num1) >= float(num2)
print("The sum of {0} >= {1} = {2}" .format(num1, num2, sum5))

sum6 = float(num1) <= float(num2)
print("The sum of {0} <= {1} = {2}" .format(num1, num2, sum6))
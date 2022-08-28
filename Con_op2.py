salary = 5000

if salary > 5000:
	salary = salary + 500
	print("Revised Salary is:", salary)
elif salary < 5000:
	salary = salary + 700
	print("Revised Salary is:", salary)
elif salary == 5000:
	salary = salary + 1000
	print("Revised Salary is:", salary)
else:
	print("Salary Value is invalid")
    
n = 55

if n == 25:
    print("If Block")
elif n != 55:
    print("First Elif")
elif n > 25:
    print("Second Elif")
elif n < 14:
    print("Third Elif")
elif n >= 5:
    print("Forth Elif")
else:
    print("Else Block")
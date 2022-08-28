sal = 5000

if sal == 5000:
	inc = 1000
	allow = 50
	sal = sal + inc + allow
	print("Revised salary is:", sal)
elif sal > 5000:
	inc = 1100
	allow = 100
	sal = sal + inc + allow
	print("Revised salary is:", sal)
elif sal < 5000:
	inc = 1000
	allow = 50
	sal = sal + inc + allow
	print("Revised salary is:", sal)
else:
	print ("Salary value is invalid")

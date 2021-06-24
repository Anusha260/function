# create calculator by using user input

print("select operators :")
print("1:addition")
print("2:subtraction")
print("3:multiplication")
print("4:division")
user = input("enter choice(1/2/3/4):")
if user in ('1','2','3','4'):
	n1=int(input("enter the number :"))
	n2=int(input("enter the number :"))
	if user=='1':
		print(n1,"+",n2,"=",n1+n2)
	elif user=='2':
		print(n1,"-",n2,"=",n1-n2)
	elif user =='3':
		print(n1,"*",n2,"=",n1*n2)
	elif user=='4':
		print(n1,"/",n2,"=",n1/n2)
	else:
		pass
a=0
b=1
c=0
while c<=100:
    print(a)
    sum=a+b
    a=b
    b=sumdef total_budget():
    students=int(input("enter the num"))

    kharch=int(input("enter the num"))
    total_budget=students*kharch
    if total_budget<50000:
        print("budget is andar hai")
    elif total_budget>50000:
       print("budget is bahar hai")
total_budget()     
    
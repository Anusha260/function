def vote():
    v=int(input("enter the number"))

    if v>=18:
        print("eligible for vote")
    else:
        print("not eligible")

vote()
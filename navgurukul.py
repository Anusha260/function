def num():
    i=0
    while i <=1000:
        if i%3==0:
            print("nav")
        if i%7==0:
            print("gurukul")
        if i%21==0:
            print("navgurukul")
        else:
            print(i)
        i=i+1
num()
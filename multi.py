def multiply():
    list1=[5,10,50,20]
    list2=[2,20,3,5]
    i=0
    j=0
    a=[]
    while i<len(list1):
        b=list1[i]*list2[j]
        a.append(b)
        j=j+1
        i=i+1
    print(a)
multiply()


        


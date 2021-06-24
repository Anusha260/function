def harshad():
    n=int(input('enter the num'))
    num=1
    hc=0
    while hc<n:
	    a=num
	    sum=0
	    while a>0:
		    d=a%10
		    sum=sum+d
		    a=a//10
	    if num%sum==0:
		    print(num,'harshad')
		    hc=hc+1
	    num=num+1
harshad()
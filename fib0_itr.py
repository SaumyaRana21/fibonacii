n=int(input("enter any no: "))
a,b=0,1
seq = " "
for i in range(1,n):
    c=a+b
    temp=b
    b=c
    a=temp 
    if c<=1:
        seq+= "0 1"+" "+str(c)+" "
    else:
        seq+=str(c)+" "
print(seq)

    


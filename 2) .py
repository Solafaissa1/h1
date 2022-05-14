d=int(input('enter the decimal number'))
i=0
res=0
while d!=0:
    res=res+(d%2)*(10**i)
    d=d//2
    i=i+1
print('the binary nmber is:',res)


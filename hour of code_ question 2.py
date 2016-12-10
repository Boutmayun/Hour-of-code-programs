n=input('Enter number:')
ex=input('Enter exponent:')
ans=0
total=0
def expo(num,exp):
    global ans
    global total
    increment=num
    if exp!=1:
        ans=num
        for i in range(1,exp):
            for j in range(1,num):
                ans+=increment
            increment=ans
        return ans
    else:return 1
print expo(n,ex)

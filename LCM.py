a,b=map(int,input().split())
p=a*b
while a!=0 and b!=0:
    if a>b:
        a=a%b
    else:
        b=b%a
gcd=a if b==0 else b
lcm=p//gcd
print(lcm)
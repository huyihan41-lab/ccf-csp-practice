n=int(input())
ans1=[]
ans2=[]
for i in range(n):
    s=input().strip()
    a,b=s.split('.')
    a=int(a)
    b=int(b)
    if b<=4:
        ans1.append(a)
    else:
        ans1.append(a+1)

    if b<5:
        ans2.append(a)
    elif b>5:
        ans2.append(a+1)
    else:
        if a%2==0:
            ans2.append(a)
        else:
            ans2.append(a+1)
print(*ans1)
print(*ans2)
    
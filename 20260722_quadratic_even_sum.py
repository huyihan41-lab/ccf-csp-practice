b,c,l,r=map(int,input().split())
sum=0
for x in range(l,r+1):#注意range可以这样用
    if x%2==0:
        sum+=x*x+b*x+c
print(2*sum)#若print和if同一级缩进 则每if循环一次就输出一次 结果就会出现四个答案
    
    
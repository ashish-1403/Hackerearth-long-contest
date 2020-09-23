n=int(input())
ans=0
while n!=1:
    if n==1:
        break
    else:
        n=n//3 + (n%3 != 0)
        ans+=1
    if(n<=3):
        ans+=1
        break

print(ans)

 

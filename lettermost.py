n=int(input())
s=input()
s1=set(s)

q=[]
for i in s1:
    p=s.count(i)
    q.append(p)
print(max(q))

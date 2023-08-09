#Nama : Aland Mulia Pratama
#NIM : 19622296

n = int(input())
m = int(input())

a = list(map(int,input().strip().split()))
ans = 0

for i in range(n):
    found = False
    for j in range (n):
        if(i!=j and not(found) and a[i]==a[j]and abs(i-j)<=m):
            found = True
            ans += 1
print (ans)
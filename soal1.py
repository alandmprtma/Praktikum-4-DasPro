#Nama : Aland Mulia Pratama
#NIM : 19622296

a = int(input())
b = int(input())

ans = 0

for i in range (a,b+1):
    if (i%3==0 or i%4==0):
        ans += 1

if (ans==0):
    print("Tidak Ada")
else:
    print (ans)
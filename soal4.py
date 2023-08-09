#Nama : Aland Mulia Pratama
#NIM : 19622296

def getDigitSum (x):
    ret = 0
    while (x!=0):
        ret += x%10
        x //= 10
    return ret

n = int(input())
a = list (map(int,input().strip().split()))

ans = 0
for i in range (n):
    while (a[i]>=10):
        a[i] = getDigitSum (a[i])
        ans += 1

print (ans)
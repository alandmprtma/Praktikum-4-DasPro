#Nama : Aland Mulia Pratama
#NIM : 19622296

n = int(input())
m = int(input())

rowBefore = [0]

print(m)
rowBefore[0] = m

for i in range(2, n+1):
    cur = [0 for k in range (i)]
    for j in range(i):
        if(j == 0):
            cur[j]=rowBefore[0]
        elif (j == i-1):
            cur[j]=rowBefore[len(rowBefore)-1]
        else:
            cur[j]=rowBefore[j-1] + rowBefore[j]

    rowBefore = [0 for k in range(i)]

    for j in range(len(cur)):
        rowBefore[j] = cur[j]
        print(cur[j], end="")
        if(j!=len(cur)-1):
            print(" ",end="")
    print()
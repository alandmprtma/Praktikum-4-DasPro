#Nama : Aland Mulia Pratama
#NIM : 19622296

N = int(input())

if(N<=0 or N>=100):
    print("Tidak valid")
else:
    arr = list(map(int, input().strip().split()))
    x = int(input())

    diff1 = 3000
    pos1 = -1

    for i in range (N):
        if (0<arr[i]-x<diff1):
            diff1 = arr[i]-x
            pos1 = i
            diff2 = 3000
            pos2 = -1
    
    for i in range (N):
        if(0<arr[i]-x<diff2 and i != pos1):
            diff2 = arr[i]-x
            pos2 = i

    if(pos2 == -1):
        print(-1)
    else:
        print(arr[pos2])

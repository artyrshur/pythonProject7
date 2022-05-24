a = [int(y) for y in input().split()]
N = len(a)
b = [1]*N
if N == 0:
    b = [0]
elif N == 1:
    b = a
else:
    for i in range(0,N-1):
        b[i] = a[i-1] + a[i+1]
    b[N-1] = a[N-2] + a[0]
for j in b:
    print(j,end=' ')





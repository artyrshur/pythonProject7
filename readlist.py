a = [int(i) for i in input(). split()]
b = int(input())
if b not in a:
    print("Отсутствует")
else:
    for i in range(len(a)):
        if b == a[i]:
            print(i, end =' ')
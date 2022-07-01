mylist = [int(i) for i in input().split()]
for i in set(mylist):
    if mylist.count(i) > 1:
         print(i, end=' ')
#принимает на ввод список , делает без дубликатов и выводит овторяющиеся значения
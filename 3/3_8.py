# -- coding: utf-8 --
n = int(input())
print('::::::')
if n<=9:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, sep='', end='')
        print()
     
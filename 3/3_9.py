# -- coding: utf-8 --
n = int(input())
f1 = 1
f2 = 2
print('::::::')
for i in range (3, n+1):
  f_s = f1 + f2
  f1 = f2
  f2 = f_s
print(f_s)
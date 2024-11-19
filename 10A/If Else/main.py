import math
# 1.
n = math.sqrt(16) # float tipi
print(n)

# 2.
n = 16**0.5
print(n)

a = 5
b = "a"

print(a*b)  # aaaaa
print("a+b") # a+b
print("a"+"b") # ab

a = '12'
b = '23'


print(a*b)


print("Yusif","Memmedli",'15', end="*")
print("Yusif","Memmedli",'15', sep="\n")

# if elif else

a = 6
b = 5

if a>b:
    print('1.')
if a==b:
    print('2.')
else:
    print('3.')

a = 6
b = 5

if a > b:
    print('1.')
    if a==b:
        print('2.')
    else:
        print('3.')
else:
    print('4.')


# * + - / 
# // tam hissəni tapır  
# %  qaliq hisseni tapir
# ** quvvet
# =  menimsetme

#  muqayise operator
# == beraberdimi
# != beraber deyil mi
# >, <
# >=, <=

a = -5
b = -4

c = abs(a+b)
print(c)


# #  3 reqemli eded daxil edin ve hemin 3 reqemli ededin reqemleri cemini tapin

n = int(input()) # 345
a = n//100
b = n//10%10
c = n%10
print(a+b+c)  

# ededin tek ve ya cut oldugun yoxlayan proqram yazin

n = int(input())
if n>0:
    if n%2 != 0:
        print('Tek')
    else:
        print('Cut')

# Test


n = int(input()) 
m = n+1
while m%2 == 0 or m%3 == 0 or m%5 == 0:
    m = m+1
print(m)





# 18 Daxil edilmiş ədədin 2-lik ədəd olub-olmadığını yoxlayan proqram qur

n = int(input()) # 1010
n = str(n)
flag = 1
for i in n:
    if int(i) >= 2:
        flag = 0
if flag == 1:
    print('Yes')
else:
    print('No')
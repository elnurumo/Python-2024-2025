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

# ------>>>>>>>>>>>>

# 53

n =int(input())
if n>2:
    if n%2==0:
        print(n-2)
    else:
        print(n-1)
else:
    print('eded yanlishdir')

# 54

a = int(input())
b = int(input())
c = int(input())
if a == b ==c:
    print('Beraberterefli')
elif a!=b and b!=c and a!=c:
    print('Muxtelifterefli')
else:
    print('Beraberyanli')

# 55


n =int(input())
if n>0:
    if n%6==0:
        print('He')
    else:
        print('Yox')
else:
    print('N natural eded olmalidir')

# 56

n = int(input()) #6
if n>0 and n<10:
    x = 'Birreqemli'
elif n>9 and n<100:
    x = 'ikireqemli'
print(x)

# 57

n = int(input()) 
if n%2 ==0:
    print(n-1,n+1,'Tekdir')
else:
    print(n-1,n+1,"Cutdur")


58
# 1. usul
x = float(input())
if x<=5:
    y = abs(x+2)+3*x
elif x>7:
    y = x**3-2
else:
    y = (3*x**4+10)**0.5
print(y)

# 2. usul
import math
x = int(input())
if x<=5:
    y = abs(x+2)+3*x
elif x>7:
    y = x**3-2
else:
    y = math.sqrt(3*x**4+10)
print(y)


# 59
a=float(input())
b=float(input())
if a<b:
    z=3*b/abs(a-b)+3*(a+b)
elif a>b:
    z=a**2/abs(a+b)
else:
    z=(2*a**2+abs(b**3))**0,5    
print(z) 

60






# 61

saat1 = int(input()) *3600
deqiqe1 = int(input()) * 60
saniye1 = int(input())
saat2 = int(input()) * 3600
deqiqe2 = int(input()) * 60
saniye2 = int(input())
a2 = saat2+deqiqe2+saniye2
a1 = saat1+deqiqe1+saniye1
if a2>a1:
    x = a2-a1
else:
    x = 'Saatlar duzgun daxil olunmuyub'
print(x)

# 62

a=int(input())
b=int(input())
c=int(input())
if a<b<c or c<b<a:
    print(b)
elif b<a<c or c<a<b:
    print(a)
elif a<c<b or b<c<a:
    print(c)

# 63

n = input() #kitab
            #01234
m = len(n) # 5
if m%2 == 0:
    print('0')
else:
    print(n[m//2])

# 64

azn = float(input())
kQiymet = float(input())
kSay = int(azn//kQiymet)
qaliqPul = azn%kQiymet
print(kSay,qaliqPul)

# 65

n = int(input())
if n==12 or n==1 or n==2:
    print('Qishdir')
elif n==3 or n==4 or n==5:
    print('Yaz')
elif 6<=n<=8:
    print('yay')
elif 9<=n<=11:
    print('Payiz')
else:
    print('bele bir ay nomresi yoxdur')

# 66

Email = 'email@inbox.ru'
password = '321abc'

userEmail = input()
userPassword = input()
if userEmail == Email and password== userPassword:
    print('Xosh geldiniz')
else:
    print('Email ve ya shifre yanlishdir')

# 67

n = int(input())
b = int(input())
say = 0
for i in range(1,n):
    x = i*i
    if x%b == 0:
        say = say + 1
print('Ededlerin sayi',say)

# 68

n = int(input()) #3756
                 #0123
m = str(n)
c = 0
s = 0
for i in m:
    i = int(i)
    if i%2 != 0:
        c = c + i
        s = s + 1
print(c,s)
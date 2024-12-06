import math
# 1. üsul
n = math.sqrt(36)
print(n)

# interger int(5), float  float(), string - sətir str()

# 2. üsul

n = 25**(1/2)
print(n)

# integer

a = 5
b = 6

print(a+b) # 11
print('a+b') # a+b
print('a'+'b') # ab

a = '5'
b = '6'

print(a+b) # 56

a = '6'
b = 5

print(a+b) # eror

a = '5'
b = 6

print(a*b) # 555555

a = 5
b = 4

if a>b:
    print('1.')  # 1.
elif a>b:
    print('2.')
else:
    print('3.')

a = 5
b = 4

if a>b:
    print('1.')  
if a<b:
    print('2.')
else:
    print('3.')


a = 5 
b = 4

if a>b:
    if a>b:
        print('1.')
    if a<b:
        print('4.')
    else:
        print('2.')
else:
    print('3.')


# sep operator print üçün alt alta çap
a = 5
b = 4

print(a,b, sep='\n')

#  end operator print üçün yanaşı çap
print(a, end=' ')
print(b, end='')
print(6)


n = 4 == 4
print(type(n)) #boolean

print(0==False)


# 3 rəqəmli ədədin rəqəmləri cəmini hesabla. Məsələn 455,  %, //, /

n = int(input())
   #abc
s = 0
a = n//100
b = n//10%10
c = n%10
s = a+b+c
print(s)


# 3 reqemli ededin reqemlerinden qiymetce orta olani tap

n = int(input()) # 375
s = 0
a = n//100
b = n//10%10
c = n%10
if a<b<c or c<b<a:
    s = b
elif b<a<c or c<a<b:
    s = a
elif a<c<b or b<c<a:
    s = c
print(s)

# Deyişen adı necə olmalıdı?
salam12 = 5 # ola biler
# 12salam = 5 #ola bilmez eror



if 5<4:
    print('1')
    if 6>3:
        print('2.')
else:
    print('3.')
    if 7>8:
        print('4')
    else:
        print('5')

a= 5
b = 6

if a>2:
    print('1.')
    if b>a:
        print('2.')
    elif a<b:
        print('3.')
else:
    print('4.')
    if 6>2:
        print('5.')
    else:
        print('6.')

a = int(input())

if a%2==0:
    print('1.')
    if 3>5:
        print('2')
    elif 4>5:
        print('4.')
    else:
        print('5.')
else:
    print('6')


# Dövrlər

a = 'Salam'


for i in range(100):
    print(i,'.',a)

# integer, float, string str(), list, boolean bool()

# boolean True, False
#  1, 0

n = 1
while True:
    print(n,'.',5)
    n = n+1

# Reqemlerinin sayı ixtiyarı olan ədəd daxil olunur. Həmin ədədin rəqəmləri cəmini tap

n = int(input()) # 1750
s = 0
while n>0:
    q = n%10
    s = s+q
    n = n//10
print(s)


# Suallar If else

# 34

# 41,42,44,47,52,45,49,50,48,32

print(2, end=' ')
print(7)
print(7,end=' ')
print(5)


print(2,7, sep='\n')

a = 16.5
b = int(a)
print(b)


# 53

n = int(input())
if n>2:
    if n%2 == 0:
        print(n-2)
    elif n%2!=0:
        print(n-1)


# 54

a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print('Beraberterefli')
elif a!=b and b!=c and a!=c:
    print('Muxtelif terefli')
else:
    print('Beraberyanli')

# 55

n = int(input()) # tam ededlere çeviri int()
if n>0:
    if n%6 == 0:
        print('He')
    else:
        print('yox')
else:
    print('natural eded daxil olunmuyub')


# 56

n = int(input())
if n>0 and n<10:
    print('Birreqemli')
elif n>9 and n<100:
    print('Ikireqemli')


# 57

n = int(input())
if n % 2 == 0:
    print(n-1,n+1, 'tek ededler')
else:
    print(n-1,n+1,'cut ededler')


# 58

x = int(input())
if x<=5:
    y = abs(x+2)+3*x
elif x>7:
    y = x**3-2
else:
    y = (3*x**4+10)**0.5
print(y)

# 59

a = int(input())
b = int(input())
if a<b:
    z = 3*b/abs(a-b)+3*(a+b)
elif a>b:
    z = a**2/abs(a+b)
else:
    z =(2*a**2+abs(b**3))**0.5
print(z)


# 60

n1 =int(input())
n2 =int(input())
n3 =int(input())
if n1==n2==n3:
    print('3')
elif n1!=n2 and n2!=n3 and n1!=n3:
    print('0')
else:
    print('2')


# 61

saat1 = int(input('Saat1: '))
deqiqe1 = int(input('Deqiqe1: '))
saniye1 = int(input('Saniye1: '))
saat2 = int(input('Saat2: '))
deqiqe2 = int(input('Deqiqe2: '))
saniye2 = int(input('Saniye2: '))
a1 = saat1*3600+deqiqe1*60+saniye1
a2 = saat2*3600+deqiqe2*60+saniye2
ferq = a2-a1
print(ferq)

# 62

a = int(input())
b = int(input())
c = int(input())
if a<b and b<c or c<b and b<a:
    print('Qiymetce orta olan=',b)
elif a<c and c<b or b<c and c<a:
    print('Qiymetce orta olan=',c)
else:
    print('Qiymetce orta olan=',a)
    

# Sual str aid

name = 'info'
m = len(name)//2
n = name[m]
print(n)

# 63

n = input()
m = len(n)
if m%2 == 0:
    print(0)
else:
    print(n[m//2])

# 64

azn = float(input())
kQiymet = float(input())
kSay = azn // kQiymet
QaliqPul = azn - kQiymet*kSay  
print(kSay,QaliqPul)

# 65

n = int(input())
if n == 12 or n == 1 or n == 2:
    print('Qışdır')
elif n == 3 or n == 4 or n == 5:
    print('Yazdir')
elif n == 6 or n == 7 or n == 8:
    print('Yaydir')
elif n == 9 or n == 10 or n == 11:
    print('Payizdir')
else:
    print('Bele bir ay sırasi yoxdur')


n = int(input())
if 1<=n<=2 or n==12:
     print('Qisdir')
elif 3<=n<=5:
    print('Yazdir')
elif 6<=n<=8:
    print('Yaydir')
elif 9<=n<=11:
    print('Payizdir')

# 66

email = 'email@inbox.ru'
password = '321abc'
userEmail = input()
userPassword = input()
if userEmail == email and userPassword == password:
    print('Xosh geldiniz')
else:
    print('Email ve ya shifre yanlishdir')

   
# 67

n = int(input())
b = int(input())
s = 0 # say 
for i in range(1,n):
    k = i*i # n den kiçik kvadratlar
    if k%b == 0:
        s = s+1
print('Ədədlərin sayı',s)

# 68

n = int(input()) # 3756
n = str(n)
say = 0
cem = 0
for i in range(0,len(n)):
    if int(n[i]) % 2 != 0: #ededin tek olub olmamasini yoxlayir
        say = say+1
        cem = cem+int(n[i])
print(cem,say)



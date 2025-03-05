# hefte 1 
# 1

a = int(input()) # '9'---> 9    string setir 'salam'  "salam"
b = int(input())
s = (a*b)/2
print(s)

# 2

# 1 - ci usul
n = 325
a = n//100 #3
b = n//10%10 #2
c = n%10 # 5
s = str(a)+' '+str(b)+' '+str(c)
print(s)

# 2-ci usul

n = 325
a = n//100 #3
b = n//10%10 #2
c = n%10 # 5
print(a,b,c)

# 3

# 1 -ci usul

a = 5
b = 6
c = a 
a = b
b = c
print('a:',a,'b:', b)

# 2 -ci usul

a = 5 
b = 6
a,b = b,a
print(a,b)


# 3

a = int(input())
b = int(input())
c = a
a = b
b = c

a = int(input())
b = int(input())
a,b = b,a

# 4

n = 24 #---> 42
#   01
n = str(n)
a = n[0] # 2
b = n[1] # 4
s = b+a
s = int(s)
print(s)

# 5

n = 345
n = str(n)
a = n[0] # 3
b = n[1] # 4
c = n[2] # 5
s = c+b+a
s = int(s)
print(s)

# 6

n = 543
a = str(n//100) # 3
b = str(n%100) # 45
s = b+a
s = int(s)
print(s)



# 7

n = 345
a = str(n//100) # '3'
b = str(n//10%10)
c = str(n%10) 
s = b+a+c
print(s)


# 8

n = 1024
a = n//1000%10
print(a)

# 9

n = 54321
a = n//10000
b = n//1000%10
c = n//10%10
d = n%10
s = (a+b) - (c+d)
print(s)

# if elif else

a = 5
b = 7

if a<b:
    print('1')
    if a<=b:
        print('2')
if a == 5:
    print('3')
else:
    print('4')


n = int(input())
if n%2==0:
    print('Cutdur')
elif n%2!=0:
    print('Tekdir') 

# 53

n = int(input())
if n>2:
    if n%2 == 0:
        s = n-2
    else:
        s = n-1
    print(s)
else:
    print('Eded duzgun qeyd olunmayib')

# 54

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Berabertereflidir')
elif a != b != c and a != c:
    print('Muxtelif terefli')
else:
    print('Beraberyanli')


56 
n=int(input())
if 100>n>10:
    print("ikireqemlidir")
elif 10>n>0:
    print("birreqemlidir")

57
n=int(input())
if n>0:
    if n%2==0:
        print(n-1,n+1,"tek ededlerdir")
    else:
        print(n-1,n+1,"cut ededlerdir")

58
x=int(input())
if x<=5:
    print(abs(x+2)+3*x)
elif x>7:
    print(x**3-2)
else:
    print((3*x**4+10)**0.5)

import math
# from math import*
x=int(input())
if x<=5:
    print(abs(x+2)+3*x)
elif x>7:
    print(x**3-2)
else:
    print(math.sqrt(3*x**4+10))


59
import math
a=int(input())
b=int(input())
if a<b:
    print((3*b)/abs(a-b)+3*(a+b))
elif a>b:
     print((a**2)/abs(a+b))
else:
     print(math.sqrt(2*a**2+abs(b**3)))

60
a=int(input())
b=int(input())
c=int(input())
if a==b==c:
    print(3)
elif a!=b!=c and a!=c:
    print(0)
else:
    print(2)

61
saat1=int(input("saat1= "))
deqiqe1=int(input())
saniye1=int(input())
saat2=int(input())
deqiqe2=int(input())
saniye2=int(input())
a=saat1*3600+deqiqe1*60+saniye1
b=saat2*3600+deqiqe2*60+saniye2
s=b-a
print(s)

#62
a=int(input())
b=int(input())
c=int(input())
if a<b<c or c<b<a:
    answer=b
elif b<a<c or c<a<b:
    answer=a
else:
    answer=c
print("Qiymetce orta olan=", answer)
print(f'Qiymetce orta olan={answer}')

# 63

n=input() # kitab
          # 01234
l=len(n) # 5
if l%2==0:
    print(0)
else:
    print(n[l//2])


64

azn=float(input())
kazn=float(input())
ks=azn//kazn
azn=azn-ks*kazn
print(ks,azn)

#65
n=int(input())
if n == 12 or n==1 or n==2:
    print('Qış')
elif n == 3 or n == 4 or n == 5:
    print('Yaz')
elif n == 6 or n==7 or n==8:
    print('Yay')
elif n == 9 or n== 10 or n == 11:
    print('Payız')
else:
    print('Belə bir ay sırası yoxdur!!')









    

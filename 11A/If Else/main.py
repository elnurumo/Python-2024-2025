# import math

# n = math.sqrt(25)
# print(n)

# n = 25**(1/2)
# print(n)

# n = input('Daxil et: ')
# print('çapa verildi:', n)

# a = 5
# b = 'a'

# print(a+b) # eror
# print(a*b) # 
# print('a+b') # a+b
# print('a'+'b') # ab

# a = 6
# b = 5

# if a>b:
#     print('1.')
# if a>b:
#     print('2.')
# if a==b:
#     print('3.')
# else:
#     print('4.')

# a = 6
# b = 5

# if a>=b:
#     print('1.')
#     if a == b:
#         print('2.')
#     elif a<=b:
#         print('3.')
#     else:
#         print('4.')
# else:
#     print('5.')

# print('Ulvi','Velizade',16, end='*')
# print('Salam')
# print('necesen')

# n = input()
# print(type(n))

# # ededin cut ve ya tek olduğun yoxla

# a = int(input())

# if a%2 != 0:
#     print('Tek')
# else:
#     print('Cut')

# # 3 reqemli ededin reqemleri cemini tap

# n = int(input()) # 345
# a = n//100
# b = n//10%10
# c = n%10
# s = a+b+c
# print(s)


# Ətraflılar ------->>>>>>>>>>>>>>>>>>>

# # 53

# n = int(input())
# if n>2:
#     if n%2 == 0:
#         print(n-2)
#     else:
#         print(n-1)


# # 54

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     print('Beraberterefli')
# elif a!=b and b!=c and a!=c:
#     print('Muxtelif terefli')
# else:
#     print('beraber yanli')

# # 55

# n = int(input())
# if n%6==0:
#     print('He')
# else:
#     print('Yox')

# # 56
# n = int(input())
# if n>0 and n<10:
#     print('Birreqemli')
# elif n>=10 and n<100:
#     print('Ikireqemli')

# # 57

# n = int(input())
# if n%2==0:
#     print(n-1,n+1, 'tekdir')
# else:
#     print(n-1,n+1, 'cutdur')

# # 58

# x = int(input())
# if x<=5:
#     y = abs(x+2) +3*x
# elif x>7:
#     y = x**3-2
# else:
#     y = (3*x**4+10)**0.5
# print(y)

# # 60
# a = int(input())
# b = int(input())
# c = int(input())
# if a==b==c:
#     print('3')
# elif a!=b and b !=c and a!=c:
#     print('0')
# else:
#     print('2')

# # 61

# s1 =int(input())*3600
# d1 = int(input())*60
# sn1 = int(input())
# s2 = int(input())*3600
# d2 = int(input())*60
# sn2 = int(input())
# a = (s1+d1+sn1)
# b = (s2+d2+sn2)
# if b>a:
#     c = b-a
# else:
#     c = 'Saatlar duzgun daxil olmayib'
# print(c)


# # 62
# a = int(input())
# b = int(input())
# c = int(input())
# if a<b<c or c<b<a:
#     y = b
# elif b<a<c or c<a<b:
#     y = a
# elif a<c<b or b<c<a:
#     y= c
# print('Qiymetce orta olan =',y)

# # 63

# n = input()
# m = len(n)
# if m%2 == 0:
#     print(0)
# else:
#     print(n[m//2])

# 64
# azn = float(input())
# kQiymet = float(input())
# kSay= azn//kQiymet
# qalanPul = azn %kQiymet
# print(kSay,qalanPul)


# # 65

# n = int(input())
# if n == 12 or n==1 or n==2:
#     print('Qishdir')
# elif n == 3 or n== 4 or n==5:
#     print('Yazdir')
# elif n == 6 or n== 7 or n==8:
#     print('Yaydir')
# elif n == 9 or n== 10 or n==11:
#     print('Payizdir')
# else:
#     print('Bele bir ay nomresi yoxdur')

# # 66
# Email = 'email@inbox.ru'
# password = '321abc'
# userEmail = input()
# userPassword = input()
# if Email == userEmail and password == userPassword:
#     print('Xosh geldiniz')
# else:
#     print('Email ve ya shifre yanlishdir')

# # 67

# n = int(input())
# b = int(input())
# say = 0
# for i in range(1,n):
#     c = i*i
#     if c%b == 0:
#         say=say+1
# print('Ededlerin sayi',say)

# 68

n = int(input())
c = 0
s = 0
for i in str(n):
    i = int(i)
    if i % 2 != 0:
        s = s+1
        c = c+i
print(c,s)
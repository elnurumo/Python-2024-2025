# import math
# # 1.
# n = math.sqrt(25)
# print(n)

# # 2.

# n = 25**(1/2)
# print(n)

# print('Hello world')
# Elnur = 5
# Fizuli = 6

# print(Elnur+Fizuli) # 11
# print('a+b') # 11 , a+b
# print('Elnur'+'Fizuli') #  ab

# a = 5
# b = "6"

# # print(a+b) # eror
# print(a*b) # 66666
# print("a+b") # a+b
# print("a"+"b") # ab


# print(type(25/12))

# # 3 reqemli ededin reqemleri ceminin tapilmasi

# n = int(input()) # str ---->> Int 564 
# a = n//100 
# b = n//10%10
# c = n%10
# cem = a+b+c
# print(cem)




# # --------------------------->>>>>>>>>>>>

# # 53

# n = int(input())
# if n>2 and n%2==0:
#     print(n-2)
# elif n>2 and n%2!=0:
#     print(n-1)
    
    

# # 54

# a = int(input())
# b = int(input())
# c = int(input())
# if a==b==c:
#     print('Beraberterefli')
# elif a!=b and b!=c and a!=c:
#     print('Muxtelifterefli')
# else:
#     print('beraberyanli')


# # 59

# a = int(input())
# b = int(input())
# if a<b:
#     z = 3*b/abs(a-b) + 3*(a+b)
# elif a>b:
#     z = a*a/abs(a+b)
# else:
#     z=(2*a*a +abs(b**3))**0.5
# print(z)


# # 57

# n = int(input())
# if n%2==0:
#     print(n-1,n+1,'tekdir')
# else:
#     print(n-1,n+1,'cutdur')



# # 61

# saat1 = int(input('saat1: ')) *3600
# deqiqe1 = int(input("deqiqe1: "))*60
# saniye1 = int(input('saniye1: '))
# saat2 = int(input('saat2: '))*3600
# deqiqe2 = int(input("deqiqe2: "))*60
# saniye2 = int(input("saniye2: "))
# a2 = saat2+deqiqe2+saniye2
# a1 = saat1+deqiqe1+saniye1
# if a2>a1:
#     x = a2-a1
# else:
#     x = 'saatlar duzgwn daxil edilmeyib'
# print(x)

# # 62

# a = int(input())
# b = int(input())
# c = int(input())
# if a<b<c or c<b<a:
#     print(b)
# elif b<a<c or c<a<b:
#     print(a)
# elif a<c<b or b<c<a:
#     print(c)

# # 53

# n =int(input())
# if n>2:
#     if n%2==0:
#         print(n-2)
#     else:
#         print(n-1)
# else:
#     print('eded yanlishdir')

# # 54

# a = int(input())
# b = int(input())
# c = int(input())
# if a == b ==c:
#     print('Beraberterefli')
# elif a!=b and b!=c and a!=c:
#     print('Muxtelifterefli')
# else:
#     print('Beraberyanli')

# # 55


# n =int(input())
# if n>0:
#     if n%6==0:
#         print('He')
#     else:
#         print('Yox')
# else:
#     print('N natural eded olmalidir')

# # 56

# n = int(input()) #6
# if n>0 and n<10:
#     x = 'Birreqemli'
# elif n>9 and n<100:
#     x = 'ikireqemli'
# print(x)

# # 57

# n = int(input()) 
# if n%2 ==0:
#     print(n-1,n+1,'Tekdir')
# else:
#     print(n-1,n+1,"Cutdur")


# 58
# # 1. usul
# x = float(input())
# if x<=5:
#     y = abs(x+2)+3*x
# elif x>7:
#     y = x**3-2
# else:
#     y = (3*x**4+10)**0.5
# print(y)

# # 2. usul
# import math
# x = int(input())
# if x<=5:
#     y = abs(x+2)+3*x
# elif x>7:
#     y = x**3-2
# else:
#     y = math.sqrt(3*x**4+10)
# print(y)


# # 59
# a=float(input())
# b=float(input())
# if a<b:
#     z=3*b/abs(a-b)+3*(a+b)
# elif a>b:
#     z=a**2/abs(a+b)
# else:
#     z=(2*a**2+abs(b**3))**0,5    
# print(z) 

# 60






# # 61

# saat1 = int(input()) *3600
# deqiqe1 = int(input()) * 60
# saniye1 = int(input())
# saat2 = int(input()) * 3600
# deqiqe2 = int(input()) * 60
# saniye2 = int(input())
# a2 = saat2+deqiqe2+saniye2
# a1 = saat1+deqiqe1+saniye1
# if a2>a1:
#     x = a2-a1
# else:
#     x = 'Saatlar duzgun daxil olunmuyub'
# print(x)

# # 62

# a=int(input())
# b=int(input())
# c=int(input())
# if a<b<c or c<b<a:
#     print(b)
# elif b<a<c or c<a<b:
#     print(a)
# elif a<c<b or b<c<a:
#     print(c)

# # 63

# n = input() #kitab
#             #01234
# m = len(n) # 5
# if m%2 == 0:
#     print('0')
# else:
#     print(n[m//2])

# # 64

# azn = float(input())
# kQiymet = float(input())
# kSay = int(azn//kQiymet)
# qaliqPul = azn%kQiymet
# print(kSay,qaliqPul)

# # 65

# n = int(input())
# if n==12 or n==1 or n==2:
#     print('Qishdir')
# elif n==3 or n==4 or n==5:
#     print('Yaz')
# elif 6<=n<=8:
#     print('yay')
# elif 9<=n<=11:
#     print('Payiz')
# else:
#     print('bele bir ay nomresi yoxdur')

# # 66

# Email = 'email@inbox.ru'
# password = '321abc'

# userEmail = input()
# userPassword = input()
# if userEmail == Email and password== userPassword:
#     print('Xosh geldiniz')
# else:
#     print('Email ve ya shifre yanlishdir')

# # 67

# n = int(input())
# b = int(input())
# say = 0
# for i in range(1,n):
#     x = i*i
#     if x%b == 0:
#         say = say + 1
# print('Ededlerin sayi',say)

# # 68

# n = int(input()) #3756
#                  #0123
# m = str(n)
# c = 0
# s = 0
# for i in m:
#     i = int(i)
#     if i%2 != 0:
# #         c = c + i
# #         s = s + 1
# # print(c,s)


# n=int(input())
# if n>2:
#     if n%2==0:
#         n=n-2
#     else:
#         n=n-1
#     print(n)

# # a=int(input())
# # b=int(input())
# # c=int(input())
# # if a==b==c:
# #     print("beraberterefli")
# # elif a!=b!=c and a!=c:
# #     print("muxtelifterefli")
# # else:
# #     print("beraberyanli")

# # # 55
# # n=int(input())
# # if n%6==0:
# #     print("He")
# # else:
# #     print("Yox")
# # n=int(input())
# # if n<100 and n>9:
# #    print("ikireqemli")
# # elif 0<n<10:
# #    print("birreqemli")

  
# # 57
# # n=int(input())
# # if n%2==0:
# #    print(n-1,n+1,"tek ededlerdir")
# # else:
# #    print(n-1,n+1,"cut ededlerdir")
# # 58
# # x=int(input())
# # if x<=5:
# #     print(abs(x+2)+3*x)
# # elif 5<x<=7:
# #     print((3*x**4+10)**0.5)
# # else:
# #     print(x**3-2)
# # 60
# # a=int(input())
# # b=int(input())
# # c=int(input())
# # if a==b==c :
# #    print('3')
# # elif a!=b!=c and a!=c:
# #    print('0')
# # else:
# #    print('2')
# sa1=int(input())*3600
# de1=int(input())*60
# san1=int(input())
# # sa2=int(input())*3600
# # de2=int(input())*60
# # san2=int(input())
# # a=sa1+de1+san1
# # b=sa2+de2+san2
# # f=b-a
# # print(f)
# # 62
# a=int(input())
# b=int(input())
# c=int(input())
# if a<b<c or c<b<a:
#     print(b,"orta ededdir")
# elif b<a<c or c<a<b:
#     print(a,"orta ededdir")
# else:
#     print(c,"orta ededdir")

# 58

# x = int(input())
# if x<=5:
#     y = abs(x+2)+3*x
# elif x>7:
#     y = x**3-2
# else:
#     y = (3*x**4+10)**0.5

# 59

# # 64

# m = float(input('manat: ')) # 2.5, 2, 3.5
# k = float(input('Keks qiymet: ')) 
# ks = m//k
# pq = m-ks*k
# print(ks,pq)

# 66

# Email = 'email@inbox.ru'
# password = '321abc'
# EmailUser = input('Email: ')
# passwordUser = input("Password: ")
# if Email == EmailUser and password == passwordUser:
#     print('Xoş gəlmisiz')
# else:
#     print('Email ve ya şifre yanlışdır')


#   99, 102, 101, 100,107, 110
# 94, 

# # 67

# n = int(input()) # 2345
# m = str(n)
# a = int(m[1])
# b = int(m[2])
# if b%2 == 0:
#     print(a+b)
# else:
#     print(a*b)

# # 72

# nsayi = int(input('Ededlerin sayin daxil et: ')) #3
# b = []
# for i in range(0,nsayi):
#     n = int(input('Eded daxil et: ')) 
#     b.append(n)
# kiçik = min(b)
# print("çıxış:",kiçik)

# a = [1,2,3,56,78,90]
# b = a[1:3]
# print(b)


# # 83
# s = 0
# for x in range(-10,11):
#     if x>3:
#         y = x**2-5*x+6
#     elif x<=3:
#         y = (x+2)**2
#     if y%3==0:
#         s = s+1
# print(s)

# 89

# n = int(input())
# s = 0
# f = 1
# k = -1
# for i in range(1,n+1):
#     f = f*i
#     s = s + k*(1/f**i)
#     k = -k
# print(s)

# 93

# n = int(input())
# b = []
# n = str(n)
# for i in n:
#     i = int(i)
#     if i%2!=0:
#         b.append(i)
# if len(b) > 0:
#     print(min(b))
# else:
#     print('Ədəddə tək rəqəm yoxdur')

# 99

# n = int(input())
# s = 0
# n = list(str(n))
# for i in n:
#     if min(n) == i:
#         s = s+1
# print(s)




# 66

# 1. 
# n = 2564
# n = str(n)
# for i in n:
#     print(i)

# 2.

# n = 2564
# b = []
# while n>0:
#     k = n%10
#     b.insert(0,k)  # [2,5,6,4]
#     n = n//10
# for i in b:
#     print(i)

# # 67

# n = int(input()) # 2345
# a = n//100%10 # 3
# b = n%100//10 # 4
# if b%2 == 1:
#     print(a*b)
# else:
#     print(a+b)


# # 68

# s = 0
# n = int(input())
# for i in range(1,n+1):
#     s = s + 1/i**2
# print(s)


# #  69

# s = 0
# n = int(input())
# for i in range(1,n+1,2):
#     s = s + (1/i)**i
# print(s)

# # 70

# n = int(input())
# s = 0
# for i in str(n):
#     i = int(i)
#     s = s+i
# if n % s == 0:
#     print('Bolunur')
# else:
#     print('Bolunmur')

# 71

# n = int(input()) # 3
# s = 0
# for i in range(n):
#     a = int(input()) # 10
#     s = s + a # 21
# edediOrta = s/n
# print(edediOrta)

# 72

# n = int(input())
# b = []
# for i in range(n):
#     a = int(input())
#     b.append(a)
# print(min(b))

# 74

# for i in range(1,1000,2):
#     print(i)

# 75

# a = [15,12,16,11,9]
# for i in a:
#     if i%2!=0:
#         print(i**2)


# 76

# n = int(input())
# if n == 12 or n == 1 or n == 2:
#     print('Sizin ad gununüz qışdadır.')
# elif n == 3 or n == 4 or n == 5:
#     print('Sizin ad gununüz Yazdadir.')
# elif n == 6 or n == 7 or n==8:
#     print('Sizin ad gununüz yaydadir.')
# elif n == 9 or n == 10 or n == 11:
#     print('Sizin ad gununüz payizdadir.')
# else:
#     print('Bele bir ay nomresi yoxdur')


# # 77
# s = 0
# for i in range(1,100):
#     i = str(i)
#     s = s + i.count("3")
# print(s)


# # 78

# n = int(input())
# m = []
# k = []
# for i in range(n):
#     a = int(input())
#     if a %2 == 0:
#         m.append(a)
#     else:
#         k.append(a)
# print(m,k)

# # 79

# n = int(input()) # 2300
# s = 0
# while n%10 == 0:
#     s = s+1
#     n = n//10
# print(s)


# # 80

# n = int(input())
# s = 0
# if n>1:
#     for i in range(2,n//2+1):
#         if n%i == 0:
#             s = s+1
#     if s > 0:
#         print( "Mürəkkəb ədəddir")
#     else:
#         print("Sadə ədəddir")
# elif n == 1:
#     print('1 ne sade nede murekkebdir')


# # 81

# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = s + (-1)**(i+1)*i*(i+1)
# print(s)

# # 82

# a = [3,4, 15, 9, 18, 16]
# for i in a:
#     k=i**0.5
#     if i**0.5==int(k):
#         print(i)

# # 83

# s = 0
# for x in range(-10,11):
#     if x>3:
#         y = x**2 - 5*x+6
#     elif x<=3:
#         y = (x+2)**2
#     if y % 3 == 0:
#         s = s+1
# print(s)
    

# # 84

# a = [3,4,2,1,6,9,7,8,12,10,5,14]
# s = 0
# n = 0
# for i in range(0,len(a)):
#     if i%2 != 0 and a[i] %2 == 0:
#         s = s + a[i]
#         n = n+1
#     elif i%2 == 0 and a[i]%2 != 0:
#         s = s + a[i]
#         n = n+1
# print(s/n)

# 85

# 100


# n = int(input())
# s = 0
# while n>1:
#     s = s+1
#     n = n //2
# print(s)


# klaviaturada daxil edilen ededlerden polindrom olanlarindan
# en boyukunu çapa ver

# n = int(input())  # say
# l1 =[]
# for i in range(n):
#     a = int(input())  # eded 
#     l1.append(a)
# l2 = []
# for i in l1:
#     c = str(i) # '123'
#     k = list(c)  #['1','2','3']
#     k.reverse() # ['3','2','1']
#     k = ''.join(k) # '321'
#     if c == k:
#         l2.append(c)
# m = max(l2)
# print('Polindrom max eded =',m)

# 101

# # 1-ci üsul
# day = 5
# s = 0
# for i in range(1,6):
#     s = s + day
#     day = day + day*20/100
# print(s)

# 2-ci üsul
# day = 5
# s = 0
# i = 1
# while i<=5:
#     s = s + day
#     day = day + day*20/100
#     i = i+1
# print(s)

# 105
#  1-ci usul
# n=input()
# s=0
# for i in n:
#     if "0"<=i and i<='9':
#         s = s + 1
# print(s)

# # 2-ci usul

# n = input()
# s = 0
# reqemler = '0123456789'
# for i in n:
#     if reqemler.count(i) == 1:  
#         s = s+1
# print(s)


# 106
# s=input()
# n=[]
# for i in s:
#     if n.count(i)==0:
#        n.append(i)
# print(n)

# # 107
# n=int(input()) # 11001
# onluq = 0
# l = len(str(n))-1
# for i in str(n):
#     onluq = onluq + int(i) * 2 ** l
#     l = l-1
# sekkizlik = ''
# while onluq>0:
#     q = onluq % 8
#     sekkizlik = str(q) + sekkizlik   # '53'
#     onluq = onluq//8
# print(sekkizlik)


# 109

# a = [123,4532,3431,2345,67864]
# for i in range(0,len(a)):
#     k = str(a[i])
#     k = list(k)
#     k.reverse()
#     k = ''.join(k)
#     k = int(k)
#     a[i] = k
# print(a)


# #  list vs split

# # list
# # '124 25' -->  ['1','2','4',' ','2','5']


# # m = '124 25' ---> ['1','4 ','5']
# # m.split('2')
# m = '124 25'
# m = m.split('')
# print(m)

# m = '124 25'
# m = list(m)
# print(m)

# # join

# m = ['34','55','60']
# m = '-'.join(m)
# print(m)
# # n = int(input()) # 5456
# # n = str(n)
# # maxi = max(n)
# # s = 0
# # f = 0 # flag
# # for i in n:
# #     if n.count(i)>1:
# #         f = 1
# # if f == 1:
# #     print('Reqemleri eynidir')
# # else:
# #     for i in n:
# #         if i!=maxi:
# #             s = s+int(i)
# #     print(s)


# # 


# # a = [0,0,0,0,0,0,0,0,0,0]
# # for i in range(1,6):
# #     a[10-i] = (10-i)*(i-10)
# #     a.reverse()
# # print(a)


# # 1

# # n=int(input())
# # n=str(n)
# # s=''
# # for i in n:
# #     if i!=n[len(n)-1]:
# #         s=s+i+'1'
# #     else:
# #         s=s+i
# # s=int(s)
# # print(s*s)
# # 
# # n=int(input())
# # s=''
# # a='0123456789ABCDEF'
# # while n>0:
# #     q=n%16
# #     s=a[q]+s
# #     n=n//16
# # print(s)
# # 
# # n=input().upper()
# # l=len(n)-1
# # s=0
# # a='0123456789ABCDEF'
# # for i in n:
# #     s=s+a.index(i)*16**l
# #     l=l-1
# # print(s)


# # Rekursiv Function

# def f(n):
#     if n<1:
#         return 1
#     return n*f(n-1)

# print(f(5))

# a=[351,648,776,918]
# for i in a:
#     x= i//100
#     y= i%10
#     S= (x+y)*2
#     print(S)

# # 8

# s = 0
# a = int(input())
# b = int(input())
# if 1<a<b:
#     for i in range(a,b+1):
#         f = 0
#         for j in range(2,i//2+1):
#             if i%j==0:
#                 f = 1
# #         if f == 0:
# #             s = s+i
# #     print(s)


# # 9

# n = [5,8,9,45,63]
# m = []
# m.append(n[0])
# for i in range(0,len(n)-1):
#     c = n[i+1] - n[i]
#     m.append(c)
# print(m)

# n = [5,8,9,45,63]
# m = []
# a = n[0]
# m.append(a)
# for i in range(1,len(n)):
#     c = n[i]-a
#     m.append(c)
#     a = n[0+i]
# print(m)

# # 10

# n = input() # salam123
# reqemler = '0123456789'
# s = ''
# for i in n:
#     if reqemler.count(i) == 1:
#         s = s + 'a'
#     else:
#         s = s + i
# print(s)


# # 11

# n = 1111
# n = str(n)
# l = len(n)-1
# reqemler = '0123456789ABCDEF'
# onluq = 0
# for i in n:
#     onluq = onluq + int(i)*2**l
#     l = l-1
# s = ''
# while onluq>0:
#     q = onluq%16
#     s = reqemler[q]+s
#     onluq = onluq//16
# print(s)


# 

# n = ['s','a','l','1','2','3']
# # reqemler = '0123456789'
# for i in range(0,len(n)):
#     if n[i]>='0' and n[i] <='9':
#         n[i] = 'a'
# print(n)


# n = int(input())
# m = str(n)
# s = len(m)
# c = 0
# for i in m:
#     c = c + int(i)
# h = s*c
# while s!=c:
#     if s>c:
#         s = s-c
#     else:
#         c = c-s
# Ebob = s
# Ekob = h/Ebob
# print(Ebob+Ekob)

# n = input()
# hs = 0
# rs = 0
# reqemler = '0123456789'
# for i in n:
#     if reqemler.count(i) == 1:
#         rs = rs + 1
#     else:
#         hs = hs + 1
# print(rs*3,hs*3)


# n=input().split()
# for i in range(0,len(n)):
#     n[i] = int(n[i])
# b=0
# s=0
# while b<=30:
#     a=max(n)
#     b=b+a
#     n.remove(a)
#     n.append(a//2)
#     s=s+1
# print(s)


# 5
# reqemler = '0123456789'
# n = input()
# t = []
# c = []
# s = 0
# for i in n:
#     if reqemler.count(i)==1:
#         if int(i)%2==0:
#             c.append(int(i))
#         else:
#             t.append(int(i))
# k = min(t)
# b = max(c)
# print(b+k)

# 6

# for i in range(1,5):
#     print(i)



# 1

# a = int(input())
# b = int(input())
# s = a*b/2
# print(s)

# # 2
# n = 324
# n = str(n)
# a = n[0]
# b = n[1]
# c = n[2]
# s = a+' '+b+' '+c
# print(s)


# a = [2,7,4,5,6,8]
# b = []
# for i in a:
#     if i!=4 and i != 7:
#         b.append(i)
# print(b)


# import math
# n = int(input())
# k = math.sqrt(n)
# if k == int(k):
#     print('Yes')
# else:
#     print('No')


# from math import*
# n = int(input())
# k = sqrt(n)
# if k == int(k):
#     print('Yes')
# else:
#     print('No')


# 

# n = int(input())  # 5
# a = ['Bazar ertesi',  # 1 -- 0
#      'Çərşənbə axşamı', # 2 -- 1
#      "Çərşənbə",  # 3--- 2
#      'Cuma axshami', # 4 --- 3
#      'Cuma', # 5 --- 4
#      'Shanba',
#      'Bazar'
#      ]
# if 0 < n <=7:
#     print(a[n-1])
# else:
#     print('Bele bir gun yoxdur')



#  1

# def reversedNumber(x):
#     x = str(x)
#     x = list(x)
#     x.reverse() # ['5','4','2']
#     x = ''.join(x) # '542'
#     x = int(x) # 542
#     return x

# a = int(input())
# b =int(input())
# a = reversedNumber(a)
# b = reversedNumber(b)
# s = a+b
# s = reversedNumber(s)
# print(s)

# 2

# n = [11,3,4,5,0]
# maxi = max(n)
# mini = min(n)
# imax = n.index(maxi)
# imin = n.index(mini)
# result = abs(imax-imin) 
# print(result)

# n = [10,22,9,33,21,50,41,45,80]
# b = []
# b.append(n[0])
# j = 0
# for i in range(0,len(n)):
#     if b[j]<n[i]:
#         b.append(n[i])
#         j = j+1
# print(b)
# 

# k = int(input())
# n = [1,2,3,4,5]
# s = []
# a = 0
# while a<k:
#     b=n[len(n)-1]
#     n.remove(b)
#     s.append(b)
#     a= a+1
# s= s+n
# print(s)

# # 66

# n = int(input())
# n = str(n)
# for i in n:
#     print(i)


# # 85
# s = 0
# for i in range(1,201):
#     if i%5==0 and i%3!=0:
#         s = s+1
# print(s)

# # 86

# n = float(input()) # 5.6
# tam = ''
# if n>0:
#     n = str(n)
#     for i in range(0,len(n)):
#         if n[i] == '.':
#             tam = n[0:i]
#             kesr = '0' + n[i:]
# else:
#     n = str(n)
#     for i in range(0,len(n)):
#         if n[i] == '.':
#             tam = int(n[0:i]) - 1
#             kesr = 10**len(n[i+1:]) - int(n[i+1:])
#             kesr = kesr/10**len(str(kesr))
        
#     print(tam,kesr)


# # 94

# n = input().upper() # 2B
# reqemler = '0123456789ABCDEF'
# l = len(n)-1
# onluq = 0
# for i in n:
#     onluq = onluq + reqemler.find(i) * 16 ** l
#     l = l-1
# print(onluq)

# 108

# n = int(input()) # 208
# n = str(n) # '208'
# f = 0
# for i in n:
#     if i>='8':
#         f = 1
# if f ==1:
#     print('Mövcud deyil')
# else:
#     print('Mövcuddur')



# sınaq Dim 16 mart

# # 89
# n = abs(int(input())) # 256
# a = n//100
# b = n//10%10
# c = n%10
# kub = a**3+b**3+c**3
# kv = a**2+b**2+c**2
# ferq = kub - kv
# print(ferq)

# 90

# firstMonth = ['Yanvar', # 0
#               'Fevral', # 1
#               'Mart', #2
#               'Aprel', # 3
#               'May', # 4
#               'Iyun' # 5
#               ]
# b = []
# for i in range(len(firstMonth)):
#     a = int(input())
#     b.append(a)
# for i in range(1,len(b)-1):
#     if b[i-1]<b[i]>b[i+1]:
#         print(firstMonth[i],':',b[i],'ədəd')
# else:
#     print('Uğurlu ay yoxdur')


# suQ = 100
# n = int(input())
# if 1<=n<=1000:
#     n = n*100
#     say = n//suQ
# print(say)



# print(55,end=" ")
# print(30,end=' ')
# print(25)
# print(33)
# print(10)

# import math
# x = 1
# y = (5+math.sqrt(x))/abs(x-4)*3
# print(y)

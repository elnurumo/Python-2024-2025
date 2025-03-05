# suallar
#  90, 76, 75, 67,  ---10


# a = [2,45,4,3,60,-4]
# maxsimal = a[0]
# for i in a:
#     if maxsimal<i:
#         maxsimal = i
# print(maxsimal)

# def maxsi(list):
#     maxsimal = list[0]
#     for i in list:
#         if maxsimal<i:
#             maxsimal = i
#     return maxsimal

# a = [2,45,4,3,60,-4]
# f = maxsi(a)
# print(f)

# n = int(input())
# m = n
# s = ''
# while n>0:
#     q = n%10
#     s = s + str(q)
#     n = n//10
# if m == int(s):
#     print('Polindrom')
# else:
#     print('Polindirom deyil')



# 250


# n = int(input()) 

# s = 0
# f = 0
# for i in range(n):
#     a = int(input())
#     if a>0:
#         s = s+a
#     else:
#         n = n-1
# print(s/n)



# print(4)
# print(5,end='')
# print(6)


# 30

# s = 0
# for i in range(1,100):
#     i = str(i)
#     s = s + i.count('3')
# print(s)




# n = input()
# reqemler = '0123456789'
# s = ''
# for i in range(0,len(n)):
#     if reqemler.count(n[i]) == 0:
#         s = s+str(i)
#     else:
#         s = s + n[i]
# print(s)


# a = 5
# b = a
# a = 6
# print(a,b)

# a = [1,2,3]
# b = a
# b.append(4)
# print(a,b)


# 83,84,88,89,90,95,
# 101,102, 105-112

# def f(a,b):
#     s = a*b
#     s = s*a+b
#     return s
# a = 5
# b = 20
# n = f(a,b)
# print(n)

# a = 'informatika'
# b = a.replace('a','')
# print(len(a)-len(b))

# str1 = int(input())
# stn1 = int(input())
# str2 = int(input())
# stn2 = int(input())
# reng1 = ''
# reng2 = ''
# if (str1%2 == 0 and stn1%2==0) or (str1%2 != 0 and stn1%2!=0):
#     reng1 = 'Qara'
# else:
#     reng1 = 'Ağ'
# if (str2%2 == 0 and stn2%2==0) or (str2%2 != 0 and stn2%2!=0):
#     reng2 = 'Qara'
# else:
#     reng2 = 'Ağ'
# if reng1 == reng2:
#     print('Yes')
# else:
#     print('No')



# hstr1 = int(input())
# hstn1 = int(input())
# mstr2 = int(input())
# mstn2 = int(input())
# if (mstr2 == hstr1+2 or mstr2 == hstr1-2) and (mstn2 == hstn1 +1 or mstn2 == hstn1-1):
#     print('Yes')
# elif (mstn2 == hstn1 +2 or mstn2 == hstn1-2) and (mstr2 == hstr1+1 or mstr2 == hstr1-1):
#     print('Yes')
# else:
#     print('No')


# # 1

# n = int(input())
# n =str(n)
# print(len(n))

# 2

# 1/usul
# n = int(input())
# s = 0
# h = 1
# while n>0:
#     q = n%10
#     s = s + q
#     h = h*q
#     n = n//10
# print(s,h)

# # 2/usul

# n = int(input())
# n = str(n)
# s = 0
# h = 1
# for i in n:
#     s = s + int(i)
#     h = h * int(i)
# print(s,h)

# 3

# n = int(input())
# while n%2 == 0:
#     n=n//2
# if n==1:
#     print('Yes')
# else:
#     print('No')

# # 17

# n = int(input())
# n = str(n)
# s = ''
# for i in n:
#     if i!='1' and i!='5':
#         s = s + i
# print(int(s))

# 18

# n = int(input())
# n = str(n)
# s = ''
# for i in range(len(n)-1,-1,-1):
#     s = s + n[i]
# if s == n:
#     print('Yes')
# else:
#     print('no')


# n = 'Salam'
# m = n[::-1] 
# print(m)


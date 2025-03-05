# # 53

# n = -20
# if n>2:
#     if n%2==0:
#         print(n-2)
#     else:
#         print(n-1)
# else:
#     print('Eded 2 den kiçikdir')

# # 3
# a = 5
# b= 7
# a,b = b,a
# print(a,b)

# # 9

# n = int(input()) # 12345
# a = n//10000
# b = n//1000%10
# c = n//10%10
# d = n%10
# firstC = a+b
# lastC = c+d
# print(firstC-lastC)

# # 2

# n = 345
# a = n//100
# b = n//10%10
# c = n%10
# print(a,b,c)


# 4

# n = 24
# a = str(n//10)
# b = str(n%10)
# s = b+a
# print(s)


# # Hefte 2
# # 9

# n = int(input()) # 4542
# a = n//1000
# b = n//100%10
# c = n//10%10
# d = n%10
# if n%a==0 and n%b==0 and n%c==0 and n%d==0:
#     print('Yes')
# else:
#     print('No')

# n =int(input())
# n = str(n)
# f = 0
# if 999<int(n)<10000:
#     for i in n:
#         i = int(i)
#         if int(n)%i!=0:
#             f=1
#     if f == 1:
#         print('No')
#     else:
#         print('Yes')

# # 7

# n = int(input()) # 4554
# if 999<n<10000:
#     a = n//1000
#     b = n//100%10
#     c = n//10%10
#     d = n%10
#     if a==d and b==c:
#         print('Yes')
#     else:
#         print('No')   
# else:
#     print('4 reqemli deyil')         


# 5

# x = float(input())
# y = float(input())
# if y!=x:
#     if x<y:
#         c = x
#         x = (x+y)/2
#         y = (c+y)*2
#     else:
#         c = x
#         x = (x+y)*2
#         y = (c+y)/2
#     print(x,y)

# # 10

# n = int(input()) # 4556
# a = n//1000
# b = n//100%10
# c = n//10%10
# d = n%10
# s = ''
# if a%2!=0:
#     s = s+str(a)
# if b%2!=0:
#     s = s+str(b)
# if c%2!=0:
#     s = s+str(c)
# if d%2!=0:
#     s = s+str(d)
# s = int(s)
# print(s)


# hefte 2
# 13.

# str1 = int(input())
# stn1 = int(input())
# str2 = int(input())
# stn2 = int(input())
# if (str1%2 == 0 and stn1%2==0) or (str1%2 != 0 and stn1%2!=0):
#     a1 = 'Qara'
# else:
#     a1 = 'Ağ'
# if (str2%2 == 0 and stn2%2==0) or (str2%2 != 0 and stn2%2!=0):
#     a2 = 'Qara'
# else:
#     a2 = 'Ağ'
# if a1 == a2:
#     print('Yes')
# else:
#     print('No')


##  horse moves

# hrow = int(input()) # 4
# hcol = int(input()) # 5
# mrow = int(input()) # 6
# mcol = int(input()) 
# if (hrow+2==mrow or hrow-2==mrow) and (hcol+1==mcol or hcol-1==mcol) or (hcol+2 == mcol or hcol-2==mcol) and (hrow+1 == mrow or hrow-1 == mcol):
#     print('Yes')
# else:
#     print('No')


# Hefte 3

# 18, 20, 22-28


# 14

# n = int(input())
# while n%2 == 0:
#     n = n//2
# if n == 1:
#     print('Yes')
# else:
#     print('No')


# # 15

# n = int(input())
# m = str(n)
# m = list(m)
# m.reverse()
# m = ''.join(m)
# m = int(m)
# print(m)


## 17

# n=int(input())
# n = str(n)
# n = list(n)
# b = []
# for i in range(0,len(n)):
#     if int(n[i]) != 1 and int(n[i])!=5:
#         b.append(n[i])
# b = ''.join(b)
# b = int(b)
# print(b)

# 18

# n = int(input()) # 253
# k = str(n) # '253'
# k = list(k) # ['2','5','3']
# k.reverse() # ['3','5','2']
# k = ''.join(k) # '352'
# k = int(k)
# if k == n:
#     print('Yes',k,n)
# else:
#     print('No',k,n)


# # 3 reqemli

# n = 252
# a = n//100
# b = n//10%10*10
# c = n%10*100
# s = a+b+c
# if s == n:
#     print('Yes')
# else:
#     print('No')


# n = int(input())
# m = 0
# while n>0:
#     q = n%10
#     if m<q:
#         m=q
#     n = n//10
# print(m) 


# 
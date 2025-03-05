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

# 2
n = 324
n = str(n)
a = n[0]
b = n[1]
c = n[2]
s = a+' '+b+' '+c
print(s)
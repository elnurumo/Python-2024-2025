# hefteler 3  hefteler 2-8
# 21

# f = []
# for i in range(100,1000):
#     a = i//100
#     b = i//10%10
#     c = i%10
#     s = a**3+b**3+c**3
#     if i == s:
#         f.append(i)
# print(f)

# # hefteler 2 
# # 8

# n = int(input()) # 25765
# a = n//10000
# b = n//1000%10
# c = n//100%10
# d = n//10%10
# e = n%10
# if a<b and b<c and c<d and d<e:
#     print('Yes',n)
# else:
#     print('No',n)

# 28

# def checkSimple(x):
#     f = 0
#     for i in range(2,x//2+1):
#         if x%i==0:
#             f=1
#     return f

# n = int(input())
# for i in range(2,n):
#     if checkSimple(i) == 0:
#         print(i)


# 26

# n =int(input())
# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

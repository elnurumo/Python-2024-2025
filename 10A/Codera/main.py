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

s = 0
for i in range(1,100):
    i = str(i)
    s = s + i.count('3')
print(s)
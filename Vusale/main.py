# # 85

# s = 0
# for i in range(1,201):
#     if i%5==0 and i%3!=0:
#         s = s+1
# print(s)

# 86

# n = float(input())
# tam = ''
# if n>0:
#     n = str(n) # '5.6'
#     for i in range(0,len(n)):
#         if n[i] == '.':
#             tam = n[0:i]
#         if n[i] == '.':
#             kesr = '0' + n[i:]
# else:
#     n = str(n)
#     for i in range(0,len(n)):
#         if n[i] == '.':
#             tam = int(n[0:i]) - 1
#         if n[i] == '.':
#             kesr = 10 - int(n[i+1:])
#             kesr = '0.' + str(kesr)
# print(tam,kesr)


# # 86

# n = float(input())
# if n>0:
#     tam = int(n)
#     kesr = n - tam
# elif n<0:
#     tam = int(n-1)
#     kesr = n-tam
# print(tam,kesr)

## 87

# n = int(input())
# f = 1
# if n%2 == 0:
#     for i in range(1,n+1):
#         f = f*i
#     print(f)
# else:
#     k = n**2*2
#     print(k)


# 88

# s = 0
# for i in range(100,1000):
#     a = i//100
#     b = i//10%10
#     c = i%10
#     if a+b+c >=12 and i%2 == 0 and i%5 == 0:
#         s = s+1
# print(s)


# Zehra's code fixed
# s = 0
# for i in range(100,1000):
#     rqmCem = 0
#     eded = i
#     while i>0:
#         a = i%10
#         rqmCem = rqmCem + a
#         i = i//10
#     if rqmCem >=12 and eded %5==0 and eded %2==0:
#         s = s+1
# print(s)


# # 89

# n = int(input())
# k = -1
# f = 1
# s = 0
# for i in range(1,n+1):
#     f = f*i
#     s = s + k*1/f**i
#     k = -k
# print(s)


# # 90

# n = int(input())
# s = 0
# k = 1
# if n>=3:
#     for i in range(3,n+1,2):
#         s = s + k*i
#         k = -k
#     print(s)

# # 93

# n = int(input())
# n = str(n)
# b = []
# for i in n:
#     i = int(i)
#     if i %2 != 0:
#         b.append(i)
# if len(b) >0:
#     print(min(b))
# else:
#     print('Ədəddə tək rəqəm yoxdur')


# # 94

# n = input() # AA
# reqemler = '0123456789ABCDEF'
# l = len(n) - 1
# onluq = 0
# for i in n:
#     onluq = onluq + reqemler.find(i)*16**l
#     l = l-1
# print(onluq)

# # 95

# n = int(input())
# n = str(n)
# l = len(n)-1
# onluq = 0
# for i in n:
#     onluq = onluq + int(i)*8**l
#     l = l-1
# print(onluq)


# 96

# m = int(input())
# for i in range(100,1000):
#     a = i//100
#     b = i//10%10
#     c = i%10
#     if m == a*b*c and a!=1 and b!=1 and c!=1:
#         print(i)
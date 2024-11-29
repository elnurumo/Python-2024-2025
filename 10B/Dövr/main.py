# float, integer, string -- setir, list, boolean ---> Data Type (Data tipler) 

# n = ["Alma", 24, 2.5, True, [2,3,5]]
# n = str(245)

# for i in n:
#     print(i)

# boolean  True, False

# while True:
#     print(1)

# n = 5 == 4
# print(n)

# n = '2' // 2
# print(n)


# for i in 'salam':
#     print(i,end=" ")

# print('s', end=" ")
# print('a', end=" ")
# print('l')

# print('s','a','l', sep="\n")


# # ixtiyari reqemli ededin reqemleri cemini tap

# n = int(input()) # 345
# s = 0
# while n>0:
#     q = n % 10
#     s = s + q
#     n = n // 10
# print(s)

# 80,81,83,90,102,103,104,72,73,84,110,111,92 


# # 71

# n = int(input('ededin sayi: ')) # 3
# s = 0
# for i in range(0,n):
#     a = int(input(f'{i+1}. ededi daxil et: '))
#     s = s+a
# edediOrta = s/n
# print(edediOrta)

# # 72
# n = int(input())
# b = []
# # print(b)
# for i in range(1,n+1):
#     a = int(input(f'{i}. ededi daxil et: '))
#     b.append(a)
# print(min(b))

# # 74

# for i in range(1,1000,2):
#     print(i)

# # 75
# a = [15,12,16,11,9]
# for i in a:
#     if i%2 != 0:
#         print(i**2)

# 80

# n = int(input()) # 24
# s = 0
# if n>1:
#     for i in range(2,n//2+1):
#         if n%i==0:
#             s = s+1
#     if s>0:
#         print('Murekkebdir')
#     elif s == 0:
#         print('Sadedir')
# elif n == 1:
#     print('1 ne sadedir nede murekkeb')



# n =int(input()) # 4
# b = []
# for i in range(0,n):
#     a = int(input())
#     b.append(a)
# print(max(b))

# # listin içindən minimum ədədi tap

# a = [45,23,35,-4,5]
# # print(min(a))
# mini = a[0]
# for i in a:
#     if i<mini:
#         mini = i
# print(mini)

# 94

# n = input().upper() # AA
# reqemler = '0123456789ABCDEF'
# m = len(n)-1 # 1
# onluq = 0
# for i in n:
#     onluq = onluq + reqemler.find(i)*16**m
#     m=m-1
# print(onluq)
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

# 80,


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

# 


# # 108

# n = int(input()) # 208 
# m = str(n) # '208'
# f = 0
# for i in m:
#     if i>='8':
#         f = 1
# if f == 1:
#     print('Mövcud deyil')
# else:
#     print('Mövcuddur')


# # 68

# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = s + 1/i**2
# print(s)

# # 69

# n = int(input())
# s = 0
# for i in range(1,n+1,1):
#     s = s + (1/i)**i
# print(s)

# # 81

# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = s + (-1)**(i+1)*i*(i+1)
# print(s)

# 83


# s = 0
# for x in range(-10,11):
#     if x>3:
#         y = x**2-5*x+6
#     else:
#         y = (x+2)**2
#     if y % 3 ==0:
#         s = s + 1
# print(s)

## 84

# a = [3,4,2,1,6,9,7,8,12,10,5,14]
# s = 0
# c = 0
# for i in range(0,len(a)):
#     if i%2 != 0 and a[i] % 2 == 0:
#         s = s + 1
#         c = c + a[i]
#     elif i%2 == 0 and a[i]%2 != 0:
#         s = s + 1
#         c = c + a[i]
# edediOrta = c/s
# print(edediOrta,c,s)

## 89

# n = int(input())
# s = 0
# k = -1
# f = 1
# for i in range(1,n+1):
#     f = f * i
#     s = s + k*1/f**i
#     k = -k
# print(s)


# # 90

# n = int(input())
# s = 0
# k = 1
# if n >=3:
#     for i in range(3,n+1,2):
#         s = s + k*i
#         k = -k
#     print(s)

# # 92

# s = 0
# for i in range(100,1000,2):
#     a = i//100
#     b = i//10%10
#     if a%2 == 0 and b %2 == 0:
#         s = s + i
# print(s)


# # 102

# x = int(input())
# n = int(input())
# s = 0
# f = 1
# for i in range(1,n+1):
#     f = f * i
#     s = s + (-1)**(i+1)*x**i/f
# print(s)

# # 103

# n= int(input())
# s = 0
# for i in range(1,n+1,2):
#     s = s + i*(i+1)*(i+2)
# print(s)

# # 105

# n = input() # str tipindedi sade halda
# reqemler = '0123456789'
# s = 0
# for i in n:
#     if reqemler.count(i) == 1:
#         s = s + 1
# print(s)

# # 110

# azn = 100
# ay = 0
# while azn<=200:
#     azn = azn + azn*0.05
#     ay = ay + 1
# print(ay,azn)

# # 111

# x = 29
# g = 1
# while x<=100:
#     x = x + (x+5)
#     g = g + 1
# print(g,x)

# 112

n = int(input())
s = 0
while n>0:
    n = str(n)
    a = int(n[0])
    b = int(n[len(n)-1])
    c = a+b
    n = int(n) - c
    s = s+1
print(s)
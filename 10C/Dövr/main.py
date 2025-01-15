# n = 'Salam Dunya'

# for i in range(0,100):  # for yeni sayğacli dövr
#     print(n)

# i = 0
# while i<100:
#     print(i,n)
#     i = i+1

# for i in range(0,100,5):
#     print(i)


# # müxtəlif rəqəmli n natural ədədin rəqəmləri cəmini tap. meselen n = 456  cem = 15   n = 3456   cem = 18

# #  1. üsul

# n =  int(input()) # 5456
# c = 0
# while n>0:
#     q = n%10
#     c = c+q
#     n = n//10
# print(c)

# # 2. üsul
# n = int(input()) # 356
# n = str(n)
# c = 0
# for i in n:
#     i = int(i)
#     c = c+i
# print(c)


# Suallar 
# 
# 


# 17
#   salam
# s1 = malas

# 18


#  find methodu

# n = 'salam'.find('a',)
# print(n)


# a = [45,4,2,7,15]
# #    0  1 2 3  4
# # length len()
# l = len(a)-1
# print(l)
# c = a[l]
# print(c)


# a = 'Kenan'
# f = a.find('n',3,len(a))
# print(f)

# a = [] # list 
# a.append(5)
# a.append(4)
# a.append(4)
# a.append(5)
# print(a)

# a = [5,4,5,4,4]
# a.remove(4)
# print(a)

# a = [4,5,3,2]
# a.insert(3,20)
# print(a)

# c = max(a)
# print(c)

# a = [4,5,6,7,2,-5,-45,0]
# minimum = a[0]
# for i in a:
#     if minimum>i:
#         minimum = i
# print(minimum)




# a=[4,5,6,7,2]
# maxsimal = a[0]
# for i in a:
#     if maxsimal<i:
#         maxsimal=i
# print(maxsimal)


# Split vs List

# Hər ikisidə str --->> listə çevirir

# a = "Hello world"
# a = list(a) # Qəssab Tikələdi
# print(a)

# # Split
# a = 'Kenan'
# a = a.split('n')
# print(a)

# a = [2,4,6]
# b = 5
# a.append(b)
# print(a)

# m = []
# index = 2
# element = 5
# m.insert(0,6)
# m.insert(index,element)
# print(m)

# a = 'Salam dunya'
# b = a
# a = list(a)
# print(a)
# b = b.split()
# print(b)

# a = ['Salam','Dunya']
# a = '-'.join(a) # list den str e çevirir
# print(a)

# Suallar




# # 67
# n = int(input()) # 1555
# n = str(n) # '1555'
# a = int(n[1])  #onluq
# b = int(n[2])  # teklik
# if b%2==0:
#     c = a+b
# else:
#     c = a*b
# print(c)

# # 68

# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = s + 1/i**2
# print(s)

# # 69
# n = int(input())
# s = 0
# for i in range(1,n+1,2):
#     s = s + (1/i)**i
# print(s)



# # 72

# n = int(input()) # ededlerin sayi
# b = []
# for i in range(0,n):
#     a = int(input())
#     b.append(a)
#     # print(b)
# print(min(b))

# 83,84,88,89,90,95,
# 101,102, 105-112


# # 73
# n = int(input())
# b = []
# for i in range(n):
#     a = int(input())
#     b.append(a)
# print(max(b))

# # 76

# n = int(input('Doğulduğun ay: '))
# if n==12 or n==1 or n==2:
#     print('Qışdadır')
# elif n==3 or n==4 or n==5:
#     print('yazdadır')
# elif n==6 or n==7 or n==8:
#     print('Yaydadır')
# elif n==9 or n==10 or n==11:
#     print('Payızdadır')
# else:
#     print('Belə bir ay yoxdur')


# # 78

# n = int(input('Ededlerin sayi: ')) # say
# k = [] # tek
# m = [] # cut
# for i in range(n):
#     a = int(input('Ededi daxil et: '))
#     if a%2==0:
#         m.append(a)
#     else:
#         k.append(a)
# print(m,k)


# # 79

# n = int(input()) # 205
# s = 0 # 0 ların sayı üçün
# while n%10==0: 
#     s = s+1
#     n = n//10
# print(s)

# # 80

# n = int(input())
# s = 0
# if n>1:
#     for i in range(2,n//2+1):
#         if n%i==0:
#             s = s+1
#     if s>0:
#         print('Mürəkkəb')
#     else:
#         print('Sadədir')



# 81

# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = s + (-1)**(i+1)*i*(i+1)
# print(s)

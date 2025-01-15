# a = 'Salam'
# # a = a.find('a')
# a = a[1::2]
# print(a)

# a = [1,2,3,45]
# a.append(5)
# a = a.count(2)
# print(a)

# a = 'aaaaabbbbb'
# a = a.replace('a','*')
# a = a.replace('b','a')
# a = a.replace('*','b')

# print(a)

# a = [1,2,3,4]
# b = a
# b.append(5)
# del a[0]
# b = a + [2,3,4]
# b.append(10)
# print(a,b)

# a = [3,2,1,0,45]
# maxsimal = a[0]
# for i in a:
#     if maxsimal < i:
#         maxsimal = i
# print(maxsimal)

# split vs list

# ikiside str-den listde çevirir
# list qessab
# a = 'Hello world'
# a = list(a)
# print(a)

# # split

# a = 'Hello world'
# a = a.split()
# print(a)

# # join

# a = ['051','391' , '23','33']
# a = '-'.join(a)
# print(a)

# Etrafli

# n=input()
# n=n.split()
# for i in n:
#     print(len(i))
# 
# 51ci sual
# amil=16
# eltac=amil/2
# anar=eltac+5
# edediorta=(amil+eltac+anar)/3
# print(edediorta)
# 
# 52ci tap
# a=['Anar','Amil','Eltac']
# cem=0
# for i in a:
#     cem=cem+len(i)
# print(cem)
# 
# 53cu tap
# a='1231451617189'
# a=a.replace('1','bir')
# print(a)
# 
# 54cu tap
# x=[13,27,19,23]
# b=[]
# cem=0
# for i in x:
#     a=i//10
#     c=i%10
#     cem=a+c
#     b.append(cem)
# print(b)
# 
# 55ci tap
# n=input()
# n=n.split()
# print(len(n))
# 
# 56ci tap
# n=input()
# s=0
# for i in n:
#     if n.count(i)==1:
#         s=s+1
# print(s)
# 
# 57ci tap
# n=['salam','necesen','paka']
# m=[]
# for i in n:
#     a=len(i)
#     m.append(a)
# print(max(m))
# 
# 58ci tap
# n=input()
# n=n.split()
# sira=0
# for i in n:
#     a=i.count('w')
#     sira=sira+1
#     print('daxil edilmis cumlenin',sira,'sayli sozunde',a,'sayda w simvolu movcuddur')
# 
# 59cu tap
# n=int(input())
# k=len(str(n))
# if k>2:
#     n=str(n)
#     n=list(n)
#     n.sort()
#     n.reverse()
#     n=''.join(n)
#     n=int(n)
#     print(n)
# 
# 60ci tap
# a=[12,45,23,16,121,34,66,15]
# s=0
# for i in a:
#     i=str(i)
#     if i.count('1')>0:
#         s=s+1
# print(s)
# 
# 61ci tap
# n=input()
# s=''
# a='0123456789'
# for i in n:
#     if a.count(i)==0:
#         s=s+i
# print(s)

# Suallar 
#  - 9-10

# 66-68,73-75,89,90,80,78, 87,83,82 --> 11


# a = 5
# b = 5
# c = a==b
# print(c)

# if 5>=4:
#     print('1')
#     if 5==5:
#         print('2')
#     elif 6>5:
#         print('3')
# else:
#     print('4')


# while

# a = 5
# while True:
#     print('Hello')
#     # a = a - 1 

# a = 'Zeynəb'
# s = 0
# for i in a:
#     if 'y' == i:
#         s = s + 1
# print(s)

# s = a.count('y',3,5)
# print(s)


# a = '        salam      '
# a = a.strip()
# print(a) 

# a = 5
# b = 4
# x = '5'
# y = '4'
# c = a+b
# z = x + y
# print(c) # 9
# print(z) # 54

# a = 'Salam'
# c = a.find('a')
# print(c)

# a = 'Informatika'
# a = a.replace('t','s')
# a = a.replace('k','y')
# print(a)

# a = 'Salam'
# a = a.replace('a','b')
# print(a)


# a = 'Zeyneb'
# for i in a:
#     print(i)

# a = 'Salam Dunya'

# for i in range(1000):
#     # print(i+1,'-ci',a)
#     print(f'{i+1}-ci {a}')



# list vs split
# her ikisi setirden liste çevirir

# arr = [1,2,3,'Zeyneb',6]
# a = 'Hello world'
# # a = list(a)
# a = a.split()
# print(a)

# join

# a = ['+994','51',"391",'23','33'] # listin içi mütləq str tipində olmalıdı
# # a = [1,2,3,4]  eror verir chunki int tipindedi
# a = ' '.join(a)
# print(a)


# 50
# n=input()
# n=n.split()
# for i in n:
#    s=len(i)
#    print(s)


# #51
# Amil=16
# Eltac=Amil/2
# Anar= Eltac+5
# S= (Amil+Eltac+Anar)/3
# print (S)

# # 52

# a=['Amil','Anar','Eltac']
# s=0
# for i in a:
#     s=s+len(i)
# print(s)



# Suallar


# a = 'salam'
# b = a.find('b')
# print(b)

# a = 'Informatika'
# a = a.replace('tika','siya')
# print(a)


# 
# 57

# a = ['Elnur','Zeynəb']
# b = []
# for i in a:
#     s = len(i)
#     b.append(s)
# print(max(b))

# # 58

# n = input().split(' ') # windows view www
# print(n)
# s = 1
# for i in n:
#     c = i.count('w')
#     print('daxil edilmiş cümlənin',s,
#           'saylı sözündə',2,
#           "sayda w simvolu mövcuddur")
#     s = s + 1

# # 63

# b = []
# for i in range(1,8):
#     a = int(input(f'{i}. gün: '))
#     b.append(a)
# print(b)

# # 65

# a = [351,648,776,918]
# for i in a:
#     i = str(i)
#     a = int(i[0])
#     b = int(i[len(i)-1])
#     c = (a+b)*2
# print(c)

# # 72

# a = [2314,342,1206,4321,57,78965]
# for i in range(0,len(a)):
#     a[i] = str(a[i])
#     maxi = int(max(a[i]))
#     mini = int(min(a[i]))
#     c = maxi**2+mini**2
#     a[i] = c
#     # print(i,c)
#     # print(type(i))
# print(a)


# # 73

# a = [2345,421,356,876,45678,43321]
# for i in range(0,len(a)):
#     a[i]=str(a[i])
#     b=a[i]
#     x=int(b[0])
#     y=int(b[len(b)-1])
#     c=x**2+y**2
#     print(c)

# # 74

# a = input().split(' ') #
# n = []
# for i in a:
#     s = i.count('a') 
#     n.append(s)
# print(n)

#

# print(1)
# print(1,end=' ')
# print(1)
# print(1)

# # 56

# n = input()
# b = []
# for i in n:
#     if n.count(i) == 1:
#         b.append(i)
# print(len(b)) 

# 60

# a = [12,45,23,16,121,34,66,15]
# s = 0
# for i in a:
#     i = str(i)
#     if i.count('1') >= 1:
#         s = s + 1
# print(s)

# # 62 

# a = [3,4,5,6,7,8,2,9,1,12]
# s = sum(a)
# edediOrta = s/len(a)
# for i in a:
#     if i>edediOrta:
#         print(i)

# # 63
# a = [1,2,3,4]
# for i in range(1,8):
#     n = int(input('Mehsulun sayi: '))
#     a.append(n)
# print(a)


# a = 'Elnur'
# a = a.replace('nur','mir')
# print(a)

# # 70

# n = input()
# s = 0
# b = []
# for i in n:
#     if i == 's':
#         s = s+1
#     else:
#         b.append(s)
#         s = 0
# print(max(b))


# #  suallar 3
# n = input().split() # happy new year
# s = ''
# for i in range(0,len(n)):
#     if n[i].count('a') >= 1 and i != len(n)-1:
#         s = s + n[i] + ',' + " "
#     elif n[i].count('a') >= 1:
#         s = s+ n[i]
# print(s)

# 4

# b = input().split()
# miniUz = len(b[0])
# for i in b:
#     if len(i) < miniUz:
#         miniUz = len(i)
# print(miniUz)

# m = 'beli'
# b = []
# while m == 'beli':
#     n = input('Söz daxil et: ')
#     b.append(n)
#     m = input('Davam etmək istəyirsən? (beli ve ya xeyir): ')
# print(b)


s = 0
for i in range(1001,10000,2):
    a = i//1000
    b = i//100%10
    c = i//10%10
    if a %2 !=0 and b%2!=0 and c%2!= 0:
        s = s+i
print(s)



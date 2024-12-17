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


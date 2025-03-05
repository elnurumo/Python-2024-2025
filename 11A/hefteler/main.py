#  HEFTE 2

# # 3
# n = int(input())
# if n%2 == 0:
#     print('Cütdür')
# else:
#     print('tekdir')

# # 4

# x = float(input())
# y = float(input())
# if x>y:
#     print(x)
# elif y>x:
#     print(y)

# # 5

# x = float(input())
# y = float(input())
# if x!=y:
#     if x<y:
#         x,y = (x+y)/2, (x+y)*2
#     else:
#         y,x = (x+y)/2, (x+y)*2
#     print(x,y)


# # 6
# n = int(input())
# m = str(n)
# q = len(m)
# a = int(m[0])
# b = int(m[1])
# c = int(m[2])
# s = a**q+b**q+c**q
# if n==s:
#     print('Yes')
# else:
#     print('No')

# 7

# n = int(input()) # 3245
# m = str(n)
# a = m[0] # 3
# b = m[1] # 2
# c = m[2] # 4
# d = m[3] # 5
# s = int(d+c+b+a)
# if n==s:
#     print('Yes polind')
# else:
#     print('No Polind')

# # 8

# n = 12345
# a = n//10000
# b = n//1000%10
# c = n//100%10
# d = n//10%10
# e = n%10
# if a<b<c<d<e:
#     print('Yes')
# else:
#     print('No')


# # 9

# n = 1234
# a = n//1000
# b = n//100%10
# c = n//10%10
# d = n%10
# if n%a==0 and n%b==0 and n%c==0 and n%d==0:
#     print('Yes')
# else:
#     print('No')


# 13

# str1 = int(input())
# stn1 = int(input())  # 1ci xana
# str2 = int(input())
# stn2 = int(input()) # 2ci xana
# if ((str1 + stn1)%2 == 0 and (str2+stn2)%2 == 0) or ((str1 + stn1)%2 != 0 and (str2+stn2)%2 != 0):
#     print('Yes')
# else:
#     print('No')


# Horse moves

# hstr = int(input())
# hstn = int(input())
# mstr = int(input())
# mstn = int(input())
# if (hstr+2==mstr or hstr-2==mstr) and (hstn+1 == mstn or hstn-1 == mstn):
#     print('Yes')
# elif (hstr+1==mstr or hstr-1==mstr) and (hstn+2 == mstn or hstn-2 == mstn):
#     print('Yes')
# else:
#     print('No')

# n = '5244'
# print(max(n))

# 15

# n = int(input())  # 123456 --->654321
# n = str(n)
# s = ''
# for i in n:
#     s = i + s
# s = int(s)
# print(s)


# n = int(input()) #123456
# s = ''
# while n>0:
#     k = str(n%10)
#     s = s + k
#     n = n//10
# print(s)

# n = int(input())
# n = list(str(n))
# n.reverse()
# n = ''.join(n)
# n = int(n)
# print(n)\



# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def sayHello(self):
#         print('Hello', self.name)

# n  = Person('Ülvi',17)
# n.sayHello()



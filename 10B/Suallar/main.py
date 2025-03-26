# # a = ['alma','armud','nar']
# # b = []
# # for i in a:
# #     c = len(i)
# #     b.append(c)
# # print(min(b))

# # # 6
# # # 1-ci üsul
# # s =0
# # for i in range(1001,10000,2):
# #     a = i//1000
# #     b = i//100%10
# #     c = i//10%10
# #     if a%2!=0 and b%2!=0 and c%2!=0:
# #         s = s+i
# # print(s)

# # # 2-ci üsul

# # s = 0
# # for i in range(1001,10000,2):
# #     i = str(i)
# #     if int(i[0])%2!=0 and int(i[1])%2!=0 and int(i[2])%2!=0:
# #         s = s+int(i)
# # print(s)



# # 12

# def sadeorMrkkb(n):
#     f = 0
#     for i in range(2,n//2+1):
#         if n%i==0:
#             f = 1
#     return f
# n = int(input()) # 35
# fn = 0
# for i in range(2,n//2+1):
#     if n%i==0:
#         fn = 1
# if fn == 1:
#     n = n-1
#     while sadeorMrkkb(n) == 1:
#         n = n-1
# else:
#     n = n+1
#     while sadeorMrkkb(n) == 1:
#         n = n+1
# s = 0
# for i in str(n):
#     i= int(i)
#     s = s+i
# print(s)


# # Rekursiv Function

# def rekursiv(n):
#     if n<1:
#         return 1
#     return n + rekursiv(n-1)

# print(rekursiv(6))


# Part 2


# # 1

# n = int(input())
# c = 0
# s = 0
# while n>0:
#     q = n%10
#     c = c + q
#     s = s + 1
#     n = n//10
# a = s
# b = c
# h = a*b
# while a!=b:
#     if a>b:
#         a = a-b
#     elif b>a:
#         b =b-a
# ebob = a
# ekob = h/a
# print(ebob+ekob)


# # strip
# # 3
# n = input().split() # ['5','6']
# for i in range(0,len(n)):
#     n[i] = int(n[i])
# b = 0
# s = 0
# while b<=30:
#     a = max(n)
#     b = b+a
#     new = a//2
#     n.remove(a)
#     n.append(new)
#     s = s + 1
# print(s,'Dövr bəs edir.',)


# n = int(input())
# if n>2:
#     if n%2==0:
#         print(n-2)
#     else:
#         print(n-1)
# else:
#     print('Qaqa nağarsan?')


# # 19

# n = int(input())
# sade_vuruq = 2
# while n > 1:
#     if n%sade_vuruq==0:
#         n = n//sade_vuruq
#         print(sade_vuruq)
#     else:
#         sade_vuruq = sade_vuruq + 1


# # 17
# a = [2,3,-9,5,-1,4,7,-4,6]
# for i in range(0,len(a),2):
#     if a[i]< 0:
#         print(abs(a[i])) 


# # 
# n = int(input()) 
# n = str(n)
# f = 0
# for i in n:
#     i = int(i)
#     if i!=1 and i!=0:
#         f = 1
# if f == 0:
#     print('Yes')
# else:
#     print('No')

        


# n = int(input()) # 14276
# n = str(n)
# s = ""
# for i in n:
#     if i != "4" and i!="7":
#         s = s+i
# print(s)

# n = int(input()) # 14276
# n = str(n)
# s = []
# for i in n:
#     if i != "4" and i!="7":
#         s.append(i)
# print(''.join(s))



# n = int(input())
# if n>0:
#     m = n**0.5
#     if int(m) == n**0.5:
#         print('Yes')
#     else:
#         print('No')
# else:
#     print("Ədəd natural ədəd olmalıdır")



    
# n = int(input())
# a = ['Bazar ertesi','Ç.A', "Ç", "C.a","C","Ş","Bazar"]
# #      0              1     2     3    4   5
# if 1<=n<8:
#     print(a[n-1])
# else:
#     print('Belə bir gün yoxdur')




# 
# a = 'AbACAdFEa'
# b= [] # ['b', 'CC','ddd','FFFF','EEEEE']
# #         0    1     2     3       4
# k=1
# for i in a:
#     if i!="A" and i!="a":
#         b.append(i*k) # 'b' * 1
#         k=k+1  # 5
# print(len(b[2])+len(b[len(b)-1]))
#  #        3    +   5   =  8      


# def fibonacci(x):
#     a,b = 0,1
#     for i in range(0,n):
#         a , b = b , a+b
#     return a

# n = int(input())
# if n % 2==0:
#     print(fibonacci(n)**2)
# else:
#     print(fibonacci(n))
# print(fibonacci(n)**2 if n%2==0 else fibonacci(n))


# 2

# a = input().split() #
# s = 0
# for i in a:
#     if a.count(i) == 1:
#         s = s+1
# print(s)




# 3

# k = 2
# a = [1,2,3,4,5]
# l = len(a)-1
# for i in range(k):
#      a.insert(0,a[l])
# print(a[0:l+1])

# 5


# #  EBOB
# a =int(input())
# b = int(input())
# C = a*b
# while a!=b:
#     if a>b:
#         a = a-b
#     else:
#         b = b-a
# ekob =C/a
# print(ekob)


# #  16 lıqdan 10luğa

# n = input() # AA
# reqemler = '0123456789ABCDEF'
#          #  0123456789101112
# l = len(n)-1
# onluq = 0
# for i in n:
#     onluq = onluq + reqemler.find(i)*16**l
#     l = l-1
# print(onluq)


# def reversedNumber(x):
#     x = str(x)
#     x = list(x)
#     x.reverse()
#     x = ''.join(x)
#     x = int(x)
#     return x

# a = int(input())
# b = int(input())
# s = reversedNumber(a) + reversedNumber(b)
# s = reversedNumber(s)
# print(s)

# # 

# n = [3,8,1,5,6]
# mini = min(n)
# maxi = max(n)
# minIndex = n.index(mini)
# maxIndex = n.index(maxi)
# print(abs(minIndex-maxIndex)) 


# # 89

# n = int(input())
# n = abs(n)
# a = n//100
# b = n//10%10
# c = n%10
# kub = a**3+b**3+c**3
# kvdrt = a**2+b**2+c**2
# print(kub+kvdrt)


# # 90

# firstMonths = ["Yanvar",'Fevral', 'Mart', 'Aprel', 'May','Iyun' ]
# b = []
# f = 0
# for i in range(len(firstMonths)):
#     a = int(input())
#     b.append(a)
# for i in range(1,len(b)-1):
#     if b[i-1] < b[i] > b[i+1]:
#         print(firstMonths[i], ':', b[i], 'ədəd')
#         f = 1
# if f == 0:
#     print('Uğurlu ay yoxdur')



# # # 

# n = int(input()) # 2548
# kub = 0
# kvadrat = 0
# while n>0:
#     q = n%10
#     kub = kub + q**3
#     kvadrat = kvadrat + q**2
#     n = n//10
# print(kvadrat+kub)


# # 5

# a = int(input())
# b = int(input())
# c = a*b
# while a!=b:
#     if a>b:
#         a = a-b
#     else:
#         b = b-a
# ekob = c/a
# print(ekob)

# 1

# def fibonacci(x):
#     a,b = 0,1
#     for i in range(x):
#         a,b = b, a+b
#     return a

# n = int(input())
# a = fibonacci(n)
# if n%2 == 0:
#     a = a**2
#     print(a)
# else:
#     print(a)


# a = 5
# b = a
# c 


# 


# print(5, end=' ')
# print(3,end='-')
# print(4)
# print(2)

# a = 5
# b = a
# a = 6
# print(a,b)

# a = [2,4,6]
# b = a
# a.append(7)
# b = b+[3,4,5] # qrılma nöqtəsi
# print(a,b)

# a = [2,4,6]
# b = [2,4,6]
# a.append(7)
# print(a,b)


# n = 5
# n = list(str(n))
# print(n)

# def f(x,y):
#     return x+y*x-y
# x = 5
# y = 6
# print(f(6,5))


# #  method nedi? funksiya nedi?

# a = []
# a
# print(a)


# # join methodu
# a = ['Toğrul', "Fexri", 'Yusif', 'Valide']
# x = ' '.join(a)
# print(x)


# # split vs list

# a = 'Salam dunya necesen sagol getdim'
# # x = list(a) qessab
# x = a.split('e')
# print(x)


# c = '7'=='4'
# print(c)

# m = ['A','a','b','B']
# print(max(m))

# Suallar ------->>>>>>>
# 70

# a = [2,3,4,5]
# b =  [2,3,4,5]
# a.append(23)
# print(a,b)

# print(2,3,4,5, sep='@')


# print(1,end=' ')
# print(2,end=' ')
# print(3,end=' ')
# print(4,end=' ')
# print()
# print(5)

# # 57

# a = ['Toğrul','Fexri', 'Revane', 'Yusif']
# b =[]
# for i in a:
#     b.append(len(i))
# print(max(b))

# # 59

# n = int(input()) # 345
# k = len(str(n))
# if k > 2:
#     n = str(n)
#     n = list(n)
#     n.sort()
#     n.reverse()
#     n = ''.join(n)
#     n = int(n)
#     print(n)

# # 63


# b = []
# for i in range(1,8):
#     n = int(input(f'{i}. gün: '))
#     b.append(n)
# print(b)

# # 64

# n = int(input())
# if n>0:
#     n = list(str(n))
#     n.reverse()
#     n = ''.join(n)
#     n = int(n)
#     print(n)
# else:
#     print('Eded musbet deyil')



## 66

# n = input()
# n = n.replace('a','*')
# n = n.replace('b','a')
# n = n.replace('*','b')
# print(n)


# # 70

# n = input() # ssbbbsssbc
# s = 0
# b = []
# for i in n:
#     if i == 's':
#         s = s + 1
#     else:
#         b.append(s)
#         s = 0
# print(max(b))
    


# ## 72

# a = [2314,342,1206,4321,57,78965]
# for i in range(0,len(a)):
#     b = str(a[i])
#     ma = int(max(b))
#     mi = int(min(b))
#     c = ma*ma + mi*mi
#     a[i] = c 
# print(a)


# # 
# n = int(input())
# s = 0
# m = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         s = s+i
#         m = m + 1
# print(s/m)


# 

# s = 0
# for i in range(1001, 10000,2):
#     a = i//1000
#     b = i//100%10
#     c = i//10%10
#     if a%2!=0 and b%2!=0 and c%2!=0:
#         s = s+i
# print(s) 


# Suallar
# 74,60,63,     ----55
# 63-93, 80,92  11.4



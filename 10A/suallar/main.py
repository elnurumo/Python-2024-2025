# n = int(input())
# n = str(n)
# f = 0
# s = 0 
# for i in n:
#     if n.count(i) > 1:
#         f=1
# if f == 1:
#     print('Reqemleri tekrarlanir')
# else:
#     for i in n:
#         if max(n) != i:
#             s = s + int(i)
#     print(s)


# 1

# n = int(input())
# s = ''
# n = str(n)
# for i in range(0,len(n)):
#     if i != len(n)-1:
#         s = s+n[i]+'1'
#     else:
#         s = s + n[i]
# print(int(s)**2)


# n = int(input())
# n =str(n)
# n = '1'.join(n)
# print(int(n)**2)

# # 2

# a = [8,4,5,8,15,68,19,15,19]
# b = [8,19,15,5,2,367]
# c = []
# for i in b:
#     if a.count(i) > 0:  
#         if c.count(i) == 0:
#             c.append(i)
# print(c, len(c))

# 3

# n = input().split()
# a = []
# for i in n:
#     m = i.replace('a',',')
#     a.append(m)
# # for i in range(0,len(a)):
# #     a[i] = ','.join(a[i])

# a = ' '.join(a)
# print(a)

# n = input().split()
# a = []
# for i in n:
#     if  i.count('a') >= 1:
#         a.append(i)
# a = ','.join(a)
# print(a)

# 4

# a = ['Valide','Yusif','Toğrul',"Fəxri"]
# b = []
# for i in a:
#     b.append(len(i))
# print(min(b))

# 5
# n=input() # aaaajjaaaaa
# a=[]
# s=0
# if n.count('a') > 0 :
#     for i in n:
#         if i=='a':
#             s=s+1
#         else:
#             s=0
#         a.append(s)
#     print(max(a))

# 7

# n = int(input())  # 2415
# k = list(str(n)) # ['2','4','5']
# k.sort() # ['2','4','5']
# k = "".join(k) # '245'
# k = int(k) #1245
# if k==n:
#     print('Artan sıra ilə düzülüb')
# else:
#     print('Artan sıra ilə düzülməyib')


# # 
# s = 0
# for i in range(1001,10000,2):
#     a = i//1000
#     b = i//100%10
#     c = i//10%10
#     if a%2!=0 and b%2!=0 and c%2!=0:
#         s = s + i
# print(s)




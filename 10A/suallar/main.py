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


# 


# 14

# m = 2
# n = 6
# k = 9
# if m+n<k:
#     print(k//(n-m))
# else:
#     print(k%(n-m))

# n = 's4sdfs2sfsdf5dsfa7'
# reqemler = '0123456789'
# t = []
# c = []
# for i in n:
#     if reqemler.count(i) == 1:
#         if int(i)%2 == 0:
#             c.append(int(i))
#         else:
#             t.append(int(i))
# maxi =max(c)
# mini = min(t)
# print(maxi,mini,maxi+mini)


# 28
# n = int(input())
# while n>0:
#     print('Informatika')
#     n = n-1

# n = int(input())
# for i in range(0,n):
#     print('Informatika')

# 29

# aaaabbbbbcccc -->> bbbbaaaaacccc

# n = input('Giriş: ')
# n = n.replace('a','*')
# n = n.replace('b','a')
# n= n.replace('*','b')
# print('Çıxış: ',n)

# Klaviaturadan daxil edilmiş iki sözü yəni söz birləşməsindəki sözlərin yerin dəyiş
# kitab oxu --- oxu kitab

# n = input().split()
# n.reverse()
# n = ' '.join(n)
# print(n)

# n = input()
# n = n.replace('kitab','*')
# n = n.replace("oxu",'Kitab')
# n = n.replace('*','oxu')
# print(n)


# n = input().split()
# for i in range(0,len(n)):
#     n[i] = int(n[i])
# b = 0
# s = 0
# while b<=30:
#     a = max(n)
#     b = b+a
#     n.remove(a)
#     n.append(a//2)
#     s = s + 1
# print(s)

# n = int(input()) # 246
# n = str(n)
# d = int(n[len(n)-1])-int(n[len(n)-2])
# f = 0
# for i in range(0,len(n)-1):
#     if d != int(n[i+1])-int(n[i]):
#         f = 1
# if f == 1:
#     print('Ededi silsile deyil')
# else:
#     print('Ededi silsiledir')

# n = int(input())
# s = str(n)
# c =0
# for i in n:
#     c = c + int(i)
# h = s*c
# while s!=c:
#     if s>c:
#         s = s -c
#     else:
#         c = c-s
# ebob = s
# ekob = h/ebob
# print(ebob+ekob)

# # 6

# n = 345
# a = n//100
# b = a*100
# n = n - b
# n = n*10+a
# print(n)

# 5

# n = 345
# a = n//100
# b = n//10%10
# c = n%10
# c = c*100
# b = b*10
# n = a+b+c
# print(n)

# # 2

# n = 345
# a = n//100
# b = n//10%10
# c = n%10
# print(a,b,c)


# # 1

# a = 5
# b = 7
# a,b = b,a
# print(a,b)

# n = int(input())
# s = 0 
# for i in range(1,n+1):
#     s = s + (-1)**(i+1)*i*(i+1)
# print(s)


# say sistemleri suallar


# # 89

# a = ['1','10','25','0','35','20']
# maxsima = a[0]
# for i in a:
#     if i > maxsima:
#         maxsima = i
# print(maxsima)

# # 90

# my = [1,2,3,4,2,5,6,1,7]
# b = []
# for i in my:
#     if my.count(i) == 1:
#         b.append(i)
# say = len(b)
# print(say)



# #  29

# n = int(input())
# n = str(n)
# k = n[0]+n[1]
# s = n.count(k)
# if s>1:
#     print('Yes')
# else:
#     print('No')

# 30

# a = [3,241,0,9,0,256,0]
# b = max(a)
# for i in range(len(a)):
#     if a[i] == 0:
#         a[i] = b
# print(a)

# 30
# klaviaturadan daxil edilmish 10 luqdan to 16liqa

# n = int(input()) # 45
# reqemler = '0123456789ABCDEF'
# s = ''
# while n>0:
#     q = n%16
#     s = reqemler[q] + s
#     n = n//16
# print(s)


# 29

# a = [2,12,5,3,22,5,7,12,8,3]
# h = 1
# s = 0
# for i in a:
#     if i%2 == 0:
#         s = s+i
#     else:
#         h = h*i
# print(s,h)


# 89

# n = int(input()) # 3456
# a = n//100
# b = n%100
# if a==b:
#     print('Beraberdir')
# else:
#     print('Not beraber')


# 90

# n = int(input())
# b = []
# for i in range(n):
#     a = int(input())
#     b.append(a)
# menfi = []
# musbet = []
# for i in b:
#     if i<0:
#         menfi.append(i)
#     elif i>0:
#         musbet.append(i)
# print(min(musbet)+max(menfi))


# # 16

# n = int(input())
# s = 0
# while n != 0 : 
#     if n>0:
#         s = s + 1
#     n = int(input())
# print(s,'sayda musbet eded daxil etdiniz')


# xoş geldiz
# alışveriş etmək istəyirsiz?
# cavab: beli
# ne aldınız?
# erzagi sebete elave et
# Alışverişe davam edirsen?

# print('Xoş gəldiniz')
# print('Alışveriş etmək istəyirsiniz? beli/xeyir')
# cavab = input().lower()
# sebet = []
# if cavab == 'beli':
#     while (cavab == 'beli' and cavab!='Xeyir'):
#         print('Ne aldiniz?')
#         a = input("Erzaqi daxil et: ")
#         sebet.append(a)
#         print('Alışverişe davam edirsen? beli/xeyir')
#         cavab = input().lower()
# else:
#     print('Səbət boşdur')
# if cavab == 'xeyir':
#     print(len(sebet))

# 90

# n = int(input())
# a = []
# for i in range(n):
#     b = int(input())
#     a.append(b)
# menfi = []
# musbet = []
# for i in a:
#     if i<0:
#         menfi.append(i)
#     else:
#         musbet.append(i)
# print(max(menfi)+min(musbet))

# 1

# def reversed(x):
#     x = str(x)
#     x = list(x)
#     x.reverse()
#     x = ''.join(x)
#     x = int(x)
#     return x

# a = int(input())
# b = int(input())
# sum = reversed(a) + reversed(b)
# print(reversed(sum))



# 3

# n = [10,22,9,33,21,50,41,60,80]
# s = 1
# for i in range(0, len(n)-1):
#     if n[i]<n[i+1]:
#         s = s + 1
# print(s)

# 4

# n = [0,1,9,8,4,0,2,7,0]
# b = []
# s = 0
# for i in n:
#     if i != 0:
#         b.append(i)
#     else:
#         s = s+1
# for i in range(s):
#     b.append(0)
# print(b)

# 5

# n = input() 
# s = 0
# for i in n:
#     if n.count(i) == 1:
#         s = s+1
# print(s)







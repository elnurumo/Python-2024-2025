# # # # # Suallar 
# # # # # 1.
# # # # # 2. 53-56 , 57


# # # # # print(4,5,6, sep='\n')

# # # # # a = ['a','ac','aa', 'aabc','ab']
# # # # # a.sort()
# # # # # a.reverse()
# # # # # print(a)
# # # # # print(a.index('ab'))



# # # # # a = [1,2,43,5]
# # # # # # a.append(5)
# # # # # a = a.insert(2,5)
# # # # # print(a) 


# # # # # 
# # # # # 


# # # # # a = 'salam necesen'.split(" ")
# # # # # a1 = a[0]
# # # # # print(a1)

# # # # # a = 'Yusif'
# # # # # a= a[::-1]
# # # # # print(a)

# # # # # a = 5
# # # # # b = 4
# # # # # print(a,b)
# # # # # a,b = b,a
# # # # # print(a,b)

# # # # # s = 0
# # # # # for i in range(1000,10000):
# # # # #     a = i//1000
# # # # #     b = i//100%10
# # # # #     c = i//10%10
# # # # #     d = i%10
# # # # #     if a%2!=0 and b%2!=0 and c%2!=0 and d%2!=0:
# # # # #         s = s + i
# # # # # print(s)


# # # # ## 1

# # # # # n = int(input())
# # # # # b = []
# # # # # for i in range(0,n):
# # # # #     a = int(input())
# # # # #     b.append(a)
# # # # #     print(b)
# # # # # print(max(b))

# # # # # # 2

# # # # # n = input().split(' ')
# # # # # # ['0','1','2','3']
# # # # # # print(n)
# # # # # for i in range(len(n)):
# # # # #     n[i] = int(n[i])
# # # # # # print(n)
# # # # # s = n.count(0)
# # # # # for i in range(s):
# # # # #     n.remove(0)
# # # # #     n.append(0)
# # # # # print(n)


# # # # # # 3
# # # # # s = 0
# # # # # for i in range(100,10000):
# # # # #     i = str(i)
# # # # #     a = int(i[0])
# # # # #     b = int(i[len(i)-1])
# # # # #     if a + b > 10:
# # # # #         s = s+1
# # # # # print(s)

# # # # # n = input().split(' ')
# # # # # d = 0
# # # # # for i in n:
# # # # #     s = len(i)
# # # # #     if s%2 == 0:
# # # # #         d = d+1
# # # # # print(d)


# # # # n=input().split(' ')
# # # # a=int(input())
# # # # s=0
# # # # for i in n:
# # # #     if len(i)>a:
# # # #         s=s+1
# # # # print(s)       

# # # # n sayda ixtiyari tam ededden 
# # # # yanliz tek olanlarinin ededi 
# # # # ortasini tapan phyton kodu:
# # # s=0
# # # a=0
# # # n=int(input())
# # # for i in range(0,n):
# # #     x=int(input())
# # #     if x%2==1:
# # #      s=s+1
# # #      a=a+x
# # # print(a/s)

# # [1:n] ededlerin kvadratlarinin 
# # ededi ortasini tapan kod
# a=0
# s=0
# n=int(input())
# if n>1: 
#     for i in range(1,n+1):
#         s=s+i*i
#         a=a+1
#     print(s/a)       




# 37

# print(2,end='')
# print(3,end='')
# print(4)


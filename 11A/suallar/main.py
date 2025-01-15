# n = int(input()) # 5456
# n = str(n)
# maxi = max(n)
# s = 0
# f = 0 # flag
# for i in n:
#     if n.count(i)>1:
#         f = 1
# if f == 1:
#     print('Reqemleri eynidir')
# else:
#     for i in n:
#         if i!=maxi:
#             s = s+int(i)
#     print(s)


# 


# a = [0,0,0,0,0,0,0,0,0,0]
# for i in range(1,6):
#     a[10-i] = (10-i)*(i-10)
#     a.reverse()
# print(a)


# 1

# n=int(input())
# n=str(n)
# s=''
# for i in n:
#     if i!=n[len(n)-1]:
#         s=s+i+'1'
#     else:
#         s=s+i
# s=int(s)
# print(s*s)
# 
# n=int(input())
# s=''
# a='0123456789ABCDEF'
# while n>0:
#     q=n%16
#     s=a[q]+s
#     n=n//16
# print(s)
# 
# n=input().upper()
# l=len(n)-1
# s=0
# a='0123456789ABCDEF'
# for i in n:
#     s=s+a.index(i)*16**l
#     l=l-1
# print(s)


# Rekursiv Function

def f(n):
    if n<1:
        return 1
    return n*f(n-1)

print(f(5))
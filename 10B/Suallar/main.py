# a = ['alma','armud','nar']
# b = []
# for i in a:
#     c = len(i)
#     b.append(c)
# print(min(b))

# # 6
# # 1-ci üsul
# s =0
# for i in range(1001,10000,2):
#     a = i//1000
#     b = i//100%10
#     c = i//10%10
#     if a%2!=0 and b%2!=0 and c%2!=0:
#         s = s+i
# print(s)

# # 2-ci üsul

# s = 0
# for i in range(1001,10000,2):
#     i = str(i)
#     if int(i[0])%2!=0 and int(i[1])%2!=0 and int(i[2])%2!=0:
#         s = s+int(i)
# print(s)



# 12

def sadeorMrkkb(n):
    f = 0
    for i in range(2,n//2+1):
        if n%i==0:
            f = 1
    return f
n = int(input()) # 35
fn = 0
for i in range(2,n//2+1):
    if n%i==0:
        fn = 1
if fn == 1:
    n = n-1
    while sadeorMrkkb(n) == 1:
        n = n-1
else:
    n = n+1
    while sadeorMrkkb(n) == 1:
        n = n+1
s = 0
for i in str(n):
    i= int(i)
    s = s+i
print(s)






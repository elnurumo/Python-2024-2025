
# Rekursiv funksiya

def togrul(n):
    if n<1:
        return 1
    return n + togrul(n-1)

print(togrul(5))

# suallar html
# 12

n=int(input())
f = 0
for i in range(2,n//2+1):
    if n%i==0:
        f = 1
if f==1:
    print('Mürəkkəb')
else:
    print('sadedir')

def checkSadeOrMurekkeb(n):
    f = 0
    for i in range(2,n//2+1):
        if n%i==0:
            f = 1
    return f

n = int(input())
s = 0
if checkSadeOrMurekkeb(n) == 0:
    n = n+1
    while checkSadeOrMurekkeb(n) != 0:
        n = n+1
    n = str(n)
    for i in n:
        s = s + int(i)
    print(s)
else:
    n = n-1
    while checkSadeOrMurekkeb(n) != 0:
        n = n-1
    n = str(n)
    for i in n:
        s = s +int(i)
    print(s)




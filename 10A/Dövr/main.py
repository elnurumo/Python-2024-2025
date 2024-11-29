#  integer, float, list, string, boolean

# bolean- ------> True, False

n = 'salam'
# print(n[len(n)-1], end=' ')
# print(n[0], end=' ')
# print(n[1])

print(n[0], n[len(n)-1], sep='\n')

n = ['Sebine', 'Dilruba', 'Ulvi']

for i in range(0,len(n)):
    print(n[i][0])

n = False==0
print(n)

# ixtiyari sayda reqemleri olan ededin reqemleri cemin tap

n = int(input()) # 345
s = 0
while n>0:
    q = n%10
    s = s+q
    n = n//10
print(s)



# ------------------>> suallar toplu Dövr

89, 94, 99

# 71

n = int(input('Ədədlırin sayı: ')) # say: 3
s = 0
for i in range(0,n):
    a = int(input(f'{i+1}. ədədi daxil et: '))
    s = s + a
edediOrta = s/n
print(f'Ədədi orta = {edediOrta}')

# 72

n = int(input())
b = []
for i in range(0,n):
    a = int(input())
    b.append(a)
mini = min(b)
print(mini)

#  [5,7,8]

a = [10,2,5,25,45,0]
kichik = a[0]
for i in a:
    if i<kichik:
        kichik = i
print(kichik)


# 80

n = int(input())
s = 0
if n>1:
    for i in range(2,n//2+1):
        if n%i == 0:
            s = s+1
    if s>0:
        print('Murekkebdir')
    else:
        print('sadedir') 
elif n == 1:
    print('1 nə sadədir nədə müərkkəb')

# 81

n = int(input())
s = 0
for i in range(1,n+1):
    s = s + (-1)**(i+1)*i*(i+1)
print(s)

# 89

n = int(input())
s = 0
k = -1
f = 1
for i in range(1,n+1):
    f = f*i
    s = s + k*1/(f)**i
    k = k*-1
print(s)


# 94

n = input().upper() # AA
reqemler = '0123456789ABCDEF'
q = len(n)-1
onluq = 0
f = 1
for i in n:
    if reqemler.find(i) != -1:
        onluq = onluq + reqemler.find(i)*16**q
        q = q - 1
    else:
        f = 0
if f == 1:
    print(onluq)
else:
    print('Belə bir ədəd mövcud deyil')

# 99
# 1.
n = int(input())
m = str(n)
s = 0
mini = min(m)
s = m.count(mini)
print(s)

# 2.
n = int(input())
m = str(n)
s = 0
for i in m:
    if min(m) == i:
        s = s+1
print(s)

# 107

n = int(input()) # 1011
n = str(n)
q = len(n)-1
onluq = 0
for i in n:
    onluq = onluq + int(i)*2**q
    q = q - 1
sekkizlik = ''
while onluq>0:
    qaliq = str(onluq%8)
    sekkizlik = qaliq + sekkizlik
    onluq = onluq//8
print(sekkizlik)



n = 5
print(n)


# 102, 93, 86, 105 -->Dövr

86

print(1-0.7)

n = float(input())
if n>=0:
    t = int(n)
    q = n - t
    print(t,q)
elif n<0:
    if int(n) == n:
        print(int(n), 0)
    else:
        t = int(n)-1
        q = -1*t+n
        print(t,q)

n = float(input())
if n > 0:
    n = str(n)
    t = n[0:n.find('.')]
    q = '0'+n[n.find('.'):]
    print(t,q)
elif n<0:
    n = str(n)
    t = int(n[0:n.find('.')]) - 1
    q = '0.'+str(10**len(n[n.find('.')+1:])-int(n[n.find('.')+1:]))
    print(t,q)

# 93

n = int(input())
n = str(n)
b = []
if int(n)>0:
    for i in n:
        if int(i)%2 != 0:
            b.append(i)
    if len(b) != 0:
        print(min(b))
    else:
        print('Ədəddə tək rəqəm yoxdur')

# 102

x = int(input())
n = int(input())
s = 0
f = 1
for i in range(1,n+1):
    f = f*i
    s = s + (-1)**(i+1)*x**i/f
print(s)

# 105

n = input()
s = 0
reqemler = '0123456789'
for i in n:
    if reqemler.count(i) == 1:
        s = s+1
print(s)

# 99

n = int(input())
m = str(n)
mini = min(m)
s = m.count(mini)
print(s)

n = int(input()) # 57846
n = str(n)
s = 0
f = 0 # flag metodu
for i in n:
    if n.count(i) != 1:
        f = 1
if f==0:
    for i in n:
        if max(n) != i:
            s = s+int(i)
    print(s)
else:
    print('reqemleri müxtelif deyil')


# 
a = int(input())
b = int(input())
s = 0
if 1<a<b:
    for i in range(a+1,b):
        f = 0 
        for j in range(2,i//2+1):
            if i % j ==0:
                f = 1
        if f==0:
            s = s+1
    print(s)


# float, integer, string, list, boolean

# True, False ---->> Boolean bool

n = False==0
m = '2'//2 
print(n)

for i in str(123):
    print(i)

for i in range(101,1000,2):
    print(i)


# ixtiyari reqemli ededin reqemleri cemini tap

n = int(input()) # 123
s = 0
while n>0:
    q = n%10
    s = s + q
    n = n//10
print(s)


# ------------------->>>>>>>>> Suallar
# 52 



n = ' Salam'.strip().capitalize()
print(n)


# Dövr ətraflı

# 66
# 1.
n = int(input())
n = str(n)
for i in n:
    print(i)

# 2.
n = int(input())
b = []
while n>0:
    q = n%10
    b.append(q)
    n = n//10
b.reverse()
for i in b:
    print(i)

# # 67
# # 1.
n = int(input()) # 2345
                 # 0123
n = str(n)
a = int(n[1]) # '3'
b = int(n[2]) # 4
if b%2 == 0:
    print(a+b)
else:
    print(a*b)
# 2.
n = int(input()) # 2345
a = n//100%10
b = n//10%10
if b%2 == 0:
    print(a+b)
else:
    print(a*b)

# 68

n = int(input())
s = 0
for i in range(1, n+1):
    s = s + 1/i**2
print(s)


# 69

n = int(input())
s = 0
for i in range(1,2*n,2):
    s = s + (1/i)**i
print(s)


# 70
#  1.
n = int(input())
m = n
s = 0
while m > 0:
    q = m%10
    s = s+q
    m = m//10
if n%s==0:
    print('Bölünür')
else:
    print("Bölünmür")
# 2.
n = int(input())
m = str(n)
s = 0
for i in m:
    s = s + int(i)
if n%s == 0:
    print('Bolonur')
else:
    print('Bolunmur')

#  71

n = int(input('Ededlerin sayini daxil et: ')) # ededlerin sayini daxil etdim
s = 0
for i in range(0,n):
    a = int(input(f'{i+1}. Ededi daxil et: '))
    s = s + a
edediOrta = s/n
print(edediOrta)

# 72

n = int(input())
b = []
for i in range(1,n+1):
    a = int(input())
    b.append(a)
minimum  = min(b) 
print(minimum,b)

# 73
# 1.
for i in range(1,1000,2):
    print(i)

# 2.
for i in range(1,1000):
    if i%2 != 0:
        print(i)

# 75
a = [15,12,16,11,9]
for i in a:
    if i%2!=0:
        print(i**2)

# 94

n = input().upper() # AA
reqemler = '0123456789ABCDEF'
s = 0
q = len(n)-1
for i in n:
    s = s + reqemler.find(i)*16**q
    q = q-1
print(s)

# 77
s = 0
for i in range(1,100):
    i = str(i)
    s = s + i.count('3')
print(s)

# 76

n = int(input())
if n == 12 or n ==1 or n==2:
    print('Qishdadirr')
elif n == 3 or n == 4 or  n== 5:
    print('Yaz')
elif n == 6 or n == 7 or n == 8:
    print('yay')
elif n == 9 or  n == 10 or n==11:
    print('Payiz')
else:
    print('Bele bir ay nomresi yoxdur')



# 86,89,90,98,107-112

# 71

n = int(input('Ededlerin sayi: ')) # 3
s = 0
for i in range(0,n):
    a = int(input(f'{i+1}. ededi daxil et: '))
    s = s + a
edediOrta = s/n
print(edediOrta)

# 2.
n = int(input()) # ededlerin sayi
b = [] # bosh list
for i in range(0,n):
    a = int(input())
    b.append(a)
s = sum(b)
print('ededi orta: ',s/n)

# 72

n = int(input()) # ededlerin sayi
b = [] # bosh list
for i in range(0,n):
    a = int(input())
    b.append(a)
mini = min(b)
print('Cavab: ',mini)


# 77
s = 0
for i in range(1,100):
    i = str(i)
    s = s + i.count('3')
print(s)

# 78

n = int(input())
k = []
m = []
for i in range(n):
    a = int(input())
    if a%2 == 0:
        m.append(a)
    else:
        k.append(a)
print(m,k)

# 80

n =int(input())
f = 0 # flag metodu
if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            f = 1
    if f == 1:
        print('Mürəkkəb')
    else:
        print('Sadə')
elif n==1:
    print('1 nə sadədir nə də mürəkkəb')

# 81

n = int(input())
s = 0
for i in range(1,n+1):
    s = s + (-1)**(i+1)*i*(i+1)
print(s)

# 83
s = 0
for x in range(-10,11):
    if x>3:
        y = x**2-5*x+6
    else:
        y = (x+2)**2
    if y%3 == 0:
        s = s + 1
print(s)

# 84
s = 0
c = 0
a = [3,4,2,1,6,9,7,8,12,10,5,14]
for i in range(0,len(a)):
    if i%2 != 0 and a[i] % 2 == 0:
        c = c + a[i]
        s = s + 1
    elif i%2 == 0 and a[i]%2 !=0:
        c = c + a[i]
        s = s + 1
edediOrta = c/s
print(edediOrta,c,s)

86

n = float(input())
if n>0:
    t = int(n)
    q = n - t
    print(t,q)
elif n < 0:
    t = int(n) -1
    q = -1*t+n
    print(t,q)

n = float(input())
if n>0:
    n = str(n)
    t = n[0:n.find('.')]
    q = '0'+n[n.find('.'):]
    print(t,q)
elif n<0:
    n = str(n)
    t = int(n[0:n.find('.')]) - 1
    q = '0.'+str(10**len(n[n.find('.')+1:]) - int(n[n.find('.')+1:]))
    print(t,q)

print(7 - 0.8)

# 89

n = int(input())
s = 0
k = -1
f = 1
for i in range(1,n+1):
    f = f * i
    s = s + k*1/(f)**i
    k = -k
print(s)

# 90

n = int(input())
s = 0
k = 1
if n>=3:
    for i in range(3,n+1,2):
        s = s + k*i
        k = -k
print(s)

# 94

n = input().upper()
reqemler = '0123456789ABCDEF'
onluq = 0
q = len(n)-1
for i in n:
    onluq = onluq + reqemler.find(i)*16**q
    q = q-1
print(onluq)



# Suallar --------->>>>
# 90-112
 


# 90

n = int(input())
s = 0
k = 1
if n >=3:
    for i in range(3,n+1,2):
        s = s+k*i
        k = -k
    print(s)


# 91

s = 0
for i in range(100,1000):
    a = i//100
    b = i//10%10
    c = i%10
    if a%3==0 and b%3 == 0 and c%3==0:
        s = s+1
print(s)


# 92

cem = 0
for i in range(100,1000,2):
    a = i//100
    b = i//10%10
    if a%2 == 0 and b%2 == 0:
        cem = cem+i
print(cem)


# 93

n = int(input())
m = str(n)
b = []
for i in m:
    i = int(i)
    if i%2 != 0:
        b.append(i)
s = len(b)
if s == 0:
    print('Ədəddə tək rəqəm yoxdur')
else:
    mini = min(b)
    print(mini)


# a = [2,3,4,-4,45,0] listinden
# minimum ededi tap. min() funksiyasindan 
# istifade etme !!!!!!!!

a = [2,3,4,-4,45,0]
min = a[0]
for i in a:
    if i<min:
        min = i
print(min)

# 95

n = int(input())
n = str(n)
reqemler = '01234567'
q = len(n)-1
onluq = 0
for i in n:
    onluq = onluq + reqemler.index(i) * 8 **q
    q = q-1
print(onluq)

# 96

m = int(input())
for i in range(200,1000):
    a = i//100
    b = i//10%10
    c = i%10
    if b!=1 and c!=1:
        if a*b*c == m:
            print(i)

# 97

n = int(input())
n = str(n)
s = 0
if int(n)>0:
    for i in n:
        i = int(i)
        if i%2 != 0:
            s = s+1
    print(s)


98

# sade vuruq
n = int(input())
sadeVuruq = 2
while n > 1:
    if n%sadeVuruq == 0:
        n = n//sadeVuruq
        print(sadeVuruq)
    else:
        sadeVuruq = sadeVuruq + 1



# sade bolen

n = int(input())
sadeBolen = 2
b = []
while n > 1:
    if n%sadeBolen == 0:
        n = n//sadeBolen
        if b.count(sadeBolen) == 0:
            b.append(sadeBolen)
    else:
        sadeBolen = sadeBolen + 1
for i in b:
    print(i)

# 99

n = int(input()) # 33345
n = str(n)
b = []
for i in n:
    if i == min(n):
        b.append(i)
print(len(b))

n = int(input())
n = str(n)
m = min(n)
s = n.count(m)
print(s) 

# 100

n = int(input())
s = 0
f = 0
while n>1:
    if n%2!=0:
        f = 1
    else:
        s = s+1
    n = n/2
if f == 0:
    print(s)
else:
    print('Eded yanlishdir')

# 101

g = 1
s = 5
while g<=5:
    g = g + 1
    s = s + s*20/100
print(s)

## 102

x = int(input())
n = int(input())
s = 0
f = 1
for i in range(1,n+1):
    f = f * i
    s = s + (-1)**(i+1)*x**i/f
print(s)

# 105

n = input() #Dim9912info2
reqemler = '0123456789'
s = 0
for i in n:
    if reqemler.count(i) == 1:
        s = s+1
print(s)


# 106

s = input()
n = []
for i in s:
    if n.count(i) == 0:
        n.append(i)
print(n)


# 107

n = int(input())
n = str(n)
reqemler = '01'
onluq = 0
q = len(n)-1
for i in n:
    onluq = onluq + reqemler.index(i) * 2 **q
    q = q -1
s = ''
while onluq > 0:
    q = onluq%8
    s = str(q) + s
    onluq = onluq//8
print(s)

109

a = [123,4532,3431]
for i in range(0,len(a)):
    b = str(a[i])
    b = list(b)
    b.reverse()
    b = ''.join(b)
    a[i] = int(b)
print(a)

# 112

n = int(input())
s = 0
while n>0:
    n = str(n)
    a = int(n[0])
    b = int(n[len(n)-1])
    n = int(n)-(a+b)
    s = s+1
print(s)





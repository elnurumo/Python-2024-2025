

print(5, end=' ')
print(3,end='-')
print(4)
print(2)

a = 5
b = a
a = 6
print(a,b)

a = [2,4,6]
b = a
a.append(7)
b = b+[3,4,5] # qrılma nöqtəsi
print(a,b)

a = [2,4,6]
b = [2,4,6]
a.append(7)
print(a,b)


n = 5
n = list(str(n))
print(n)

def f(x,y):
    return x+y*x-y
x = 5
y = 6
print(f(6,5))


#  method nedi? funksiya nedi?

a = []
a
print(a)


# join methodu
a = ['Toğrul', "Fexri", 'Yusif', 'Valide']
x = ' '.join(a)
print(x)


# split vs list

a = 'Salam dunya necesen sagol getdim'
# x = list(a) qessab
x = a.split('e')
print(x)


c = '7'=='4'
print(c)

m = ['A','a','b','B']
print(max(m))
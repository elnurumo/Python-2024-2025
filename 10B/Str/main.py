# 35,36,38,41,37

# 16

a = [1,2,3,2,4,1,5,6,5]
b = []
for i in a :
    if a.count(i) > 1:
        if b.count(i) == 0:
            s = a.count(i)
            b.append(s)
print(b)

# 19


n = 5
n = list(str(n))
print(n)

a = ['Elnur','Amin','Fizuli','Məryəm','Yusif']
x = ' '.join(a)
print(x)

a = 'Meryem Fizuli Amin Yusif'
x = a.split()
print(x)

# split() vs list()

a = 'Meryem Fizuli Amin Yusif'
b = list(a)
x = a.split()
print(x,b)
 

print(5,end=' ')
print(4)
print(3)
print(6)







n = 'Salam Dunya'

for i in range(0,100):  # for yeni sayğacli dövr
    print(n)

i = 0
while i<100:
    print(i,n)
    i = i+1

for i in range(0,100,5):
    print(i)


# müxtəlif rəqəmli n natural ədədin rəqəmləri cəmini tap. meselen n = 456  cem = 15   n = 3456   cem = 18

#  1. üsul

n =  int(input()) # 5456
c = 0
while n>0:
    q = n%10
    c = c+q
    n = n//10
print(c)

# 2. üsul
n = int(input()) # 356
n = str(n)
c = 0
for i in n:
    i = int(i)
    c = c+i
print(c)


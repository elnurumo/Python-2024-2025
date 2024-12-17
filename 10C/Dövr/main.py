# n = 'Salam Dunya'

# for i in range(0,100):  # for yeni sayğacli dövr
#     print(n)

# i = 0
# while i<100:
#     print(i,n)
#     i = i+1

# for i in range(0,100,5):
#     print(i)


# # müxtəlif rəqəmli n natural ədədin rəqəmləri cəmini tap. meselen n = 456  cem = 15   n = 3456   cem = 18

# #  1. üsul

# n =  int(input()) # 5456
# c = 0
# while n>0:
#     q = n%10
#     c = c+q
#     n = n//10
# print(c)

# # 2. üsul
# n = int(input()) # 356
# n = str(n)
# c = 0
# for i in n:
#     i = int(i)
#     c = c+i
# print(c)


# Suallar 
# 
# 


# 17
#   salam
# s1 = malas

# 18


#  find methodu

# n = 'salam'.find('a',)
# print(n)


# a = [45,4,2,7,15]
# #    0  1 2 3  4
# # length len()
# l = len(a)-1
# print(l)
# c = a[l]
# print(c)


# a = 'Kenan'
# f = a.find('n',3,len(a))
# print(f)

# a = [] # list 
# a.append(5)
# a.append(4)
# a.append(4)
# a.append(5)
# print(a)

# a = [5,4,5,4,4]
# a.remove(4)
# print(a)

# a = [4,5,3,2]
# a.insert(3,20)
# print(a)

# c = max(a)
# print(c)

# a = [4,5,6,7,2,-5,-45,0]
# minimum = a[0]
# for i in a:
#     if minimum>i:
#         minimum = i
# print(minimum)




# a=[4,5,6,7,2]
# maxsimal = a[0]
# for i in a:
#     if maxsimal<i:
#         maxsimal=i
# print(maxsimal)


# Split vs List

# Hər ikisidə str --->> listə çevirir

# a = "Hello world"
# a = list(a) # Qəssab Tikələdi
# print(a)

# # Split
# a = 'Kenan'
# a = a.split('n')
# print(a)

# a = [2,4,6]
# b = 5
# a.append(b)
# print(a)
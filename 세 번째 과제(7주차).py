# #과제11
# x=input('숫자5개 입력:').split()
# y=input('숫자1개 입력:')
# x.append(y)
# print(x)

# #과제12
# x=input('숫자5개 입력:').split()
# x=x[:-2]
# print(x)

# #과제13
# x=input('숫자5개 입력:').split()
# for index, value in enumerate(x, start=101):
#     print(index, value)

# #과제14
# a=[10,20,30,40,30,20,10]
# b=a.count(20)
# print(b)

# #과제15
# x=input('숫자10개 입력:').split()
# y=min(x)
# z=max(x)

# print(y,'and',z)

# #과제16
# x=list(map(int, input('숫자10개 입력:').split()))
# x.remove(min(x))
# x.remove(max(x))
# print(sum(x))

# #과제17
# a=[10,20,30,40,30,20,10]
# while 20 in a:
#     a.remove(20)
# print(a)

# #과제18
# x=[i for i in range(1,6)]
# print(x)

#과제19
x=[i for i in range(1,20)if i%2==1]
print(x)

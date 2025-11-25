#과제11
x=input('숫자5개 입력:').split()
y=input('숫자1개 입력:')
x.append(y)
print(x)

#과제12
x=input('숫자5개 입력:').split()
x=x[:-2]
print(x)

#과제13
x=input('숫자5개 입력:').split()
for index, value in enumerate(x, start=101):
    print(index, value)

#과제14
a=[10,20,30,40,30,20,10]
b=a.count(20)
print(b)

#과제15
x=input('숫자10개 입력:').split()
y=min(x)
z=max(x)

print(y,'and',z)

#과제16
x=list(map(int, input('숫자10개 입력:').split()))
x.remove(min(x))
x.remove(max(x))
print(sum(x))

#과제17
a=[10,20,30,40,30,20,10]
while 20 in a:
    a.remove(20)
print(a)

#과제18
x=[i for i in range(1,6)]
print(x)

#과제19
x=[i for i in range(1,20)if i%2==1]
print(x)

#과제20
x, y=map(int, input('정수 2개를 입력:').split())
z=[2**i for i in range(x,y+1)]
del z[1]
del z[-2]
print(z)

#과제21
x=input('Hello, world! 입력:')
print(x.replace('Hello','Hi'))

#과제22
x=input('문자 4개 입력:').split()
x="/".join(x)
print(x)

#과제23
x=input('본인의 성을 영어로 입력:')
y=x.lower()
z=y.rjust(10)
print(z)

#과제24
x=input('여러 물품 가격 입력:').split(';')
x=list(map(int, x))
x.sort(reverse=True)
for i in x:
    print(str(i).rjust(9))

#과제25
x=input('키 입력:').split()
y=input('값 입력:').split()
z=dict(zip(x, y))
print(z)

#과제26
park={'korean':94,'english':91,'mathematics':89,'science':83}
print(park['english'])
print(park['science'])

#과제27
kim={'korean':94,'english':91,'mathematics':89,'science':83}
kim.update(korean=100, english=100, mathematics=100, science=100)
print(kim)

#과제28
lee={'korean':94,'english':91,'mathematics':89,'science':83}
if 'english' in lee:
    print(lee['english'])
else:
    print(None)

#과제29
lim={'korean':94,'english':91,'mathematics':89,'science':83}
for i, j in lim.items():
    print(i, j)

#과제30
choi={'korean':94,'english':91,'mathematics':89,'science':83}
x={key for key, value in choi.items() if value >= 90}
print(x)

#과제31
yoo={'korean':94,'english':91,'mathematics':89,'science':83}
x=sum(yoo.values())/len(yoo)
print(x)

#과제32
x={1,2,3,4,5}
y={2,4,6,8,10}
a=x|y
b=x&y
print(a)
print(b)

#과제33
x={1,2,3,4,5}
y={2,4,6,8,10}
a=x-y
b=x^y
print(a)
print(b)

#과제34
x={1,2,3,4,5}
x.update({100})
print(x)

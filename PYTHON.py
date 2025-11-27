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

#과제35
a={100,200,300,400,500}
b={400,500,600,700,800}

x=a.copy()
x.intersection_update(b)
print(x)

y=a.copy()
y.difference_update(b)
print(y)

z=a.copy()
z.symmetric_difference_update(b)
print(z)

#과제36
a={100,200,300,400,500}
b={100,200,300,400,500}

if a.issuperset(b) and a.issubset(b):
    print("동시")
elif a.issuperset(b):
    print("상위")
elif a.issubset(b):
    print("부분")

#과제37
x={1,2,3,4,5}
x.add(1000)
x.remove(1000)
print(x)

#과제38
multiples={x for x in range(1,101)if x%3==0 and x%5==0}
print(multiples)

#과제39
def print_odd_numbers(a):
    for i in range(a + 1):
        if i % 2 == 1:
            print(i, end=' ')

x = int(input("양수 입력: "))
print_odd_numbers(x)

#과제40
def function(a):
    if a % 3 == 0:
        print(a)

x = int(input("숫자 입력: "))
function(x)

#과제41
def function(a,b,c,d):
    return max(a,b,c,d), min(a,b,c,d)

num1 = int(input("첫 번째 숫자 입력: "))
num2 = int(input("두 번째 숫자 입력: "))
num3 = int(input("세 번째 숫자 입력: "))
num4 = int(input("네 번째 숫자 입력: "))

y, z= function(num1, num2, num3, num4)
print("최댓값:", y)
print("최솟값:", z)

#과제42
def function(a):
    for i in range(a + 1):
        if i % 2 == 1:
            print(i, end=' ')

x = int(input("양수 입력: "))
function(x)

#과제43
def function(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

x = int(input("0 이상의 정수 입력: "))
print(function(x))

#과제44
def function(i, j):
    result = 0
    for x in range(1, i+1):
        for y in range(1, j+1):
            if x*y >= 30:
                result += x*y
    return result

i = int(input("2 이상 9 이하의 첫 번째 숫자 입력: "))
j = int(input("2 이상 9 이하의 두 번째 숫자 입력: "))
print(function(i, j))
#     1
A=int(input())
B=int(input())
C=int(input())

#максимальное чисало

if A>=B and A>=C:
    maximum=A
elif B>=A and B>=C:
    maximum=B
else:
    maximum=C

#минимальное число

if A<=B and A<=C:
    mini=A
elif B<=A and B<=C:
    mini=B
else:
    mini=C
print(maximum, mini)

#     2

import math

a=float(input())
b=float(input())
c=float(input())

if a==0:
    if b==0:
        if c==0:
            print('Корней нет')
        else:
            print('Корней нет')
    else:
        x=-c/b
        print(x)

else:
    D=b*b-4*a*c
    if D<0:
        print('Корней нет')
    elif D==0:
        x=-b/(2*a)
        print(x)
    else:
        x1=(-b+ math.sqrt(D))/(2*a)
        x2=(-b- math.sqrt(D))/(2*a)
        print(x1,x2)
#     3

a=float(input())
b=float(input())
c=float(input())

if a+b>c and a+c>b and c+b>a:
    print("Да")
    if a==b==c:
        print("Равносторонний треугольник")
    elif a==b or a==c or b==c:
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")
else:
    print("Нет")

#     4

x=float(input())
y=float(input())

krug=(x*x+y*y<=1) and (y>=0)
treug=(x <= 0) and (y <= 0) and (x + y >= -2)

if krug or treug:
    print("Да")
else:
    print("Нет")
#     №5
M=int(input())
D=int(input())

# Существование месяца:
if M<1 or M>12:
    print(-1)
else:
# Существование дня в этом месяце:
    if M==2:
        max_days=28
    elif M in (4, 6, 9, 11):
        max_days=30
    else:
        max_days=31

    if D<1 or D>max_days:
        print(-1)
    else:
        past_days=0
        if M==2:
            past_days=31
        elif M==3:
            past_days=31+28
        elif M==4:
            past_days=31+28+31
        elif M==5:
            past_days=31+28+31+30
        elif M==6:
            past_days=31+28+31+30+31
        elif M==7:
            past_days=31+28+31+30+31+30
        elif M==8:
            past_days=31+28+31+30+31+30+31
        elif M==9:
            past_days=31+28+31+30+31+30+31+31
        elif M==10:
            past_days=31+28+31+30+31+30+31+31+30
        elif M==11:
            past_days=31+28+31+30+31+30+31+31+30+31
        elif M==12:
            past_days=31+28+31+30+31+30+31+31+30+31+30

# Прибавляем текущий день
        past_days=past_days+D
# Считаем
        days_left=365-past_days
        print(days_left)

#     6

K=int(input())
if K<0:
    print("Мы не находили грибы, а только теряли...((")
else:
    if K % 10==1 and K%100 !=11:
        slovo="гриб"
    elif K%10 in (2,3,4) and K%100 not in (12,13,14):
        slovo="гриба"
    else:
        slovo='грибов'
    print(f'Мы нашли в лесу {K} {slovo}')

#     7

t=int(input())
if t<0:
    print("Ошибка")
else:
    m=t%5
    if m<3:
        print("Зеленый")
    else:
        print("Красный")

#     8

A=int(input())
h=A//30
m=(A%30)*2

print(h,m)

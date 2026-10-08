#     1
#A=int(input())
#B=int(input())
#C=int(input())

#максимальное чисало

#if A>=B and A>=C:
#    maximum=A
#elif B>=A and B>=C:
#    maximum=B
#else:
#    maximum=C

#минимальное число

#if A<=B and A<=C:
#    mini=A
#elif B<=A and B<=C:
#    mini=B
#else:
#    mini=C

#print(maximum, mini)

#     2

#import math

#a=float(input())
#b=float(input())
#c=float(input())

#if a==0:
#    if b==0:
#        if c==0:
#            print('корней нет')
#        else:
#            print('корней нет')
#    else:
#        x=-c/b
#        print(x)
#
#else:
#    D=b*b-4*a*c
#    if D<0:
#        print('корней нет')
#    elif D==0:
#        x=-b/(2*a)
#        print(x)
#    else:
#        x1=(-b+ math.sqrt(D))/(2*a)
#        x2=(-b- math.sqrt(D))/(2*a)
#        print(x1,x2)

#     3#     3

#a=float(input())
#b=float(input())
#c=float(input())

#if a+b>c and a+c>b and c+b>a:
#    print("да")
#    if a==b or a==c or b==c:
#        print("равнобедренный треугольник")
#    elif a==b==c:
#        print("равносторонний треугольник")
#    else:
#        print("разносторонний треугольник")
#else:
#    print("нет")

#     4

#x=float(input())
#y=float(input())

#krug=(x*x+y*y<=2) and (y>=0)
#treug=(abs(x)+abs(y)<=2) and (y<=0)

#if krug or treug:
#    print("да")
#else:
#    print("нет")

#     5

#M= int(input())
#D=int(input())

#if M<1 or M>12 or D<1 or D>31:
#    print(-1)
#else:
#    days= [31,28,31,30,31,30,31,31,30,31,30,31]
#    if D>days[M-1]:
#        print(-1)
#    else:
#        c=0
#        for i in range(M-1, 12):
#            c=c+days[i]
#        c=c-D
#        print(c)

#     6

#K=int(input())

#if K<0:
#    print("мы не находили грибы, а только теряли...((")
#else:
#    if K % 10==1 and K%100 !=11:
#        slovo="гриб"
#    elif K%10 in (2,3,4) and K%100 not in (12,13,14):
#        slovo="гриба"
#    else:
#        slovo='грибов'
#    print(f'Мы нашли в лесу {K} {slovo}')

#     7

#t=int(input())

#if t<0:
#    print("ошибка")
#else:
#    m=t%5
#    if m<3:
#        print("зеленый")
#    else:
#        print("красный")

#     8

#A=int(input())

#h=A//30
#m=(A%30)*2

#print(h,m)

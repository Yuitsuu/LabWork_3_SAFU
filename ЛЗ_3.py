#     №1
#A=int(input())
#B=int(input())
#N=int(input())
#d=(A*100+B)*N
#rub=d//100
#cop=d%100
#print(rub, cop)
from multiprocessing.pool import mapstar

#     №2
#N=int(input())
#print(N%2==0)

#     №3
#N=int(input())
#K=int(input())
#oreh=K//N
#turnir=K-(oreh*N)
#print(oreh, turnir)

#     №4
#a=int(input())
#sotni=a//100
#des=(a//10)%10
#eden=a%10
#print(sotni+des+eden)
#print(sotni*des*eden)

#     №5
#klass1=int(input())
#klass2=int(input())
#klass3=int(input())
#part=(klass1+klass2+klass3)%2
#partNada=(klass1+klass2+klass3)//2+part
#print(partNada)

#     №6
#A=float(input())
#B=float(input())
#L=float(input())
#N=int(input())

# вертикаль: N-1 (по A)
# горизонталь: 2N-2 (по B)
# свободные концы: 2l

#dlina=((N-1) * A + (2*N-2) * B + 2 * L)*2
#print(dlina)

#     №7
h=int(input())
m=int(input())
s=int(input())
h1=int(input())
m1=int(input())
s1=int(input())

t= h * 3600 + m * 60 + s
t1= h1 * 3600 + m1 * 60 + s1

raz= t1 - t

h3=raz//3600
m3=(raz%3600)//60
s3=raz%60
print(h3, 'ч', m3, 'м', s3, 'с')
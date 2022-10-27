# a=input()
# b=input()
# x=input()
# y=input()
# z=input()
# if (x<a and y<b)or(y<a and x<b)or(y<a and z<b)or(z<a and y<b)or(z<a and x<b)or(x<a and z<b):
#     print('true')
# else:
#     print('false')

# a=int(input())
# b=int(input())
# c=int(input())
# print(str(not bool(a-b)))
# print(str(not bool(a-c)))
# print(str(not bool(c-b)))
#
# pol=int(input())
# print(str(pol)==str(pol)[::-1])
from random import *
# k1 = randrange(0,9)
# k2 = randrange(0,9)
# k3 = randrange(0,9)
# kod = str(k1) + str(k2) + str(k3)
# n = 5
# while n !=0:
#     kod1 = str(input())
#     if kod1==kod:
#         print("true")
#         n=0
#     elif kod1=='0':
#         n=0
#         print('err')
#     else:
#         n-=1
#         print("err")
# k1 = randrange(0,9)
# if k1%3 == 0:
#     print('0')
# elif k1%3==1:
#     print('')
# else:
#     print('err')


# result = 0
# n = int(input())
# # for i in range(n):
#     result+=(-1**i)*i
# #
# # #     result += int(input())
# # print(result)
#
# if n%2==0:
#     print(n/2)
# else:
#     print((n-1)/2-n)
# result = 0
# for i in range(2,100,2):
#     result+=i
# print(result)
# result = 0
# for i in range(2,100,2):
#     result+=i
# print(result)
# result = 0
# kolich = 0
# a = 1
# while a!=0:
#     a=int(input())
#     result+=a
#     kolich+=1
# print(result/kolich)

# x = int(input())
# y = int(input())
# i = 1
# while x<y:
#     x*=1.1
#     i+=1
# print(i)


# x=1
# k=int(input())
# while k>2:
#     k-=3
#     x*=2
# print(x)

#
# b = [12,3,21,43,6467,6,2,56,-4,-3,-35,0]
# # result = 0
# for i in range(len(b)):
#      if b[i]<0:
#          print(b[i])
# for i in range(len(b)):
#      if b[i]>=0:
#          print(b[i])
#         result+=1
# print(result)

# b=[]
# result = 0
# for i in range(1,50):
#     b.append(i)
#     result+=b[i-1]
# print(result/len(b))
#
# srt = 'qwerty'
# print(srt[::2])
# print(srt[1::2])
#
#
#
# ss = 'zdf*zdf*sdf*sdf*'
# print(ss.replace('*','-'))
#
#
# print('*88'+'\n'+'88*')


# t = [1,3,5,6,3,2,5,3,2]
from random import *


def pull(num):
    s = []
    minuss = []
    for i in range(10):
        s.append(randrange(0,num+1))
    for i in range(10):
        minuss.append(randrange(-num,1))
    s= tuple(s)
    minuss = tuple(minuss)
    t = s + minuss
    print(t)
    print(t.count(0))
pull(3)

t = {1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100,11:121,12:144}
def creates(t):
    print(t)
    for i in range(1,len(t)+1):
        print(str(i)+' -- '+str(t[i]))
# creates(t)



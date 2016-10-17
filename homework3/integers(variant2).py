print('Введите число a:')
a=int(input())
print('Введите число b:')
b=int(input())
print('Введите число c:')
c=int(input())
d='не'
e='не'
if a*b==c:
    d=''
if a*c+b==0:
    e=''
print('произведение ',a,'и ',b,d,'равно ',c)
print(c,e,'является корнем уравнения ',a,'x+',b,'=0')



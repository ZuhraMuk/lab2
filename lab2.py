# n=input('Введите число ');
# n=float(n);
# x=n**2;
# print('Квадрат числа: ', x);

# for i in range(1,100):
#     if (i%2==0):
#         print(i)

# x=input('x=')
# y=input('y=')
# z=input('z=')
# x=float(x)
# y=float(y)
# z=float(z)
# b=x**2+y**2+z**2
# print('x^2+y^2+z^2',b)

# print('Консольный калькулятор')
# q1 = int (input('Вводим первое число: '))
# q2 = int (input('Вводим второе число: '))
# v = int(input('Выбор операции \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n'))

# if v==1:
#     r=q1+q2
#     p='+ (СЛОЖЕНИЕ)'
#     t=p
# if v==2:
#     r=q1-q2
#     l='- (ВЫЧИТАНИЕ)'
#     t=l
# if v==3:
#     r=float(q1/q2)
#     m='/ (ДЕЛЕНИЕ)'
#     t=m
# if v==4:
#     r=float(q1*q2)
#     n='* (УМНОЖЕНИЕ)'
#     t=n

# print('Резуультат ',t,' = ',r)





#/календарь с tkinter/
# from tkinter import *
# import calendar 
# import datetime

# root = Tk()
# root.title('Calendar')
# days = []
# now = datetime.datetime.now()
# year = now.year
# month = now.month

# def prew():
#     global month, year
#     month -= 1
#     if month ==0:
#         month = 12
#         year -= 1
#     fill()

# def next():
#     global month, year
#     month += 1
#     if month ==13:
#         month = 1
#         year += 1
#     fill()

# def fill():
#     info_label['text'] = calendar.month_name[month] + ',' + str(year)
#     month_days = calendar.monthrange(year, month) [1]
#     if month == 1:
#         prew_month_days = calendar.monthrange(year-1, 11) [1]
#     else:
#         prew_month_days = calendar.monthrange(year, month -1) [1]
#     week_day = calendar.monthrange(year, month) [0]
#     for n in range(month_days):
#         days[n + week_day] ['text'] = n+1
#         days[n + week_day] ['fg'] = 'white'
#         if year == now.year and month == now.month and n == now.day - 1:
#             days[n + week_day]['background'] = 'darkgray'
#             days[n + week_day] ['fg'] = 'gray'
#         else:
#             days[n + week_day] ['background'] = 'lightgray'

#     for n in range(week_day):
#         days[week_day - n - 1] ['text'] = prew_month_days - n
#         days[week_day - n - 1] ['fg'] = 'gray'
#         days[week_day - n - 1] ['background'] = '#f3f3f3'
#     for n in range(6*7 - month_days - week_day):
#         days[week_day + month_days + n] ['text'] = n+1
#         days[week_day + month_days + n] ['fg'] = 'gray'
#         days[week_day + month_days + n] ['background'] = '#f3f3f3'

# prew_button = Button(root, text ='<', command=prew)
# prew_button.grid(row=0, column=0, sticky='nsew')
# next_button = Button(root, text ='>', command=next)
# next_button.grid(row=0, column=6, sticky='nsew')
# info_label = Label(root, text='0', width=1, height=1, font=('Verdana', 16, 'bold'), fg='blue')
# info_label.grid(row=0, column=1, columnspan=5, sticky='nsew')

# for n in range(7):
#     lbl = Label(root, text=calendar.day_abbr[n], width=1, height=1, font=('Verdana', 10, 'normal'), fg='darkblue')
#     lbl.grid(row=1, column=n, sticky='nsew')
# for row in range(6):
#     for col in range(7):
#         lbl = Label(root, text='0', width=4, height=2, font=('Verdana', 16, 'bold'))
#         lbl.grid(row=row+2, column=col, sticky='nsew')
#         days.append(lbl)
# fill()
# root.mainloop()




# Калькулятор tkinter
# from tkinter import *
# from decimal import *

# root = Tk()
# root.title('Калькулятор')

# buttons = (('7','8','9','/','4'),
#            ('4','5','6','*','4'),
#            ('1','2','3','-','4'),
#            ('0','.','=','+','4')
#            )

# activeStr = ''
# stack = []

# def calculate () :
#     global stack
#     global label
#     result = 0
#     operand2 = Decimal(stack.pop())
#     operation = stack.pop()
#     operand1 = Decimal(stack.pop())
#     if operation == '+':
#         result = operand1 + operand2
#     if operation == '-':
#         result = operand1 - operand2
#     if operation == '/':
#         result = operand1 / operand2
#     if operation == '*':
#         result = operand1 * operand2
    
#     label.configure(text=str(result))

# def click(text):
#     global activeStr
#     global stack
#     if text == 'CE':
#         stack.clear()
#         activeStr = ''
#         label.configure(text='0')
#     elif '0' <= text <= '9':
#         activeStr += text
#         label.configure(text=activeStr)
#     elif text == '.':
#         if activeStr.find('.') == -1:
#             activeStr += text
#             label.configure(text=activeStr)
#     else:
#         if len(stack) >=2:
#             stack.append(label['text'])
#             calculate()
#             stack.clear()
#             stack.append(label['text'])
#             activeStrm = ''
#             if text != '=':
#                 stack.append(text)
#         else:
#             if text != '=':
#                 stack.append(label['text'])
#                 stack.append(text)
#                 activeStr =''
#                 label.configure(text='0')


# label = Label(root, text='0', width=40)
# label.grid(row=0, column=0, columnspan=4, sticky='nsew')

# button = Button(root, text='CE', command=lambda text='CE': click(text) )
# button.grid(row=1, column=3, sticky='nsew')
# for row in range(4):
#     for col in range(4):
#         button = Button(root, text=buttons[row] [col],
#                 command=lambda row=row, col=col: click(buttons[row][col]))
#         button.grid(row=row + 2, column=col, sticky='nsew')

# root.grid_rowconfigure(6, weight=1)
# root.grid_columnconfigure(4, weight=1)

# root.mainloop ()



# Лаброторные работы 
# x=5
# y=6

# print('x= ', x)
# print('y= ', y)

# z = x+y
# print('z= ',z)
# z = x-y
# print('z= ',z)
# z = x/y
# print('z= ',z)
# z = x*y
# print('z= ',z)


# x=11
# print('{:4} {:4} {:4}'.format(x,x,x))

# name = input('Введите ФИО: ')
# age = input('Введите возраст: ')
# house = input('Введите ваше место жительство: ')

# print(f'Ваш ФИО: {name}, возраст: {age}, место жительство: {house}')


# x=5
# y=2
# z=3
# print(x+y)
# print(x-y)
# print(x/y)
# print(x*y)
# print(x//y)
# print(x%y)
# print(-x)
# print(abs(-x))
# print(divmod(x,y))
# print(x**y)
# print(pow(x,y,z))


# import math

# a=10
# b=-5
# c=4.3
# d=3

# print('a= ',a)
# print('b= ',b)
# print('c= ',c)
# print('d= ',d)

# z=math.ceil(c)
# print(f'math.ceil({c}) = {z}')
# z=math.fabs(b)
# print(f'math.fabs({b}) = {z}')
# z=math.factorial(a)
# print(f'math.factorial({a}) = {z}')
# z=math.floor(c)
# print(f'math.floor({c}) = {z}')
# z=math.exp(b)
# print(f'math.exp({b}) = {z}')
# z=math.log2(a)
# print(f'math.log2({a}) = {z}')
# z=math.log10(a)
# print(f'math.log10({a}) = {z}')
# z=math.log(d,a)
# print(f'math.log({d}, {a}) = {z}')
# z=math.pow(a,d)
# print(f'math.pow({a}, {d}) = {z}')
# z=math.sqrt(a)
# print(f'math.({a}) = {z}')


# import math

# x=1
# print('x =',x)

# z=math.cos(x)
# print(f'math.cos({x}) = {z}')

# z=math.sin(x)
# print(f'math.sin({x}) = {z}')

# z=math.tan(x)
# print(f'math.tan({x}) = {z}')

# z=math.acos(x)
# print(f'math.acos({x}) = {z}')

# z=math.asin(x)
# print(f'math.asin({x}) = {z}')

# z=math.atan(x)
# print(f'math.atan({x}) = {z}')


# import math
# x=int(input('Введите переменную x: '))
# t=int(input('Введите переменную t: '))
# z=((9*math.pi*t+10*math.cos(x))/(math.sqrt(t)-math.fabs(math.sin(t))))*math.pow(math.e,x)
# print("z = {0:.2f}".format(z))


# A=input("Введите A: ")
# B=input("Введите B: ")

# if A==B:
#     print('A равен B')
# else:
#     print('A не равен B')


# a=int(input("Введите число: "))

# if a < 0:
#     print(a, 'меньше нуля')
# elif a == 0:
#     print(a, 'равен нулю')
# else:
#     print(a, 'больше нуля')


# a=int(input('Введите целое число \n'))
# b=int(input('Введите целое число \n'))
# c=int(input('Введите целое число \n'))

# if a<b:
#     if a<c:
#         y=a
#     else:
#         y=c
# else:
#     if b<c:
#         y=b
#     else:
#         y=c

# print('минимальное: ', y)

# number = int(input('Введите число: '))

# i = 1
# factorial= 1

# while i <= number:
#     factorial *= i
#     i += 1

# print(f'Факториал {number} равен {factorial}')


# n = int(input('Введите количество элементов последовательности: '))
# x=1
# s=0
# print(x)
# for i in range(n):
#     s+=x
#     x/=-2
#     print(x)

# print('Сумма ряда: ',s)


# n= int(input('Введите целое число не меньшее 2\n'))
# i=2
# while n%i !=0:
#     i+=1

# print('наименьший натуральный делитель: ', i)



# s1= 'Пропаганда'
# s2= 'Сенсация'
# s3='Сенсация*Сенсация*Сенсация*Сенсация'
# s4="ГнГнГнКн"
# print('s1 = ',s1)
# print('s2 = ',s2)
# print('s3 = ',s3)
# print('s4 = ',s4)
# print('s1+s2 = ',s1+s2)
# print('s1*3 = ',s1*3)
# print('s1[2] = ',s1[2])
# print('s1[2,4] = ',s1[2:4])
# print('s3.count = ',s3.count(s2))
# print('s1.find("а") = ',s1.find('а'))
# print('s1.index("п") = ',s1.index('п'))
# print('s1.rindex("д") = ',s1.rindex('д'))
# print('s4.replace("Гн","Кн",2) = ',s4.replace("Гн","Кн",2))
# print('s3.split("*") = ',s3.split('*'))
# print('s1.upper = ',s1.upper())
# print('s1.lower = ',s1.lower())



# s=input('Введите строку \n')
# flag=1
# string=''
# for i in range(len(s)):
#     if s[i]!=' ':
#         string+=s[i]
# print(string)
# for i in range(len(s)//2):
#     if string[i]!=string[-i-1]:
#         flag=0
#         break
# if flag: print('Палиндром')
# else : print('не палиндром')


# s= input('Введите строку \n')
# res=s.split(" ")
# for i in range(len(res)):
#    if res[i][-1] == 'я':
#       print(res[i])


# l = [i for i in range(10)]
# print(l)



# c= [c*3 for c in "list"]
# print(c)

# l = [(i+1)+i for i in range(12)]
# print(l)



# from random import *
# l = [randint(10,80) for i in range(10)]
# print('10 чисел сгенерированных случайным образом в диапазоне (10,80)')
# print('l = [randint(10,80) for x in range(10)]: ')
# print(l)

# l = [random() for i in range(10)]
# print('10 чисел сгенерированных случайным образом в диапазоне (10,80)')
# print('l = [random() for i in range(10)] : ')
# print(l)



# print('Ввод списка. Пример 1: ')
# x=[]
# for i in range(4):
#     x.append(int(input()))
# print(x)

# x=[]
# print('Ввод списка. Пример 2: ')
# x= [int(input()) for i in range(4)]
# print(x)



# a=[0,2,2,2,4]
# b=[5,6,7,2,9]
# print('Исходный список a: ',a)
# print('Исходный список b: ',b)
# x=99
# y=5

# a.append(x)
# print('a.append(x): ',a)

# a.extend(b)
# print('a.extend(b): ',a)

# a.insert(3,x)
# print('a.insert(3,x): ',a)

# a.remove(x)
# print('a.remove(x): ',a)

# print('a.pop(S): ',a.pop(5))
# print(a)

# print('a.index(y,0,len(a)): ', a.index(y,0,len(a)))

# print('a.count(2): ',a.count(2))

# a.reverse()
# print('a.reverse(): ',a)

# z=a.copy()
# print('z=a.copy(): ',z)

# z.clear()
# print('z.clear(): ')
# print('z = ',z)




# n=int(input('Введите длину массива \n'))
# m=int(input('Введите число M\n'))
# x=[]
# y=[]
# for i in range(n):
#     print('Введите',i,'элемент: ')
#     x.append(int(input()))
# for i in range(n):
#     if abs(x[i])>m:
#         y.append(x[i])

# print('Введенное число M: ',m)
# print('Массив X: ',x)
# print('Массив Y: ',y)



# m=int(input('Введите количество строк: '))
# n=int(input('Введите количество столбцов:'))
# a=[]

# for i in range(m):
#     b=[]
#     for j in range(n):
#         print(f"Введите ['{i}','{j}'] элемент")
#         b.append(int(input()))
#     a.append(b)

# print('Исходный массив: ')
# for i in range(m):
#     for j in range(n):
#         print(a[i][j],end=' ')
#     print()

# print()
# print('Итог: ')
# for i in range(m):
#     for j in range(n):
#         if a[i][j]<0: a[i][j]=0
#         elif a[i][j]>0: a[i][j]=1

# for i in range(m):
#     for j in range(n):
#         print(a[i][j],end=' ')
#     print()





# n=3
# a=[]
# for i in range(n):
#   b=[]
#   for j in range(n):
#     print(f"Введите ['{i}', '{j}']  элемент")
#     b.append(int(input()))
#   a.append(b)

# for i in range(n):
#   for j in range(n):
#     print(a[i][j], end=" ")
#   print()

# maximum=a[0][2]
# for i in range(n):
#   for j in range(n):
#     if maximum<a[i][2]:
#       maximum=a[i][2]
# print('Максимальный элемент третьего столбца:', maximum)

# maximum=[1][0]
# for i in range(n):
#   for j in range(n):
#     if maximum<a[1][j]:
#       maximum=a[1][j]
# print('Максимальный элемент второй строки:', maximum)





# n=3
# A=[]

# for i in range(n):
#     A.append([9]*n)

# for i in range(n):
#     for j in range(n):
#         print(A[i][j], end=' ')
#     print()

# for i in range(n):
#     A[i]= [2]*i+[0]+[1]*(n-i-1)

# print()

# for i in range(n):
#     for j in range(n):
#         print(A[i][j], end=' ')
#     print()




# n=3
# A=[]

# for i in range(n):
#     A.append([9]*n)

# for i in range(n):
#     for j in range(n):
#         print(A[i][j], end=' ')
#     print()

# for i in range(n):
#     for j in range(0,i):
#         A[i][j]=2
#     A[i][i]=0
#     for j in range(i+1,n):
#         A[i][j]=1

# print()

# for i in range(n):
#     for j in range(n):
#         print(A[i][j], end=' ')
#     print()




# n=3
# A=[]

# for i in range(n):
#     A.append([9]*n)

# for i in range(n):
#     for j in range(n):
#         print(A[i][j], end=' ')
#     print()

# for i in range(n):
#     for j in range(n):
#         if i<j:
#             A[i][j]=1
#         elif i>j:
#             A[i][j]=2
#         else:
#             A[i][j]=0

# print()

# for i in range(n):
#     for j in range(n):
#         print(A[i][j], end=' ')
#     print()




# A=[[1,2,3,4],[5,6,7,8]]

# print('Массив A: ')
# for i in A:
#     print(' '.join(list(map(str,i))))

# s=0
# for i in range(len(A)):
#     for j in range(len(A[i])):
#         s+=A[i][j]
# print('Пример 1. Сумма всех элементов: ',s)

# s=0
# for row in A:
#     for elem in row:
#         s+=elem
# print('Пример 2. Сумма всех элементов: ',s)




# A=[[2,6,33,1,66,8],[2,45,1,8,65,32]]
# for row in A:
#     for elem in row:
#         print(elem,end=' ')
#     print()





# n=3
# A=[]
# for i in range(n):
#   B=[]
#   for i in range(n):
#     B.append(int(input()))
#   A.append(B)

# for i in range(n):
#   for j in range(n):
#     print(A[i][j], end=' ')
#   print()






# n=3
# A=[]
# for i in range(n):
#   B=[]
#   for i in range(n):
#     B.append(int(input()))
#   A.append(B)

# print(A)





# n=6
# m=2
# A=[]
# for i in range(n):
#   A.append([0]*m)

# print(A)





# n=3
# m=3
# A=[0]*n
# for i in range(n):
#   A[i]=[0]*m

# print('A: ',A)





# def zam(X):
#   tmp=X[0]
#   X[0]=X[len(X)-1]
#   X[len(X)-1]=tmp

# A=[]
# m=int(input('Введите количество элементов массива: '))
# for i in range(m):
#   print('Введите ',i,'-й элемент массива: ')
#   A.append(int(input()))

# print(A)
# zam(A)
# print(A)





# import math
# def s(x,y,z):
#   p=(x+y+z)/2
#   s=math.sqrt(p*(p-x)*(p-y)*(p-z))
#   return s
  
# A=[]

# for i in range(3):
#   print('Введите стороны',i+1,'-го треугольника: ')
#   a=int(input('a: '))
#   b=int(input('b: '))
#   c=int(input('c: '))
#   A.append(s(a,b,c))

# for i in range(3):
#     print(f'Площадь {i}-го треугольника: {A[i]}')

# if A[0]==A[1]==A[2]:
#     print('Треугольники равносторонние')
# else:
#     print('Треугольники не равносторонние')





# def sumD(n):
#   summa=0
#   while n!=0:
#     summa+=n%10
#     n//=10
#   return summa

# print(sumD(int(input())))





# def printChar(s):
#   print(s)

# sim=input('Введите что нибудь: ')
# printChar(sim)
# printChar("Hello")





# n=int(input('Введите длину массива: '))
# d=[]
# sum=0
# for i in range(n):
#   d.append(int(input(f'Введите {i}-й элемент массива: ')))
# for x in range(len(d)):
#   if x%2 !=0:
#     sum+=d[x]

# print('Массив: ', d)
# print('Сумма элементов с нечетными индексами: ', sum)
  



# n=int(input('Введите длину массива: '))
# a=[]
# for i in range(n):
#   print('Ведите', i,'элемент: ')
#   a.append(int(input()))
# print('Исходный массив: ', a)
# for i in range(n):
#   if a[i]<0:
#     a[i]=-a[i]
# print('Измененный массив: ', a)




# n=int(input("Введите длину массива\n"))
# m=int(input("Введите число М\n"))
# x=[]
# y=[]
# for i in range(n):
#   print('Введите', i,'элемент массива: ')
#   x.append(int(input()))
# for i in range(n):
#   if abs(x[i])>m:
#     y.append(x[i])

# print('Ввденное число M:', m)
# print('Массив X:', x)
# print('Массив Y:', y)    




#?решение задач на Python

# n=input("Введите трех значное число: ")
# a=int(n[0])
# b=int(n[1])
# c=int(n[2])
# print(f'Сумма цифр числа: {a+b+c}')












# import math
# print("Введите коэфиценты для уравнения")
# print("ax^2+bx+c=0:")
# a=float(input("a="))
# b=float(input("b="))
# c=float(input("c="))
# discr=b**2-4*a*c
# print(f'Дискриминант D={discr}')

# if discr>0:
#     x1=(-b+math.sqrt(discr))/(2*a)
#     x2=(-b-math.sqrt(discr))/(2*a)
#     print(f'x1={x1} \n x2={x2}')
# elif discr==0:
#     x=-b/(2*a)
#     print(f'x={x}')
# else:
#     print("Корней нет")












# import math

# AB = input("Длина первого катета: ")
# AC = input("Длина второго катета: ")
# AB = float(AB)
# AC = float(AC)
# BC = math.sqrt(AB**2+AC**2)
# S = (AB*AC)/2
# P = AB+AC+BC

# print(f'Площадьтреугольника: {S}')
# print(f'Периметр треугольника: {P}')


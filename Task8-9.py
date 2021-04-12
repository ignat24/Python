from math import *
import random

def Task1():
    print("Task 1, Hello User")
    names=[]
    user_n=input("What's your name? \n:")
    if user_n!='':
        names.append(user_n)
    if len(user_n)==0:
        print('We need to find some users!')
    for name in names:
        if(name =='Admin'):
            print('Hello',name,"I hope you're well" )
        else:
            print('Hello',name,'thank you for logging in again!')
def Task2():
    print("Task 2, triangle - hexagon")
    d = {3: 'triangle', 4:'rectangle or square',5:'pentagon',6:'hexagon'}
    print("Hello User, let's start!")
    print('Enter the number of corners(3-6)')
    while type:
        corner = input(': ')  # Ввод числа
        try:
            corner = int(corner)
        except ValueError:
            print('"' + corner + '"' + ' - не является числом')
        else:
            break

    try:
        assert corner in d.keys()
        print("Your figure is",d[corner])
    except AssertionError:
        print('Error, Try again!')

def Task3():
    print("Task 3, -st,-nd,-rd,-th")
    list=[i+1 for i in range(9)]
    for i in list:
        if i==1:
            print(str(i)+'-st')
        elif i==2:
            print(str(i)+'-nd')
        elif i==3:
            print(str(i)+'-rd')
        else:
            print(str(i)+'-th')
def Task4():
    print("Task 4, Pair or no pair")
    print("Hello User, let's start!")
    print('Enter the number')
    while type:
        k = input(': ')
        try:
            k = int(k)
        except ValueError:
            print('"' + k + '"' + ' - не является числом')
        else:
           break
    if(k%2==0):
        print("Number is pair")
    else:
        print("Number isn't pair")
def Task5():
    print("Task 5, Number of days in a month")
    print("Hello User, let's start!")
    print("1 - Ordinary year, 2 - Leap year")
    while type:
        year = input(': ')
        try:
            year = int(year)
        except ValueError:
            print('"' + year + '"' + ' - не является числом')
        else:
            break
    if year>2 or year <1:
        print("Error!")
        exit()

    month = {'january':31,'february':28,'march':31,'april':30,'may':31,'june':30,'july':31,'august':31,'september':30,
             'october':31,'november':30,'december':31,}
    enter_month=input('Enter month(in English, Please): ')

    try:
        assert enter_month in month.keys()
        if year == 1 and enter_month == 'february':
            print('Number of days in your month is:', month[enter_month] + 1)
        else:
            print('Number of days in your month is:', month[enter_month])
    except AssertionError:
        print("Error, please enter correct month!")





def Task6():
    print("Task 6, Ordinary year or Leap year")
    print("Hello User, let's start!")
    print("Enter year from 1900 to 3000")
    while type:
        year = input(': ')
        try:
            year = int(year)
        except ValueError:
            print('"' + year + '"' + ' - не является числом')
        else:
            break
    if year>1900 and year < 3000:
        if (year%4==0 and year%100!=0) or year%400==0:
            print(year,"is Leap year!")
        else:
            print(year, "is Ordinary year!")
    else:
        print("Error, please enter correct year!")




def Task7():
    print("Task 7, Summa of numbers")
    print("Hello User, let's start!")

    numbers=list()
    per=1
    sum=0
    while(per!=0):
        while type:
            per = input('Enter integer number(0 - finish): ')
            try:
                per = int(per)
            except ValueError:
                print('"' + per + '"' + ' - не является числом')
            else:
                break

        numbers.append(per)
    for i in numbers:
        sum+=i
    print("Summa is ",sum)

def Task8():
    print("Task 8, Calculator")
    print("Hello User, let's start!")
    while True:
        while True:
            numb_1=input("Enter first number: ")
            numb_2 = input("Enter second number: ")
            if numb_1=='' or numb_2=='':
                print('Try again:')
            else:
                numb_1 = float(numb_1)
                numb_2 = float(numb_2)
                break




        act = input("Enter action(0-exit): ")
        if act=='0':
            break
        if act =='':
            print("Error, enter correct form")

        else:
            if act=='+':
                print("X+Y = ",numb_1+numb_2)
            elif act=='-':
                print("X-Y = ",numb_1-numb_2)
            elif act=='*':
                print("X*Y = ",numb_1*numb_2)
            elif act=='/':
                if numb_2!=0:
                    print("X/Y = ",numb_1/numb_2)
                else:
                    print("Division by zero!")
            elif act=='mod':
                print("X%Y = ",numb_1%numb_2)
            elif act=='div':
                print("X//Y = ",numb_1//numb_2)
            elif act=='pow':
                print("X**Y = ",numb_1**numb_2)





def Task9():
    print("Task 9,People on bills")
    print("Hello User, let's start!")
    people={1:'Володимир Великий',2:'Ярослав Мудрий',5:'Богдан Хмельницький',10:'Іван Мазепа',20:'Іван Франко',
            50:'Михайло Грушевський',100:'Тарас Шевченко',200:'Леся Українка',500:'Григорій Сковорода'}
    try:
        while type:
            bill = input('Please, Enter denomination(1,2,5,10,20,50,100,200,500): ')
            try:
                bill = int(bill)
            except ValueError:
                print('"' + bill + '"' + ' - не является числом')
            else:
                break

        assert bill in people.keys()
        print("On",bill,"depicted",people[bill])
    except AssertionError:
        print('Bill is not found,try again!')

def Task10():
    print("Task 10,Chess board")
    print("Hello User, let's start!")


    while type:
        letter=input("Enter letter(a-h): ")
        try:
            letter=ord(letter)
            if letter<97 or letter>104:
                print("Error")
                exit()

            letter=chr(letter)
        except ValueError:
            print('"' + number + '"' + ' - не является числом')
        else:
            break
    while type:
        number = input('Please, Enter number(1-8): ')
        try:
            number = int(number)
        except ValueError:
            print('"' + number + '"' + ' - не является числом')
        else:
            break

    count=1
    let=['a','b','c','d','e','f','g','h',]
    for i in let:
        if i==letter:
            break
        count+=1

    if count%2==0:
        color=1
        if number%2==0:
            color=0
    else:
        color=0
        if number%2==0:
            color=1


    if color==0:
        print("Black")
    else:
        print("White")



def Task11():
    print("Task 10,From 10 to 2")
    print("Hello User, let's start!")


    while type:
        per = input("Enter number(0-10): ")
        try:
            per = int(per)
        except ValueError:
            print('"' + per + '"' + ' - не является числом')
        else:
            break
    b=''
    if per<100 and per>-1:
        while per>0:
            b=str(per%2)+b
            per=per//2
        print("Binary = ",b)
    else:
        print("Error!")
    len_b=len(b)
    k=0
    for i in range(0,len_b):
        k=k+int(b[i])*(2**(len_b-i-1))
    print("From '10'", b,"to 2 =",k)


def Task12():
    print("Task 10,Камень, ножницы, бумага")
    print("Hello User, let's start!")
    while True:
        while type:
            user = input("1 - Камень, 2 - Ножницы, 3 - Бумага, 10 - Завершить: ")
            try:
                user = int(user)
            except ValueError:
                print('"' + user + '"' + ' - не является числом')
            else:
                break

        if user == 10:
            break
        if user > 3 or user < 1:
            print("Error")
            break
        else:
            if user==1:
                print("Вы выбрали Камень")
            if user==2:
                print("Вы выбрали Ножницы")
            if user==3:
                print("Вы выбрали Бумага")
            comp=random.randint(1,3)
            if comp==1:
                print("Компьютер выбрал Камень")
            if comp==2:
                print("Компьютер выбрал Ножницы")
            if comp==3:
                print("Компьютер выбрал Бумага")
            if comp==user:
                print("Ничья")
            if comp==1 and user == 2:
                print("Ты проиграл")
            if comp == 2 and user == 3:
                print("Ты проиграл")
            if comp == 3 and user == 1:
                print("Ты проиграл")
            else:
                print("Ты победил")
            print("Давай еще сыграем!")




def switchTask(selection):
    return {1: Task1, 2: Task2,3:Task3,4:Task4,5:Task5,6:Task6,7:Task7,8:Task8,9:Task9,10:Task10,11:Task11,12:Task12}.get(selection,'error')

while True:
    print('0 - Завершить\n 1 - Приветствие\n 2 - Название геометрической фигуры\n 3 - Порядковые числительные\n 4 - Черное или нечетное\n '
          '5 - Кол-во дней в месяце\n 6 - Высокосный или нет\n 7 - Сумма чисел\n 8 - Калькулятор\n 9 - Имена на банкнотах\n'
          ' 10 - Chess board\n 11 - From 10 to 2\n 12 - К_Н_Б\n')
    selection = int(input('\n:'))
    if selection>12 or selection<0:
        print('Что-то пошло не так(')
    else:
        switchTask(selection)()
    select = input('Меню(1-Да,0-Нет): ')
    if select == '0':
        break
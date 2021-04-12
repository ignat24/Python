from re import*
from io import *
import codecs
from sqlite3 import *
import csv


def Task1():
    print('Задание 1:')
    sum=0
    file=open('numbers.txt','r')
    file1=open('sum_numbers.txt','w')
    for lines in file:
        a=int(lines)
        sum=sum+a
    b=str(sum)
    print(sum)
    file1.write(b)
def Task2():
    print('--------------------------------')
    print('Задание 2:')
    z=0
    file=open('number_par.txt','w')
    per=input('Введите целое число: ')
    for i in range(len(per)):
        if(per[i]=='.' or per[i]==','):
            z=1
    if(z==1):
        print('Вы ввели не целое число')
    else:
        per=int(per)
        if(per%2==0):
            print('Четное')
            file.write('Четное')
        else:
            print('Нечетное')
            file.write('Нечетное')
def Task3():
    print('--------------------------------')
    print('Задание 3:')
    data=list()
    file = 'learning_python.txt'
    with open(file) as openfile:
        for line in openfile:
            line=line.rstrip()
            data.append(line)

    for i in data:
        print(i)

def Task4():
    print('--------------------------------')
    print('Задание 4:')
    data = list()
    file = 'learning_python.txt'
    with open(file) as openfile:
        for line in openfile:
            line = line.rstrip()
            data.append(line)

    for word in data:
        if findall('Python',word):
            word=word.replace('Python','C++')
            print(word)

        else:
            print(word)


def Task5():
    print('--------------------------------')
    print('Задание 5:')
    name = list()
    per = input('Name =' )
    file =open('guest_books.txt','w')
    while(per!=''):
        per='Hello '+per
        file.write(per+'\n')
        print(per)
        print('Завершить - Enter')
        per = input('Name =')



def Task6():
    print('--------------------------------')
    print('Задание 6:')
    count = 0
    word='the'
    file = 'book.txt'
    with open(file) as openfile:
        for line in openfile:
            line=line.lower()
            if findall(word,line):
                count=count+1


    print('Кол-во "the" =',count)


def Task7():
    print('--------------------------------')
    print('Задание 7:')
    text=list()
    endl='\n'
    file ='book.txt'
    with open(file) as openfile:
        text=open(file).readlines()

    file1='formatted_text.txt'
    with open(file1,'w') as openfile1:
        for line in text:
            line=sub("^\s+|\n|\r|", '', line)
            openfile1.write(line)

            



def Task8():
    print('--------------------------------')
    print('Задание 8:')
    file = 'book1.txt'
    file1 = 'chapters.txt'
    with open(file1,'w') as openfile1:
        with codecs.open(file, "r", "utf_8_sig") as openfile:
            for line in openfile:
                line=line.rstrip()
                if line.startswith('CHAPTER'):
                    openfile1.write(line+'\n')


def Task9():
    print('--------------------------------')
    print('Задание 9:')
    file='book2.txt'
    count_A=0
    count_a=0
    with codecs.open(file, "r", "utf_8_sig") as openfile:
        for line in openfile:
            for words in line:
                if words.lower():
                    count_a+=1
                if words.isupper():
                    count_A+=1
        per=count_a*100/(count_A+count_a)
        print('Кол-во маленьких букв = ',per)
        print('Кол-во больших букв = ',100-per)


def Task10():
    print('--------------------------------')
    print('Задание 10:')


    def createDataBase():
        conn = connect('imdb.db')
        curs = conn.cursor()
        curs.execute('''CREATE TABLE IF NOT EXISTS ratings (id INT PRIMARY KEY, title VARCHAR(20), 
                                                    year INT, rating FLOAT)''')
        conn.commit()

    def addData():
        conn = connect('imdb.db')
        curs = conn.cursor()
        count_id = 0
        name_file = 'IMDb movies.csv'
        with codecs.open(name_file, 'r', 'utf_8_sig') as open_file:
            reader = csv.DictReader(open_file, dialect='excel')
            for row in reader:
                count_id += 1
                title = str(row['title'])
                year = str(row['year'])
                rating = str(row['reviews_from_critics'])
                try:
                    curs.execute('INSERT INTO ratings (id, title, year, rating) VALUES(?,?,?,?)',
                                 (int(count_id), title, int(year), float(rating)))
                except:
                    print('Error!')
                    break
                conn.commit()
                if count_id == 15:
                    print('Count =', count_id)
                    break

    def sortDatabase():
        conn = connect('imdb.db')
        curs = conn.cursor()
        curs.execute('SELECT * FROM ratings ORDER BY title')
        conn.commit()
        rows = curs.fetchall()
        print('\nФильмы с рейтингом больше 8.7:\n')
        print('id   movies   year   rating')
        for tpl in rows:
            if tpl[3] >= 8.70:
                for value in tpl:
                    print(value, '  ', end='')
                print('\n', end='')

    createDataBase()
    addData()
    sortDatabase()


def switchTask(selection):
    return {1: Task1, 2: Task2,3:Task3,4:Task4,5:Task5,6:Task6,7:Task7,8:Task8,9:Task9,10:Task10}.get(selection,'error')

while True:
    print('0 - Завершить\n 1 - Первое задание\n 2 - Второе задание\n 3 - Третье задание\n 4 - Четвертое задание\n 5 - Пятое задание\n 6 - Шестое задание\n 7 - Седьмое задание\n 8 - Восьмое задание\n 9 - Девятое задание\n 10 - Десятое задание\n')
    selection = int(input('\n:'))
    if selection>10 or selection<0:
        print('Что-то пошло не так(')
    else:
        switchTask(selection)()
    select = input('Продолжить(1-Да,0-Нет): ')
    if select == '0':
        break
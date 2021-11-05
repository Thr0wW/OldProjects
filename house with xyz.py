from math import*
from turtle import*
def login_and_password_verification():
    name='Игнат'
    password='q1w2e3r4'
    n=input('Введите ваш логин:')
    p=input('Пароль:')
    if n==name and p==password:
        
        return True
    else:
        return False

def checking_the_height_of_the_house():
    minimal=50
    maximal=400
    while True:
        global x
        x= int (input('высота дома:'))
        if x > minimal and x < maximal:
            print('Будет сделано господин!')
            return x
        else:
            print('Недопустимая высота дома!Высота дома должна быть меньше ', maximal, ' и больше ' , minimal)
def build_the_house(x):
    global y
    global z

    y=sqrt(x**2+x**2)
    z=y/2
    forward(x) 
    left(90)
    forward(x)
    left(45)
    forward(z)
    left(90)
    forward(z)
    left(45)
    forward(x)
    left(135)
    forward(y)
    left(135)
    forward(x)
    left(135)
    forward(y)


#verification=login_and_password_verification()
#if verification==False:
 #   print('Логин или пароль неверный')
  #  exit()
#else:
 #   print('доступ разрешен.')
x = checking_the_height_of_the_house()
build_the_house(x) 

             
  

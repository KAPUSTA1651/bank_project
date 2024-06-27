import json
from colorama import init
init()
from colorama import Fore, Back, Style
user = {}
import random



def loos_user():
    global user
    with open("registr.json", "r", encoding="utf-8") as jf:
        user = json.load(jf)


def save_user():
    with open("registr.json", "w", encoding="utf-8") as ot:
        json.dump(user, ot)

def zapros():
    while True:
        a=input('введите логин: ')
        b=input('введите пороль: ')
        if a in user and b==user[a]:
            print(Fore.BLACK, Back.GREEN+'добро пожалывать:',a+Style.RESET_ALL )
            break
        else:
            print(Fore.BLACK, Back.RED+'вы ввели неверный логин или пороль!'+Style.RESET_ALL )

def reg():
    global user
    while True:
        print(Fore.BLACK, Back.RED+'вы находитесь в регистрации аккаунта'+Style.RESET_ALL)
        a=input('введите имя пользователя: ')
        print('1 - ввести пароль вручную')
        print('2 - сгенерировать пороль')
        pas=input('введите номер действия: ')
        if pas=='1':
            while True:
                print(Fore.BLACK, Back.CYAN +'ВНИМАНИЕ! Пороль должен содержать не меньше 8 символов, заглавные и строчные буквы, а также цифры!'+ Style.RESET_ALL)
                b=input('введите пороль: ')
                g=input('повторите пороль: ')
                if b==g and  len(a) >= 8 and not a.isupper() and not a.islower() and not a.isalpha() and not a.isdigit():
                    user[a]=b
                    save_user()
                    print(Fore.BLACK, Back.GREEN + 'ваша запись успешно добавлена!' + Style.RESET_ALL)
                    break
                else:
                    print(Fore.BLACK, Back.RED+'вы ввели два разных пороля, попробуйте ещё раз!'+Style.RESET_ALL)
        elif pas=='2':
            while True:
                k=generate_password()
                print(k)
                h=input('ок - введите 1 / заменить - введите 2')
                if h=='1':
                    user[a]=k
                    save_user()
                    break
                elif h=='2':
                    pass


        break



def vabr():
    while True:
        print('1 - войти')
        print('2 - зарегистрироватся')
        a=(input('выберите номер: '))
        if a=='1':
            zapros()
            break
        elif a=='2':
            reg()
            break
        else:
            print(Fore.BLACK, Back.RED+'вы ввели неверное действие!'+Style.RESET_ALL)

def generate_password(number=6):
    n=[]
    for i in range(number):
        x=random.randint(1,3)
        if x==1:
            n.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        elif x==2:
            n.append(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
        elif x==3:
            n.append(random.choice('0123456789'))
    m=''
    for a in n:
        m+=a
    return m







loos_user()
# zapros()
# reg()
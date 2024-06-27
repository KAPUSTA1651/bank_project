import time

from colorama import init
init()
from colorama import Fore, Back, Style

def complain():
    a=input('Введите жалобу: ')
    with open('complains.txt', 'a',encoding='utf=8') as f:
        f.write('\n'+a)
    print(Fore.BLACK, Back.GREEN+'Ваша жалоба будет рассмотрена в скором времени.'+Style.RESET_ALL )
    time.sleep(2)
# complain()

def suggestions():
    print('Предложения Bank')
    with open('suggestions.txt','r', encoding='utf=8') as g:
        text=g.read()
        print(text)

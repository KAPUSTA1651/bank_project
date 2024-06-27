import os
from registr import*
from bank import *
from client import *
from plot import *
from colorama import init
init()
from colorama import Fore, Back, Style

def clear():
    return os.system('cls')

if __name__ == '__main__':
    load()
    vabr()
    command = ''
    while command != '10':
        print('Доступные действия')
        print('- - - - - - - - - -')
        print('1 - Посмотреть предложения банка')
        print('2 - Отправить жалобу')
        print('3 - Информация о счетах')
        print('4 - Посмотреть прогноз доходов и расходов на следующий месяц')
        print('5 - Добавить транзакцию')
        print('6 - Посмотреть график доллара к рублю')
        print('7 - Посмотреть график доллара к биткоину')
        print('8 - Посмотреть график доллара к йене')
        print('9 - Посмотреть график выброса отходов в океан от 2002 до 2010')
        print('10 - Выйти')
        print('- - - - - - - - - -')
        command = input('выберите действие: ')

        if command == '1':
            print('- - - - - - - - - -')
            suggestions()
            print('- - - - - - - - - -')
        elif command == '2':
            complain()
            clear()
        elif command == '3':
            show_info()
        elif command=='4':
            predict()
            clear()
        elif command=='5':
            make_transaction()
            clear()
        elif command=='6':
            plot_rub_usd()
            clear()
        elif command=='7':
            plot_usd_btc()
            clear()
        elif command == '8':
            plot_usd_yn()
            clear()
        elif command=='9':
            plot_more()
            clear()
        elif command == '10':
            print(Fore.BLACK, Back.GREEN+'Сохранение изменений...'+Style.RESET_ALL )
            save()
            print('До свидания.')
        else:
            print(Fore.BLACK, Back.RED+'вы включили режим ДУРОЧКА. Побробуйте еще раз!'+Style.RESET_ALL )

        # else:
        #     print(Fore.BLACK, Back.RED+'Действие не распознано. Попробуйте ещё раз.'+Style.RESET_ALL )

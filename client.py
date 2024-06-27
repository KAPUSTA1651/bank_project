import json
from colorama import init
init()
from colorama import Fore, Back, Style

client_info = {}



def load():
    global client_info
    with open("client_info.json", "r", encoding="utf-8") as json_file:
        client_info = json.load(json_file)


def save():
    with open("client_info.json", "w", encoding="utf-8") as outfile:
        json.dump(client_info, outfile)


def show_info():
    print("Информация о счетах")
    print("----------------------------------")
    for i in client_info['accounts']:
        print('Имя: ',i['name'])
        print('Платёжная система: ',i['system'])
        print('Номер',i['number'])
        print('Тип',i['type'])
        print('Баланс',i['balance'])
        print('Срок действия',i['validity period'])
        print("----------------------------------")


def predict():
    global client_info
    expenses = 0 # расходы
    income = 0  # доходы
    months = []  # список месяцев, в которые происходили операции

    for transaction in client_info["transactions"]:
        if transaction["type"] =='списание':
            expenses+= transaction["amount"]

        if transaction["type"] =='зачисление':
            income += transaction["amount"]

        if transaction["date"] not in months:
            months.append(transaction["date"])
    print(Fore.BLACK, Back.CYAN+'Предполагаемые расходы в следующем месяце:'+Style.RESET_ALL, expenses/len(months))
    print(Fore.BLACK, Back.MAGENTA+'Предполагаемые доходы в следующем месяце:'+Style.RESET_ALL, income/len(months))

def make_transaction():
    global client_info
    print(Fore.BLACK, Back.CYAN+"Доступные счета:"+Style.RESET_ALL )
    i = 1
    for account in client_info["accounts"]:
        print(i, "-", account["name"], "-", account["number"])
        i += 1

    account_num = input("Введите счёт: ")

    try:
        account_num = int(account_num)
    except:
        print(Fore.BLACK, Back.RED+"Ошибка ввода. Прерываю транзакцию..."+Style.RESET_ALL )
        return

    for i in range(len(client_info["accounts"])):
        if i + 1 == account_num:
            account = client_info["accounts"][i]["number"]
            break
    else:
        print(Fore.BLACK, Back.RED+"Такого счёта не существует. Прерываю транзакцию..."+Style.RESET_ALL)
        return
    print(Fore.BLACK, Back.CYAN+"Типы транзакций:"+Style.RESET_ALL)
    print("1 - списание")
    print("2 - зачисление")
    transaction_type = input("Выберите тип транзакции: ")
    if transaction_type == "1":
        transaction_type = "списание"
    elif transaction_type == "2":
        transaction_type = 'зачисление'
    else:
        print(Fore.BLACK, Back.RED+"Такого типа не существует. Прерываю транзакцию..."+Style.RESET_ALL)
        return

    print(Fore.BLACK, Back.MAGENTA+"Дата транзакции"+Style.RESET_ALL)
    year = input("Введите год: ")
    month = input("Введите месяц: ")

    if int(year) > 2022 or int(month) > 12  or int(month) < 1:
        print(Fore.BLACK, Back.RED+'Неверная дата. Прерываю транзакцию...'+Style.RESET_ALL)
        return
    try:
        amount = int(input("Введите сумму: "))
    except:
        print(Fore.BLACK, Back.RED+'Ошибка ввода. Прерываю транзакцию...'+Style.RESET_ALL)
        return
    if amount < 1 :
        print(Fore.BLACK, Back.RED+"Сумма не может быть меньше 1. Прерываю транзакцию..."+Style.RESET_ALL)
        return

    new_data = {"account": account,
    		"type":transaction_type,
              "date": {"year": year, "month": month},
            "amount": amount}
    print(new_data)
    if transaction_type == 'списание':
        client_info["accounts"][account_num - 1]["balance"] -= amount
    elif transaction_type == 'зачисление':
        client_info["accounts"][account_num - 1]["balance"] += amount

    client_info["transactions"].append({"account":account,
                                        "type": type,
                                        "date": {"year": year, "month": month},
                                        "amount": amount})

    #print(client_info['transactions'][-1])
    print(Fore.BLACK, Back.GREEN+"Транзакция записана. Текущий баланс на счёте:"+Style.RESET_ALL, client_info["accounts"][account_num - 1]["balance"])

load()
def main_menu():
    balance = 0
    purchases = []

    while True:
        print('\n1. Пополнение счета')
        print('2. Покупка')
        print('3. История покупок')
        print('4. Выход')

        choice = input('Выберите пункт меню: ')
        
        if choice == '1':
            balance = top_up(balance)
        elif choice == '2':
            balance, purchases = make_purchase(balance, purchases)
        elif choice == '3':
            show_history(purchases)
        elif choice == '4':
            print("Выход из программы")
            break
        else:
            print('Неверный пункт меню')

def top_up(balance):
    amount = float(input('Введите сумму для пополнения: '))
    balance += amount
    print(f'Счет пополнен на {amount}. Баланс: {balance}')
    return balance

def make_purchase(balance, purchases):
    amount = float(input('Введите сумму покупки: '))
    if amount > balance:
        print('Недостаточно средств.')
    else:
        item = input('Введите название покупки: ')
        balance -= amount
        purchases.append((item, amount))
        print(f'Покупка "{item}" на сумму {amount} завершена. Баланс: {balance}')
    return balance, purchases

def show_history(purchases):
    if purchases:
        print('История покупок:')
        for item, amount in purchases:
            print(f'{item}: {amount}')
    else:
        print('История покупок пуста.')

# Запуск программы
main_menu()

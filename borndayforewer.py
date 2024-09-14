def check_year():
    year = input('Введите год рождения А.С.Пушкина: ')
    while year != '1799':
        print("Не верно")
        year = input('Введите год рождения А.С.Пушкина: ')
    return True

def check_day():
    day = input('Введите день рождения Пушкина: ')
    while day != '6':
        print("Не верно")
        day = input('В какой день июня родился Пушкин? ')
    return True

if check_year():
    if check_day():
        print('Верно')

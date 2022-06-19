right_name = 'angelina'
right_password = 'ZXCV1234'

def check(name, password, number = 3):
    n = 1
    while n < number:
        if name == right_name and password == right_password:
            return print('Вход выполнен!')
        else:
            name = input('Введите имя пользователя: ')
            password = input('Введите пароль: ')
            n += 1
    print('Количество попыток для входа:', number,'Система заблокирована. Повторите попытку через 5 минут.')
check(input('Введите имя пользователя: '), input('Введите пароль:' ))

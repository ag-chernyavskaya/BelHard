right_name = 'angelina'
right_password = 'ZXCV1234'

def check(name, password, number = 3, mess = 'Система заблоктрована. Повторите попытку через 5 минут.'):
    if number < 0:
        return mess
    for i in range(number):
        if name == right_name and password == right_password:
            return 'Вход выполнен!'
        else:
            name = input('Введите заново имя пользователя: ')
            password = input('Введите заново пароль: ')
            check(name=name, password=password,number=-1)

def validate(input_login,input_password):
    name = input_login
    password = input_password
    result = check(name=name,password=password)
    return result
print(validate('ang',123))

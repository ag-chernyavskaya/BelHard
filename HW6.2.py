def information(**kwargs):
    if 'deth' in kwargs:
        if 'patr' in kwargs:
            return f"{kwargs['name'][0]}.{kwargs['patr'][0]}.{kwargs['surname']} " \
                   f"({kwargs['birth']} - {kwargs['deth']}) - {kwargs['krt']}"
        else:
            return f"{kwargs['name'][0]}.{kwargs['surname']} " \
                   f"({kwargs['birth']} - {kwargs['deth']}) - {kwargs['krt']}"
    else:
        if 'patr' in kwargs:
            return f"{kwargs['name'][0]}.{kwargs['patr'][0]}.{kwargs['surname']} " \
                   f"({kwargs['birth']}) - {kwargs['krt']}"
        else:
            return f"{kwargs['name'][0]}.{kwargs['surname']} " \
                   f"({kwargs['birth']}) - {kwargs['krt']}"



print(information(name ='Александр', patr = 'Сергеевич', surname = 'Пушкин', birth = '6.06.1799',
                  deth = '10.02.1837',krt ='русский поэт, драматург и прозаик'))
print(information(name ='Иегошуа',surname = 'Соболь', birth = '24.08.1939',
                  krt ='израильский драматург, писатель и режиссер'))
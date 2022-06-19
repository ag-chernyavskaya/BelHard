def information(**kwargs):
    if 'deth' in kwargs:
        return f"{kwargs['name']} ({kwargs['birth']}-{kwargs['deth']}) - {kwargs['krt']}"
    else:
        return f"{kwargs['name']} ({kwargs['birth']}) - {kwargs['krt']}"


print(information(name ='А.С.Пушкин', birth = '6.06.1799', deth = '10.02.1837',krt ='русский поэт, драматург и прозаик'))
print(information(name ='И.Соболь', birth = '24.08.1939',krt ='израильский драматург, писатель и режиссер'))
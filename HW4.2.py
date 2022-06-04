note = '''In a distant, but not so unrealistic, future where mankind has abandoned
earth because it has become covered with trash from products sold by the
powerful multi-national Buy N Large corporation, WALLE, a garbage
collecting robot has been left to clean up the mess. Mesmerized with
trinkets of Earth's history and show tunes, WALLE is alone on Earth except
for a sprightly pet cockroach. One day, EVE, a sleek (and dangerous)
reconnaissance robot, is sent to Earth to find proof that life is once again
sustainable.'''
print(f' Длинна текста в записке равна {len(note)}')
print(f'Текст записки в нижнем регистре: {note.lower()}')
print(f"Замена неправильно написанного слова: {note.replace('WALLE','WALL-E')}")
print(f"Слово Earth встречается в записке {note.count('Earth')} раза")
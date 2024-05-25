humor = "Не знаю, как там в Лондоне, я не была. Может, там собака - друг человека. А у нас управдом  - друг человека!"
reve_str = "Python yes"
reve_log = "Я Денис"
print(len(humor))
print(reve_str[ : : -1])
print(humor.title())
print(humor.upper())
print(humor.count('нд'))
print(humor.count('ам'))
print(humor.count('о'))
print(humor.replace(' ', ''))
print(humor[:])
a = reve_log.split()
a.reverse()
reve_log = ' '.join(a)
print(reve_log)
name = 'Katia Karytsko'
print(f'Меня зовут {name} и мне бы {len(humor) - 8}% хотелось, чтобы был {reve_str}!')
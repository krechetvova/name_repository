first_name = 'Vladimir'
last_name = 'Ivanov'
a = 2
b = 3
result = a + b

print('Меня зовут ' + first_name + ' ' + last_name)

if (result == 5):
    print('Результат: ' + str(result));
else:
    print('Ошибка')

name = input('Как тебя зовут?')
age = int(input('Сколько тебе лет?'))
result = 'Привет ' + name + ', тебе ' + str(age) + ' лет.'
print(result)
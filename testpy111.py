''''''
#from num2words import num2words
import random
import math

def strok_ekvival2(nomer_int):
    '''
    Основная функция ниже это отдельная функция для окончания двойки и единицы
    :param nomer_int: номер введеное числа
    :return: pass
    '''
    Capitals = dict()
    Capitals[0] = ' '
    Capitals[1] = 'Одна'
    Capitals[2] = 'Две'# Две 2000 2999 ххх 102000 992000
    Capitals[3] = 'Три'
    Capitals[4] = 'Четыре'
    Capitals[5] = 'Пять'
    Capitals[6] = 'Шесть'
    Capitals[7] = 'Семь'
    Capitals[8] = 'Восемь'
    Capitals[9] = 'Девять'
    Capitals[10] = 'Десять'
    Capitals[11] = 'Одиннадцать'
    Capitals[12] = 'Двенадцать'
    Capitals[13] = 'Тринадцать'
    Capitals[14] = 'Четырнадцать'
    Capitals[15] = 'Пятнадцать'
    Capitals[16] = 'Шестнадцать'
    Capitals[17] = 'Семнадцать'
    Capitals[18] = 'Восемнадцать'
    Capitals[19] = 'Девятнадцать'
    Capitals[20] = 'Двадцать'
    Capitals[30] = 'Тридцать'
    Capitals[40] = 'Сорок'
    Capitals[50] = 'Пятьдесят'
    Capitals[60] = 'Шестьдесят'
    Capitals[70] = 'Семьдесят'
    Capitals[80] = 'Восемьдесят'
    Capitals[90] = 'Девяносто'
    Capitals[100] = 'Сто'
    Capitals[200] = 'Двести'
    Capitals[300] = 'Триста'
    Capitals[400] = 'Четыреста'
    Capitals[500] = 'Пятьсот'
    Capitals[600] = 'Шестьсот'
    Capitals[700] = 'Семьсот'
    Capitals[800] = 'Восемьсот'
    Capitals[900] = 'Девятсот'

    if nomer_int < 21:
        print(Capitals[nomer_int], ' ', end='')
    elif nomer_int < 100:
        print(Capitals[nomer_int // 10 * 10], ' ', end='')
        strok_ekvival2(nomer_int % 10)
    elif nomer_int < 1000:
        print(Capitals[nomer_int // 100 * 100], ' ', end='')
        strok_ekvival2(nomer_int % 100)
pass


def strok_ekvival(nomer_int):
    '''
    Выводит прописью целое введеное число от 0 до 1000001
    :param nomer_int: номер введеное числа
    :return: pass
    '''
    Capitals = dict()
    Capitals[0] = ' '
    Capitals[1] = 'Один'
    Capitals[2] = 'Два'
    Capitals[3] = 'Три'
    Capitals[4] = 'Четыре'
    Capitals[5] = 'Пять'
    Capitals[6] = 'Шесть'
    Capitals[7] = 'Семь'
    Capitals[8] = 'Восемь'
    Capitals[9] = 'Девять'
    Capitals[10] = 'Десять'
    Capitals[11] = 'Одиннадцать'
    Capitals[12] = 'Двенадцать'
    Capitals[13] = 'Тринадцать'
    Capitals[14] = 'Четырнадцать'
    Capitals[15] = 'Пятнадцать'
    Capitals[16] = 'Шестнадцать'
    Capitals[17] = 'Семнадцать'
    Capitals[18] = 'Восемнадцать'
    Capitals[19] = 'Девятнадцать'
    Capitals[20] = 'Двадцать'
    Capitals[30] = 'Тридцать'
    Capitals[40] = 'Сорок'
    Capitals[50] = 'Пятьдесят'
    Capitals[60] = 'Шестьдесят'
    Capitals[70] = 'Семьдесят'
    Capitals[80] = 'Восемьдесят'
    Capitals[90] = 'Девяносто'
    Capitals[100] = 'Сто'
    Capitals[200] = 'Двести'
    Capitals[300] = 'Триста'
    Capitals[400] = 'Четыреста'
    Capitals[500] = 'Пятьсот'
    Capitals[600] = 'Шестьсот'
    Capitals[700] = 'Семьсот'
    Capitals[800] = 'Восемьсот'
    Capitals[900] = 'Девятсот'
    Capitals[1000] = 'Тысяч'
    Capitals[1000000] = 'Миллион'

    if nomer_int < 21:
        print(Capitals[nomer_int], ' ', end='')
    elif nomer_int < 100:
        print(Capitals[nomer_int // 10 * 10], ' ', end='')
        strok_ekvival(nomer_int % 10)
    elif nomer_int < 1000:
        print(Capitals[nomer_int // 100 * 100], ' ', end='')
        strok_ekvival(nomer_int % 100)
    elif nomer_int >= 1000 and nomer_int <= 1999:
        print('Тысяча', ' ', end='')
        strok_ekvival(nomer_int % 1000)
    elif nomer_int >= 2000 and nomer_int <= 2999:
        print('Две Тысячи', ' ', end='')
        strok_ekvival(nomer_int % 1000)
    elif nomer_int >= 3000 and nomer_int <= 4999:
        strok_ekvival(nomer_int // 1000)
        print('Тысячи', ' ', end='')
        strok_ekvival(nomer_int % 1000)
    elif nomer_int >= 21000 and nomer_int <= 991999 and ((nomer_int // 1000) % 10) == 1 and ((nomer_int // 1000) % 100) != 11:
        strok_ekvival2(nomer_int // 1000)
        print('Тысяча', ' ', end='')
        strok_ekvival(nomer_int % 1000)
    elif nomer_int >= 22000 and nomer_int <= 993999:
        strok_ekvival2(nomer_int // 1000)
        if(((nomer_int // 1000) % 10 == 2 or (nomer_int // 1000) % 10 == 3 or (nomer_int // 1000) % 10 == 4) and (nomer_int // 1000) % 100 > 20):
            print('Тысячи', ' ', end='')
        else:
            print(Capitals[1000], ' ', end='')
        strok_ekvival(nomer_int % 1000)
    elif nomer_int < 1000000:
        strok_ekvival(nomer_int // 1000)
        print(Capitals[1000], ' ', end='')
        strok_ekvival(nomer_int % 1000)
    elif nomer_int == 1000000:
        print(Capitals[1000000], ' ', end='')

pass

if __name__ == "__main__":

  nomer_chisla = int(input("\nВведите номер числа от 0 включительно до 1000000 включительно "))

  if (nomer_chisla < 0 or nomer_chisla > 1000000):
    print("Введенное число не соотвецтвует условию")
  else:
    if nomer_chisla != 0:
      strok_ekvival(nomer_chisla)
    elif nomer_chisla == 0:
      print('Ноль')


  print('\nprogram --> {}\n'.format("OFF"))


# i = 0
# while i < 10:
#     nomer_chisla = random.randint(1,1000000)
#     print("\n")
#     print(nomer_chisla)
#     strok_ekvival(nomer_chisla)
#     i = i + 1
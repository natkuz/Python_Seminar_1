# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

week_day = int(input('Enter number day of the week from 1 to 7: '))

if 1 <= week_day <= 7:
    if week_day == 6 or week_day == 7:
        print('Yes, the day is a day off')
    else:
        print('No, the day is not a day off')
else:
    print('No such day of the week')
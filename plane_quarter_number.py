# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0,
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('Enter x coordinate other than 0: '))
y = int(input('Enter y coordinate other than 0: '))

if x != 0 and y != 0:
    if x > 0 and y > 0:
        number_plane = 1
    if x < 0 and y > 0:
        number_plane = 2
    if x < 0 and y < 0:
        number_plane = 3
    if x > 0 and y < 0: 
        number_plane = 4   
    
    print(f'For coordinates x = {x} and y = {y} plane quarter number is {number_plane}')

else:
    if x == 0 and y == 0:
        print('The point is the same as the origin of the coordinate system')
    elif x == 0:
        print('The point lies on the axis y')
    elif y == 0:
        print('The point lies on the axis x')
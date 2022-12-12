# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number_plane = int(input("Enter number of plane 1, 2, 3 or 4: "))

if 1 <= number_plane <= 4:
    if number_plane == 1:
        print(f'Coordinate range in quarter plane {number_plane} is: x and y > 0')
    if number_plane == 2:
        print(f'Coordinate range in quarter plane {number_plane} is: x < 0 and y > 0')
    if number_plane == 3:
        print(f'Coordinate range in quarter plane {number_plane} is: x and y < 0')
    if number_plane == 4:
        print(f'Coordinate range in quarter plane {number_plane} is: x > 0 and y < 0')
else:
    print('There is no such quarter plane')
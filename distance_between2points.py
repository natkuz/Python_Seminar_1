# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21

xa = int(input('Enter coordinate x of point A: '))
ya = int(input('Enter coordinate y of point A: '))
xb = int(input('Enter coordinate x of point B: '))
yb = int(input('Enter coordinate y of point B: '))

distance = round((((xa - xb) ** 2 + (ya - yb) ** 2) ** 0.5), 2)

print(f'The distance between two points = {distance}')
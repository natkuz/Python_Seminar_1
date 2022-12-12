# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(f'for x = {x}, y = {y}, z = {z}')
            expression1 = not (x or y or z)
            expression2 = not x and not y and not z
            if expression1 == expression2:
                print(f'Expression is {True}')
            else:
                print(f'Expression is {False}')
            print()

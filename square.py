from math import pi, sqrt

def circle_square(r):
        try:
        r = float(r)
    except ValueError:
        raise ValueError("Радиус должен быть числом")
    
    return pi * r * r

def triangle_square(a, b, c):
    
    try:
        a, b, c = float(a), float(b), float(c)
    except ValueError:
        raise ValueError("Длины сторон треугольника должны быть числами")

    if a * a + b * b == c * c:
        return a * b / 2
    else:
        p = (a + b + c) / 2
        return sqrt(p * (p - a) * (p - b) * (p - c))

def figure():
    
    while True:
        data = input("Введите параметры фигуры (для окружности - радиус, для треугольника - стороны через пробел): ").split()
        if len(data) == 1:
            try:
                return circle_square(float(data[0]))
            except ValueError as e:
                print(e)
        elif len(data) == 3:
            try:
                return triangle_square(float(data[0]), float(data[1]), float(data[2]))
            except ValueError as e:
                print(e)
        else:
            print("Неверное количество параметров. Пожалуйста, повторите ввод.")

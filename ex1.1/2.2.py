input_usuario = input().split(' ')
a = float(input_usuario[0])
b = float(input_usuario[1])
c = float(input_usuario[2])

delta = ( b ** 2 ) - (4 * a * c)

if a == 0 or delta < 0:
    print('Impossivel calcular ')
else:
    x1 = (- b + (delta ** 0.5)) / (2 * a)
    print(f'X1 = {x1:.5f}')
    x2 = (- b - (delta ** 0.5)) / (2 * a)
    print(f'X2 = {x2:.5f}')

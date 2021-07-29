n = int(input('Digite qtd de vezes: '))
contador = 1
dentro = 0
fora = 0

while contador <= n:
    nros = int(input('Digite: '))
    if nros >= 10 and nros <= 20:
        dentro += 1
    else:
        fora += 1
    contador += 1

print(f'{dentro} in')
print(f'{fora} out')

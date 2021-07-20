produto1 = input().split(' ')
pum1 = int(produto1[0])
pum2 = int(produto1[1])
pum3 = float(produto1[2])

produto2 = input().split(' ')
pdois1 = int(produto2[0])
pdois2 = int(produto2[1])
pdois3 = float(produto2[2])

calculo_um = pum2 * pum3
calculo_dois = pdois2 * pdois3


print(f'VALOR A PAGAR: R${calculo_um + calculo_dois:.2f}')

# Calculo Simples

cod1, qtd1, v1 = input().split(" ")
qtd1 = int(qtd1)
v1 = float(v1)

cod2, qtd2, v2 = input().split(" ")
qtd2 = int(qtd2)
v2 = float(v2)

soma = (v1 * qtd1) + (v2 * qtd2)

print(f'VALOR A PAGAR: R$ {soma:.2f}')
      

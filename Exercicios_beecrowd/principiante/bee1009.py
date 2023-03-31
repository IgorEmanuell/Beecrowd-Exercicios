# Salario bonus

nome = str(input())
salario = float(input())
vendas = float(input())

valor = (vendas * 0.15) + salario

print(f'TOTAL = R$ {valor:.2f}')

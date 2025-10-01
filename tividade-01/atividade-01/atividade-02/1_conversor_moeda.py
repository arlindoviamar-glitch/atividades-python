# 1- Conversor de Moeda
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Calcula os valores convertidos
valor_dolares = valor_reais / taxa_dolar
valor_euros = valor_reais / taxa_euro

# Exibe os resultados formatados
print("--- Conversor de Moeda ---")
print(f"Valor original: R$ {valor_reais:.2f}")
print(f"Valor em Dólares: US$ {valor_dolares:.2f}")
print(f"Valor em Euros: € {valor_euros:.2f}")

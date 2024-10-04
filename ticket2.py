total_pagantes = int(input("Digite a quantidade total de pagantes: "))
valor_total = float(input("Informe o valor total do dia: "))
valor_inteira = float(input("Informa o valor da inteira: "))
valor_meia = float(input("Informe o valor da meia: "))

x = (valor_total-valor_meia * total_pagantes) / (valor_inteira - valor_meia)
y = total_pagantes - x

print(f"Pagantes Inteira: {x}")
print(f"Pagantes meia: {y}")

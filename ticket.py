def exibirMensagem (nome, idade, filme, total_pagantes, x, y):
    print(f"{nome}{idade}{filme}{total_pagantes}{x}{y}")

nome = input("Qual seu nome: \n\n")
idade = input("\nQual a sua idade: \n\n")
filme = input("\nQual filme que você deseja assistir: \n\n")
total_pagantes = int(input("\nDigite a quantidade total de ingressos: \n\n"))
valor_total = float(input("\nQual o valor total que deseja pagar: \n\n"))
valor_inteira = 30
valor_meia = 15

x = (valor_total-valor_meia * total_pagantes) / (valor_inteira - valor_meia)
y = total_pagantes - x

exibirMensagem(nome, idade, filme, total_pagantes, x, y)


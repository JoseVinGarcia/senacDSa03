#Exemplo 1 - Operadores Logicos
import os
os.system('cls')

# # Transforma para maiusculo utilizando o Upper
# profissao = input("Insira sua profissão: ").upper()
# localidade = input("Insira sua região: ").upper()

# if profissao == "PROFESSOR" and localidade == "RIO DE JANEIRO":
#     print("Desconto")
# else:
#     print("Sem Desconto")

#EXEMPLO 2

# pega apenas o indice 0 do conjunto de caracteres
resposta = input("Quer um desconto? Responda Sim ou Não: ")[0].upper()

if resposta=="S":
    print("Desconto!")
else:
    print("Sem desconto.")


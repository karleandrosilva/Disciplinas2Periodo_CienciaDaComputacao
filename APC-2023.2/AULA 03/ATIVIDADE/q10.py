# 10.Toda apresentação de trabalho tem seus requisitos mínimos, que precisam ser atendidos,
# caso contrário, o trabalho não é aceito e o aluno fica com nota 0.
# A apresentação de Programação 1 está chegando, e o Professor deixou claro que se os
# trabalhos não passassem por todos os requisitos mínimos, ele não iria julgar o trabalho.
# Eis os requisitos:
# ● Requisito 1: Interface gráfica OU Inteligência Artificial.
# ● Requisito 2: Encapsulamento E Indentação.
# ● Requisito 3: Uso de Structs
# A entrada é composta de 5 números, representando respectivamente Interface Gráfica,
# Inteligência Artificial, Encapsulamento, Indentação e Structs.
# Para cada requisito, o usuário deve digitar:
# 0 - Se o trabalho não possui tal quesito.
# 1 - Se o trabalho possui tal quesito.

interface_graf = int(input('Interface Gráfica: [0] ou [1]: '))
inteligencia_art = int(input('Inteligência Artificial: [0] ou [1]: '))
encapsulamento = int(input('Encapsulamento: [0] ou [1]: '))
identacao = int(input('Identação: [0] ou [1]: '))
structs = int(input('Structs: [0] ou [1]: '))

if interface_graf == 1 or inteligencia_art == 1:
    requisito1 = 1
else:
    requisito1 = 0

if encapsulamento == 1 and identacao == 1:
    requisito2 = 1
else:
    requisito2 = 0

if structs == 1:
    requisito3 = 1
else:
    requisito3 = 0

saida = requisito1 + requisito2 + requisito3
if saida == 3:
    print('Seu trabalho será avaliado.')
else:
    print('Seu trabalho não será avaliado, nota 0.')
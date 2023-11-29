# B) Escreva um programa no qual o usuário entre com dois ângulos internos de um triângulo e o programa calcule o 3o ângulo do triângulo.

angulo1 = int(input('Informe o valor do primeiro ângulo: '))
angulo2 = int(input('Informe o valor do segundo ângulo: '))
angulo3 = angulo1 + angulo2 - 180

print(f'O valor do terceiro ângulo é: {angulo3}')
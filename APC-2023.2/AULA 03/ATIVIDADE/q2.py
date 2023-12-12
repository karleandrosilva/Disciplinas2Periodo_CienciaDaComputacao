# 2. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
# podem ou não formar um triângulo.

reta1 = int(input('Informe o primeiro valor da reta para o triângulo: '))
reta2  = int(input('Informe o segundo valor da reta para o triângulo: '))
reta3 = int(input('Informe o terceiro valor da reta para o triângulo: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print(f'OS VALORES {reta1}, {reta2} e {reta3} FORMAM UM TRIÂNGULO!')
else:
    print(f'OS VALORES {reta1}, {reta2} e {reta3} NÃO FORMAM UM TRIÂNGULO!')

# 3. Refaça a questão anterior, acrescentando o recurso de mostrar que tipo de triângulo será
# formado:
# ● Triângulo Equilátero: três lados iguais;
# ● Triângulo Isósceles: quaisquer dois lados iguais;
# ● Triângulo Escaleno: três lados diferentes;

reta1 = int(input('Informe o primeiro valor da reta para o triângulo: '))
reta2  = int(input('Informe o segundo valor da reta para o triângulo: '))
reta3 = int(input('Informe o terceiro valor da reta para o triângulo: '))

if reta1 < (reta2 + reta3) and reta2 < (reta1 + reta3) and reta3 < (reta1 + reta2):
    print(f'OS VALORES {reta1}, {reta2} e {reta3} FORMAM UM TRIÂNGULO!')

    if reta1 == reta2 and reta1 == reta3:
        print('O TRIÃNGULO É EQUILÁTERO!')

    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('O TRIÂNGULO É ISÓSCELES!')

    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print('O TRIÂNGULO É ESCALENO!')

else:
    print(f'OS VALORES {reta1}, {reta2} e {reta3} NÃO FORMAM UM TRIÂNGULO!')
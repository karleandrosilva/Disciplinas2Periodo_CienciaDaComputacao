'''7. Escreva um programa que receba como entrada dois números e retorne a quantidade
de números positivos menores que 50 que são múltiplos de ambos.'''

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

contador = 0

for numero in range(1, 50):
    if numero % numero1 == 0 and numero % numero2 == 0:
        contador += 1

print(f"A quantidade de números positivos menores que 50 e múltiplos de ambos {numero1} e {numero2} é: {contador}")
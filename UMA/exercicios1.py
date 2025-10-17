# Ex 3
'''
print ("vou pedir lhe 2 numeros")

x = int(input("Escreva o valor de x: \n"))
y = int(input("Escreva o valor de y: \n"))

res = x + y

print (f"{x} + {y} = {res}")

# Ex 4

print("Vou calcular o tempo KM/h")
x = int(input("Escreva o valor de km: \n"))
y = int(input("Escreva o tempo em minutos: \n"))

print("velocidade média em km/h: " + str(x/y*60))
print("velocidade média em m/s: " + str(x*1000) / (y*60))

#EX5



print("Forneça uma quantidade de segundos")
x = int(input("Escreva o valor de segundos: \n"))

print("segundos em dias: " )

X

#EX8

x = input("Introduza X: \n")

while True:
    if x > 1 and x < 5:
        print("Numero aceite")
        break
    else:
        print("numero incorreto")
        x = input("Introduza X: \n")



#EX9

print("Numero maior")
x = eval(input("Escreva um valor: \n"))
y = eval(input("Escreva outro valor: \n"))
z = eval(input("Escreva outro valor: \n"))

maior = max(x,y,z)

print(f"Maior numero é {maior}")

'''

#exercício 10
'''
ano=int(input("Introduza o valor do ano para ver se é bissexto: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano é bissexto.")
else:
    print("O ano não é bissexto")
'''

#exercício 11
'''
print("Calculador de salarios")
x = int(input("Introduza o numero de horas de trabalho esta semana :"))
y = int(input("Introduza o seu salário por hora :"))

salario = x * y

if x < 40 :
    print("salario", salario)
else:
    horasextra = x - 40
    salarioextra = (x * y ) + (horasextra * y * 2)

    print(f"O seu sálario é: {salarioextra}€")
'''

#exercício 12
'''
numero=input("Introduza um numero inteiro positivo: ")
ímpares=""
for digito in numero:
    if int(digito)%2!=0:
        ímpares=ímpares+digito
print("Número apenas com os números ímpares: ", ímpares)
'''

#exercício 13
'''
numero = input("Introduza um número inteiro positivo: ")
invertido = numero[::-1]
print("O número invertido é", invertido)
'''
#exercício 14

numero = int(input("Introduza um número inteiro positivo: "))
for i in range (1, 11):
    print(f"{numero}*{i} = {numero*i}")

#exercício 15



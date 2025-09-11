print(20*"=", "VAMOS CALCULAR SEU IMC", 20*"=")
nome = str(input("Qual seu nome? "))
altura = float(input("Qual sua altura em metros? "))
peso = float(input("Qual seu Peso? "))

imc = peso / (altura * altura)

print(f"Seu IMC é de: {imc:.2f}")

if imc >= 40:
    print("Obesidade Grave")
if imc >= 30 and imc <= 39.9:
    print("Obesidade")
if imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
if imc >= 18.5 and imc <= 24.9:
    print("Normal")
if imc <= 18.5:
    print("Magreza")


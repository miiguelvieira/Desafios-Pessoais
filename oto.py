n = int(input("Digite um número de linhas para o triangulo retangulo: "))
print (f"Você escolheu um triangulo com {n} lihas")

print("="*35)
print("Vai começar")
print("="*35)

 
i = 1

while i <= n:
    print(" " * (n - i) + "$" * (2 * i - 1))
    i += 1


 ### testando commit ###

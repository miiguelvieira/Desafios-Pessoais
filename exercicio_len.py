xute = input("Digite uma palavra: ")
print(f"Você digitou '{xute}'")

#print(variavel[0:5])
#print(variavel[6:11])

nome = (len(xute))
print(xute[::-1])

print(type(nome))

invertida = ""

for i in range(nome-1, -1, -1):
    invertida += xute[i]
   
print(invertida)



print("="*60)
print("começa daqui vai")
print("="*60)


if xute == "":
    print("Desculpe você não digitou nada no nome.")
else:

    print(f"Seu nome é: {xute}")

    print("Seu nome invertido é: ", xute[::-1])

    if " " in xute:
        print("Contem espaço no seu nome.")
    else:
        print("Não contem espaço")

    print(f"Seu nome tem {len(xute)} letras")

    print(f"A primeira letra do seu nome é: {xute[0]}")
    print(f"A ultima letra do seu nome é: {xute[-1]}")




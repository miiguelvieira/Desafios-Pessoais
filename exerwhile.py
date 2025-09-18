nome = input("Digite seu nome aqui: ")
lenome = len(nome)

i = 0

while i <= lenome:
    print(f"*{nome[i]}*")
    i += 1

    if i == lenome:
        break



nome = input("Digite seu nome aqui: ")
lenome = len(nome)

i = 0

while i <= lenome:
    print(f"{nome[i]}")
    i += 1

    if i == lenome:
        break



j = 0
new_name = ''

while j < lenome:
    letra = nome[j]
    new_name += f'*{letra}*'
    j += 1

    print(new_name)

print("="*50) 
print(new_name)

sem_bobebira = new_name.replace("*","").upper()
print(sem_bobebira)
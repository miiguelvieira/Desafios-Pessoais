num1 = input('Digita um número: ')

x = num1.isdigit()  

i = 0

while x == False:
    i += 1
    print("Você não digitou um número inteiro ")
    num2 = input('Digite um número novamente por favor: ')
    y = num2.isdigit()

    if y == True:
        pr = int(num2)
        if pr % 2 == 0:
            print("Você digitou um número par :) ")
            print(f"Você tentou digitar um inteiro {i} vezes")
        else:
            print("Você digitou um número impar")
            print(f"Você tentou digitar um inteiro {i} vezes")
                         
    print(f"Você já tentou {i +1} vezes, restam mais {4 - i} tentativas")

    if i >= 4:
        print(f"Você é muito burro!!! você digitou {i} vezes algo que não é um número e agora bloqueou o programa")
        break
                   
    if y == True:
        
        break

if x == True:
    if int(num1) % 2 == 0:
        print("Você digitou um número par")
    else:
        print("Você digitou um número impar")



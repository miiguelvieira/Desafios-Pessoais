"""""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.

"""
#aqui voce vai digitar um número
num1 = input('Digita um número: ')

#aqui você transforma uma variavel em boleano (True or False) com verificação .isdigit (se for número é True e se não é False)
x = num1.isdigit()  

i = 0
#aqui vai começar o loop. Enquanto X for False ele vai executar o loop depois dos dois pontos :
while x == False:
    i += 1
    #primeiro ele te avisa que ta errado
    print("Você não digitou um número inteiro ")
    #agora ele armazena em uma outra variavel num2 o seu input
    num2 = input('Digite um número novamente por favor: ')
    #cria uma variavel Y boleana checada pelo isdigit que pode ser True or False
    y = num2.isdigit()
    #só conta quantas vezes a pessoa não digitou errado.

    
    #se Y for true executa   
    if y == True:
        #aqui eu crio mais uma variavel e transformo num2, o número que ja foi checado em int pois estava em str
        pr = int(num2)
        #aqui eu checo se pr é divisivel por 2 e sobra 0, se for é par se não é impar
        if pr % 2 == 0:
            print("Você digitou um número par :) ")
        else:
            print("Você digitou um número impar")
    else:
        print(f"Você só tem mais {4 - i} tentativas")                 

    if i >= 4:
        print(f"Você é muito burro!!! você digitou {i} vezes algo que não é um número e agora bloqueou o programa")
        break
       
    #Aqui eu checo de se o bloco de if foi executado, se ele for executado já tenho a resposta se é par ou impar e lanço um break para parar o loop no while.
    # Se y for False, não vai chegar no break e logo vai continuar repetindo o while        
    if y == True:
        print(f"Você tentou digitar um inteiro {i} vezes")
        break

#aqui é o simples, digitou o número veio para uma chcagem de par ou impar e GG
if x == True:
    if int(num1) % 2 == 0:
        print("Você digitou um número par")
    else:
        print("Você digitou um número impar")











"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

#hora = int(input("Que horas são? "))
hora = input("Que horas são? ")

if hora.isdigit():
    hora1 = int(hora)

    if hora1 == 0 or hora1 <= 11:
        print("Bom dia")
    elif hora1 == 12 or hora1 <= 17:
        print("Boa tarde")
    else:
        print("Boa noite")
else:
    print('Você Não digitou um número :)')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("Qual seu primeiro nome? ")

lenome = len(nome)

if lenome <= 4:
    print("Nome Pequeno")
elif lenome == 5 or lenome <= 6:
    print("Nome Normal")
else:
    print("Nome Grande")

print(f"Seu nome tem {lenome} caracteres")
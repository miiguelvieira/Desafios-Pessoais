operadores = ["/", "*", "+", "-"]
while True:
    init = input("Quer iniciar a calculadora? (S) sim, (N) não. ")
    resultado = ""

    init = init.upper()

    

    if init == "S":
        resultado = ""
        print("="*40)
        print("CALCULADORA INICIADA".center(40," "))
        print("="*40)
        while True:
            num1 = input("Digite um número: ")
            try:
                num1f = float(num1)
                num1t = True
            except ValueError:
                num1t = False
            if num1t:
                while True:               
                    opera = input("Digite um operador: ")
                    if opera in operadores:
                        break
                    else:
                        print("Você não digitou um operador Volte e digite novamente ")
                num2 = input("Digite outro número ")
                try:
                    num2f = float(num2)
                    num2t = True
                except ValueError:
                    num2t = False              
                if num2t:
                    if opera == "*":
                        resultado = num1f * num2f
                        print(f"Resultado: {resultado:.2f}")                    
                    elif opera == "/":
                        resultado = num1f / num2f
                        print(f"Resultado: {resultado:.2f}")                   
                    elif opera == "+":
                        resultado = num1f + num2f
                        print(f"Resultado: {resultado:.2f}")                    
                    elif opera == "-":
                        resultado = num1f - num2f
                        print(f"Resultado: {resultado:.2f}") 
                continuar = input(f"Você Quer continuar com o valor {resultado}? [S] Sim e [N] Não: ")
                continuar = continuar.upper()
                if continuar == "S":
                    print(f"Vamos continuar com {resultado}")
                    while True:               
                        opera2 = input("Digite o segundo operador: ")
                        if opera2 in operadores:
                            break
                        else:
                            print("Você não digitou um operador Volte e digite novamente ")

                    num3 = input("Digite outro número: ")
                    try:
                        num3f = float(num3)
                        num3t = True
                    except ValueError:
                            num3t = False              
                    if num3t:
                        if opera2 == "*":
                            resultado2 = resultado * num3f
                            print(f"Resultado: {resultado2:.2f}")                    
                        elif opera2 == "/":
                            resultado = resultado / num3f
                            print(f"Resultado: {resultado2:.2f}")                   
                        elif opera2 == "+":
                            resultado = resultado + num3f
                            print(f"Resultado: {resultado2:.2f}")                    
                        elif opera2 == "-":
                            resultado = resultado - num3f
                            print(f"Resultado: {resultado2:.2f}")
                elif continuar == "N":
                    print("Você não quer continuar, calculadora encerrada")
                    break
                else:
                    break
                                               
                break
            else:
                print("Você não digitou um numero válido")
                continue   
                        
    elif init == "N":
        print("Você encerrou o programa.")
        break
    else:
        print("Você não digitou algo válido")
        break



    
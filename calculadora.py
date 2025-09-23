operadores = ["/", "*", "+", "-"]

resultado_atual = None
xx = True

if True:
    init = input("Quer iniciar a calculadora? (S) sim, (N) não. ")

    init = init.upper()

    

    if init == "S":
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
                        resultado_atual = resultado                   
                    elif opera == "/":
                        resultado = num1f / num2f
                        print(f"Resultado: {resultado:.2f}")
                        resultado_atual = resultado                                          
                    elif opera == "+":
                        resultado = num1f + num2f
                        print(f"Resultado: {resultado:.2f}")
                        resultado_atual = resultado                                         
                    elif opera == "-":
                        resultado = num1f - num2f
                        print(f"Resultado: {resultado:.2f}")     
                        resultado_atual = resultado   
            break                                                                                                         
    elif init == "N":
        print("Você não quer usar a calculadora")
    else:
        print("Você não digitou algo válido")
        

    while True:
        continuar = input(f"Você quer continuar com o número {resultado_atual:.2f} [S] Sim ou [N] Não: ")
        continuar = continuar.upper()

        if continuar != "S":
            print(f"Calculadora encerrada")
            break

        while True:
            opera = input("Digite um próximo operador: ")
            if opera in operadores:
                break
            else:
                print("Operador invalido, tente novamente por favor.")

        while True:
            num = input("Digite mais um número: ")
            try:
                numf = float(num)
                break
            except ValueError:
                print('Você digitou um número invalido!!')

        if opera == "*":
            resultado_atual = resultado_atual * numf
            print(f"Resultado: {resultado_atual:.2f}") 
                              
        elif opera == "/":
            resultado_atual = resultado_atual / numf
            print(f"Resultado: {resultado_atual:.2f}")
                                                    
        elif opera == "+":
            resultado_atual = resultado_atual + numf
            print(f"Resultado: {resultado_atual:.2f}")
                                                    
        elif opera == "-":
            resultado_atual = resultado_atual - numf
            print(f"Resultado: {resultado_atual:.2f}")     
         
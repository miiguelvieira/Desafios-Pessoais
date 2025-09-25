y = 0
j = 0
i = 0
voltas_i = 4

# Contadores de voltas completas
voltas_completas_y = 0
voltas_completas_j = 0
voltas_completas_i = 0

print("="*63)
print("SISTEMA DE ENGRENAGENS - SIMULAÇÃO COM CONTAGEM")
print("="*63)

for i in range(voltas_i):
    if i == voltas_i - 1:
        # Última volta: engrenagens menores na posição zero
        y = 0
        j = 0
        print(f"⚙️ POSIÇÃO FINAL: {i=}, {j=}, {y=}")
        voltas_completas_i += 1
        break

    for j in range(4):
        for y in range(4):
            print(f"{i=}, {j=}, {y=}")
            
            # Conta voltas de Y (cada vez que y chega no máximo)
            if y == 3:  # y=3 é a posição final do range(4)
                voltas_completas_y += 1
                print(f"  ↳ Volta completa de Y! Total: {voltas_completas_y}")
        
        # Conta voltas de J (cada vez que j chega no máximo)
        if j == 3:  # j=3 é a posição final do range(4)
            voltas_completas_j += 1
            print(f"  ↪ Volta completa de J! Total: {voltas_completas_j}")
    
    # Conta voltas de I (cada iteração do loop principal)
    voltas_completas_i += 1
    print(f"⟲ Volta completa de I! Total: {voltas_completas_i}")

print("="*63)
print("RELATÓRIO FINAL DE VOLTAS:")
print(f"Engrenagem Y (pequena): {voltas_completas_y} voltas completas")
print(f"Engrenagem J (média): {voltas_completas_j} voltas completas")
print(f"Engrenagem I (grande): {voltas_completas_i} voltas completas")
print("="*63)

# Cálculo da relação entre as engrenagens
print("RELAÇÃO DE ENGRENAGENS:")
print(f"1 volta de I = {voltas_completas_j/voltas_completas_i} voltas de J")
print(f"1 volta de J = {voltas_completas_y/voltas_completas_j} voltas de Y")
print(f"1 volta de I = {voltas_completas_y/voltas_completas_i} voltas de Y")
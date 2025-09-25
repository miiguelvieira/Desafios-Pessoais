
w = 4

count_volta_i = 0
count_volta_j = 0
count_volta_y = 0

print("="*63)
print("INICIANDO A ENGRENAGEM ")
print("="*63)

for v in range(w):
    for i in range(4):
        if i == w-1:
            y = 0
            j = 0
            print(f"{i=}, {j=}, {y=}")
            count_volta_i += 1
            break

        for j in range(4):

            for y in range(4):
                print(f"{i=}, {j=}, {y=}")
                if y == 3:
                    count_volta_y += 1
            if j == 3:
                count_volta_j += 1            
        
        #count_volta_i += 1
            
print("="*63)
print("RELATÓRIO FINAL DE VOLTAS:")
print(f"Engrenagem Y (pequena): {count_volta_y} voltas completas")
print(f"Engrenagem J (média): {count_volta_j} voltas completas")
print(f"Engrenagem I (grande): {count_volta_i} voltas completas")
print("="*63)

# Cálculo da relação entre as engrenagens
print("RELAÇÃO DE ENGRENAGENS:")
print(f"1 volta de I = {count_volta_j/count_volta_i} voltas de J")
print(f"1 volta de J = {count_volta_y/count_volta_j} voltas de Y")
print(f"1 volta de I = {count_volta_y/count_volta_i} voltas de Y")
    
   
            

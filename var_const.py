input('Podemos começar? ')
print(" | "* 20)

velocidade = 61
local_car = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passou_radar_1 = velocidade > RADAR_1
carro_multado_radar_1 = local_car >=(LOCAL_1 - RADAR_RANGE) and \
      local_car <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar_1:
    print("Carro esta em uma velocidade maior que a do radar 1")

if carro_multado_radar_1 and velocidade_carro_passou_radar_1:
    print("Carro multado em radar 1")


# ESSA FOI UMA DAS PIORES AULAS QUE EU JA TIVE, O CARA FEZ UMA BAGUNÇA #
# FINAL DA AULA ELE SE PERDEU JOGOU A RESPONSA PRA A GENTE E FEZ PARECER QUE ERA DE \
# PROPOSITO ESSA BAGUNÇA

# DESSE JEITO É RUIM #
# if local_car >=(LOCAL_1 - RADAR_RANGE) and local_car <= (LOCAL_1 + RADAR_RANGE) and \
#velocidade > RADAR_1:
#    print("Carro Multado em Radar 1")


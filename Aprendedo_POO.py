#apenas uma anotação antes do hello world



class Pessoa:

    def __init__(self, nome, idade, altura, peso, graduate):
        self.nome = nome
        self.idade = float(idade)
        self.altura = float(altura)
        self.peso = peso 
        self.graduate = graduate
       
        

    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura:.2f}, Peso: {self.peso:.2f}, Gaduração: {self.graduate})"

#usuario = Pessoa("Miguel Vieira Araujo", 29, 1.70, 85.0, "Administracao")

#print(usuario)

print("Por favor, preencha os dados da pessoa:")
nome = input("Nome: ")
idade = input("Idade: ")
altura = float(input("Altura (em metros): "))
peso = float(input("Peso (em kg): "))
graduate = input("Formação: ")

paciente1 = Pessoa(nome, idade, altura, peso, graduate)


print(f'Dados do usuário: {paciente1}')


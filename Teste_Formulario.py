import json
from datetime import datetime

class FormularioPessoa:
    def __init__(self, nome, idade, altura, peso, graduate):
        self.nome = nome
        self.idade = int(idade)
        self.altura = float(altura)
        self.peso = float(peso)
        self.graduate = graduate
        self.data_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.id = hash(f"{nome}{datetime.now().timestamp()}")  # ID único
    
    def to_dict(self):
        """Converte o objeto para dicionário (serializável)"""
        return {
            'id': self.id,
            'nome': self.nome,
            'idade': self.idade,
            'altura': self.altura,
            'peso': self.peso,
            'graduate': self.graduate,
            'data_registro': self.data_registro
        }
    
    def __str__(self):
        return (f"ID: {self.id}\n"
                f"Nome: {self.nome}\n"
                f"Idade: {self.idade} anos\n"
                f"Altura: {self.altura:.2f}m\n"
                f"Peso: {self.peso:.2f}kg\n"
                f"Formação: {self.graduate}\n"
                f"Data de Registro: {self.data_registro}")

class SistemaFormulario:
    def __init__(self, arquivo_dados='formulario_data.json'):
        self.arquivo_dados = arquivo_dados
        self.pessoas = self.carregar_dados()
    
    def carregar_dados(self):
        """Carrega os dados do arquivo JSON"""
        try:
            with open(self.arquivo_dados, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                return [FormularioPessoa(**pessoa) for pessoa in dados]
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def salvar_dados(self):
        """Salva os dados no arquivo JSON"""
        with open(self.arquivo_dados, 'w', encoding='utf-8') as f:
            dados = [pessoa.to_dict() for pessoa in self.pessoas]
            json.dump(dados, f, ensure_ascii=False, indent=2)
    
    def cadastrar_pessoa(self):
        """Interface para cadastrar uma nova pessoa"""
        print("\n" + "="*50)
        print("CADASTRO DE PESSOA")
        print("="*50)
        
        nome = input("Nome: ")
        idade = self.obter_numero("Idade: ", "inteiro")
        altura = self.obter_numero("Altura (em metros): ", "decimal")
        peso = self.obter_numero("Peso (em kg): ", "decimal")
        graduate = input("Formação: ")
        
        nova_pessoa = FormularioPessoa(nome, idade, altura, peso, graduate)
        self.pessoas.append(nova_pessoa)
        self.salvar_dados()
        
        print(f"\nPessoa cadastrada com sucesso! ID: {nova_pessoa.id}")
    
    def obter_numero(self, mensagem, tipo):
        """Valida a entrada de números"""
        while True:
            try:
                valor = input(mensagem)
                if tipo == "inteiro":
                    return int(valor)
                else:
                    return float(valor)
            except ValueError:
                print("Por favor, digite um número válido.")
    
    def listar_pessoas(self):
        """Lista todas as pessoas cadastradas"""
        print("\n" + "="*50)
        print("PESSOAS CADASTRADAS")
        print("="*50)
        
        if not self.pessoas:
            print("Nenhuma pessoa cadastrada.")
            return
        
        for pessoa in self.pessoas:
            print(pessoa)
            print("-" * 30)
    
    def buscar_pessoa(self):
        """Busca uma pessoa por nome ou ID"""
        termo = input("\nDigite o nome ou ID para buscar: ")
        
        resultados = []
        for pessoa in self.pessoas:
            if (termo.lower() in pessoa.nome.lower() or 
                termo == str(pessoa.id)):
                resultados.append(pessoa)
        
        if resultados:
            print(f"\nEncontrado(s) {len(resultados)} resultado(s):")
            for pessoa in resultados:
                print(pessoa)
                print("-" * 30)
        else:
            print("Nenhuma pessoa encontrada com esse termo.")
    
    def menu_principal(self):
        """Menu interativo do sistema"""
        while True:
            print("\n" + "="*50)
            print("SISTEMA DE FORMULÁRIO")
            print("="*50)
            print("1. Cadastrar nova pessoa")
            print("2. Listar todas as pessoas")
            print("3. Buscar pessoa")
            print("4. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                self.cadastrar_pessoa()
            elif opcao == "2":
                self.listar_pessoas()
            elif opcao == "3":
                self.buscar_pessoa()
            elif opcao == "4":
                print("Saindo do sistema. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

# Executar o sistema
if __name__ == "__main__":
    sistema = SistemaFormulario()
    sistema.menu_principal()
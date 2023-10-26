from datetime import datetime
from enum import Enum
import os.path

class PetTipo(Enum):
    CACHORRO = 1
    GATO = 2
    COELHO = 3
    HAMSTER = 4
    PASSARO = 5
    OUTRO = 0
    

class Pet:
    def __init__(self, tipo: PetTipo = None, nome: str = None, raca: str = None, peso: float = None, data: datetime = None) -> None:
        self.tipo = tipo
        self.nome = nome
        self.raca = raca
        self.peso = peso
        self.data = data
                
                
lista_pets = []


def cadastrar():
    tipo = -1
    while True:
        print("""
        ------------------------------
        \tCADASTRAR PET
        ------------------------------
        [1] Cachorro
        [2] Gato
        [3] Coelho
        [4] Hamster
        [5] Pássaro
        [0] Outro
        ------------------------------
        Selecione o tipo do pet: 
        """, end = '')
        op = input()
        op_validas = ['1', '2', '3', '4', '5', '0']
        if op not in op_validas:
            print("[Opção inválida]")
        else:
            tipo = int(op)
            break
    nome = str(input("\tDigite o nome: "))
    raca = str(input("\tDigite a raça: "))
    peso = float(input("\tDigite o peso: "))
    data = datetime.strptime(input("\tDigite a data de nascimento: "), "%d/%m/%Y")
    print("O pet foi cadastrado com sucesso!")
    pet = Pet(PetTipo(tipo), nome, raca, peso, data)
    lista_pets.append(pet)
    salvar()


def editar():
    listar()
    print("Selecione o pet que deseja editar: ")
    op = int(input())
    pet = lista_pets[op - 1]
    print("""
        ------------------------------
        \tEDITAR PET
        ------------------------------
        [1] Nome
        [2] Raça
        [3] Peso
        [4] Data de Nascimento
        [5] Tipo do Pet
        ------------------------------
        Selecione a opção que deseja editar: 
        """, end = '')
    op = int(input())
    match op:
        case 1:
            pet.nome = input("Digite o novo nome do pet: ")
        case 2:
            pet.raca = input("Digite a nova raça do pet: ")
        case 3:
            pet.peso = float(input("Digite o novo peso do pet: "))
        case 4:
            pet.data = datetime.strptime(input("Digite a nova data de nascimento do pet: "), "%d/%m/%Y")
        case 5: 
            print("""
            --------------------------  
            Digite o novo tipo do pet: 
            --------------------------
            [1] Cachorro
            [2] Gato
            [3] Coelho
            [4] Hamster
            [5] Pássaro
            [0] Outro""")
            pet.tipo = PetTipo(int(input()))
    print("Edição concluída com sucesso!")
    salvar()


def excluir():
    listar()
    print("Selecione o pet que deseja excluir: ")
    op = int(input())
    del lista_pets[op - 1] 
    print("O pet foi excluído com sucesso!")
    salvar()


def listar():
    for i in range(len(lista_pets)):
        pet: Pet = lista_pets[i]
        print(f"[{i + 1}] {pet.tipo.name} {pet.nome} {pet.raca} {pet.peso} {datetime.strftime(pet.data, '%d/%m/%Y')}")


def salvar():
    with open('pets.info','w') as arquivo:
        for pet in lista_pets:  
            arquivo.write(f"{pet.tipo.value}|{pet.nome}|{pet.raca}|{pet.peso}|{datetime.strftime(pet.data, '%d/%m/%Y')}\n")


def carregar():
    if os.path.exists('pets.info'):  
        with open('pets.info', 'r') as arquivo:
            for linha in arquivo.readlines():
                dados = linha.split('|') 
                pet = Pet()
                pet.tipo = PetTipo(int(dados[0]))
                pet.nome = dados[1]
                pet.raca = dados[2]
                pet.peso = float(dados[3])
                pet.data = datetime.strptime(dados[4][0:10], '%d/%m/%Y')
                lista_pets.append(pet)
    return lista_pets


def main():
    carregar()
    while True:
        print("""
        ------------------------------
        \tMENU PRINCIPAL
        ------------------------------
        [1] Cadastrar pet
        [2] Editar pet
        [3] Excluir pet
        [4] Listar pets
        [0] Sair
        ------------------------------
        Digite a opção desejada: 
        """, end = '')
        op = input()
        match op:
            case '1':
                cadastrar()
            case '2':
                editar()
            case '3':
                excluir()
            case '4':
                listar()
            case '0':
                exit(0)
            case _:
                print("[Opção inválida]")


if __name__ == '__main__':
    main()
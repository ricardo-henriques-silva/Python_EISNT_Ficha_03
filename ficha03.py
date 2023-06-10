# Inicialização da lista de personagens

print("\n===Programa de criação e manipulação de perfis de personagens===\n")

lista_personagens =[]

def adicionar_personagem(lista_personagens):
    novapersonagem = {
    "nome": input("Introduza o nome da personagem:\n"),
    "idade": input("Introduza a idade da personagem:\n"),
    "profissão": input("Introduza a profissão da personagem:\n"),
    "hobbies": input("Introduza os hobbies da personagem, separados por ;\n").split(";"),
    "descrição": input("Introduza uma descrição da personagem:\n")
    }
    lista_personagens.append(novapersonagem)

def modificar_personagem(lista_personagens):
    print("Função 2\n")

def remover_personagem(lista_personagens):
    print("Função 3\n")

def visualizar_personagem(lista_personagens):
    print("Função 4\n")

def pesquisar_personagem(lista_personagens):
    print("Função 5\n")

continuar = "True"
while continuar:
    print("===Escolha uma das seguintes Funcionalidades===\n")
    print("0. Sair")
    print("1. Adicionar um novo perfil de personagem")
    print("2. Modificar um perfil de personagem existente")
    print("3. Remover um perfil de personagem")
    print("4. Visualizar a lista completa de personagens")
    print("5. Pesquisar um personagem específico pelo nome")
    opcao_texto=input("Escolha uma opção de 1 a 5:\n")
    try:
        modulo=int(opcao_texto)
        if modulo == 0:
            print("Programa terminado. Obrigado por utilizar.\n")
            break
        elif modulo == 1:
            adicionar_personagem(lista_personagens)
        elif modulo == 2:
            modificar_personagem(lista_personagens)
        elif modulo == 3:
            remover_personagem(lista_personagens)
        elif modulo == 4:
            visualizar_personagem(lista_personagens)
        elif modulo == 5:
            pesquisar_personagem(lista_personagens)
        else:
            print("Introduza uma opção de 0 a 5\n")            
    except:
        print("Introduza uma opção de 0 a 5\n")    



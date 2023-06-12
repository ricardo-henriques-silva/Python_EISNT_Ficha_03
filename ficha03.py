print("\n===Programa de criação e manipulação de perfis de personagens===\n")

# lista_personagens = []
# Inicialização da lista de personagens com algumas personagens de exemplo, para não terem de ser introduzidas em cada teste
# Cada personagem é um dicionário. O conjunto das personagens é uma lista de dicionários
lista_personagens = [{'nome': 'Abel', 'idade': 22, 'profissão': 'Artesão', 'hobbies': ['Arqueologia','Arco-e-flecha'], 'descrição': 'Aéreo'},
                     {'nome': 'Beatriz', 'idade': 33, 'profissão': 'Bióloga', 'hobbies': ['Badminton','Bowling'], 'descrição': 'Boa pessoa'},
                     {'nome': 'Caim', 'idade': 44, 'profissão': 'Carpinteiro', 'hobbies': ['Culinária','Crochet'], 'descrição': 'Curioso'},
                     {'nome': 'Fanã', 'idade': 66, 'profissão': 'Comentador do Facebook', 'hobbies': ['Jornais desportivos','Conversas de café'], 'descrição': 'Tem um palito no canto da boca'}
                     ]

# Função "adicionar personagem" utiliza o método list.append para adicionar um novo dicionário: 
def adicionar_personagem(lista_personagens):
    novapersonagem = {
    "nome": input("Introduza o nome da personagem:\n"),
    "idade": input("Introduza a idade da personagem:\n"),
    "profissão": input("Introduza a profissão da personagem:\n"),
    "hobbies": input("Introduza os hobbies da personagem, separados por ;\n").split(";"),
    "descrição": input("Introduza uma descrição da personagem:\n")
    }
    print(novapersonagem)
    lista_personagens.append(novapersonagem)

# Função "modificar personagem" utiliza o método dicionary.update para editar os valores de cada chave do dicionário seleccionado:
def modificar_personagem(lista_personagens):
    personagem_input = input("\nIndique o nome da personagem que pretende modificar: ")   
    for personagem in lista_personagens:  
        if personagem["nome"]==personagem_input:
            print("\nVamos então alterar os dados da personagem "+ personagem["nome"])
            personagem.update({"nome": input("Introduza o novo nome da personagem:\n")})
            personagem.update({"idade": input("Introduza a nova idade da personagem:\n")})
            personagem.update({"profissão": input("Introduza o nova profissão da personagem:\n")})
            personagem.update({"hobbies": input("Introduza os novos hobbies da personagem, separados por ;\n").split(";")})
            personagem.update({"descrição": input("Introduza a nova descrição da personagem:\n")})
            print("\nEis os novos dados da personagem:")
            print("Nome:", personagem["nome"])
            print("Idade:", personagem["idade"])
            print("Profissão:", personagem["profissão"])
            print("Hobbies:", "; ".join(personagem["hobbies"]))
            print("Descrição:", personagem["descrição"])
            print("===================================")

# Função "remover personagem" utiliza o método list.del
def remover_personagem(lista_personagens):
    personagem_input = input("\nIndique o nome da personagem que pretende remover: ")
    for i in range(len(lista_personagens)): 
        if lista_personagens[i]['nome'] == personagem_input: 
            del lista_personagens[i]
            # após a eliminação da personagem, é invocada a função de visualização da lista actualizada, para confirmação de que esta ficou conforme o esperado 
            print(personagem_input + " removido/a. A lista de personagens actual é:\n")
            visualizar_personagem(lista_personagens)
            break
    print("\n")

# Função "visualizar personagem" percorre cada personagem da lista e imprime cada valor de cada dicionário
def visualizar_personagem(lista_personagens):
    for personagem in lista_personagens:
        print("\nNome:", personagem["nome"])
        print("Idade:", personagem["idade"])
        print("Profissão:", personagem["profissão"])
        print("Hobbies:", "; ".join(personagem["hobbies"]))
        print("Descrição:", personagem["descrição"])
        print("===================================")
    print("\n")   

# Função "pesquisar personagem" percorre cada personagem da lista e imprime apenas os valores do dicionário seleccionado pelo utilizador
def pesquisar_personagem(lista_personagens):
    personagem_input = input("\nIndique o nome da personagem que pretende pesquisar: ")
    for personagem in lista_personagens:  
        if personagem["nome"]==personagem_input:
            print("Nome:", personagem["nome"])
            print("Idade:", personagem["idade"])
            print("Profissão:", personagem["profissão"])
            print("Hobbies:", "; ".join(personagem["hobbies"]))
            print("Descrição:", personagem["descrição"])
            print("===================================")
    print("\n")        
    
continuar = "True"
while continuar:
    print("===Opções disponíveis===")
    print("0. Sair")
    print("1. Adicionar um novo perfil de personagem")
    print("2. Modificar um perfil de personagem existente")
    print("3. Remover um perfil de personagem")
    print("4. Visualizar a lista completa de personagens")
    print("5. Pesquisar um personagem específico pelo nome")
    opcao_texto=input("Escolha uma opção de 0 a 5:\n")
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
            print("Opção " + opcao_texto + " não disponível. Introduza uma opção de 0 a 5\n")            
    except:
        print("Opção " + opcao_texto + " não disponível. Introduza uma opção de 0 a 5\n")    



# Inicialização da lista de personagens
personagens =[]

print("\n===Programa de criação e manipulação de perfis de personagens===\n")
print("===Escolha uma das seguintes Funcionalidades===\n")
print("1. Adicionar um novo perfil de personagem")
print("2. Modificar um perfil de personagem existente")
print("3. Remover um perfil de personagem")
print("4. Visualizar a lista completa de personagens")
print("5. Pesquisar um personagem específico pelo nome")
modulo=input("Escolha uma opção de 1 a 5:\n")

# Funcionalidade 1 Novo perfil
novapersonagem = {
    "nome": input("Introduza o nome da personagem:\n"),
    "idade": input("Introduza a idade da personagem:\n"),
    "profissão": input("Introduza a profissão da personagem:\n"),
    "hobbies": input("Introduza os hobbies da personagem, separados por ;\n").split(";"),
    "descrição": input("Introduza uma descrição da personagem:\n")
    }
personagens.append(novapersonagem)
print(personagens)
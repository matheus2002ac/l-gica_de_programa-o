# primeiro só os gêneros

lista_categorias = ["Romance", "Ficção", "Fantasia"]

# daí por aqui pra baixo agnt coloca só os livros

lista_romance = [
    "Orgulho e Preconceito - Jane Austen",
    "O Morro dos Ventos Uivantes - Emily Brontë",
    "Dom Casmurro - Machado de Assis",
    "Anna Karenina - Liev Tolstói",
    "Cem Anos de Solidão - Gabriel García Márquez",
    "Jane Eyre - Charlotte Brontë",
    "A Megera Domada - William Shakespeare",
    "Madame Bovary - Gustave Flaubert",
    "Razão e Sensibilidade - Jane Austen",
    "O Grande Gatsby - F. Scott Fitzgerald"
]

lista_ficcao = [
    "1984 - George Orwell",
    "Admirável Mundo Novo - Aldous Huxley",
    "Fahrenheit 451 - Ray Bradbury",
    "O Conto da Aia - Margaret Atwood",
    "Neuromancer - William Gibson",
    "Laranja Mecânica - Anthony Burgess",
    "A Revolução dos Bichos - George Orwell",
    "A Máquina do Tempo - H.G. Wells",
    "Fundação - Isaac Asimov",
    "Solaris - Stanisław Lem"
]

lista_fantasia = [
    "O Senhor dos Anéis - J.R.R. Tolkien",
    "Harry Potter e a Pedra Filosofal - J.K. Rowling",
    "As Crônicas de Nárnia - C.S. Lewis",
    "A Canção de Gelo e Fogo - George R.R. Martin",
    "O Hobbit - J.R.R. Tolkien",
    "A Roda do Tempo - Robert Jordan",
    "Mistborn: O Império Final - Brandon Sanderson",
    "A Terra das Sombras - Neil Gaiman",
    "Eragon - Christopher Paolini",
    "O Último Desejo (Saga do Bruxo Geralt de Rívia) - Andrzej Sapkowski"
]

carrinho_de_compras = [] #vazio por enquanto

precos = {"Romance": 45.90,"Ficção": 35.90,"Fantasia": 39.90}

#função exibir lista da aula 4

def exibir_lista(lista):
    for i in range(len(lista)):
        print(f"{i + 1} - {lista[i]}")

# tentativa de criar um negócio pra escolher os livros

def escolher_livro(categoria, lista_livros):
    exibir_lista(lista_livros)
    escolha = int(input(f"Escolha o número do livro de seu interesse conforme a categoria: {categoria}: ")) - 1
    if 0 <= escolha < len(lista_livros):
        livro_escolhido = lista_livros[escolha]
        carrinho_de_compras.append((livro_escolhido, precos[categoria]))  # Adiciona ao carrinho
        print(f"Você adicionou '{livro_escolhido}' ao carrinho.")
    else:
        print("Escolha inválida!")

# agora o menu com o carrinho de compras

#função pra ver o carrinho
def exibir_carrinho():
    if len(carrinho_de_compras) == 0:
        print("Seu carrinho está vazio!")
    else:
        total = 0
        print("\nItens no seu carrinho:")
        for i, (livro, preco) in enumerate(carrinho_de_compras):
            print(f"{i + 1} - {livro}: R$ {preco:.2f}")
            total += preco
        print(f"\nTotal: R$ {total:.2f}\n")


#tirar coisas do carrinho
def remover_item_carrinho():
    exibir_carrinho()
    if len(carrinho_de_compras) > 0:
        escolha = int(input("Escolha o número do item que deseja remover: ")) - 1
        if 0 <= escolha < len(carrinho_de_compras):
            removido = carrinho_de_compras.pop(escolha)
            print(f"Você removeu '{removido[0]}' do carrinho.")
        else:
            print("Escolha inválida!")
    print()


#função do menu
def menu_principal():
    while True:
        print("Seja bem-vindo à livraria Ysma!")
        print("1 - Escolher livros de Romance")
        print("2 - Escolher livros de Ficção")
        print("3 - Escolher livros de Fantasia")
        print("4 - Ver carrinho de compras")
        print("5 - Remover item do carrinho")
        print("6 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            escolher_livro("Romance", lista_romance)
        elif opcao == 2:
            escolher_livro("Ficção", lista_ficcao)
        elif opcao == 3:
            escolher_livro("Fantasia", lista_fantasia)
        elif opcao == 4:
            exibir_carrinho()
        elif opcao == 5:
            remover_item_carrinho()
        elif opcao == 6:
            print("Obrigado por visitar a livraria Ysma! Até logo.")
            break
        else:
            print("Opção inválida, tente novamente!")
        print()

menu_principal()
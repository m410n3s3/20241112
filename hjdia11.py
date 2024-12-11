def adicionar_contato(contatos, nome, telefone, email):
    contatos[nome] = {"telefone": telefone, "email": email}
    print(f"Contato {nome} adicionado com sucesso!")

contatos = {}

while True:
    print("Bem-vindo(a) à sua lista de contatos")
    print("O que deseja fazer?")
    escolha = int(input("Adicionar contato(1), remover contato(2), ver contatos(3), procurar contatos(4), parar de operar(5): "))
    
    if escolha == 1:
        nome = input("Insira o nome do contato: ")
        telefone = input("Insira o telefone do contato: ")
        email = input("Insira o email do contato: ")
        adicionar_contato(contatos, nome, telefone, email)
    elif escolha == 2:
        nome = input("Insira o nome do contato a ser removido: ")
        if nome in contatos:
            del contatos[nome]
            print(f"Contato {nome} removido com sucesso.")
        else:
            print(f"Contato {nome} não encontrado.")
    elif escolha == 3:
        if not contatos:
            print("Nenhum contato encontrado.")
        else:
            for nome, info in contatos.items():
                print(f"Nome: {nome}, Telefone: {info['telefone']}, Email: {info['email']}")
    elif escolha == 4:
        nome = input("Insira o nome do contato a ser procurado: ")
        if nome in contatos:
            info = contatos[nome]
            print(f"Nome: {nome}, Telefone: {info['telefone']}, Email: {info['email']}")
        else:
            print(f"Contato {nome} não encontrado.")
    elif escolha == 5:
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida! Por favor, escolha uma operação válida.")


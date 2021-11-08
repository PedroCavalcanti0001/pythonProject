users = []

while True:
    print("MENU DE OPÇÕES: ")
    print("0 - Listar todos os usuários.")
    print("1 - Inserir novo usuário.")
    print("2 - Terminar aplicação.")
    print("")
    opcao = input("Digite uma opção válida: \n")
    if not opcao.isnumeric():
        print("Por favor digite um numero válido!\n")
    elif int(opcao) == 0:
        print("\nLista de usuarios:")
        if len(users) > 0:
            print("")
            for u in users:
                print("Nome:", u["nome"], "Idade:", u["idade"])
        else:
            print("Lista de usuários vázia!")
        print("--------------- \n")
    elif int(opcao) == 1:
        while True:
            concluded = False
            nome = input("Digite o nome do usuário: \n")
            idade = input("Qual é sua idade? \n")
            users.append({"nome": nome, "idade": idade})
            while True:
                continuar = input("deseja continuar? [sim, não]\n")
                if continuar == "sim":
                    break
                elif continuar in ("não", "n", "nao"):
                    concluded = True
                    break
                else:
                    continue
            if concluded:
                break
    elif int(opcao) == 2:
        exit()
    else:
        print("escolha uma opção válida!\n")
        continue

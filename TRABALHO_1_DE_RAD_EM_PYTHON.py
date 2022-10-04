import os

n = 1

while n == 1:
    print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    print("-- o que deseja fazer?  --")
    selecionar = int(input("Criar um Arquivo [1] - Abrir um Arquivo [2] - Alterar um Arquivo [3] - Deletar um arquivo [4] - Sair [5]:"))

    if selecionar == 1:
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        Arquivo = open(str(input("|Informe o nome do arquivo a ser criado [Obs.: Insira o formato do arquivo ex.: .txt no final]: ")), "w")
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|--Insira as suas Informações --")

        # Informações pessoais

        Arquivo.write("-> Cpf: ")
        Cpf = Arquivo.write(str(input("Informe seu cpf: ")) + "\n")

        Arquivo.write("-> Primeiro nome: ")
        Nome = Arquivo.write(str(input("Informe o seu primeiro nome: ")) + "\n")

        Arquivo.write("-> Nome do meio: ")
        Nome = Arquivo.write(str(input("Informe o seu nome do meio: ")) + "\n")

        Arquivo.write("-> Sobrenome: ")
        Sobrenome = Arquivo.write(str(input("Informe o seu sobrenome: ")) + "\n")

        Arquivo.write("-> Idade: ")
        Idade = Arquivo.write(str(input("Informe a sua idade: ")) + "\n")

        Arquivo.write("-> Conta: ")
        Conta = Arquivo.write(str(input("Informe a sua conta: ")) + "\n")

     # Informações da conta

        Arquivo.write("-> Agência: ")
        Agência = Arquivo.write(str(input("Informe a sua agência: ")) + "\n")

        Arquivo.write("-> Número: ")
        Número = Arquivo.write(str(input("Informe o seu número: ")) + "\n")

        Arquivo.write("-> Saldo: ")
        Saldo = Arquivo.write(str(input("Informe o seu saldo: ")) + "\n")

        Arquivo.write("-> Gerente: ")
        Gerente = Arquivo.write(str(input("Informe o seu gerente: ")) + "\n")

        Arquivo.write("-> Titular: ")
        Titular = Arquivo.write(str(input("Informe o seu titular: ")) + "\n")

        Arquivo.close()

    if selecionar == 2:
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|Informe o arquivo a ser Aberto/Editado: ")
    try:
        with open(input("|Informe o nome do arquivo a ser aberto [Obs.: Insira o formato do arquivo ex.: .txt no final]: "), "r+") as abrir: # Colocar para criar arquivos
            for Abrir in abrir:
                print(Abrir)
    except FileNotFoundError as error:
        print("O arquivo não pôde ser lido porque não foi encontrado ou não existe")




    if selecionar == 3:

        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        Arquivo = open(str(input("|Informe o nome do arquivo a ser alterado [Obs.: Insira o formato do arquivo ex.: .txt no final]: ")),"w")  # Colocar para criar arquivos


        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print("|--Insira as suas Informações --")

        Arquivo.write("-> Cpf: ")
        Cpf = Arquivo.write(str(input("Informe seu cpf: ")) + "\n")

        Arquivo.write("-> Primeiro nome: ")
        Nome = Arquivo.write(str(input("Informe o seu primeiro nome: ")) + "\n")

        Arquivo.write("-> Nome do meio: ")
        Nome = Arquivo.write(str(input("Informe o seu nome do meio: ")) + "\n")

        Arquivo.write("-> Sobrenome: ")
        Sobrenome = Arquivo.write(str(input("Informe o seu sobrenome: ")) + "\n")

        Arquivo.write("-> Idade: ")
        Idade = Arquivo.write(str(input("Informe a sua Idade: ")) + "\n")

        Arquivo.write("-> Conta: ")
        Conta = Arquivo.write(str(input("Informe a sua Conta: ")) + "\n")

        Arquivo.write("-> Agência: ")
        Agência = Arquivo.write(str(input("Informe a sua agência: ")) + "\n")

        Arquivo.write("-> Número: ")
        Número = Arquivo.write(str(input("Informe o seu número: ")) + "\n")

        Arquivo.write("-> Saldo: ")
        Saldo = Arquivo.write(str(input("Informe o seu saldo: ")) + "\n")

        Arquivo.write("-> Gerente: ")
        Gerente = Arquivo.write(str(input("Informe o seu gerente: ")) + "\n")

        Arquivo.write("-> Titular: ")
        Titular = Arquivo.write(str(input("Informe o seu titular: ")) + "\n")

        Arquivo.close()

    if selecionar == 4:
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        if n == 1:
            try:
                os.remove(str(input("Informe o nome do arquivo a ser deletado: (obs: inserir .txt ao final do arquivo) ")))
                print("!!!Seu arquivo foi deletado com Sucesso!!!")
                n == 1

            except:
                print("!!!O nome foi escrito de forma incorreta!!!")





    else:

        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        n = int(input("pressione [1] para voltar ao MENU, pressione [2] para Sair" ))

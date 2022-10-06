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
        
        
        
        
        
        
        
        /////////////////////////////////////////////////////////////////////////////////////////
        
        Implementação Do Banco De Dados
        
import psycopg2
from psycopg2 import OperationalError

#Criando a conexão com o banco de dados Postgresql
# Insirindo os dados para a conexão com o banco de dados

def create_connection(rad_db, username, pwd, hostname, db_port):
connection = None

try:       
    conn = psycopg2.connect(
            database = rad_db
            user = username,
            password = pwd,
            host = hostname,
            port = db_port)

#Tratamento de exceções

print("Conexão com o banco ", db_name, " foi bem sucedida")
except OperationalError as e:
        print(f"O erro '{e}' ocorreu")
return connection

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executada com sucesso")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")

def create_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Tabela criada com sucesso!")
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")

# Conexão com o banco de dados default
connection = create_connection("postgres, jlucas13, adm10, localhost, 5432")

create_database_query = "CREATE DATABASE Trabalho_RAD"
create_database(connection, create_database_query)

connection.close()


connection = create_connection("Trabalho_RAD", "postgres", "admin12345", "127.0.0.1", "5432")

#Criação da tabelas pessoa e conta


cur = conn.cursor()


table_Pessoa_query = ''' CREATE TABELA Pessoa (
                        CPF char(15) PRIMARY KEY,
                        Nome varchar(50) NOT NULL,
                        Sobrenome varchar(50) NOT NULL,
                        Idade int CONSTRAINT idade_positiva CHECK (idade >= 0),
                        Conta varchar(30) NOT NULL '''
                        

table_Conta_query= """CREATE TABELA IF NOT EXISTS Conta (
                        Agencia integer NOT NULL,
                        Numero integer NOT NULL,
                        Saldo CONSTRAINT saldo_positivo CHECK (saldo <= 0),
                        Gerente varchar(50) FOREIGN KEY(Gerente) REFERENCES Pessoa(CPF) NOT NULL,
                        Titular varchar(50) NOT NULL FOREIGN KEY(Titular) REFERENCES Pessoa(CPF),
)
"""


# Inserindo valores

table_insert_pessoa = '''INSERT INTO Conta (Agencia, Saldo, Gerente, Titular)'
VALUES = (101.010.101.00, 1010, 50, 'Leonardo', 'Matheus Castro')
''''

table_insert_conta = '''INSERT INTO Pessoa (CPF, Nome, Sobrenome, Idade, Conta)' 
insert_values = (11121.3, 'Carlos Lucas', 'Sampaio', 25, 'Poupanca')
'''

insert_table(connection, table_insert_endereco)
insert_table(connection, table_insert_pessoa)

connection.close()

# Implementando função Select

q1 = """
SELECT *
FROM Pessoa;
"""

# Implementando função Delete 

DELETE FROM Pessoa
 WHERE CPF = 101.010.101.00;



 # Implementando função Update

UPDATE  
    Pessoa 
SET
 descrição = 'Idade',
   idade  =  26 ,
WHERE
  CPF= 101.010.101.00

  conn.commit()



connection = create_connection("Trabalho_RAD", "postgres", "admin12345", "127.0.0.1", "5432")

def select_table(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Consulta feita com sucesso!")

        lista_consulta = cursor.fetchall()
        for Pessoa in lNome_consulta:
            print(linha)

        cursor.close()
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")

        
connection.close()

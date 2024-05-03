import sqlite3, os, time
from pathlib import Path

class clinica:
    def __init__(self):
        self.Cep = 0
        self.Num_Filial = 0
        self.opcaoGer = 0
    
    def criarDB(self):
        conexao = sqlite3.connect("Clinica.db")
        cursor = conexao.cursor()
        cursor.execute('CREATE TABLE Clientes(NOME TEXT, CPF TEXT, TELEFONE FLOAT, TIPO_ATENDIMENTO INT, ID_Cliente INT,  PRIMARY KEY(ID_CLIENTE));')
        cursor.execute('CREATE TABLE Funcionarios(NOME TEXT, CPF TEXT, TELEFONE FLOAT, NUM_IDENTIFICACAO INT, AREA_DE_TRABALHO TEXT, ID_FUNCIONARIO INT,  PRIMARY KEY(ID_FUNCIONARIO));')
        conexao.commit()
        conexao.close()
        print("DB Construido!")

    def menuGeral(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Qual lista deseja manipular?")
        print("1) Cliente")
        print("2) Funcionarios")
        print("3) sair")
        self.opcaoGer=int(input("digite a opção desejada "))
        while self.opcaoGer<1 or self.opcaoGer>3:
            self.opcaoGer=int(input("digite a opção desejada "))

    def executarGeral(self):
        while self.opcaoGer!=3:
            self.menuGeral()
            time.sleep(0.5)
            os.system("CLS")

            if self.opcaoGer==1:
                a = Clientes()
                a.executarClientes()
            elif self.opcaoGer==2:
                a = Funcionarios()
                a.executarFuncionarios()
            elif self.opcaoGer==3:
                break

    def Cadastrar(self, esc):
        if esc==1:
            b=Clientes()
            b.setID(int(input("digite o id do cliente: ")))
            id = b.getID()
            b.setCPF(input("digite o cpf do cliente EX: 355.977.891.03: "))
            cpf = b.getCPF()
            nome=input("digite o nome do cliente: ")
            telefone=input("digite o telefone do cliente EX: (42)4853-1293: ")
            tipo_atendimento = input("digite o tipo de atendimento que esse cliente deseja receber: ").upper()
            conexao = sqlite3.connect('Clinica.db')
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Clientes (NOME, CPF, TELEFONE, TIPO_ATENDIMENTO, ID_Cliente) VALUES ('"+nome+"', '"+cpf+"', '"+telefone+"', '"+tipo_atendimento+"', "+str(id)+"); ")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")
        if esc==2:
            b=Funcionarios()
            b.setID(int(input("digite o id do Funcionario: ")))
            id = b.getID()
            b.setCPF(input("digite o cpf do Funcionario EX: 355.977.891.03: "))
            cpf = b.getCPF()
            nome=input("digite o nome do Funcionario: ")
            telefone=input("digite o telefone do Funcionario EX: (42)4853-1293: ")
            num_ident = input("digite o numero de identificação do Funcionario : ")
            area_trab = input("digite a area de trabalho do funcionario: ").upper()
            conexao = sqlite3.connect('Clinica.db')
            cursor = conexao.cursor()
            cursor.execute("INSERT INTO Funcionarios (NOME, CPF, TELEFONE, NUM_IDENTIFICACAO, AREA_DE_TRABALHO, ID_FUNCIONARIO) VALUES ('"+nome+"', '"+cpf+"', '"+telefone+"', '"+num_ident+"','"+area_trab+"', "+str(id)+"); ")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")

    def Imprimir(self, esc):
        if esc==1:
            print("----------------------------------------")
            conexao = sqlite3.connect('Clinica.db')
            cursor = conexao.cursor()
            retorno = cursor.execute('SELECT * FROM Clientes;')
            lista = []
            for linha in retorno:
                lista.append(linha[:])
            print(lista)
            conexao.close()  
            print("----------------------------------------") 
        if esc==2:
            print("----------------------------------------")
            conexao = sqlite3.connect('Clinica.db')
            cursor = conexao.cursor()
            retorno = cursor.execute('SELECT * FROM Funcionarios;')
            lista = []
            for linha in retorno:
                lista.append(linha[:])
            print(lista)
            conexao.close()  
            print("----------------------------------------")    

    def Deletar(self, esc):
        if esc==1:
            resp = int(input("digite o id do cliente: "))

            conexao = sqlite3.connect('Clinica.db')
            cursor = conexao.cursor()
            cursor.execute(" DELETE FROM Clientes WHERE ID_Cliente = "+str(resp)+" ;")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ") 
        if esc==2:      
            resp = int(input("digite o id do Funcionario: "))

            conexao = sqlite3.connect('Clinica.db')
            cursor = conexao.cursor()
            cursor.execute(" DELETE FROM Funcionarios WHERE ID_FUNCIONARIO = "+str(resp)+" ;")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ") 

    def Atualizar(self, esc):
        if esc==1:
            resp= int(input("digite o id do Cliente que deseja alterar"))

            c=Clientes()
            c.setID(int(input("digite o id do cliente: ")))
            id = c.getID()
            c.setCPF(input("digite o cpf do cliente EX: 355.977.891.03: "))
            cpf = c.getCPF()
            nome=input("digite o nome do cliente: ")
            telefone=input("digite o telefone do cliente EX: (42)4853-1293: ")
            tipo_atendimento = input("digite o tipo de atendimento que esse cliente deseja receber: ")

            conexao = sqlite3.connect('Clinica.db')
            cursor = conexao.cursor()
            cursor.execute("UPDATE Clientes SET NOME = '"+nome+"', CPF = '"+cpf+"', TELEFONE = '"+telefone+"', TIPO_ATENDIMENTO = '"+tipo_atendimento+"', ID_CLIENTE = "+str(id)+" WHERE ID_CLIENTE = "+str(resp)+";")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")
        if esc==2:
            resp= int(input("digite o id do Funcionario que deseja alterar"))

            b=Funcionarios()
            b.setID(int(input("digite o id do Funcionario: ")))
            id = b.getID()
            b.setCPF(input("digite o cpf do Funcionario EX: 355.977.891.03: "))
            cpf = b.getCPF()
            nome=input("digite o nome do Funcionario: ")
            telefone=input("digite o telefone do Funcionario EX: (42)4853-1293: ")
            num_ident = input("digite o numero de identificação do Funcionario : ")
            area_trab = input("digite a area de trabalho do funcionario: ")

            conexao = sqlite3.connect('Clinica.db')
            cursor = conexao.cursor()
            cursor.execute("UPDATE Funcionarios SET NOME = '"+nome+"', CPF = '"+cpf+"', TELEFONE = '"+telefone+"', NUM_IDENTIFICACAO = '"+num_ident+"', AREA_DE_TRABALHO = '"+area_trab+"', ID_FUNCIONARIO = "+str(id)+" WHERE ID_FUNCIONARIO = "+str(resp)+";")
            conexao.commit()
            conexao.close()
            print("comando Inserido!!! ")    

class Clientes(clinica):
    def __init__(self):
        self.__ID = 0
        self.Nome = ""
        self.__CPF = ""
        self.Telefone = ""
        self.Tipo_Atendimento = "" 
        self.opcaoCliente = 0

    def getID(self):
        return self.__ID

    def getCPF(self):
        return self.__CPF

    def setID(self, id):
        self.__ID = id

    def setCPF(self, cpf):
        self.__CPF = cpf

    def menuCliente(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Oque deseja fazer?")
        print("1) Cadastrar Cliente")
        print("2) Deletar Cliente")
        print("3) Atualizar Cliente")
        print("4) Exibir Clientes") 
        print("5) Exibir Clientes de X tipo de atendimento") 
        print("6) Exibir quantidade de Clientes cadastrados") 
        print("7) Sair")
        self.opcaoCliente=int(input("digite a opção desejada "))
        while self.opcaoCliente<1 or self.opcaoCliente>7:
            self.opcaoCliente=int(input("digite a opção desejada "))

    def executarClientes(self):
        while self.opcaoCliente!=7:
            self.menuCliente()
            c=clinica()

            if self.opcaoCliente==1:
                time.sleep(0.5)
                os.system("CLS")
                c.Cadastrar(1)
            elif self.opcaoCliente==2:
                time.sleep(0.5)
                os.system("CLS")
                c.Deletar(1)
            elif self.opcaoCliente==3:
                time.sleep(0.5)
                os.system("CLS")
                c.Atualizar(1)
            elif self.opcaoCliente==4:
                time.sleep(0.5)
                os.system("CLS")
                c.Imprimir(1)
            elif self.opcaoCliente==5:
                time.sleep(0.5)
                os.system("CLS")
                self.TipoAtendimento()
            elif self.opcaoCliente==6:
                time.sleep(0.5)
                os.system("CLS")
                self.numdeclientes()        
            elif self.opcaoCliente==7:
                break     

    def TipoAtendimento(self):
        """retorna os clientes que buscam certo atendimento informado."""
        op32 = input("digite o tipo de atendimento desejado").upper()

        conexao = sqlite3.connect('Clinica.db')
        cursor = conexao.cursor()
        retorno = cursor.execute("SELECT NOME FROM Clientes WHERE TIPO_ATENDIMENTO = '"+op32+"';")
        lista = []
        for linha in retorno:
            lista.append(linha[:])
        print(lista)
        conexao.close()

    def numdeclientes(self):
        """exibe quantos clientes ja foram cadastrados"""    
        print("----------------------------------------")
        conexao = sqlite3.connect('Clinica.db')
        cursor = conexao.cursor()
        retorno = cursor.execute('SELECT ID_Cliente FROM Clientes;')
        lista = []
        for linha in retorno:
            lista.append(linha[:])
        print(len(lista))
        conexao.close()  
        print("----------------------------------------") 

class Funcionarios(clinica):
    def __init__(self):
        self.__ID = 0
        self.Nome = ""
        self.__CPF = ""
        self.Telefone = ""
        self.Area_trabalho = ""
        self.Numero_identificacao = ""
        self.opcaoFuncionario = 0

    def getID(self):
        return self.__ID

    def getCPF(self):
        return self.__CPF

    def setID(self, id):
        self.__ID = id

    def setCPF(self, cpf):
        self.__CPF = cpf

    def menuFuncionario(self):
        print("|############################################################|")
        print("|                        OOP PYTHON                          |")
        print("|############################################################|")
        print("Oque deseja fazer?")
        print("1) Cadastrar Funcionario")
        print("2) Deletar Funcionario")
        print("3) Atualizar Funcionario")
        print("4) Exibir Funcionarios")
        print("5) Exibir Funcionarios de X tipo de Area de trabalho") 
        print("6) Exibir quantidade de Funcionarios cadastrados") 
        print("7) Sair")
        self.opcaoFuncionario=int(input("digite a opção desejada "))
        while self.opcaoFuncionario<1 or self.opcaoFuncionario>7:
            self.opcaoFuncionario=int(input("digite a opção desejada "))

    def executarFuncionarios(self):
        while self.opcaoFuncionario!=7:
            self.menuFuncionario()
            c=clinica()

            if self.opcaoFuncionario==1:
                time.sleep(0.5)
                os.system("CLS")
                c.Cadastrar(2)
            elif self.opcaoFuncionario==2:
                time.sleep(0.5)
                os.system("CLS")
                c.Deletar(2)
            elif self.opcaoFuncionario==3:
                time.sleep(0.5)
                os.system("CLS")
                c.Atualizar(2)
            elif self.opcaoFuncionario==4:
                time.sleep(0.5)
                os.system("CLS")
                c.Imprimir(2)
            elif self.opcaoFuncionario==5:
                time.sleep(0.5)
                os.system("CLS")
                self.AreaTrabalho()
            elif self.opcaoFuncionario==6:
                time.sleep(0.5)
                os.system("CLS")
                self.numdeFuncionarios()        
            elif self.opcaoFuncionario==7:
                break     

    def AreaTrabalho(self):
        """retorna os Funcionarios que atuam em certa area de trabalho."""
        op32 = input("digite o tipo de atendimento desejado").upper()

        conexao = sqlite3.connect('Clinica.db')
        cursor = conexao.cursor()
        retorno = cursor.execute("SELECT NOME FROM Funcionarios WHERE AREA_DE_TRABALHO = '"+op32+"';")
        lista = []
        for linha in retorno:
            lista.append(linha[:])
        print(lista)
        conexao.close()

    def numdeFuncionarios(self):
        """exibe quantos Funcionarios ja foram cadastrados"""    
        print("----------------------------------------")
        conexao = sqlite3.connect('Clinica.db')
        cursor = conexao.cursor()
        retorno = cursor.execute('SELECT ID_FUNCIONARIO FROM Funcionarios;')
        lista = []
        for linha in retorno:
            lista.append(linha[:])
        print(len(lista))
        conexao.close()  
        print("----------------------------------------")            

sla = clinica()
caminho_arquivo = Path("Clinica.db")
if caminho_arquivo.exists():
    print("O arquivo existe!")
else:
    print("O arquivo não existe.")
    sla.criarDB()
    
sla.executarGeral()


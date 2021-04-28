import os
import pathlib
import os.path

print("*************************\n")
print("Churrascaria PYTHON CODE\n")
print("*************************\n")

def cadastro():
    
    nome = input('Insira o nome do cliente: ')
    cpf = input('CPF: ')
    credito = 0

    if(validaCadastro(cpf)):
        with open('.\cadastros\\' + cpf + '.txt', 'w') as arquivo:
            arquivo.write(nome.upper() + '\n')
            arquivo.write(cpf + '\n')
            arquivo.write(str(credito))
            print("Cadastro realizado com sucesso!")
    else:
        print("CPF INVALIDO OU JA CADASTRADO!")

def validaCadastro(cpf):

    if(len(cpf) == 11):
        try:
            with open("./cadastros/"+cpf+".txt", 'r') as f:
                return False
        except IOError:
            return True
    
def procuraCadastro():

    cpf = input("CPF: ")
    try:
        if(len(cpf) == 11):
            with open("./cadastros/"+cpf+".txt", 'r') as f:
                dados = f.readlines()
                print(f"Nome: {dados[0]}\nCPF:{dados[1]}\nCréditos:{dados[2]}")
                return True
        print("CPF INVALIDO")
        return False
    except IOError:
        print('Cadastro não encontrado')
        return False

def alteracaoCadastro():

    print("[1] Editar Cadastro\n[2] Excluir Cadastro")
    op = int(input())
    if(op == 1):
        
        cpf = procuraCadastro()
        if(cpf):

            print("[1] Alterar Nome\n[2] Alterar Crédito")
            op = int(input())
            if(op == 1):

                #Busca as informações de cpf e credito do cadastro
                with open("./cadastros/"+cpf+".txt", 'r') as f:
                    lines = f.readlines()
                    cpf_cadastro = lines[1]
                    credito = lines[2]
                #altera o nome e insere as informaçõe salvas anteriormente.
                with open("./cadastros/"+cpf+".txt", 'w') as f:
                    nome = input('Altere o nome: ')
                    f.write(nome.upper() + '\n')
                    f.write(cpf_cadastro)
                    f.write(credito)

            elif(op == 2):
                #Busca as informações de nome e cpf do cadastro
                with open("./cadastros/"+cpf+".txt", 'r') as f:
                    lines = f.readlines()
                    nome_cadastro = lines[0]
                    cpf_cadastro = lines[1]
                #altera o credito e insere as informaçõe salvas anteriormente.
                with open("./cadastros/"+cpf+".txt", 'w') as f:
                    novo_credito = input('Qual o valor do credito: ')
                    f.write(nome_cadastro.upper())
                    f.write(cpf_cadastro)
                    f.write(novo_credito)
            else:
                print("Opção Invalida!")
    elif(op==2):

        cpf_remove = input("Digite o CPF cadastrado para exclusão: ")
        try:
            os.remove("./cadastros/"+cpf_remove+'.txt')
            print("Removido com Sucesso")
            return True
        except IOError:
            print("ERRO! Não existe cadastro com esse CPF")
            return True

def vericaCadastroBebida(bebida):
    try:
        with open("./bebidas/"+bebida+".txt", 'r') as f:
            return False
    except IOError:
        return True

def vericaCadastroPrato(prato):

    try:
        with open("./pratos/"+prato+".txt", 'r') as f:
            return False
    except IOError:
        return True

def cadastroPratos():

    nome_prato = input("Qual o nome do Prato: ")
    preco_prato = input("Qual o preço do Prato: R$")

    if(vericaCadastroPrato(nome_prato)):
        with open("./pratos/"+nome_prato+".txt", 'w') as f:
            f.write(nome_prato.upper() + "\n")
            f.write(preco_prato)
    else:
        print("Prato já cadastrado!")
        cadastroPratos()

def cadastroBebidas():
    nome_bebida = input("Qual o nome da Bebida: ")
    preco_bebida = input("Qual o preço da Bebida: R$")
    if(vericaCadastroBebida(nome_bebida)):
        with open("./bebidas/"+nome_bebida+".txt", 'w') as f:
            f.write(nome_bebida.upper()+ "\n")
            f.write(preco_bebida)
    else:
        print("Bebida já cadastrada!")
        cadastroBebidas()

def caixa():

    pagando = True
    preco = 0
    while(pagando):
        
        print("[1] Pratos\n[2] Bebidas\n[3]Encerrar")
        
        opcao = int(input("Qual opção: "))

        if(opcao == 1):

            pagandoPrato = True
            while(pagandoPrato):
                nome_prato_pagar = input("Digite o nome do prato ou para encerrar digite 0: ")

                if(nome_prato_pagar == '0'):
                    pagandoPrato = False
                    break
                try:
                    with open("./pratos/"+nome_prato_pagar+".txt", 'r') as f:
                        dados_prato = f.readlines()
                        preco += int(dados_prato[1])
                        print(f"Prato adicionado na conta, TOTAL: R${preco}")
                except IOError:
                    print("prato não encontrado")
                    continue
        elif(opcao == 2):
            pagandoBebida = True
            while(pagandoBebida):
                nome_bebida_pagar = input("Digite o nome da bebida ou para encerrar digite 0: ")

                if(nome_bebida_pagar == '0'):
                    break
                try:
                    with open("./bebidas/"+nome_bebida_pagar+".txt", 'r') as f:
                        dados_bebida = f.readlines()
                        preco += int(dados_bebida[1])
                        print(f"Bebida adicionado na conta, TOTAL: R${preco}")
                except IOError:
                    print("Bebida não encontrado")
                    continue
        elif(opcao == 3):
            credito_sim = input("Cliente deseja adicionar crédito? [S] ou [N]: ")
            if(credito_sim == 'S' or credito_sim == 's'):
                cpf_cliente = input("CPF do cliente: ")
                try:
                    if(len(cpf_cliente) == 11):
                        with open("./cadastros/"+cpf_cliente+".txt", 'r') as f:
                            dados = f.readlines()
                            credito_novo = float(dados[2]) + preco*0.05
                            print(credito_novo)
                            nome_cliente_cadastro = dados[0]
                    
                        with open("./cadastros/"+cpf_cliente+".txt", 'w') as f:

                            f.write(nome_cliente_cadastro.upper())
                            f.write(cpf_cliente + "\n")
                            f.write(str(credito_novo))
                            
                        with open("./cadastros/"+cpf_cliente+".txt", 'r') as f:    
                            dados = f.readlines()
                            print(f"Nome: {dados[0]}\nCPF:{dados[1]}\nCréditos: R${dados[2]}")
                            return True
                    print("CPF INVALIDO")
                    return False
                except IOError:
                    print('Cadastro não encontrado')
                    return False                           


caixa()

 

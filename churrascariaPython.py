import os
import time
import pathlib
import os.path

def menu():

    sair = True
    while(sair):
        os.system("cls")
        print("*************************\n")
        print("Churrascaria PYTHON CODE\n")
        print("*************************\n")

        print("[1] CADASTRAR CLIENTES\n[2] CADASTRAR PRATOS\n[3] CADASTRAR BEBIDAS\n[4] CONSULTAR CLIENTE\n[5] ALTERAR DADOS CLIENTES\n[6] CAIXA\n ")
        print("[0] SAIR")
        escolha = int(input("QUAL OPÇÃO: "))
        if(escolha == 1):
            cadastro()
        elif(escolha == 2):
            cadastroPratos()
        elif(escolha == 3):
            cadastroBebidas()
        elif(escolha == 4):
            consultaCadastro()
        elif(escolha == 5):
            alteracaoCadastro()
        elif(escolha == 6):
            caixa()
        elif(escolha == 0):
            print("SAINDO DO SISTEMA...")
            time.sleep(2)
            sair = False
            continue
        else:
            print("OPÇÃO INVALIDA. TENTE NOVAMENTE!")
            time.sleep(2)
            os.system("cls")
            continue
def cadastro():
    os.system("cls")
    print("********************\n CADASTRAR CLIENTES\n********************")
    nome = input('Insira o nome do cliente: ')
    cpf = input('CPF: ')
    credito = 0

    if(validaCadastro(cpf)):
        with open('.\cadastros\\' + cpf + '.txt', 'w') as arquivo:
            arquivo.write(nome.upper() + '\n')
            arquivo.write(cpf + '\n')
            arquivo.write(str(credito))
            print("Cadastro realizado com sucesso!")
            time.sleep(3)
            os.system("cls")
            menu()
    else:
        print("CPF INVALIDO OU JA CADASTRADO!")
        time.sleep(3)
        os.system("cls")
        cadastro()

def validaCadastro(cpf):
    os.system("cls")
    if(len(cpf) == 11):
        try:
            with open("./cadastros/"+cpf+".txt", 'r') as f:
                return False
        except IOError:
            return True

def consultaCadastro():
    os.system("cls")
    print("******************\nCONSULTAR CADASTRO\n******************")
    cpf = input("CPF: ")
    try:
        if(len(cpf) == 11):
            with open("./cadastros/"+cpf+".txt", 'r') as f:
                dados = f.readlines()
                os.system("cls")
                print(f"Nome: {dados[0]}\nCPF:{dados[1]}\nCréditos: {dados[2]}")
                time.sleep(3)
                return cpf
        print("CPF INVALIDO, TENTE NOVAMENTE!")
        time.sleep(3)
        os.system("cls")
        consultaCadastro()
        return False
    except IOError:
        print('Cadastro não encontrado')
        time.sleep(3)
        os.system("cls")
        menu()
        return False

def procuraCadastro():

    cpf = input("CPF: ")
    try:
        if(len(cpf) == 11):
            with open("./cadastros/"+cpf+".txt", 'r') as f:
                dados = f.readlines()
                os.system("cls")
                print(f"Nome: {dados[0]}\nCPF:{dados[1]}\nCréditos: {dados[2]}")
                return cpf
        print("CPF INVALIDO, TENTE NOVAMENTE!")
        time.sleep(3)
        os.system("cls")
        procuraCadastro()
        return False
    except IOError:
        print('Cadastro não encontrado')
        time.sleep(3)
        os.system("cls")
        menu()
        return False

def alteracaoCadastro():
    os.system("cls")
    print("********************\n ALTERAR CADASTRO\n*********************")
    print("[1] Editar Cadastro\n[2] Excluir Cadastro")
    op = int(input("QUAL OPÇÃO: "))
    os.system("cls")
    if(op == 1):
        print("********\nProcurar\n******** \n")
        cpf = procuraCadastro()
        if(cpf):
            print("********\nAlterar\n******** \n")
            print("[1] Alterar Nome\n[2] Alterar Crédito")
            op = int(input("QUAL OPÇÃO:"))
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
                print("Cadastro alterado com sucesso!")
                time.sleep(3)
                os.system("cls")
                menu()
                
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
                print("Crédito alterado com sucesso!")
                time.sleep(3)
                os.system("cls")
                menu()
            else:
                print("Opção Invalida!")
                time.sleep(3)
                os.system("cls")
                alteracaoCadastro()
    elif(op==2):

        cpf_remove = input("Digite o CPF cadastrado para exclusão: ")
        try:
            os.remove("./cadastros/"+cpf_remove+'.txt')
            print("Removido com Sucesso")
            time.sleep(3)
            menu()
            return True
        except IOError:
            print("ERRO! Não existe cadastro com esse CPF")
            time.sleep(3)
            menu()
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
    os.system("cls")
    print("********************\n CADASTRAR PRATOS\n*********************")
    nome_prato = input("Qual o nome do Prato: ")
    preco_prato = input("Qual o preço do Prato: R$")

    if(vericaCadastroPrato(nome_prato)):
        with open("./pratos/"+nome_prato+".txt", 'w') as f:
            f.write(nome_prato.upper() + "\n")
            f.write(preco_prato)
            print("Prato cadastrado com sucesso!")
            time.sleep(3)
            menu()
    else:
        os.system("cls")
        print("Prato já cadastrado!")
        time.sleep(3)
        os.system("cls")
        menu()

def cadastroBebidas():
    os.system("cls")
    print("********************\n CADASTRAR BEBIDAS\n*********************")
    nome_bebida = input("Qual o nome da Bebida: ")
    preco_bebida = input("Qual o preço da Bebida: R$")
    if(vericaCadastroBebida(nome_bebida)):
        with open("./bebidas/"+nome_bebida+".txt", 'w') as f:
            f.write(nome_bebida.upper()+ "\n")
            f.write(preco_bebida)
            print("Bebida cadastrada com sucesso!")
            time.sleep(3)
            menu()
    else:
        print("Bebida já cadastrada!")
        time.sleep(3)
        menu()

def pagamentoComCredito(valorPagar):
    os.system("cls")
    print("*****************\nPAGAR COM CRÉDITO\n*****************")
    cpf_pagamento = input("Digite o CPF do cliente: ")
    tot_credito_cliente = 0
    valorTotal = valorPagar
    try:
        if(len(cpf_pagamento) == 11):
            with open("./cadastros/"+cpf_pagamento+".txt", 'r') as f:
                dados = f.readlines()
                tot_credito_cliente = float(dados[2])
                if(tot_credito_cliente >= valorTotal):

                    tot_credito_cliente -= valorTotal
                    return True
                else:
                    print('Saldo Insuficiente')
                    time.sleep(3)
                    os.system("cls")                
                    return False
        else:
            print("CPF Invalido!Aguarde...")
            time.sleep(3)
            os.system("cls")
            return False
    except IOError:
        print('Cadastro não encontrado!')
        time.sleep(3)
        os.system("cls")
        return False

def caixa():
    os.system("cls")
    pagando = True
    preco = 0
    while(pagando):
        
        print("************\nMENU PEDIDO\n************\n")
        print(f"Valor a pagar: R${preco}")
        print("[1] Adicionar Pratos\n[2] Adicionar Bebidas\n[3] Encerrar Pedido\n[4] Pagar com crédito\n[5] Sair")
        
        opcao = int(input("Qual opção: "))

        if(opcao == 1):
            os.system("cls")
            print("****************\nAdicionar Prato\n****************")
            pagandoPrato = True
            while(pagandoPrato):
                nome_prato_pagar = input("Digite o nome do prato ou para encerrar digite 0: ")

                if(nome_prato_pagar == '0'):
                    pagandoPrato = False
                    os.system("cls")
                    break
                try:
                    with open("./pratos/"+nome_prato_pagar+".txt", 'r') as f:
                        dados_prato = f.readlines()
                        preco += int(dados_prato[1])
                        os.system("cls")
                        print(f"Prato adicionado na conta, TOTAL: R${preco}")
                except IOError:
                    print("prato não encontrado")
                    time.sleep(3)
                    os.system("cls")
                    continue
        elif(opcao == 2):
            os.system("cls")
            print("****************\nAdicionar Bebida\n****************")
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
            os.system("cls")
            print("*****************\nEncerrando Pedido\n*****************")
            credito_sim = input("Cliente deseja adicionar crédito? [S] ou [N]: ")
            if(credito_sim == 'S' or credito_sim == 's'):
                adicionar_credito = True
                while(adicionar_credito):
                    os.system("cls")
                    print("*******************\nAdicinando Crédito\n*******************\n")
                    cpf_cliente = input("CPF do cliente: ")
                    try:
                        if(len(cpf_cliente) == 11):
                            with open("./cadastros/"+cpf_cliente+".txt", 'r') as f:
                                dados = f.readlines()
                                credito_novo = float(dados[2]) + preco*0.05
                                nome_cliente_cadastro = dados[0]
                        
                            with open("./cadastros/"+cpf_cliente+".txt", 'w') as f:

                                f.write(nome_cliente_cadastro.upper())
                                f.write(cpf_cliente + "\n")
                                f.write(str(credito_novo))
                                
                            with open("./cadastros/"+cpf_cliente+".txt", 'r') as f:    
                                dados = f.readlines()
                                print("Crédito adicionado com sucesso!")
                                print(f"Nome: {dados[0]}CPF:{dados[1]}Créditos: R${dados[2]}")
                                adicionar_credito = False
                                pagando = False
                                time.sleep(3)
                                os.system("cls")
                                break
                        resp = input("CPF INVALIDO\nTentar Novamente? [S] ou [N]: ")
                        if(resp == 's' or resp == 'S'):
                            print("Aguarde...")
                            time.sleep(3)
                            os.system("cls")
                            continue
                        elif(resp == 'n' or resp == 'N'):
                            adicionar_credito = False
                            pagando = False
                        else:
                            print("Opção invalida, Insira novamente o CPF!")
                            time.sleep(3)
                            os.system("cls")
                            continue

                    except IOError:

                        resp = input("Cadastro não encontrado\nTentar Novamente? [S] ou [N]: ")
                        if(resp == 's' or resp == 'S'):
                            print("Aguarde...")
                            time.sleep(3)
                            os.system("cls")
                            continue
                        elif(resp == 'n' or resp == 'N'):
                            print("Obrigado Pela Preferência!")
                            adicionar_credito = False
                            menu()
                        else:
                            print("Opção invalida, Insira novamente o CPF!")
                            time.sleep(3)
                            os.system("cls")
                            continue
                        time.sleep(5)
                
            elif(credito_sim == 'N' or credito_sim == 'n'):
                print(f"Valor total a pagar: R${preco}")
                print("Obrigado Pela Preferência!")
                time.sleep(3)
                os.system("cls")
                break
        elif(opcao == 4):
            
            if(pagamentoComCredito(preco)):
                print("Pagamento efetuado com sucesso!\nObrigado Pela preferência!")
                pagando = False
                time.sleep(3)
                break
            else:
                continue
        elif(opcao == 5):
            print("OBRIGADO PELA PREFERÊNCIA! VOLTE SEMPRE")
            time.sleep(2)
            os.system("cls")

            break
        else:
            print("OPÇÃO INVALIDA, TENTE NOVAMENTE!")
            time.sleep(3)
            os.system("cls")
            caixa()
    menu()
menu()
 

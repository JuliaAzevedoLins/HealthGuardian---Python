#GLOBAL SOLUTION - HEALTHGUARDIAN - 1ESPW

#JULIA AZEVEDO LINS - RM98690
#LUIS GUSTAVO BARRETO GARRIDO - RM99210

#---------------------------------------------------------------
import sys
import json
import matplotlib.pyplot as plt
import pandas as pd
from prettytable import PrettyTable
import time
import sys

#===============================================================
#                        HEALTHGUARDIAN
#===============================================================

# --------------------------------------------------------------
#               FUNÇÕES DE VALIDAÇÕES E TRATAMENTOS
# --------------------------------------------------------------

def divisao(): #Função para dividir as partes do código
    a = ("-"*30)
    return a

def divisa(): #Função para dividir as partes do código
    a = ("="*30)
    return a

def blank(): #Função para espaços em branco e organização no código
    a = ("")
    return a

def validar_cpf(cpf):
    try:
        int(cpf)  # Converter o CPF em um número
        if len(cpf) != 11:
            raise ValueError("O CPF deve conter 11 dígitos.")
        return True
    except ValueError as e:
        print(f"Erro: {e}")
        return False

# --------------------------------------------------------------
#               FUNÇÕES DE IMPRIMIR DADOS PACIENTES
# --------------------------------------------------------------    

def imprimir_dados_pacientes():
    dados_pacientes = carregar_dados_pacientes()
    df = pd.DataFrame(dados_pacientes)
    
    # Escolha as colunas que você deseja exibir na tabela
    colunas_desejadas = ['nome_paciente', 'cpf_paciente', 'sintoma_paciente', 'senha_paciente']  # Adicione as colunas desejadas aqui
    
    # Filtra o DataFrame para incluir apenas as colunas desejadas
    df_selecionado = df[colunas_desejadas]
    
    # Exibir tabela no terminal usando PrettyTable
    print(divisao())
    print("Dados dos Pacientes:")
    print(divisao())
    
    # Usando PrettyTable para exibição no terminal
    pt = PrettyTable()
    pt.field_names = df_selecionado.columns
    for _, row in df_selecionado.iterrows():
        pt.add_row(row)
    
    print(pt)
    print(divisao())

    # Utilizando Matplotlib para plotar a tabela com destaque no cabeçalho
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.axis('tight')
    ax.axis('off')
    
    # Definindo a cor de fundo para azul claro apenas no cabeçalho (utilizando código hexadecimal)
    header_color = '#5E9299'
    cell_colors = [[header_color if i == 0 else 'white' for i in range(len(df_selecionado.columns))]] + [['white' for _ in range(len(df_selecionado.columns))] for _ in range(len(df_selecionado)-1)]
    
    table = ax.table(cellText=df_selecionado.values, colLabels=df_selecionado.columns, cellLoc='center', loc='center', cellColours=cell_colors)

    # Personalizando a aparência das células do cabeçalho
    for i, key in enumerate(table._cells):
        cell = table._cells[key]
        if key[0] == 0:
            cell.set_text_props(fontweight='bold', color='white')
            cell.set_facecolor(header_color)
        else:
            cell.set_facecolor((1, 1, 1, 0))  # Transparente

    plt.show()

# --------------------------------------------------------------
#                  FUNÇÕES DE CADASTRO E LOGIN
# --------------------------------------------------------------

# Carregando os dados do arquivo JSON
def carregar_dados_pacientes():
    with open('pacientes.json', 'r') as arquivo_pacientes:
        return json.load(arquivo_pacientes)
    
def carregar_dados_funcionarios():
    with open('funcionarios.json', 'r') as arquivo:
        return json.load(arquivo)

# Função para salvar os dados atualizados no arquivo JSON
def salvar_dados_pacientes(dados_pacientes):
    with open('pacientes.json', 'w') as arquivo:
        json.dump(dados_pacientes, arquivo, indent=4)

# Função para cadastrar um novo usuário
def cadastrar_pacientes(nome, cpf, sintoma, senha):
    dados_pacientes = carregar_dados_pacientes()

    # Verificando se o CPF já está registrado
    if cpf in dados_pacientes["cpf_paciente"]:
               
        print(divisao())
        print("CPF já cadastrado. Não é possível criar um novo cadastro.")
        print(divisao())
        return

    # Adicionando o novo usuário
    dados_pacientes["nome_paciente"].append(nome)
    dados_pacientes["cpf_paciente"].append(cpf)
    dados_pacientes["sintoma_paciente"].append(sintoma)
    dados_pacientes["senha_paciente"].append(senha)
    salvar_dados_pacientes(dados_pacientes)
    
    print(divisao())
    print("Cadastro realizado com sucesso!")
    print(divisao())

# Autenicação
def autenticacao():
    while True:
        print(blank())
        print(divisa())
        print("ＢＥＭ－ＶＩＮＤＯ！Escolha o tipo de usuário para acessar o HealthGuardian :)")
        print("1. Funcionário")
        print("2. Paciente")
        print("0. Sair")
        print(divisa())
        opcao = input("Escolha uma opção:")

        if opcao == "1":
            usuario_funcionario()
        elif opcao == "2":
            usuario_paciente()
        elif opcao == "0":
            print(divisa())
            print("ＳＡＩＮＤＯ ＤＯ ＰＲＯＧＲＡＭＡ．．．")
            print(divisa())
            sys.exit()
        else:
            print(divisao())
            print("Opção inválida. Escolha: 1.Funcionário | 2.Paciente | 0.Sair")
            print(divisao())

# --------------------------------------------------------------
#                   MENU DE LOGIN E CADASTRO
# --------------------------------------------------------------
def usuario_funcionario():
    print(divisao())
    print("Olá funcionário! Faça aqui o seu login:")
    usuario = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")
    
    dados_funcionarios = carregar_dados_funcionarios()

    if usuario in dados_funcionarios["usuario_funcionario"]:
        indice = dados_funcionarios["usuario_funcionario"].index(usuario)
        senha_correspondente = dados_funcionarios["senha_funcionario"][indice]

        if senha == senha_correspondente:
            print(blank())
            print(divisa())
            print("Login bem-sucedido. Bem-vindo!")
            print(divisa())
            menu_funcionario()
            return True
        else:
            print(divisao())
            print("Senha incorreta. Tente novamente.")
            print(divisao())
    else:
        print(divisao())
        print("Usuário não encontrado. Verifique o seu usuário e tente novamente.")
        print(divisao())

    return False

def usuario_paciente():
    print(divisao())
    print("Olá paciente! Faça aqui o seu login:")
    usuario_paciente = input("Digite o seu CPF: ")
    senha_paciente = input("Digite sua senha: ")

    dados_pacientes = carregar_dados_pacientes()

    if usuario_paciente in dados_pacientes["cpf_paciente"]:
        indice = dados_pacientes["cpf_paciente"].index(usuario_paciente)
        senha_correspondente = dados_pacientes["senha_paciente"][indice]

        if senha_paciente == senha_correspondente:
            print(blank())
            print(divisa())
            print("Login bem-sucedido. Bem-vindo!")
            print(divisa())
            menu_paciente()
            return True
        else:
            print(divisao())
            print("Senha incorreta. Tente novamente.")
            print(divisao())
    else:
        print(divisao())
        print("Usuário não encontrado. Verifique o seu usuário e tente novamente.")
        print(divisao())

    return False

# --------------------------------------------------------------
#                      MENU PRINCIPAL
# --------------------------------------------------------------
def menu_principal():
    while True:
        print(divisa())
        print("ＭＥＮＵ ＰＲＩＮＣＩＰＡＬ")
        print("1. Funcionário")
        print("2. Paciente")
        print("0. Sair")
        print(divisa())

        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                usuario_funcionario()
            case "2":
                usuario_paciente()
            case "0":
                print("Saindo do programa.")
                sys.exit()
            case _:
                print("Opção inválida. Tente novamente.")

# --------------------------------------------------------------
#                  MENU DO FUNCIONÁRIO
# --------------------------------------------------------------

def menu_funcionario():
    while True:
        print(divisa())
        print("ＭＥＮＵ ＤＯ ＦＵＮＣＩＯＮＡＲＩＯ")
        print("1. Cadastrar Paciente")
        print("2. Ver Lista de Pacientes")
        print("0. Voltar ao Menu Principal")
        print(divisa())
        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                cadastrar_paciente_funcionario()
            case "2":
                imprimir_dados_pacientes()
            case "0":
                return
            case _:
                print("Opção inválida. Tente novamente.")
            
# --------------------------------------------------------------
#                     MENU DO PACIENTE
# --------------------------------------------------------------

def menu_paciente():
    while True:
        print(divisa())
        print("ＭＥＮＵ ＤＯ ＰＡＣＩＥＮＴＥ")
        print("1. Falar com o HealthGuardian")
        print("0. Voltar ao Menu Principal")
        print(divisa())
        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                falar_com_healthguardian()
            case "0":
                return
            case _:
                print("Opção inválida. Tente novamente.")

# --------------------------------------------------------------
#               FUNÇÕES DE INTERAÇÃO DO PACIENTE
# --------------------------------------------------------------                                                                                                                                                                                                                                                                                                                       
                                                                                      
def falar_com_healthguardian():
    print(blank())
    print(divisa())
    print("ＢＥＭ－ＶＩＮＤＯ ＡＯ ＨＥＡＬＴＨ ＧＵＡＲＤＩＡＮ！")
    print("Responda algumas perguntas para avaliar seus sintomas.")
    
    print(divisa())
    print(blank())

    # Adicionando as perguntas que serão feitas ao paciente
    respostas = {}

    try:
        respostas["temperatura"] = float(input("Qual é a sua temperatura corporal? "))
    except ValueError:
        print("Por favor, forneça um valor numérico para a temperatura.")
        return  # Retornar para evitar a continuação do código em caso de erro

    respostas["tosse"] = input("Você está sofrendo de tosse? (y/n) ")
    respostas["dor_garganta"] = input("Você tem dor de garganta? (y/n) ")
    respostas["dificuldade_respirar"] = input("Você está com dificuldade para respirar? (y/n) ")
    respostas["contato_infectado"] = input("Você teve contato próximo com alguém diagnosticado com COVID-19 recentemente? (y/n) ")
    respostas["viagem_recente"] = input("Você fez alguma viagem internacional nos últimos 14 dias? (y/n) ")
    respostas["vacina_covid"] = input("Você recebeu a vacina contra a COVID-19? (y/n) ")
    respostas["medicamentos"] = input("Você tem sentido melhoras com o medicamento? (y/n) ")
    respostas["outras_condicoes"] = input("Você tem alguma condição de saúde pré-existente? Se sim, por favor, mencione. ")

    print(divisa())
    print("Avaliando suas respostas...")
    
    # Avaliação dos sintomas
    table = PrettyTable(["Sintoma", "Avaliação"])

    # Se a temperatura for maior que 38, sugerir contato com o médico
    try:
        if respostas["temperatura"] >= 38:
            table.add_row(["Temperatura elevada", "Recomendamos contato com o médico"])
    except KeyError:
        pass  # Chave 'temperatura' não presente nas respostas

    # Verificar a presença de sintomas específicos
    try:
        if "tosse" in respostas.get("tosse", "").lower() or "dor de garganta" in respostas.get("dor_garganta", "").lower():
            table.add_row(["Sintomas respiratórios", "Consulte um profissional de saúde se persistirem"])
    except KeyError:
        pass  # Chaves 'tosse' ou 'dor_garganta' não presentes nas respostas

   # Avaliar a eficácia do medicamento
    try:
        medicamentos = respostas.get("medicamentos", "").lower()
        if medicamentos == "y":
            table.add_row(["Eficácia do medicamento", "Continue o tratamento conforme prescrito"])
        elif medicamentos == "n":
            table.add_row(["Eficácia do medicamento", "Consulte o médico se os sintomas persistirem ou piorarem"])
    except KeyError:
        pass  # Chave 'medicamentos' não presente nas respostas

    # Verificar histórico de viagem e contato próximo
    if respostas.get("viagem_recente", "").lower() == "y" or respostas.get("contato_infectado", "").lower() == "y":
        mensagem_viagem_contato = "Devido ao seu histórico de viagem ou contato próximo, é aconselhável monitorar sua saúde e considerar a realização de um teste para COVID-19."
        table.add_row(["Histórico de viagem ou contato próximo", mensagem_viagem_contato])


    # Recomendar a vacinação se ainda não tiver sido feita
    if respostas["vacina_covid"].lower() == "n":
        print("Considere receber a vacina contra a COVID-19 para proteger a si mesmo e aos outros.")

    # Verificar condições de saúde pré-existentes
    outras_condicoes = respostas.get("outras_condicoes", "")
    if outras_condicoes:
        mensagem_condicoes = f"Levamos em consideração sua condição de saúde pré-existente: {outras_condicoes}. Mantenha-se em contato com seu médico para monitorar sua saúde."
        table.add_row(["Condições pré-existentes", mensagem_condicoes])
    
    print(table)
# --------------------------------------------------------------
#               CADASTRO DE PACIENTE PELO FUNCIONÁRIO
# --------------------------------------------------------------

def cadastrar_paciente_funcionario():
    print(divisa())
    novo_nome = input("Digite o nome do paciente: ")
    

    novo_cpf = input("Digite o novo CPF do paciente: ")
    while not validar_cpf(novo_cpf):
        print(divisa())
        novo_cpf = input("CPF inválido, digite novamente: ")
    
    novo_sintoma = input("Digite o sintoma do paciente: ")

    nova_senha = input("Digite a senha do paciente: ")
    cadastrar_pacientes(novo_nome, novo_cpf, novo_sintoma, nova_senha)

# --------------------------------------------------------------
#                   EXECUTAR O PROGRAMA
# --------------------------------------------------------------
# Serve para verificar se o script está sendo executado diretamente (como um programa principal) ou se está sendo importado como um módulo em outro script.

if __name__ == "__main__":
    menu_principal()
    autenticacao()  # Chama a função de autenticação ao iniciar o programa
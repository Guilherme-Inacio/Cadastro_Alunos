import pandas as pd

# CARREGAR DADOS

def carregar_dados():
    """
    Tenta carregar o arquivo alunos.csv.
    Se não existir, cria um DataFrame vazio com as colunas que precisa.
    """
    try:
        df = pd.read_csv("alunos.csv")
    # Carrega o arquivo alunos.csv. Se não existir, cria um novo DataFrame vazio.   
    except FileNotFoundError:
        df = pd.DataFrame(columns=[
            "matricula", "nome", "rua", "numero", "bairro",
            "cidade", "uf", "telefone", "email"
        ])
    return df

# SALVAR DADOS

def salvar_dados(df):
    """
    Salvar o dataframe no arquivo alunos.csv.
    """
    # Uso do index=False para nao salvar o indice do dataframe no csv
    df.to_csv("alunos.csv", index=False)

# GERAR MATRICULA

def gerar_matricula(df):
    """
    Gera uma nova matricula baseada na maior matricula existente.
    """
    # Se nao tiver nenhum aluno cadastrado, retorna 1 como primeira matricula
    if df.empty:
        return 1
    # Senao, retorna a maior matricula + 1
    else:
        maior_matricula = df["matricula"].max()
        return maior_matricula + 1
    
# INSERIR ALUNO
    
def inserir_aluno(df):
    """
    Insere um novo aluno no sistema.
    """
    
    nome = input("Nome do aluno: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    # Gerar matricula unica
    matricula = gerar_matricula(df)
    
    # Criar um dicionario com os dados do novo aluno
    novo_aluno = {
        "matricula": matricula,
        "nome": nome,
        "rua": rua,
        "numero": numero,
        "bairro": bairro,
        "cidade": cidade,
        "uf": uf,
        "telefone": telefone,
        "email": email
    }
    
    # Adicionar o novo aluno ao DataFrame
    novo_df =pd.DataFrame([novo_aluno])
    # Junto o aluno novo com o existente
    df = pd.concat([df, novo_df], ignore_index=True)

    salvar_dados(df)

    return df

# PESQUISAR ALUNO POR NOME OU MATRICULA

def pesquisar_aluno(df):
    """
    Pesquisa um aluno por nome ou matrícula e retorna o índice do DataFrame.
    """

    print("Pesquisar aluno por:")
    print("1 - Nome")
    print("2 - Matrícula")
    opcao = input("Escolha(1 ou 2): ")

    if opcao == "1":
        nome = str(input("Digite o nome do aluno: ")).lower().strip()
        # Comparo tudo em minúsculo pra evitar erro se o usuário digitar diferente.
        resultado = df[df["nome"].str.lower().str.strip() == nome]
        if not resultado.empty:
            print(resultado)
        else:
            print("Nenhum aluno encontrado com esse nome.")
            return None 
    
    elif opcao == "2":
            matricula = int(input("Digite a matrícula do aluno: "))
            resultado = df[df["matricula"] == matricula]
            if not resultado.empty:
                print(resultado)
            else:
                print("Nenhum aluno encontrado com essa matrícula.")
                return None
    else:
        print("Opção inválida.")
        return None

    # Retorna o índice do DataFrame do aluno encontrado
    index = resultado.index[0]
    return index

# EDITAR ALUNO

def editar_aluno(df, index):

    print("\n--- EDITAR ALUNO ---")
    print("\n DADOS ATUAIS DO ALUNO:")
    # Mostra os dados atuais do aluno
    print(df.loc[index])

    print("\nQual campo deseja editar?")
    print("1 - Nome")
    print("2 - Rua")
    print("3 - Número")
    print("4 - Bairro")
    print("5 - Cidade")
    print("6 - UF")
    print("7 - Telefone")
    print("8 - Email")
    print("0 - Voltar")

    opcao = input("Escolha: ")

    colunas = {
        "1": "nome",
        "2": "rua",
        "3": "numero",
        "4": "bairro",
        "5": "cidade",
        "6": "uf",
        "7": "telefone",
        "8": "email"
    }

    if opcao == "0":
        print("Voltando ao menu principal.")
        return df 
    
    # Verifica se a opcao é valida
    if opcao not in colunas:
        print("Opção inválida.")
        return df
    
    # Pede o novo valor para a coluna escolhida
    coluna_escolhida = colunas[opcao]
    novo_valor = input(f"Digite o novo valor para {coluna_escolhida}: ")
    df.loc[index, coluna_escolhida] = novo_valor
    salvar_dados(df)
    print("Dados atualizados com sucesso.")

    return df

# REMOVER ALUNO

def remover_aluno(df, index):
    """
    Remove o aluno e salva no CSV
    """
    print("\n--- REMOVER ALUNO ---")
    # So remove se o usuario confirmar
    confirmacao = input("Tem certeza que deseja remover este aluno? (s/n): ").lower().strip()
    if confirmacao == "s":
        # Remove o aluno do DataFrame
        df = df.drop(index)
        # Resetar o índice do DataFrame após a remoção
        df = df.reset_index(drop=True)
        salvar_dados(df)
        print("Aluno removido com sucesso.")
    else:
        print("Remoção cancelada.")

    return df

# MENU PRINCIPAL

def menu_principal():
    """
    Exibe o menu principal e gerencia as opções do usuário.
    """
    df = carregar_dados()

    while True:
        print("\n---MENU PRINCIPAL---")
        print("1 - INSERIR")
        print("2 - PESQUISAR")
        print("3 - SAIR")

        opcao = input("Escolha(1, 2 ou 3): ")

        if opcao == "1":
            # Inserir um novo aluno
            df = inserir_aluno(df)

        elif opcao == "2":
            index = pesquisar_aluno(df)
            # Se um aluno foi encontrado
            if index is not None:
                print("\nO que deseja fazer?")
                print("1 - EDITAR")
                print("2 - REMOVER")
                print("0 - VOLTAR")
                escolha = input("Escolha(1, 2 ou 0): ")

                if escolha == "1":
                    # Editar o aluno
                    df = editar_aluno(df, index)
                    df = carregar_dados()  # Recarregar os dados após a edição

                elif escolha == "2":
                    # Remover o aluno
                    df = remover_aluno(df, index)
                    df = carregar_dados()  # Recarregar os dados após a remoção

                elif escolha == "0":
                    # Voltar ao menu principal
                    continue
                
                else:
                    print("Opção inválida.")

        elif opcao == "3":
            print("Saindo do sistema.")
            # Sair do loop infinito
            break

# EXECUTA O MENU PRINCIPAL

menu_principal()
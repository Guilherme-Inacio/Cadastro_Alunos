import pandas as pd

# CARREGAR DADOS

def carregar_dados():
    """
    Tenta carregar o arquivo alunos.csv.
    Se não existir, cria um DataFrame vazio com as colunas que precisa.
    """
    try:
        df = pd.read_csv("alunos.csv")
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
    df.to_csv("alunos.csv", index=False)

# GERAR MATRICULA

def gerar_matricula(df):
    """
    Gera uma nova matricula baseada na maior matricula existente.
    """
    #se nao tiver nenhum aluno cadastrado, retorna 1
    if df.empty:
        return 1
    else:
        maior_matricula = df["matricula"].max()
        return maior_matricula + 1
    
# INSERIR ALUNO
    
def inserir_aluno():
    """
    Insere um novo aluno no sistema.
    """
    df = carregar_dados()
    
    nome = input("Nome do aluno: ")
    rua = input("Rua: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    uf = input("UF: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    
    matricula = gerar_matricula(df)
    
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
    
    novo_df =pd.Dataframe([novo_aluno])
    df = pd.concat([df, novo_df], ignore_index=True)

    salvar_dados(df)
    df.to_csv("alunos.csv", index=False)

# PESQUISAR ALUNO POR NOME OU MATRICULA

def pesquisar_aluno():
    """
    Pesquisa um aluno por nome ou matrícula e retorna o índice do DataFrame.
    """

    print("Pesquisar aluno por:")
    print("1 - Nome")
    print("2 - Matrícula")
    opcao = input("Escolha(1 ou 2): ")

    if opcao == "1":
        nome = input("Digite o nome do aluno: ")
        df = carregar_dados()
        resultado = df[df["nome"].str.lower() == nome.lower()]
        if not resultado.empty:
            print(resultado)
        else:
            print("Nenhum aluno encontrado com esse nome.")
    
    elif opcao == "2":
        matricula = int(input("Digite a matrícula do aluno: "))
        df = carregar_dados()
        resultado = df[df["matricula"] == matricula]
        if not resultado.empty:
            print(resultado)
        else:
            print("Nenhum aluno encontrado com essa matrícula.")
    else:
        print("Opção inválida.")
        return

    index = resultado.index[0]
    return index

def editar_aluno(df, index):

    print("\n--- EDITAR ALUNO ---")
    print("\n DADOS ATUAIS DO ALUNO:")
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

    if opcao == 0:
        print("Voltando ao menu principal.")
        return df 
    
    if opcao not in colunas:
        print("Opção inválida.")
        return df
    
    coluna_escolhida = colunas[opcao]
    novo_valor = input(f"Digite o novo valor para {coluna_escolhida}: ")
    df.loc[index, coluna_escolhida] = novo_valor
    salvar_dados(df)
    print("Dados atualizados com sucesso.")
    
    return df

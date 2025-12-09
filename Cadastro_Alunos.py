import pandas as pd

# 1. CARREGAR DADOS

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

# 2. SALVAR DADOS

def salvar_dados(df):
    """
    Salvar o dataframe no arquivo alunos.csv.
    """
    df.to_csv("alunos.csv", index=False)

# 3. GERAR MATRICULA

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
    

    

import pandas as pd

# 1. CARREGAR DADOS

def carregar_dados():
    """
    Tenta carregar o arquivo alunos.csv.
    Se não existir, cria um DataFrame vazio com as colunas necessárias.
    """
    try:
        df = pd.read_csv("alunos.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=[
            "matricula", "nome", "rua", "numero", "bairro",
            "cidade", "uf", "telefone", "email"
        ])
    return df
import pandas as pd
import numpy as np
import re


# ♡‧₊˚✧ Configuração inicial

MAPA_COLUNAS = {
    "CNPJ": "CNPJ",
    "Razão Social": "Razão Social",
    "Nome Fantasia": "Nome Fantasia",
    "Website": "Websites",
    "E-mail": "E-mails",
    "Telefone": "Telefones",
    "Endereço": "Endereço completo"
}

ORDEM_VERIFICACAO = [
    "CNPJ", "Website", "E-mail", "Telefone", 
    "Razão Social", "Nome Fantasia", "Endereço"
]


# ♡‧₊˚✧ Padronização

def limpar_numeros(serie):
    """Para CNPJ e Telefone"""
    # astype(str) converte NaN para "nan". O regex limpa. 
    # Depois substituímos vazios e "nan" literais por np.nan
    return (
        serie.astype(str)
        .str.replace(r"\D", "", regex=True)
        .replace({"": np.nan, "nan": np.nan})
    )

def limpar_texto(serie):
    """Para textos gerais"""
    return (
        serie.astype(str)
        .str.lower()
        .str.strip()
        .replace({"nan": np.nan, "": np.nan})
    )

def limpar_url(serie):
    """Para websites"""
    s = serie.astype(str).str.lower().str.strip()
    s = s.str.replace(r"https?://", "", regex=True)
    s = s.str.replace(r"www\.", "", regex=True)
    s = s.str.rstrip("/")
    return s.replace({"nan": np.nan, "": np.nan})


# ♡‧₊˚✧ Pipeline de deduplicação

def deduplicar_cascata(df, mapa_colunas, ordem_verificacao):
    df = df.copy()
    total_inicial = len(df)

    print("1. Padronizando dados e calculando score.")

    # Criação de colunas padronizadas temporárias
    cols_norm_map = {}
    
    # Mapeamento dinâmico das funções de limpeza
    for chave, col_original in mapa_colunas.items():
        if col_original not in df.columns:
            continue
            
        if chave in ["CNPJ", "Telefone"]:
            df[f"norm_{chave}"] = limpar_numeros(df[col_original])
        elif chave == "Website":
            df[f"norm_{chave}"] = limpar_url(df[col_original])
        else:
            df[f"norm_{chave}"] = limpar_texto(df[col_original])

    # Score: define quem "ganha" em caso de conflito
    cols_score = [f"norm_{k}" for k in ordem_verificacao if f"norm_{k}" in df.columns]
    df["score"] = df[cols_score].notna().sum(axis=1)

    # Colocamos as linhas mais completas no topo. O drop_duplicates mantém a primeira que encontrar.
    df = df.sort_values("score", ascending=False)

    print("2. Executando deduplicação.")

    for chave in ordem_verificacao:
        col_norm = f"norm_{chave}"

        # Segurança: se a coluna não existe (ex: planilha sem CNPJ), pula
        if col_norm not in df.columns:
            continue

        # Separa linhas que tem valor (ex: tem email) das que não tem (email vazio)
        mask_valido = df[col_norm].notna()
        
        df_com_valor = df[mask_valido]
        df_sem_valor = df[~mask_valido] # Estes são salvos automaticamente pois não conflitam

        # Remove duplicatas APENAS entre quem tem o dado preenchido
        antes = len(df_com_valor)
        df_com_valor = df_com_valor.drop_duplicates(subset=[col_norm], keep= "first")
        removidos = antes - len(df_com_valor)

        if removidos > 0:
            print(f"   -> {chave}: removidos {removidos} duplicados.")

        # Recombina corrigindo o índice
        df = pd.concat([df_com_valor, df_sem_valor], ignore_index=True)

    # Limpeza final das colunas auxiliares
    print("3. Finalizando.")
    cols_temp = [c for c in df.columns if c.startswith("norm_") or c == "score"]
    df = df.drop(columns=cols_temp)

    print("♡‧₊˚✧" * 10)
    print(f"Inicial:  {total_inicial}")
    print(f"Final:    {len(df)}")
    print(f"Removidos: {total_inicial - len(df)}")
    print("♡‧₊˚✧" * 10)

    return df

print("♡‧₊˚✧" * 10)
# ♡‧₊˚✧ Execução


if __name__ == "__main__":
    # Necessário ajustar os nomes conforme necessário
    entrada = "base_terceiros.xlsx"
    saida = "base_terceiros_limpo.xlsx"

    try:
        df = pd.read_excel(entrada)
        
        df_limpo = deduplicar_cascata(df, MAPA_COLUNAS, ORDEM_VERIFICACAO)
        
        df_limpo.to_excel(saida, index=False)
        print(f"Arquivo salvo com sucesso em: {saida}")
        
    except FileNotFoundError:
        print(f"ERRO: O arquivo '{entrada}' não foi encontrado.")
    except Exception as e:

        print(f"ERRO CRÍTICO: {e}")

# ==========================================
# load_data.py
# Módulo de leitura e inferência de colunas
# ==========================================

import pandas as pd

def read_csv_auto(path_or_buffer):
    """
    Lê automaticamente o CSV.
    Detecta delimitador e tenta conversão de tipos.
    """
    try:
        df = pd.read_csv(path_or_buffer)
        return df
    except Exception as e:
        raise Exception(f"Erro ao ler arquivo CSV: {e}")


def infer_columns(df: pd.DataFrame):
    """
    Faz inferência automática de:
    - Coluna de data
    - Colunas numéricas
    - Colunas categóricas
    """
    cols = df.columns.str.lower()

    # inferir data
    date_candidates = [c for c in df.columns if 'date' in c.lower() or 'data' in c.lower()]

    # numéricas
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    # categóricas
    categorical = [c for c in df.columns if c not in numeric_cols and c not in date_candidates]

    return {
        "date_cols": date_candidates,
        "numeric_cols": numeric_cols,
        "categorical_cols": categorical
    }


def ensure_date(df: pd.DataFrame, date_col: str):
    """
    Converte a coluna de data para datetime.
    """
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    if df[date_col].isna().sum() > 0:
        print("⚠️ Atenção: algumas datas não puderam ser convertidas.")
    return df

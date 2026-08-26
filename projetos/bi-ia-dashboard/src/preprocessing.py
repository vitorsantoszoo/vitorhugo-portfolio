# ==========================================
# preprocessing.py (versão atualizada)
# Tratamento inicial do dataset
# ==========================================

import pandas as pd

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpeza básica:
    - Remove colunas totalmente nulas
    - Remove espaços extras em strings
    """
    df = df.copy()
    df = df.loc[:, df.notna().sum() > 0]

    for c in df.select_dtypes(include='object'):
        df[c] = df[c].astype(str).str.strip()

    return df


def fill_numeric(df: pd.DataFrame, strategy='median'):
    """
    Preenchimento das colunas numéricas.
    Versão sem warnings (compatível com Pandas 3.0+).
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include='number').columns

    for c in numeric_cols:
        if strategy == 'median':
            # forma recomendada pelo pandas (sem inplace)
            df[c] = df[c].fillna(df[c].median())
        else:
            df[c] = df[c].fillna(0)

    return df

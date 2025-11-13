# ==========================================
# preprocessing.py
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
    """
    df = df.copy()
    numeric_cols = df.select_dtypes(include='number').columns

    for c in numeric_cols:
        if strategy == 'median':
            df[c].fillna(df[c].median(), inplace=True)
        else:
            df[c].fillna(0, inplace=True)

    return df

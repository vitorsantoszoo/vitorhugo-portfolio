# ==========================================
# metrics.py
# KPIs e agregações temporais
# ==========================================

import pandas as pd

def calc_monthly_kpis(df: pd.DataFrame, date_col: str, value_col: str):
    """
    Calcula KPIs mensais:
    - total mensal
    - crescimento percentual
    """
    s = df[[date_col, value_col]].dropna()
    s = s.set_index(date_col).sort_index()

    monthly = s.resample("M").sum()
    monthly["pct_change"] = monthly[value_col].pct_change()

    # KPIs principais
    kpis = {
        "total_periodo": float(monthly[value_col].sum()),
        "media_mensal": float(monthly[value_col].mean()),
        "crescimento_ultimo_mes": float(monthly["pct_change"].iloc[-1])
        if not monthly["pct_change"].isna().iloc[-1] else None
    }

    return monthly, kpis

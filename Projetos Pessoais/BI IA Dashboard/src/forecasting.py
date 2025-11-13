# ==========================================
# forecasting.py — versão corrigida
# ==========================================

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def create_lags(series: pd.Series, n_lags=6):
    df = pd.DataFrame({series.name: series})
    for lag in range(1, n_lags + 1):
        df[f"lag_{lag}"] = df[series.name].shift(lag)
    df = df.dropna()
    return df

def rf_forecast(series: pd.Series, n_periods=6):
    df = create_lags(series)

    X = df.drop(series.name, axis=1)
    y = df[series.name]

    rf = RandomForestRegressor(
        n_estimators=300,
        random_state=42
    )
    rf.fit(X, y)

    # usa última linha COM os nomes das colunas
    last = X.tail(1).copy()

    preds = []
    for _ in range(n_periods):
        pred = rf.predict(last)[0]
        preds.append(pred)

        # cria nova linha com lags atualizados
        new_row = last.iloc[0].shift(-1)
        new_row.iloc[-1] = pred

        last = pd.DataFrame([new_row], columns=last.columns)

    return preds

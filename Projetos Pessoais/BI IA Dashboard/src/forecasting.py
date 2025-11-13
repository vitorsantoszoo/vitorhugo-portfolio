# ==========================================
# forecasting.py — versão final sem warnings
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

    feature_names = X.columns.tolist()

    rf = RandomForestRegressor(
        n_estimators=300,
        random_state=42
    )
    rf.fit(X, y)

    # pega última linha mantendo nomes das colunas
    last = X.tail(1).copy()

    preds = []
    for _ in range(n_periods):
        # garante preservação de nomes de colunas
        last_df = pd.DataFrame(last.values, columns=feature_names)

        pred = rf.predict(last_df)[0]
        preds.append(pred)

        # atualiza lags
        new_values = last_df.iloc[0].shift(-1)
        new_values.iloc[-1] = pred
        last = pd.DataFrame([new_values], columns=feature_names)

    return preds

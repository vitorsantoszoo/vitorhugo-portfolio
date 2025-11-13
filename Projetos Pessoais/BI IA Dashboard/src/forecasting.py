# ==========================================
# forecasting.py
# Previsão de vendas/lucro com IA
# ==========================================

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def create_lags(series: pd.Series, n_lags=6):
    df = pd.DataFrame(series)
    for lag in range(1, n_lags + 1):
        df[f"lag_{lag}"] = df[series.name].shift(lag)
    df.dropna(inplace=True)
    return df

def rf_forecast(series: pd.Series, n_periods=6):
    """
    Previsão usando RandomForest e lags.
    """
    df = create_lags(series)
    X = df.drop(series.name, axis=1)
    y = df[series.name]

    model = RandomForestRegressor(n_estimators=200)
    model.fit(X, y)

    last = X.tail(1).values
    preds = []

    for _ in range(n_periods):
        p = model.predict(last)[0]
        preds.append(p)
        last = np.roll(last, -1)
        last[0, -1] = p

    return preds

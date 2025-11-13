# ==========================================
# forecasting.py — versão com intervalo de confiança (bootstrap)
# ==========================================

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def create_lags(series: pd.Series, n_lags=6):
    df = pd.DataFrame({series.name: series})
    for lag in range(1, n_lags + 1):
        df[f"lag_{lag}"] = df[series.name].shift(lag)
    df.dropna(inplace=True)
    return df


def rf_forecast_with_ci(series: pd.Series, n_periods=6, n_bootstrap=80):
    \
    Previsão usando RandomForest + intervalos de confiança via bootstrap.
    Retorna:
    - preds_mean: previsão média
    - preds_lower: limite inferior (IC 90%)
    - preds_upper: limite superior (IC 90%)
    \

    df = create_lags(series)
    X = df.drop(series.name, axis=1)
    y = df[series.name]

    feature_names = X.columns.tolist()

    # modelo base
    model = RandomForestRegressor(n_estimators=400, random_state=42)
    model.fit(X, y)

    last = X.tail(1).copy()

    preds_mean = []
    preds_lower = []
    preds_upper = []

    # forecast passo a passo
    for _ in range(n_periods):

        # previsão principal
        last_df = pd.DataFrame(last.values, columns=feature_names)
        base_pred = model.predict(last_df)[0]

        # bootstrap
        boot_preds = []
        for b in range(n_bootstrap):
            boot_model = RandomForestRegressor(
                n_estimators=120,
                random_state=42 + b,
            )
            boot_model.fit(X, y)
            boot_preds.append(boot_model.predict(last_df)[0])

        lower = np.percentile(boot_preds, 5)
        upper = np.percentile(boot_preds, 95)

        preds_mean.append(base_pred)
        preds_lower.append(lower)
        preds_upper.append(upper)

        # atualizar lags
        new_row = last.iloc[0].shift(-1)
        new_row.iloc[-1] = base_pred
        last = pd.DataFrame([new_row], columns=feature_names)

    return preds_mean, preds_lower, preds_upper

# Escrever arquivo atualizado
file_path = "/content/vitorhugo-portfolio/Projetos Pessoais/BI IA Dashboard/src/forecasting.py"
with open(file_path, "w") as f:
    f.write(forecasting_code)

print("✅ forecasting.py atualizado com sucesso!")
print("📄 Caminho:", file_path)

# Recarregar o módulo
import importlib
import src.forecasting
importlib.reload(src.forecasting)

# Testar importação
from src.forecasting import rf_forecast_with_ci

print("\n🎉 Função rf_forecast_with_ci importada com sucesso! Tudo pronto.")

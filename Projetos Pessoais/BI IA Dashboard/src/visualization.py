# ==========================================
# visualization.py
# Gráficos interativos (Plotly)
# ==========================================

import plotly.express as px

def plot_timeseries(df, x, y, title="Série Temporal"):
    fig = px.line(df, x=x, y=y, title=title, markers=True)
    return fig

def plot_top_categories(df, cat_col, value_col, top_n=10):
    agg = df.groupby(cat_col)[value_col].sum().reset_index()\
            .sort_values(value_col, ascending=False).head(top_n)
    fig = px.bar(agg, x=cat_col, y=value_col, title=f"Top {top_n} {cat_col}")
    return fig

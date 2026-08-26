# ==========================================
# nlg_agent.py
# Geração automática de relatórios (NLG)
# ==========================================

from datetime import datetime

def generate_summary(kpis: dict, forecast_list: list):
    total = kpis.get("total_periodo")
    media = kpis.get("media_mensal")
    crescimento = kpis.get("crescimento_ultimo_mes")

    tendencia = "crescimento" if crescimento and crescimento > 0 else "queda"

    txt = f"""
📊 Relatório Inteligente — BI IA Dashboard
📅 Data: {datetime.utcnow().strftime("%Y-%m-%d")}

💰 Faturamento total analisado: R$ {total:,.2f}
📅 Média mensal: R$ {media:,.2f}
📈 Variação do último mês: {crescimento*100:.2f}% ({tendencia})

🔮 Previsão (próximos períodos):
{[round(v, 2) for v in forecast_list]}

💡 Insight:
- Caso a tendência continue em {tendencia}, recomenda-se revisão de estoque e campanhas.
- Focar nos produtos mais rentáveis e regiões de maior desempenho.
    """

    return txt.strip()

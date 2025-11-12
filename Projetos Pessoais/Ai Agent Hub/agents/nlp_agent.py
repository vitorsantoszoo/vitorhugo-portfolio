# agents/nlp_agent.py
import random

class NLPAagent:
    """
    Agente de linguagem natural simples.
    - Analisa mensagens de texto do usuário.
    - Retorna respostas automáticas baseadas em intenção.
    """

    def __init__(self):
        # Banco de intenções/respostas (expandível)
        self.responses = {
            "saudacao": [
                "Olá! 😊 Como posso te ajudar hoje?",
                "Oi! Tudo bem por aí?",
                "E aí! Pronto para falar de IA?"
            ],
            "projeto": [
                "Este sistema faz parte do projeto AI Agent Hub.",
                "Estou conectado com outros agentes inteligentes, sabia?",
                "Fui criado para analisar textos e ajudar na tomada de decisão."
            ],
            "visao": [
                "O agente de visão analisa imagens e detecta objetos automaticamente.",
                "Podemos usar visão computacional para contar ou classificar itens visuais."
            ],
            "despedida": [
                "Até mais! 👋",
                "Foi bom conversar com você!",
                "Tchau! Continue explorando o AI Agent Hub!"
            ],
            "default": [
                "Desculpe, não entendi. Pode reformular?",
                "Interessante! Pode me explicar melhor?",
                "Não tenho uma resposta exata, mas posso tentar aprender!"
            ]
        }

        # Palavras-chave de intenção
        self.keywords = {
            "saudacao": ["oi", "olá", "bom dia", "boa tarde", "boa noite"],
            "projeto": ["projeto", "ai agent hub", "modelo", "inteligência"],
            "visao": ["imagem", "visão", "computacional", "foto", "objeto"],
            "despedida": ["tchau", "até", "valeu", "falou"]
        }

    def detect_intent(self, text: str) -> str:
        """Detecta a intenção básica do usuário com base em palavras-chave."""
        text_lower = text.lower()
        for intent, keywords in self.keywords.items():
            if any(k in text_lower for k in keywords):
                return intent
        return "default"

    def analyze(self, text: str) -> str:
        """Processa o texto e retorna uma resposta."""
        intent = self.detect_intent(text)
        return random.choice(self.responses[intent])

"""
Sistema de Repetição Espaçada (Spaced Repetition System)
Baseado no algoritmo SM-2 (SuperMemo 2) adaptado para aprendizado de certificações
"""

from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import math


class SpacedRepetitionEngine:
    """
    Motor de repetição espaçada para otimizar o aprendizado
    
    Implementa variação do algoritmo SM-2 com ajustes para quiz de certificação:
    - Prioriza questões nunca vistas
    - Reintroduz questões com baixa taxa de acerto
    - Espaça revisões baseado em performance
    """
    
    def __init__(self, min_easiness: float = 1.3, initial_interval: int = 1):
        """
        Inicializa o motor de repetição espaçada
        
        Args:
            min_easiness: Fator mínimo de facilidade (padrão: 1.3)
            initial_interval: Intervalo inicial em dias (padrão: 1)
        """
        self.min_easiness = min_easiness
        self.initial_interval = initial_interval
        
        # Limiares de performance
        self.mastery_threshold = 0.8  # 80% de acerto para considerar "dominado"
        self.struggle_threshold = 0.5  # <50% de acerto = dificuldade
        self.min_attempts_mastery = 3  # Mínimo de tentativas para considerar dominado
    
    def calculate_next_review(self, performance_data: Dict) -> Dict:
        """
        Calcula próxima data de revisão baseada no desempenho
        
        Args:
            performance_data: Histórico de desempenho da questão
                - attempts: número de tentativas
                - correct: número de acertos
                - easiness_factor: fator de facilidade atual
                - repetitions: número de repetições bem-sucedidas
                - last_interval: último intervalo usado
        
        Returns:
            Dict com nova data de revisão e parâmetros atualizados
        """
        attempts = performance_data.get('attempts', 0)
        correct = performance_data.get('correct', 0)
        easiness = performance_data.get('easiness_factor', 2.5)
        repetitions = performance_data.get('repetitions', 0)
        last_interval = performance_data.get('interval', self.initial_interval)
        
        # Calcular taxa de acerto
        accuracy = correct / attempts if attempts > 0 else 0
        
        # Determinar se a última tentativa foi bem-sucedida
        last_correct = accuracy >= 0.6  # Considera sucesso se >60% de acerto
        
        if last_correct:
            # Ajustar fator de facilidade (fórmula SM-2 adaptada)
            quality = self._map_accuracy_to_quality(accuracy)
            easiness = easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
            easiness = max(self.min_easiness, easiness)
            
            repetitions += 1
            
            # Calcular novo intervalo
            if repetitions == 1:
                interval = 1  # 1 dia
            elif repetitions == 2:
                interval = 6  # 6 dias
            else:
                interval = math.ceil(last_interval * easiness)
        else:
            # Reiniciar contagem em caso de erro
            repetitions = 0
            interval = 1
            easiness = max(self.min_easiness, easiness - 0.2)
        
        # Calcular próxima data de revisão
        next_review = datetime.now() + timedelta(days=interval)
        
        # Calcular nível de domínio (0.0 a 1.0)
        mastery_level = self._calculate_mastery_level(accuracy, attempts, repetitions)
        
        return {
            'next_review': next_review.isoformat(),
            'easiness_factor': round(easiness, 2),
            'repetitions': repetitions,
            'interval': interval,
            'mastery_level': round(mastery_level, 2),
            'last_accuracy': round(accuracy, 2)
        }
    
    def _map_accuracy_to_quality(self, accuracy: float) -> int:
        """
        Mapeia taxa de acerto para qualidade (0-5) do SM-2
        
        Args:
            accuracy: Taxa de acerto (0.0 a 1.0)
        
        Returns:
            Qualidade de 0 a 5
        """
        if accuracy >= 0.95:
            return 5  # Perfeito
        elif accuracy >= 0.85:
            return 4  # Bom
        elif accuracy >= 0.70:
            return 3  # Adequado
        elif accuracy >= 0.50:
            return 2  # Difícil, mas lembrado
        elif accuracy >= 0.30:
            return 1  # Muito difícil
        else:
            return 0  # Não lembrado
    
    def _calculate_mastery_level(self, accuracy: float, attempts: int, repetitions: int) -> float:
        """
        Calcula nível de domínio de 0.0 (não conhece) a 1.0 (domina)
        
        Considera:
        - Taxa de acerto
        - Número de tentativas
        - Repetições bem-sucedidas
        """
        if attempts == 0:
            return 0.0
        
        # Componente de acurácia (peso: 60%)
        accuracy_component = accuracy * 0.6
        
        # Componente de consistência (peso: 30%)
        consistency = min(attempts / self.min_attempts_mastery, 1.0)
        consistency_component = consistency * 0.3
        
        # Componente de repetições (peso: 10%)
        repetition_component = min(repetitions / 5, 1.0) * 0.1
        
        mastery = accuracy_component + consistency_component + repetition_component
        
        return min(mastery, 1.0)
    
    def get_questions_to_review(
        self, 
        all_questions: List[Dict], 
        progress_data: Dict,
        limit: int = 10
    ) -> List[Dict]:
        """
        Seleciona questões prioritárias para revisão usando algoritmo inteligente
        
        Prioridade:
        1. Questões nunca vistas
        2. Questões com revisão vencida (intervalo espaçado expirou)
        3. Questões com baixa taxa de acerto (<70%)
        4. Questões aleatórias para manter variedade
        
        Args:
            all_questions: Lista de todas as questões disponíveis
            progress_data: Dados de progresso do usuário
            limit: Número máximo de questões a retornar
        
        Returns:
            Lista priorizada de questões para estudo
        """
        now = datetime.now()
        
        never_seen = []
        due_for_review = []
        low_performance = []
        well_known = []
        
        for question in all_questions:
            q_id = question['id']
            perf = progress_data.get(q_id, {})
            
            if not perf or perf.get('attempts', 0) == 0:
                # Nunca vista
                never_seen.append((question, 0))  # Prioridade máxima
            else:
                attempts = perf.get('attempts', 0)
                correct = perf.get('correct', 0)
                accuracy = correct / attempts if attempts > 0 else 0
                
                # Verificar se está vencida para revisão
                next_review = perf.get('next_review')
                is_due = False
                days_overdue = 0
                
                if next_review:
                    try:
                        next_review_dt = datetime.fromisoformat(next_review)
                        is_due = next_review_dt <= now
                        if is_due:
                            days_overdue = (now - next_review_dt).days
                    except:
                        is_due = True  # Se erro no parse, considerar vencida
                
                # Classificar por prioridade
                if is_due:
                    # Prioridade baseada em atraso e performance
                    priority = days_overdue + (1 - accuracy) * 10
                    due_for_review.append((question, priority))
                elif accuracy < 0.7:
                    # Baixa performance
                    priority = 5 + (0.7 - accuracy) * 10
                    low_performance.append((question, priority))
                else:
                    # Bem conhecidas (menor prioridade)
                    priority = 10 + accuracy * 5
                    well_known.append((question, priority))
        
        # Ordenar cada categoria por prioridade
        due_for_review.sort(key=lambda x: x[1], reverse=True)
        low_performance.sort(key=lambda x: x[1], reverse=True)
        
        # Montar lista final
        priority_questions = (
            never_seen + 
            due_for_review + 
            low_performance + 
            well_known
        )
        
        # Retornar apenas as questões (sem prioridade) até o limite
        return [q[0] for q in priority_questions[:limit]]
    
    def get_study_recommendation(self, progress_data: Dict, all_questions: List[Dict]) -> Dict:
        """
        Gera recomendações de estudo baseadas no progresso
        
        Args:
            progress_data: Dados de progresso do usuário
            all_questions: Todas as questões disponíveis
        
        Returns:
            Dict com recomendações e estatísticas
        """
        now = datetime.now()
        
        stats = {
            'never_seen': 0,
            'due_for_review': 0,
            'struggling': 0,
            'mastered': 0,
            'in_progress': 0
        }
        
        weak_domains = {}
        strong_domains = {}
        
        for question in all_questions:
            q_id = question['id']
            perf = progress_data.get(q_id, {})
            domain = question['domain']
            
            if not perf or perf.get('attempts', 0) == 0:
                stats['never_seen'] += 1
            else:
                attempts = perf.get('attempts', 0)
                correct = perf.get('correct', 0)
                accuracy = correct / attempts if attempts > 0 else 0
                mastery = perf.get('mastery_level', 0)
                
                # Verificar se vencida
                next_review = perf.get('next_review')
                is_due = False
                if next_review:
                    try:
                        next_review_dt = datetime.fromisoformat(next_review)
                        is_due = next_review_dt <= now
                    except:
                        pass
                
                if is_due:
                    stats['due_for_review'] += 1
                
                if attempts >= 2 and accuracy < self.struggle_threshold:
                    stats['struggling'] += 1
                    weak_domains[domain] = weak_domains.get(domain, 0) + 1
                elif mastery >= 0.8 and attempts >= self.min_attempts_mastery:
                    stats['mastered'] += 1
                    strong_domains[domain] = strong_domains.get(domain, 0) + 1
                else:
                    stats['in_progress'] += 1
        
        # Gerar recomendação de ação
        if stats['due_for_review'] > 0:
            recommendation = f"Você tem {stats['due_for_review']} questão(ões) pronta(s) para revisão. Revise-as para consolidar o aprendizado!"
            action = "review"
        elif stats['never_seen'] > 0:
            recommendation = f"Explore {stats['never_seen']} novo(s) conceito(s) ainda não estudado(s)."
            action = "learn_new"
        elif stats['struggling'] > 0:
            recommendation = f"Foque em {stats['struggling']} conceito(s) que ainda apresentam dificuldade."
            action = "practice_weak"
        else:
            recommendation = "Continue praticando para manter o conhecimento fresco!"
            action = "general_practice"
        
        return {
            'stats': stats,
            'recommendation': recommendation,
            'action': action,
            'weak_domains': sorted(weak_domains.items(), key=lambda x: x[1], reverse=True)[:3],
            'strong_domains': sorted(strong_domains.items(), key=lambda x: x[1], reverse=True)[:3]
        }
    
    def is_mastered(self, performance_data: Dict) -> bool:
        """
        Verifica se uma questão está dominada
        
        Args:
            performance_data: Dados de performance da questão
        
        Returns:
            True se a questão está dominada
        """
        attempts = performance_data.get('attempts', 0)
        correct = performance_data.get('correct', 0)
        mastery = performance_data.get('mastery_level', 0)
        
        if attempts < self.min_attempts_mastery:
            return False
        
        accuracy = correct / attempts
        
        return accuracy >= self.mastery_threshold and mastery >= 0.8

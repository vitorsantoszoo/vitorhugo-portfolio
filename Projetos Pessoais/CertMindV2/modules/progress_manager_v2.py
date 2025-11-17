"""
Gerenciador de Progresso Avançado
Integra com o sistema de repetição espaçada e mantém histórico detalhado
"""

import json
import os
from datetime import datetime
from typing import Dict, Optional, List
from spaced_repetition import SpacedRepetitionEngine


class ProgressManager:
    """
    Gerencia o progresso do usuário com métricas avançadas
    
    Funcionalidades:
    - Rastreamento de acertos/erros por questão
    - Integração com repetição espaçada
    - Histórico temporal de sessões
    - Métricas por domínio e subdomínio
    """
    
    def __init__(self, progress_file: str = "data/progress_v2.json"):
        """
        Inicializa o gerenciador de progresso
        
        Args:
            progress_file: Caminho para o arquivo de progresso
        """
        self.progress_file = progress_file
        self.sr_engine = SpacedRepetitionEngine()
        self.data = self._load_progress()
    
    def _load_progress(self) -> Dict:
        """Carrega dados de progresso do arquivo"""
        if not os.path.exists(self.progress_file):
            return self._create_empty_progress()
        
        try:
            with open(self.progress_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Verificar versão e migrar se necessário
            if data.get('version') != '2.0':
                return self._migrate_old_progress(data)
            
            # Garantir que todas as chaves necessárias existem
            empty = self._create_empty_progress()
            for key in empty:
                if key not in data:
                    data[key] = empty[key]
            
            return data
        except Exception as e:
            print(f"Erro ao carregar progresso: {e}")
            return self._create_empty_progress()
    
    def _create_empty_progress(self) -> Dict:
        """Cria estrutura de progresso vazia"""
        return {
            "version": "2.0",
            "user_id": "default_user",
            "last_updated": datetime.now().isoformat(),
            "performance": {},
            "session_history": [],
            "stats": {
                "total_sessions": 0,
                "total_questions_answered": 0,
                "total_correct": 0,
                "streak_days": 0,
                "last_session_date": None
            }
        }
    
    def _migrate_old_progress(self, old_data: Dict) -> Dict:
        """Migra formato antigo de progresso para o novo"""
        new_data = self._create_empty_progress()
        # Preservar dados antigos não são compatíveis, iniciar do zero
        return new_data
    
    def _save_progress(self):
        """Salva dados de progresso no arquivo"""
        self.data['last_updated'] = datetime.now().isoformat()
        
        # Garantir que o diretório existe
        os.makedirs(os.path.dirname(self.progress_file), exist_ok=True)
        
        with open(self.progress_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
    
    def record_answer(
        self, 
        question_id: str, 
        is_correct: bool,
        exam: str,
        domain: str,
        subdomain: str
    ) -> Dict:
        """
        Registra uma resposta e atualiza métricas
        
        Args:
            question_id: ID da questão respondida
            is_correct: Se a resposta foi correta
            exam: Nome do exame (ex: "Core 1 (220-1201)")
            domain: Domínio da questão
            subdomain: Subdomínio da questão
        
        Returns:
            Dict com feedback e próxima revisão
        """
        # Inicializar estrutura se não existe
        if question_id not in self.data['performance']:
            self.data['performance'][question_id] = {
                'exam': exam,
                'domain': domain,
                'subdomain': subdomain,
                'attempts': 0,
                'correct': 0,
                'incorrect': 0,
                'first_seen': datetime.now().isoformat(),
                'last_seen': datetime.now().isoformat(),
                'easiness_factor': 2.5,
                'repetitions': 0,
                'interval': 1,
                'next_review': datetime.now().isoformat(),
                'mastery_level': 0.0,
                'history': []
            }
        
        # Atualizar contadores
        perf = self.data['performance'][question_id]
        perf['attempts'] += 1
        
        if is_correct:
            perf['correct'] += 1
        else:
            perf['incorrect'] += 1
        
        perf['last_seen'] = datetime.now().isoformat()
        
        # Registrar no histórico
        perf['history'].append({
            'timestamp': datetime.now().isoformat(),
            'correct': is_correct
        })
        
        # Limitar histórico (últimas 50 respostas)
        if len(perf['history']) > 50:
            perf['history'] = perf['history'][-50:]
        
        # Calcular próxima revisão usando repetição espaçada
        sr_update = self.sr_engine.calculate_next_review(perf)
        
        # Atualizar com dados da repetição espaçada
        perf.update({
            'next_review': sr_update['next_review'],
            'easiness_factor': sr_update['easiness_factor'],
            'repetitions': sr_update['repetitions'],
            'interval': sr_update['interval'],
            'mastery_level': sr_update['mastery_level']
        })
        
        # Atualizar estatísticas globais
        self.data['stats']['total_questions_answered'] += 1
        if is_correct:
            self.data['stats']['total_correct'] += 1
        
        # Atualizar streak
        self._update_streak()
        
        # Salvar progresso
        self._save_progress()
        
        # Retornar feedback
        return {
            'is_correct': is_correct,
            'accuracy': perf['correct'] / perf['attempts'],
            'mastery_level': perf['mastery_level'],
            'next_review_date': sr_update['next_review'],
            'next_review_days': sr_update['interval'],
            'is_mastered': self.sr_engine.is_mastered(perf)
        }
    
    def _update_streak(self):
        """Atualiza contador de dias consecutivos de estudo"""
        today = datetime.now().date()
        last_session = self.data['stats'].get('last_session_date')
        
        if last_session:
            try:
                last_date = datetime.fromisoformat(last_session).date()
                days_diff = (today - last_date).days
                
                if days_diff == 0:
                    # Mesmo dia, não altera streak
                    pass
                elif days_diff == 1:
                    # Dia consecutivo, aumenta streak
                    self.data['stats']['streak_days'] += 1
                else:
                    # Quebrou o streak
                    self.data['stats']['streak_days'] = 1
            except:
                self.data['stats']['streak_days'] = 1
        else:
            self.data['stats']['streak_days'] = 1
        
        self.data['stats']['last_session_date'] = today.isoformat()
    
    def get_question_performance(self, question_id: str) -> Optional[Dict]:
        """
        Retorna performance de uma questão específica
        
        Args:
            question_id: ID da questão
        
        Returns:
            Dict com dados de performance ou None se não existe
        """
        return self.data['performance'].get(question_id)
    
    def get_domain_stats(self, exam: str, domain: str) -> Dict:
        """
        Calcula estatísticas de um domínio específico
        
        Args:
            exam: Nome do exame
            domain: Nome do domínio
        
        Returns:
            Dict com estatísticas do domínio
        """
        domain_questions = [
            perf for perf in self.data['performance'].values()
            if perf['exam'] == exam and perf['domain'] == domain
        ]
        
        if not domain_questions:
            return {
                'total_questions': 0,
                'answered': 0,
                'mastered': 0,
                'accuracy': 0.0,
                'average_mastery': 0.0
            }
        
        total_attempts = sum(q['attempts'] for q in domain_questions)
        total_correct = sum(q['correct'] for q in domain_questions)
        mastered = sum(1 for q in domain_questions if self.sr_engine.is_mastered(q))
        avg_mastery = sum(q['mastery_level'] for q in domain_questions) / len(domain_questions)
        
        return {
            'total_questions': len(domain_questions),
            'answered': len([q for q in domain_questions if q['attempts'] > 0]),
            'mastered': mastered,
            'accuracy': (total_correct / total_attempts * 100) if total_attempts > 0 else 0,
            'average_mastery': avg_mastery
        }
    
    def get_overall_stats(self) -> Dict:
        """
        Retorna estatísticas gerais do usuário
        
        Returns:
            Dict com estatísticas globais
        """
        perf_data = self.data['performance']
        
        if not perf_data:
            return {
                'total_questions_answered': 0,
                'total_correct': 0,
                'overall_accuracy': 0.0,
                'mastered_concepts': 0,
                'streak_days': self.data['stats']['streak_days'],
                'average_mastery': 0.0
            }
        
        total_attempts = sum(p['attempts'] for p in perf_data.values())
        total_correct = sum(p['correct'] for p in perf_data.values())
        mastered = sum(1 for p in perf_data.values() if self.sr_engine.is_mastered(p))
        avg_mastery = sum(p['mastery_level'] for p in perf_data.values()) / len(perf_data)
        
        return {
            'total_questions_answered': total_attempts,
            'total_correct': total_correct,
            'overall_accuracy': (total_correct / total_attempts * 100) if total_attempts > 0 else 0,
            'mastered_concepts': mastered,
            'streak_days': self.data['stats']['streak_days'],
            'average_mastery': avg_mastery,
            'total_unique_questions': len(perf_data)
        }
    
    def get_weak_areas(self, min_attempts: int = 2, threshold: float = 0.6) -> List[Dict]:
        """
        Identifica áreas com dificuldade
        
        Args:
            min_attempts: Mínimo de tentativas para considerar
            threshold: Limite de acurácia para considerar fraco
        
        Returns:
            Lista de áreas fracas ordenadas por dificuldade
        """
        weak_areas = {}
        
        for q_id, perf in self.data['performance'].items():
            if perf['attempts'] >= min_attempts:
                accuracy = perf['correct'] / perf['attempts']
                if accuracy < threshold:
                    domain = perf['domain']
                    subdomain = perf['subdomain']
                    key = f"{domain} > {subdomain}"
                    
                    if key not in weak_areas:
                        weak_areas[key] = {
                            'domain': domain,
                            'subdomain': subdomain,
                            'count': 0,
                            'avg_accuracy': []
                        }
                    
                    weak_areas[key]['count'] += 1
                    weak_areas[key]['avg_accuracy'].append(accuracy)
        
        # Calcular média de acurácia para cada área
        result = []
        for key, data in weak_areas.items():
            avg_acc = sum(data['avg_accuracy']) / len(data['avg_accuracy'])
            result.append({
                'area': key,
                'domain': data['domain'],
                'subdomain': data['subdomain'],
                'weak_questions': data['count'],
                'average_accuracy': avg_acc * 100
            })
        
        # Ordenar por número de questões fracas (decrescente)
        return sorted(result, key=lambda x: x['weak_questions'], reverse=True)
    
    def get_questions_due_for_review(self, all_questions: List[Dict]) -> List[Dict]:
        """
        Retorna questões que estão vencidas para revisão
        
        Args:
            all_questions: Lista de todas as questões
        
        Returns:
            Lista de questões para revisar
        """
        return self.sr_engine.get_questions_to_review(
            all_questions,
            self.data['performance']
        )
    
    def start_session(self):
        """Registra início de uma nova sessão de estudo"""
        self.data['stats']['total_sessions'] += 1
        
        session = {
            'started_at': datetime.now().isoformat(),
            'questions_answered': 0,
            'correct': 0
        }
        
        self.data['session_history'].append(session)
        
        # Manter apenas últimas 100 sessões
        if len(self.data['session_history']) > 100:
            self.data['session_history'] = self.data['session_history'][-100:]
        
        self._save_progress()
    
    def get_performance_data(self) -> Dict:
        """Retorna todos os dados de performance (para uso em seleção de questões)"""
        return self.data['performance']
    
    def reset_progress(self):
        """Reseta todo o progresso (use com cuidado!)"""
        self.data = self._create_empty_progress()
        self._save_progress()

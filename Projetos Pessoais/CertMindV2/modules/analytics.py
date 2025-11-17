"""
Sistema de Analytics e Visualizações
Gera insights e estatísticas detalhadas sobre o desempenho do usuário
"""

import streamlit as st
from typing import Dict, List
import pandas as pd
from datetime import datetime, timedelta


class PerformanceAnalytics:
    """
    Sistema de análise de desempenho com visualizações ricas
    """
    
    def __init__(self, progress_manager):
        """
        Inicializa o sistema de analytics
        
        Args:
            progress_manager: Instância do ProgressManager
        """
        self.pm = progress_manager
    
    def render_dashboard(self):
        """Renderiza dashboard completo de estatísticas"""
        
        st.markdown("## 📊 Painel de Desempenho")
        st.markdown("---")
        
        # Estatísticas principais
        self._render_main_metrics()
        
        st.markdown("---")
        
        # Gráficos e visualizações
        col1, col2 = st.columns(2)
        
        with col1:
            self._render_mastery_distribution()
        
        with col2:
            self._render_domain_performance()
        
        st.markdown("---")
        
        # Áreas de dificuldade
        self._render_weak_areas()
        
        st.markdown("---")
        
        # Recomendações
        self._render_recommendations()
    
    def _render_main_metrics(self):
        """Renderiza métricas principais em cards"""
        
        stats = self.pm.get_overall_stats()
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric(
                label="📝 Questões Respondidas",
                value=stats['total_unique_questions'],
                help="Número de conceitos únicos que você já estudou"
            )
        
        with col2:
            accuracy = stats['overall_accuracy']
            st.metric(
                label="🎯 Taxa de Acerto",
                value=f"{accuracy:.1f}%",
                delta=self._get_accuracy_trend(accuracy),
                help="Porcentagem geral de acertos"
            )
        
        with col3:
            st.metric(
                label="⭐ Conceitos Dominados",
                value=stats['mastered_concepts'],
                help="Conceitos com >80% de acerto e 3+ tentativas"
            )
        
        with col4:
            streak = stats['streak_days']
            st.metric(
                label=f"🔥 Sequência",
                value=f"{streak} dia{'s' if streak != 1 else ''}",
                help="Dias consecutivos de estudo"
            )
    
    def _get_accuracy_trend(self, accuracy: float) -> str:
        """Retorna indicador de tendência da acurácia"""
        if accuracy >= 80:
            return "Excelente"
        elif accuracy >= 70:
            return "Bom"
        elif accuracy >= 60:
            return "Regular"
        else:
            return "Precisa melhorar"
    
    def _render_mastery_distribution(self):
        """Renderiza distribuição de níveis de domínio"""
        
        st.markdown("### 📈 Distribuição de Domínio")
        
        perf_data = self.pm.get_performance_data()
        
        if not perf_data:
            st.info("Nenhum dado disponível ainda. Comece a praticar!")
            return
        
        # Classificar por nível de domínio
        levels = {
            'Iniciante (0-40%)': 0,
            'Intermediário (40-70%)': 0,
            'Avançado (70-90%)': 0,
            'Mestre (90-100%)': 0
        }
        
        for perf in perf_data.values():
            mastery = perf['mastery_level']
            if mastery < 0.4:
                levels['Iniciante (0-40%)'] += 1
            elif mastery < 0.7:
                levels['Intermediário (40-70%)'] += 1
            elif mastery < 0.9:
                levels['Avançado (70-90%)'] += 1
            else:
                levels['Mestre (90-100%)'] += 1
        
        # Criar DataFrame
        df = pd.DataFrame(list(levels.items()), columns=['Nível', 'Questões'])
        
        # Exibir como gráfico de barras
        st.bar_chart(df.set_index('Nível'))
        
        # Mostrar tabela
        total = sum(levels.values())
        for level, count in levels.items():
            pct = (count / total * 100) if total > 0 else 0
            st.write(f"**{level}:** {count} ({pct:.1f}%)")
    
    def _render_domain_performance(self):
        """Renderiza performance por domínio"""
        
        st.markdown("### 🎯 Performance por Domínio")
        
        perf_data = self.pm.get_performance_data()
        
        if not perf_data:
            st.info("Nenhum dado disponível ainda.")
            return
        
        # Agrupar por domínio
        domain_stats = {}
        
        for perf in perf_data.values():
            domain = perf['domain']
            
            if domain not in domain_stats:
                domain_stats[domain] = {
                    'attempts': 0,
                    'correct': 0,
                    'mastery_sum': 0,
                    'count': 0
                }
            
            domain_stats[domain]['attempts'] += perf['attempts']
            domain_stats[domain]['correct'] += perf['correct']
            domain_stats[domain]['mastery_sum'] += perf['mastery_level']
            domain_stats[domain]['count'] += 1
        
        # Calcular médias
        domain_data = []
        for domain, stats in domain_stats.items():
            accuracy = (stats['correct'] / stats['attempts'] * 100) if stats['attempts'] > 0 else 0
            avg_mastery = (stats['mastery_sum'] / stats['count'] * 100) if stats['count'] > 0 else 0
            
            # Truncar nome do domínio
            short_domain = domain.split('.')[1][:20] if '.' in domain else domain[:20]
            
            domain_data.append({
                'Domínio': short_domain,
                'Acurácia (%)': round(accuracy, 1),
                'Domínio Médio (%)': round(avg_mastery, 1)
            })
        
        # Criar DataFrame
        df = pd.DataFrame(domain_data)
        
        # Exibir tabela
        st.dataframe(df, use_container_width=True, hide_index=True)
    
    def _render_weak_areas(self):
        """Renderiza áreas que precisam de mais atenção"""
        
        st.markdown("### ⚠️ Áreas que Precisam de Atenção")
        
        weak_areas = self.pm.get_weak_areas(min_attempts=2, threshold=0.6)
        
        if not weak_areas:
            st.success("🎉 Parabéns! Você não tem áreas fracas identificadas no momento.")
            return
        
        st.warning(f"Identificamos {len(weak_areas)} área(s) com dificuldade:")
        
        for i, area in enumerate(weak_areas[:5], 1):  # Mostrar top 5
            with st.expander(f"#{i} - {area['area']} ({area['weak_questions']} questões)"):
                st.write(f"**Domínio:** {area['domain']}")
                st.write(f"**Subdomínio:** {area['subdomain']}")
                st.write(f"**Questões com dificuldade:** {area['weak_questions']}")
                st.write(f"**Taxa de acerto média:** {area['average_accuracy']:.1f}%")
                
                # Barra de progresso visual
                progress = area['average_accuracy'] / 100
                st.progress(progress)
                
                st.info("💡 **Recomendação:** Revise conceitos fundamentais deste tópico antes de tentar novamente.")
    
    def _render_recommendations(self):
        """Renderiza recomendações personalizadas de estudo"""
        
        st.markdown("### 💡 Recomendações de Estudo")
        
        # Obter todas as questões (precisa ser passado de fora)
        # Por enquanto, vamos fazer recomendações baseadas no progresso
        
        stats = self.pm.get_overall_stats()
        weak_areas = self.pm.get_weak_areas()
        
        recommendations = []
        
        # Recomendação baseada em acurácia geral
        if stats['overall_accuracy'] < 60:
            recommendations.append({
                'icon': '📚',
                'title': 'Reforce os Fundamentos',
                'description': 'Sua taxa de acerto está abaixo de 60%. Considere revisar materiais teóricos antes de continuar com o quiz.'
            })
        
        # Recomendação baseada em conceitos dominados
        total_studied = stats['total_unique_questions']
        mastered = stats['mastered_concepts']
        mastery_rate = (mastered / total_studied * 100) if total_studied > 0 else 0
        
        if mastery_rate < 30 and total_studied >= 10:
            recommendations.append({
                'icon': '🎯',
                'title': 'Pratique com Consistência',
                'description': f'Você dominou {mastery_rate:.0f}% dos conceitos estudados. Tente revisar os mesmos conceitos múltiplas vezes para consolidar o aprendizado.'
            })
        
        # Recomendação baseada em áreas fracas
        if len(weak_areas) >= 3:
            recommendations.append({
                'icon': '⚠️',
                'title': 'Foque nas Áreas Fracas',
                'description': f'Você tem {len(weak_areas)} áreas com dificuldade. Dedique tempo extra para: {", ".join([a["subdomain"] for a in weak_areas[:2]])}.'
            })
        
        # Recomendação baseada em streak
        if stats['streak_days'] == 0:
            recommendations.append({
                'icon': '🔥',
                'title': 'Comece uma Sequência',
                'description': 'Estude pelo menos um conceito por dia para construir o hábito de aprendizado contínuo!'
            })
        elif stats['streak_days'] >= 7:
            recommendations.append({
                'icon': '🌟',
                'title': 'Continue Assim!',
                'description': f'Você está em uma sequência de {stats["streak_days"]} dias! Mantenha o ritmo para maximizar a retenção.'
            })
        
        # Recomendação geral se tudo estiver bem
        if not recommendations:
            recommendations.append({
                'icon': '🚀',
                'title': 'Excelente Progresso!',
                'description': 'Continue praticando regularmente e desafie-se com questões mais difíceis.'
            })
        
        # Renderizar recomendações
        for rec in recommendations:
            st.info(f"{rec['icon']} **{rec['title']}**\n\n{rec['description']}")


class QuizInterface:
    """Interface aprimorada para o quiz"""
    
    def render_question_card(self, question: Dict, performance: Dict = None):
        """
        Renderiza cartão de questão com informações contextuais
        
        Args:
            question: Dados da questão
            performance: Dados de performance do usuário (opcional)
        """
        
        # Header do cartão
        col1, col2, col3 = st.columns([2, 1, 1])
        
        with col1:
            st.markdown(f"### 🎯 {question['concept']}")
        
        with col2:
            difficulty_badge = self._get_difficulty_badge(question['difficulty'])
            st.markdown(difficulty_badge)
        
        with col3:
            if performance and performance.get('attempts', 0) > 0:
                accuracy = (performance['correct'] / performance['attempts']) * 100
                st.metric("Seu desempenho", f"{accuracy:.0f}%")
        
        # Tags
        if question.get('tags'):
            tags_html = " ".join([f"<span style='background-color: #e0e0e0; padding: 3px 8px; border-radius: 10px; font-size: 12px; margin-right: 5px;'>{tag}</span>" for tag in question['tags']])
            st.markdown(tags_html, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Contexto do domínio
        with st.expander("📚 Contexto"):
            st.write(f"**Domínio:** {question['domain']}")
            st.write(f"**Subdomínio:** {question['subdomain']}")
        
        # Questão
        st.markdown(f"#### {question['question']}")
        st.write("")
    
    def render_answer_options(self, question: Dict, key_suffix: str = ""):
        """
        Renderiza opções de resposta
        
        Args:
            question: Dados da questão
            key_suffix: Sufixo para key do Streamlit
        
        Returns:
            Opção escolhida pelo usuário
        """
        
        choice = st.radio(
            "Escolha a alternativa correta:",
            options=list(question['options'].keys()),
            format_func=lambda x: f"{x}) {question['options'][x]}",
            index=None,
            key=f"choice_{question['id']}_{key_suffix}"
        )
        
        return choice
    
    def render_feedback(self, question: Dict, user_choice: str, is_correct: bool, feedback_data: Dict):
        """
        Renderiza feedback detalhado após resposta
        
        Args:
            question: Dados da questão
            user_choice: Escolha do usuário
            is_correct: Se a resposta foi correta
            feedback_data: Dados adicionais de feedback
        """
        
        st.write("")
        st.markdown("---")
        
        if is_correct:
            st.success("✅ **Resposta Correta!**")
            
            # Estatísticas de progresso
            col1, col2, col3 = st.columns(3)
            
            with col1:
                accuracy = feedback_data['accuracy'] * 100
                st.metric("Sua Taxa de Acerto", f"{accuracy:.0f}%")
            
            with col2:
                mastery = feedback_data['mastery_level'] * 100
                st.metric("Nível de Domínio", f"{mastery:.0f}%")
            
            with col3:
                next_days = feedback_data['next_review_days']
                st.metric("Revisar em", f"{next_days} dia{'s' if next_days != 1 else ''}")
            
            # Badge de maestria
            if feedback_data.get('is_mastered'):
                st.balloons()
                st.success("🌟 **Parabéns! Você dominou este conceito!**")
        
        else:
            st.error("❌ **Resposta Incorreta**")
            st.markdown(f"**Resposta correta:** {question['answer']}) {question['options'][question['answer']]}")
            st.info("💪 Não desanime! Revisar erros é fundamental para o aprendizado.")
        
        # Sempre mostrar explicação
        with st.expander("📖 Explicação Detalhada", expanded=not is_correct):
            st.markdown(question['explanation'])
        
        st.markdown("---")
    
    def _get_difficulty_badge(self, difficulty: str) -> str:
        """Retorna badge HTML de dificuldade"""
        
        badges = {
            'easy': '<span style="background-color: #4CAF50; color: white; padding: 5px 12px; border-radius: 15px; font-size: 14px;">🟢 Fácil</span>',
            'medium': '<span style="background-color: #FF9800; color: white; padding: 5px 12px; border-radius: 15px; font-size: 14px;">🟡 Médio</span>',
            'hard': '<span style="background-color: #F44336; color: white; padding: 5px 12px; border-radius: 15px; font-size: 14px;">🔴 Difícil</span>'
        }
        
        return badges.get(difficulty, '<span style="background-color: #9E9E9E; color: white; padding: 5px 12px; border-radius: 15px; font-size: 14px;">⚪ Não definido</span>')

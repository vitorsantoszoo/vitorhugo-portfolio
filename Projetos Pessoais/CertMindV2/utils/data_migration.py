"""
Script de migração de dados - Remove duplicatas e enriquece questões
Transforma o banco de questões antigo no novo formato otimizado
"""

import json
import os
from typing import Dict, List, Set

class DataMigration:
    """Classe para migrar dados do formato antigo para o novo"""
    
    def __init__(self):
        self.concepts_seen: Set[str] = set()
        self.question_bank: List[Dict] = []
        
        # Mapeamento de conceitos para explicações (expandível)
        self.explanations = self._load_explanations()
        self.difficulty_map = self._generate_difficulty_map()
        self.tags_map = self._generate_tags_map()
    
    def _load_explanations(self) -> Dict[str, str]:
        """Retorna explicações para conceitos conhecidos"""
        return {
            "tethering": "Tethering permite que o smartphone funcione como hotspot móvel, compartilhando sua conexão de dados com outros dispositivos via Wi-Fi, Bluetooth ou USB. É útil quando não há Wi-Fi disponível.",
            
            "ssd_interno": "O SSD (Solid State Drive) interno é o componente responsável pelo armazenamento permanente de dados, incluindo sistema operacional, aplicativos e arquivos do usuário. É mais rápido que HDDs tradicionais.",
            
            "ram_mobile": "RAM (Random Access Memory) é a memória volátil que armazena temporariamente dados e processos em execução. Quanto mais RAM, mais aplicativos podem rodar simultaneamente sem travamentos.",
            
            "gps": "GPS (Global Positioning System) usa satélites para determinar a localização geográfica precisa do dispositivo. É essencial para navegação, mapeamento e aplicativos baseados em localização.",
            
            "nfc": "NFC (Near Field Communication) permite comunicação sem fio de curto alcance (até 10cm). Usado em pagamentos móveis, pareamento rápido de dispositivos e compartilhamento de dados.",
            
            "bluetooth": "Bluetooth é uma tecnologia de comunicação sem fio de curto alcance que permite conexão entre dispositivos para compartilhamento de dados, áudio e controle remoto.",
            
            "wifi": "Wi-Fi é um padrão de rede sem fio que permite acesso à internet e comunicação entre dispositivos em uma rede local através de ondas de rádio.",
            
            "lightning": "Lightning é o conector proprietário da Apple usado em iPhones e iPads para carregamento e transferência de dados. Substituiu o conector de 30 pinos mais antigo.",
            
            "usb_c": "USB-C é um conector reversível universal que suporta transferência rápida de dados, carregamento rápido e saída de vídeo. É o padrão atual para Android e dispositivos modernos.",
            
            "micro_usb": "Micro-USB foi o padrão anterior para Android, menor que USB-A mas não reversível. Está sendo gradualmente substituído por USB-C.",
        }
    
    def _generate_difficulty_map(self) -> Dict[str, str]:
        """Mapeia conceitos para níveis de dificuldade"""
        return {
            "tethering": "easy",
            "ssd_interno": "easy",
            "ram_mobile": "easy",
            "gps": "easy",
            "nfc": "medium",
            "bluetooth": "easy",
            "wifi": "easy",
            "lightning": "easy",
            "usb_c": "easy",
            "micro_usb": "easy",
        }
    
    def _generate_tags_map(self) -> Dict[str, List[str]]:
        """Mapeia conceitos para tags relevantes"""
        return {
            "tethering": ["conectividade", "mobile", "hotspot", "compartilhamento"],
            "ssd_interno": ["hardware", "armazenamento", "memória"],
            "ram_mobile": ["hardware", "memória", "performance"],
            "gps": ["localização", "navegação", "satélite"],
            "nfc": ["conectividade", "pagamento", "wireless"],
            "bluetooth": ["conectividade", "wireless", "pareamento"],
            "wifi": ["rede", "wireless", "internet"],
            "lightning": ["hardware", "conector", "apple", "carregamento"],
            "usb_c": ["hardware", "conector", "universal", "carregamento"],
            "micro_usb": ["hardware", "conector", "android", "carregamento"],
        }
    
    def _extract_concept_key(self, question_stem: str) -> str:
        """Extrai identificador único do conceito da questão"""
        # Remove variações de pergunta (parte depois dos dois pontos)
        base = question_stem.split(':')[0].strip().lower()
        
        # Simplifica para criar chave única
        key = base.replace("'", "").replace('"', '')
        key = ''.join(c if c.isalnum() or c.isspace() else '' for c in key)
        key = '_'.join(key.split())
        
        return key
    
    def _get_explanation(self, question_data: Dict, concept_key: str) -> str:
        """Gera explicação para a questão"""
        
        # Buscar explicação pré-definida
        for known_concept, explanation in self.explanations.items():
            if known_concept in concept_key:
                return explanation
        
        # Explicação genérica baseada na resposta correta
        correct_answer = question_data['answer']
        correct_text = question_data['options'][correct_answer]
        
        return f"A alternativa correta é '{correct_text}'. Este conceito está relacionado ao domínio '{question_data['domain']}' e é importante para a certificação CompTIA A+."
    
    def _get_difficulty(self, concept_key: str, domain: str) -> str:
        """Determina nível de dificuldade"""
        
        # Buscar dificuldade conhecida
        for known_concept, difficulty in self.difficulty_map.items():
            if known_concept in concept_key:
                return difficulty
        
        # Heurística baseada no domínio
        if "solução de problemas" in domain.lower():
            return "hard"
        elif "virtualização" in domain.lower() or "segurança" in domain.lower():
            return "medium"
        else:
            return "easy"
    
    def _get_tags(self, concept_key: str, domain: str, subdomain: str) -> List[str]:
        """Gera tags relevantes"""
        
        tags = []
        
        # Tags conhecidas
        for known_concept, concept_tags in self.tags_map.items():
            if known_concept in concept_key:
                tags.extend(concept_tags)
        
        # Tags baseadas no domínio
        domain_lower = domain.lower()
        if "móvel" in domain_lower or "mobile" in domain_lower:
            tags.append("mobile")
        if "rede" in domain_lower:
            tags.append("networking")
        if "hardware" in domain_lower:
            tags.append("hardware")
        if "segurança" in domain_lower:
            tags.append("security")
        if "sistema" in domain_lower:
            tags.append("os")
        
        return list(set(tags))  # Remove duplicatas
    
    def process_question_bank(self, old_data: Dict, exam_prefix: str) -> Dict:
        """
        Processa banco de questões removendo duplicatas e enriquecendo dados
        
        Args:
            old_data: Dados no formato antigo
            exam_prefix: Prefixo do exame (core1 ou core2)
        
        Returns:
            Dados no novo formato
        """
        
        concepts_seen = set()
        new_questions = []
        
        for question in old_data['questions']:
            # Extrair conceito único
            concept_key = self._extract_concept_key(question['stem_md'])
            
            # Pular duplicatas
            full_key = f"{question['domain']}_{question['subdomain']}_{concept_key}"
            if full_key in concepts_seen:
                continue
            
            concepts_seen.add(full_key)
            
            # Criar ID limpo
            # Extrair número do domínio e subdomínio
            domain_num = question['domain'].split('.')[0]
            subdomain_parts = question['subdomain'].split('.')
            subdomain_num = subdomain_parts[0] if len(subdomain_parts) > 0 else "0"
            
            new_id = f"{domain_num}.{subdomain_num}_{concept_key}"
            
            # Limpar pergunta (remover sufixos de variação)
            clean_question = question['stem_md'].split(':')[0].strip()
            if not clean_question.endswith('?'):
                clean_question += '?'
            
            # Extrair conceito para display
            concept_display = clean_question.replace('?', '').strip()
            if len(concept_display) > 100:
                # Se muito longo, extrair primeira frase
                concept_display = concept_display.split('.')[0]
            
            # Enriquecer questão
            enriched_question = {
                "id": new_id,
                "domain": question['domain'],
                "subdomain": question['subdomain'],
                "concept": concept_display,
                "question": clean_question,
                "options": question['options'],
                "answer": question['answer'],
                "explanation": self._get_explanation(question, concept_key),
                "difficulty": self._get_difficulty(concept_key, question['domain']),
                "tags": self._get_tags(concept_key, question['domain'], question['subdomain'])
            }
            
            new_questions.append(enriched_question)
        
        return {
            "exam_name": f"CompTIA A+ {exam_prefix.upper()}",
            "version": "2.0",
            "last_updated": "2025-11-17",
            "total_questions": len(new_questions),
            "questions": new_questions
        }
    
    def migrate_all_data(self, data_dir: str):
        """Migra todos os arquivos de dados"""
        
        print("🚀 Iniciando migração de dados...")
        print("=" * 60)
        
        # Migrar Core 1
        print("\n📦 Processando Core 1...")
        with open(os.path.join(data_dir, "core1_questions_expanded.json"), 'r', encoding='utf-8') as f:
            core1_old = json.load(f)
        
        core1_new = self.process_question_bank(core1_old, "core1")
        
        with open(os.path.join(data_dir, "core1_questions_v2.json"), 'w', encoding='utf-8') as f:
            json.dump(core1_new, f, indent=2, ensure_ascii=False)
        
        print(f"   ✅ Core 1: {len(core1_old['questions'])} → {core1_new['total_questions']} questões")
        print(f"   📉 Reduziu {len(core1_old['questions']) - core1_new['total_questions']} duplicatas")
        
        # Migrar Core 2
        print("\n📦 Processando Core 2...")
        with open(os.path.join(data_dir, "core2_questions_expanded.json"), 'r', encoding='utf-8') as f:
            core2_old = json.load(f)
        
        core2_new = self.process_question_bank(core2_old, "core2")
        
        with open(os.path.join(data_dir, "core2_questions_v2.json"), 'w', encoding='utf-8') as f:
            json.dump(core2_new, f, indent=2, ensure_ascii=False)
        
        print(f"   ✅ Core 2: {len(core2_old['questions'])} → {core2_new['total_questions']} questões")
        print(f"   📉 Reduziu {len(core2_old['questions']) - core2_new['total_questions']} duplicatas")
        
        # Criar novo arquivo de progresso
        print("\n📊 Criando novo sistema de progresso...")
        new_progress = {
            "version": "2.0",
            "user_id": "default_user",
            "last_updated": "2025-11-17T23:20:00",
            "performance": {}
        }
        
        with open(os.path.join(data_dir, "progress_v2.json"), 'w', encoding='utf-8') as f:
            json.dump(new_progress, f, indent=2, ensure_ascii=False)
        
        print("   ✅ Sistema de progresso inicializado")
        
        print("\n" + "=" * 60)
        print("✨ Migração concluída com sucesso!")
        print(f"📁 Novos arquivos criados em: {data_dir}")
        print("   - core1_questions_v2.json")
        print("   - core2_questions_v2.json")
        print("   - progress_v2.json")


if __name__ == "__main__":
    migrator = DataMigration()
    migrator.migrate_all_data("data")

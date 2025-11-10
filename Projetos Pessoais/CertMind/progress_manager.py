import json
import os

PROGRESS_PATH = os.path.join("data", "progress.json")

def load_progress():
    if not os.path.exists(PROGRESS_PATH):
        return {}
    with open(PROGRESS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_progress(progress: dict):
    with open(PROGRESS_PATH, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=4, ensure_ascii=False)


def mark_as_seen(exam: str, domain: str, sub: str, item: str):
    progress = load_progress()

    # criar estrutura se não existir ainda
    if exam not in progress:
        progress[exam] = {}
    if domain not in progress[exam]:
        progress[exam][domain] = {}
    if sub not in progress[exam][domain]:
        progress[exam][domain][sub] = set()

    # convert list to set if loaded from json
    if isinstance(progress[exam][domain][sub], list):
        progress[exam][domain][sub] = set(progress[exam][domain][sub])

    progress[exam][domain][sub].add(item)

    # salvar convertendo set → list
    progress[exam][domain][sub] = list(progress[exam][domain][sub])
    save_progress(progress)

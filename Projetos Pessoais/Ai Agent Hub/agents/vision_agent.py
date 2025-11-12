# agents/vision_agent.py
import cv2
import numpy as np

class VisionAgent:
    def __init__(self):
        pass

    def analyze(self, image_path: str):
        """Analisa uma imagem e retorna informações básicas."""
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        if image is None:
            return {"status": "erro", "msg": "Imagem não encontrada"}

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

        return {
            "status": "ok",
            "objetos_detectados": num_labels - 1,
            "dimensoes": image.shape[:2],
        }

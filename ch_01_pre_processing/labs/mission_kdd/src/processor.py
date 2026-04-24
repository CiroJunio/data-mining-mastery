import pandas as pd
import numpy as np

class KDDProcessor:
    def __init__(self, file_a, file_b):
        self.df_a = pd.read_csv(file_a)
        self.df_b = pd.read_csv(file_b)
        self.merged_df = None

    def integrate_entities(self):
        """Tarefa: Resolver Problema de Identificação de Entidade"""
        
        pass

    def clean_missing_values(self):
        """Tarefa: Imputação manual por média da classe [cite: 125, 1548]"""
        pass

    def normalize_data(self):
        """Tarefa: Implementar Min-Max manualmente [cite: 289, 1753]"""
        # v' = (v - minA)/(maxA - minA) * (new_maxA - new_minA) + new_minA
        pass

    def calculate_similarity(self, idx1, idx2):
        """Tarefa: Distância Euclidiana entre duas instâncias [cite: 1251]"""
        pass
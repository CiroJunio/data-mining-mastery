import pandas as pd
import numpy as np
import argparse
import os

def generate_data(size=40):
    os.makedirs('data/raw', exist_ok=True)
    
    # Loja Matrix (BRL)
    df_a = pd.DataFrame({
        'id_cliente': range(1, size + 1),
        'gasto_anual_brl': np.random.choice([np.nan, 500, 1500, 10000, 50000], size),
        'idade': np.random.choice([np.nan, 18, 25, 40, 99], size),
        'categoria_fidelidade': np.random.choice(['Bronze', 'Prata', 'Ouro'], size)
    })
    
    # Loja Phoenix (USD) - Inconsistência de nomes 
    df_b = pd.DataFrame({
        'user_no': range(size + 1, (size * 2) + 1),
        'total_spend_usd': np.random.choice([np.nan, 100, 300, 2000, 8000], size),
        'age': np.random.choice([np.nan, 20, 30, 50, 120], size), # Outlier 120
        'loyalty_score': np.random.choice(['Bronze', 'Prata', 'Ouro'], size)
    })
    
    df_a.to_csv('data/raw/store_matrix.csv', index=False)
    df_b.to_csv('data/raw/store_phoenix.csv', index=False)
    print(f"Dataset gerado com {size*2} registros totais.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--size', type=int, default=20)
    args = parser.parse_args()
    generate_data(args.size)
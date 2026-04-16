import numpy as np

def calculate_inventory(df):
    df['safety_stock'] = df['forecast'] * 0.2
    df['reorder_point'] = df['forecast'] + df['safety_stock']
    
    return df[['date', 'forecast', 'safety_stock', 'reorder_point']]
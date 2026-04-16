import pandas as pd
import numpy as np

def load_data():
    dates = pd.date_range(start="2023-01-01", periods=200)
    
    data = pd.DataFrame({
        "date": dates,
        "sales": np.random.randint(20, 100, size=len(dates))
    })
    
    return data
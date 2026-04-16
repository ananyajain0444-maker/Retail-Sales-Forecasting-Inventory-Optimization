def create_features(df):
    df['lag_1'] = df['sales'].shift(1)
    df['lag_7'] = df['sales'].shift(7)
    
    df = df.dropna()
    return df
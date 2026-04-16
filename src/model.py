from sklearn.ensemble import RandomForestRegressor

def train_model(df):
    X = df[['lag_1', 'lag_7']]
    y = df['sales']
    
    model = RandomForestRegressor()
    model.fit(X, y)
    
    return model

def predict(model, df):
    X = df[['lag_1', 'lag_7']]
    df['forecast'] = model.predict(X)
    
    return df
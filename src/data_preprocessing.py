import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(df):
    features = df.drop(columns=['Year', 'Cocoa_Yield'])
    target = df['Cocoa_Yield']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)
    return scaled_features, target, scaler
import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_data(df):
    features = df.drop(columns=['Year', 'Cocoa_Yield'])
    reduced_features = features.drop(columns=['Min_RH', 'Max_RH', 'Rainfall_mm', 'Wind_Speed_ms', 'Max_Temp_C'])
    target = df['Cocoa_Yield']
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(reduced_features)
    return scaled_features, target, scaler
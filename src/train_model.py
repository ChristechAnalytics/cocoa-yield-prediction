import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from data_preprocessing import load_data, preprocess_data

def train_and_save_model(data_path, model_path):
    df = load_data(data_path)
    X, y, scaler = preprocess_data(df)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    joblib.dump(scaler, 'src/scaler.pkl')

if __name__ == '__main__':
    train_and_save_model('data/cocoa_climate_ikom_2013_2022.csv', 'src/cocoa_model.pkl')
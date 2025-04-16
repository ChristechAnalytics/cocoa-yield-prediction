import joblib
from sklearn.metrics import mean_squared_error, r2_score
from data_preprocessing import load_data, preprocess_data

def evaluate_model(data_path, model_path):
    df = load_data(data_path)
    X, y, _ = preprocess_data(df)
    model = joblib.load(model_path)
    y_pred = model.predict(X)
    print(f"RMSE: {mean_squared_error(y, y_pred, squared=False):.2f}")
    print(f"R² Score: {r2_score(y, y_pred):.2f}")

if __name__ == '__main__':
    evaluate_model('data/cocoa_climate_ikom_2013_2022.csv', 'src/cocoa_model.pkl')
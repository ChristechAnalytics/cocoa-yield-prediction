# Cocoa Yield Prediction Based on Climate Variables - Ikom, Nigeria

This project predicts annual cocoa yield using climatic data in Ikom LGA, Cross River State.

## Features
- Dataset: 2013–2022 climate data
- Models: Random Forest, Linear Regression (extendable)
- Web App: Built with Streamlit for easy predictions

## Setup
```bash
git clone <repo-url>
cd cocoa-yield-prediction
pip install -r requirements.txt
python src/train_model.py
streamlit run app/streamlit_app.py
```

## Dataset
Stored in `data/cocoa_climate_ikom_2013_2022.csv`

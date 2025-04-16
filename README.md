![Cocoa Image](https://github.com/user-attachments/assets/8e35ed42-f6d6-4a79-abaa-19d502e8a4ff)

# 🌱 Cocoa Yield Prediction Based on Climate Variables - Ikom, Nigeria

## 📌 Project Objective
Predict annual cocoa yield in Ikom Local Government Area, Cross River State, using climate variables such as rainfall, temperature, humidity, wind speed, and solar radiation.

## 🧠 Background
This project is based on a real dataset from my undergraduate thesis, which explored the impact of climate variability on cocoa yield in Nigeria’s cocoa-producing region, Ikom LGA. Cocoa is highly sensitive to climate, and understanding these patterns is vital for sustainable agriculture.

## 📂 Project Structure
```bash
├── data/                  # Raw dataset (2013–2022 climate + cocoa yield)
├── notebooks/             # Jupyter notebook for EDA and modeling
├── src/                   # Python scripts for preprocessing, training, evaluation
├── app/                   # Streamlit web app
├── README.md              # This file
├── requirements.txt       # Project dependencies
└── .gitignore             # Standard gitignore rules
```

## 🚀 Features
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data scaling using `StandardScaler`
- Regression models: Random Forest, Linear Regression
- Feature importance visualizations
- Streamlit-based prediction interface

## 📈 Sample Prediction Output
![Sample Prediction Screenshot](images/Screenshot%20(138).png)

## 🛠️ How to Run the Project
```bash
# Clone the repository
https://github.com/ChristechAnalytics/cocoa-yield-prediction.git

# Navigate into the directory
cd cocoa-yield-prediction

# Install dependencies
pip install -r requirements.txt

# Train the model
python src/train_model.py

# Run the app
streamlit run app/streamlit_app.py
```

## 🔬 Model Insights
- Top influencing features: **Solar Radiation** and **Minimum Temperature**
- Models evaluated using RMSE and R²
- Model performance is suitable for guiding cocoa production decisions

## 📊 Dataset
Manually curated from research logs and climate archives:
- **Years:** 2013–2022
- **Location:** Ikom LGA, Cross River State, Nigeria
- **Source:** Cross River State Ministry of Agriculture logbooks & remote sensing datasets (CRU, TRMM, ERA-Interim)

## 🙋 About Me
I’m a meteorologist and data scientist passionate about using machine learning for sustainability. This project bridges my background in meteorology with practical data science applications.

---

> ⭐ _This project demonstrates the power of combining research with machine learning to solve real-world agricultural problems._

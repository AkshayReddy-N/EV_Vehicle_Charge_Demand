# 🚗 Electric Vehicle (EV) Adoption Forecast App

This Streamlit app forecasts electric vehicle (EV) adoption for counties in Washington State using a trained machine learning model.

## 🔧 Project Features

- Interactive EV adoption forecasting per selected county
- Comparison of forecast trends across up to 3 counties
- 3-year prediction using historical trends and time-series features
- Clean UI with dark-themed graphs and gradient background

## 📁 Files Included

- `app.py`: Streamlit frontend application
- `forecasting_ev_model.pkl`: Trained machine learning model (Joblib format)
- `preprocessed_ev_data.csv`: Cleaned dataset with historical EV stats
- `ev-car-factory.jpg`: Background banner image
- `README.md`: Project overview

## 🚀 How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

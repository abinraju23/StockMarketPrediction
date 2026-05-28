<!DOCTYPE html>

# Stock Market Prediction 📈

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=00F5D4&center=true&vCenter=true&width=620&lines=Stock+Price+Prediction+with+ML+%26+DL;AAPL+%7C+TSLA+%7C+AMZN+%7C+RELIANCE+%7C+SBIN;LSTM+%7C+Random+Forest+%7C+Scikit-learn;Flask+Web+App+Deployment;Multi-Market+%7C+Multi-Stock+Coverage" alt="Typing Animation" />
</div>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B"/>
  <img alt="TensorFlow" src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white"/>
  <img alt="Keras" src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white"/>
  <img alt="Scikit-learn" src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white"/>
  <img alt="Flask" src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img alt="Jupyter" src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white"/>
</p>

<p align="center">
  <img alt="Stocks" src="https://img.shields.io/badge/Stocks_Covered-8-00F5D4?style=flat-square"/>
  <img alt="Markets" src="https://img.shields.io/badge/Markets-US_%7C_UK_%7C_IN-FEE440?style=flat-square"/>
  <img alt="Deployed" src="https://img.shields.io/badge/Deployed-Flask_Web_App-00BBF9?style=flat-square"/>
  <img alt="License" src="https://img.shields.io/badge/license-MIT-00F5D4?style=flat-square"/>
</p>

---

## 📌 Project Overview

A **multi-stock, multi-market machine learning pipeline** that predicts stock prices across **US, UK, and Indian equity markets** using classical ML and deep learning (LSTM) models — packaged and deployed as a **Flask web application**.

Each stock has its own dedicated Jupyter Notebook covering the full workflow: data ingestion, preprocessing, feature engineering, model training, evaluation, and inference. The Flask app exposes these models through a clean web interface for interactive predictions.

---

## 🌐 Stocks Covered

<div align="center">

| Ticker | Company | Exchange | Sector |
|---|---|---|---|
| `AAPL` | Apple Inc. | NASDAQ | Technology |
| `AMZN` | Amazon.com Inc. | NASDAQ | Consumer / Cloud |
| `TSLA` | Tesla Inc. | NASDAQ | EV / Energy |
| `AZN` | AstraZeneca PLC | LSE / NASDAQ | Pharmaceuticals |
| `ULVR` | Unilever PLC | LSE | FMCG |
| `RELIANCE` | Reliance Industries Ltd. | NSE / BSE | Conglomerate |
| `SBIN` | State Bank of India | NSE / BSE | Banking |
| `TATAMOTORS` | Tata Motors Ltd. | NSE / BSE | Automotive |

</div>

---

## ✨ Key Features

<div align="center">

| 📥 **Data Pipeline** | 🤖 **ML & DL Models** | 🖥️ **Deployment** |
|---|---|---|
| Historical price ingestion (yfinance) | LSTM (Long Short-Term Memory) | Flask web application |
| OHLCV feature engineering | Random Forest Regressor | Per-stock prediction routes |
| Rolling averages & lag features | Linear Regression baseline | Interactive input forms |
| Train / validation / test splits | Scikit-learn model comparison | Model inference on live input |

</div>

---

## 🧠 ML Pipeline (Per Stock)

```
1. Data Ingestion
   └── yfinance API → historical OHLCV data

2. Preprocessing
   ├── Missing value handling
   ├── Normalisation / MinMax scaling
   └── Sequence construction for LSTM (look-back window)

3. Feature Engineering
   ├── Lag features: Close(t-1), Close(t-5), Close(t-10)
   ├── Rolling statistics: 7-day MA, 30-day MA, volatility
   └── Volume-weighted signals

4. Model Training
   ├── Baseline: Linear Regression
   ├── Ensemble: Random Forest Regressor
   └── Deep Learning: LSTM (via Keras / TensorFlow)

5. Evaluation
   ├── RMSE · MAE · R²
   └── Actual vs. Predicted price plots

6. Serialisation
   └── Trained models saved as .pkl / .h5 for Flask inference
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

**1. Clone the repository**
```sh
git clone https://github.com/abinraju23/StockMarketPrediction.git
cd StockMarketPrediction
```

**2. Install dependencies**
```sh
pip install -r requirements.txt
```

**3. Run individual notebooks**
```sh
jupyter notebook
# Open the notebook for your chosen stock, e.g. AAPL_Prediction.ipynb
```

**4. Launch the Flask web app**
```sh
python app.py
# Navigate to http://localhost:5000
```

---

## 📁 Repository Structure

```
StockMarketPrediction/
│
├── 📂 notebooks/
│   ├── AAPL_Prediction.ipynb
│   ├── AMZN_Prediction.ipynb
│   ├── AZN_Prediction.ipynb
│   ├── RELIANCE_Prediction.ipynb
│   ├── SBIN_Prediction.ipynb
│   ├── TATAMOTORS_Prediction.ipynb
│   ├── TSLA_Prediction.ipynb
│   └── ULVR_Prediction.ipynb
│
├── 📂 models/
│   └── *.pkl / *.h5                  # Serialised trained models
│
├── 📂 templates/
│   ├── index.html                    # Landing page
│   └── predict.html                  # Prediction result page
│
├── 📂 static/
│   └── css/styles.css
│
├── app.py                            # Flask application
├── requirements.txt
└── README.md
```

---

## 📦 Dependencies

```txt
pandas >= 2.0
numpy >= 1.26
scikit-learn >= 1.4
tensorflow >= 2.14
keras >= 2.14
yfinance >= 0.2.40
flask >= 3.0
matplotlib >= 3.8
seaborn >= 0.13
jupyter >= 1.0
```

```sh
pip install -r requirements.txt
```

---

## 📈 Sample Output

```
🔮 PREDICTION RESULT — AAPL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Model       : LSTM (look-back = 60 days)
Input Date  : 2024-06-01
Predicted   : $191.42
Actual      : $189.87
RMSE        : 3.21  |  MAE: 2.74  |  R²: 0.94
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 👤 Author

**Abin Raju**
MSc Data Analytics — Dublin Business School (September 2025 cohort)
Prior internship: IDatalytics — LSTM stock prediction & KNN attrition modelling

<p>
  <a href="https://www.linkedin.com/in/abinraju2308">
    <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  <a href="https://github.com/abinraju23/StockMarketPrediction">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

---

## ⚠️ Disclaimer

This project is developed for **educational and research purposes only**. Stock price predictions generated by these models are not financial advice and should not be used as the basis for real investment decisions. Past performance and model accuracy on historical data do not guarantee future results.

---

<div align="center">
  <sub>Built with Python · TensorFlow · Keras · Scikit-learn · Flask · yfinance</sub><br/>
  <sub>© 2026 Abin Raju · MSc Data Analytics · Dublin Business School</sub>
</div>

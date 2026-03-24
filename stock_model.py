import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#MODEL 1: Linear Regression

print("Running Model 1: Linear Regression")

#Get last 60 days
data1 = yf.download('AAPL', period='60d')
data1 = data1[['Close']]
data1['Days'] = np.arange(len(data1))

#Train on first 30 days
train1 = data1.iloc[:30]
X1 = train1[['Days']]
y1 = train1['Close']

model1 = LinearRegression()
model1.fit(X1, y1)

#Predict next 30 days
future1 = np.arange(30, 60).reshape(-1, 1)
pred1 = model1.predict(future1)

# Plot
plt.figure(figsize=(12,6))
plt.plot(train1['Days'], train1['Close'], label='Actual (30 days)', color='blue')
plt.plot(future1, pred1, label='Linear Regression (straight line)', linestyle='dashed', color='red', linewidth=2)
plt.legend()
plt.title('Model 1: Linear Regression - 30 Day Forecast')
plt.xlabel('Days')
plt.ylabel('Price (USD)')
plt.savefig('prediction_linear.png')
plt.show()

#MODEL 2: Polynomial Regression 

print("Running Model 2: Polynomial Regression")

#Get last 60 days
data2 = yf.download('AAPL', period='60d')
data2 = data2[['Close']]
data2['Days'] = np.arange(len(data2))

#Train on first 30 days
train2 = data2.iloc[:30]
X2 = train2[['Days']]
y2 = train2['Close']

#Polynomial transformation
poly = PolynomialFeatures(degree=2)
X2_poly = poly.fit_transform(X2)

#Train model
model2 = LinearRegression()
model2.fit(X2_poly, y2)

#Predict next 30 days
future2 = np.arange(30, 60).reshape(-1, 1)
future2_poly = poly.transform(future2)
pred2 = model2.predict(future2_poly)

#Plot
plt.figure(figsize=(12,6))
plt.plot(train2['Days'], train2['Close'], label='Actual (30 days)', color='blue')
plt.plot(future2, pred2, label='Polynomial Regression (curved)', linestyle='dashed', color='red', linewidth=2)
plt.legend()
plt.title('Model 2: Polynomial Regression - Curved AI Forecast')
plt.xlabel('Days')
plt.ylabel('Price (USD)')
plt.savefig('prediction_polynomial.png')
plt.show()

#MODEL 3: Moving Average 

print("Running Model 3: Moving Average")

#Get last 60 days
data3 = yf.download('AAPL', period='60d')
data3 = data3[['Close']]

#Calculate 5-day moving average
data3['MA_5'] = data3['Close'].rolling(window=5).mean()

#Plot
plt.figure(figsize=(12,6))
plt.plot(data3['Close'], label='Actual Price', color='blue', alpha=0.7)
plt.plot(data3['MA_5'], label='5-Day Moving Average (Trend)', color='red', linewidth=2)
plt.legend()
plt.title('Model 3: Moving Average - Trend Analysis')
plt.xlabel('Days')
plt.ylabel('Price (USD)')
plt.savefig('prediction_moving_average.png')
plt.show()







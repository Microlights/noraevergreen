import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split  
from sklearn.linear_model import LinearRegression  
from sklearn.metrics import mean_squared_error, r2_score  
  
# 读取数据  
data = pd.read_csv('data.csv')  
  
# 查看数据摘要  
print(data.describe())  
  
# 绘制数据分布图  
plt.hist(data['column_name'], bins=20, alpha=0.5)  
plt.xlabel('Column Name')  
plt.ylabel('Frequency')  
plt.show()  
  
# 将数据分为训练集和测试集  
X = data.drop('target_column', axis=1)  
y = data['target_column']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)  
  
# 训练线性回归模型  
model = LinearRegression()  
model.fit(X_train, y_train)  
  
# 预测测试集结果  
y_pred = model.predict(X_test)  
  
# 评估模型性能  
mse = mean_squared_error(y_test, y_pred)  
r2 = r2_score(y_test, y_pred)  
print(f'Mean Squared Error: {mse}')  
print(f'R2 Score: {r2}')

import pandas as pd  
import matplotlib.pyplot as plt  
  
# 读取包含就业趋势数据的CSV文件  
data = pd.read_csv('employment_trends.csv')  
  
# 处理数据  
years = data['年份']  
employment = data['就业人数']  
unemployment = data['失业人数']  
  
# 计算就业率和失业率  
employment_rate = employment / (employment + unemployment)  
unemployment_rate = unemployment / (employment + unemployment)  
  
# 绘制就业和失业趋势图  
plt.plot(years, employment, label='就业人数')  
plt.plot(years, unemployment, label='失业人数')  
plt.plot(years, employment_rate, label='就业率')  
plt.plot(years, unemployment_rate, label='失业率')  
plt.title('工作就业趋势')  
plt.xlabel('年份')  
plt.ylabel('人数')  
plt.legend()  
plt.show()

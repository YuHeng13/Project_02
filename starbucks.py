import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
%matplotlib inline

df = pd.read_csv('Starbucks satisfactory survey_01.csv')
df.head()
df.info()#檢查發現有兩個空值 要怎麼處裡?
print(df.isnull().sum())
df.columns
df.nunique()

#欄位重新命名
rename_dict = {
    '1. Your Gender' : 'Gender',
    '2. Your Age' : 'Age',     
    '3. Are you currently....?' : 'Profession',
    '4. What is your annual income?' : 'Income',
    '5. How often do you visit Starbucks?' : 'Visit Frequency',
    '6. How do you usually enjoy Starbucks?' : 'Prefered Form of Consumption',
    '7. How much time do you normally  spend during your visit?' : 'Time Spent on Visit',
    "8. The nearest Starbucks's outlet to you is...?" : 'Distance to Store',
    '9. Do you have Starbucks membership card?' : 'Membership',
    '10. What do you most frequently purchase at Starbucks?' : 'Most consumed Product',
    '11. On average, how much would you spend at Starbucks per visit?' : 'Spend per Visit',
    '12. How would you rate the quality of Starbucks compared to other brands (Coffee Bean, Old Town White Coffee..) to be:' : 'Quality Rate',
    '13. How would you rate the price range at Starbucks?' : 'Price Range Rate',
    '14. How important are sales and promotions in your purchase decision?' : 'Sales and Promotion Importance',
    '15. How would you rate the ambiance at Starbucks? (lighting, music, etc...)' : 'Ambiance Rate',
    '16. You rate the WiFi quality at Starbucks as..' : 'WiFi Quality Rate',
    '17. How would you rate the service at Starbucks? (Promptness, friendliness, etc..)' : 'Service Rate',
    '18. How likely you will choose Starbucks for doing business meetings or hangout with friends?' : 'Likely for Meetings or Hangouts',
    '19. How do you come to hear of promotions at Starbucks? Check all that apply.' : 'Form of communication to Promotions',
    '20. Will you continue buying at Starbucks?' : 'Recurrent Costumer'
            }
df = df.rename(rename_dict,axis=1)
df.columns

#先看客戶男女比例及年齡分佈柱狀圖
gender_age = df.groupby(['Gender', 'Age']).size().unstack()

gender_age.plot(kind='bar', stacked=True, figsize=(8, 6), colormap='viridis')
plt.title('Customer Distribution by Gender and Age', fontsize=14)
plt.xlabel('Gender', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.xticks(rotation=0)
plt.legend(title='Age Group', fontsize=10)
plt.tight_layout()
plt.show()


plt.bar(feature ='Profession', figsize = (10,8))

#消費頻率圓餅圖
visit_counts = df['Visit Frequency'].value_counts()

plt.figure(figsize=(8, 6))
visit_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'orange', 'pink'])
plt.title('Visit Frequency Distribution', fontsize=14)
plt.ylabel('')
plt.tight_layout()
plt.show()


# 繪製分組柱狀圖
profession_distance.plot(kind='bar', figsize=(12, 8), colormap='Set2', width=0.8)
# 添加標題與標籤
plt.title('Profession Distribution by Store Distance', fontsize=16)
plt.xlabel('Profession', fontsize=14)
plt.ylabel('Number of Customers', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.legend(title='Distance to Store', fontsize=10)
plt.tight_layout()
plt.show()



#年齡及消費產品
# 建立交叉表
age_product_ct = pd.crosstab(df['Age'], df['Most consumed Product'])
print(age_product_ct)
# 繪製堆疊柱狀圖
age_product_ct.plot(kind='bar', stacked=True, figsize=(12, 8), colormap='tab20c')
# 繪製分組柱狀圖
age_product_ct.plot(kind='bar', figsize=(12, 8), colormap='Set2')
# 添加標題和標籤
plt.title('Age Group vs Most Consumed Product', fontsize=16)
plt.xlabel('Age Group', fontsize=14)
plt.ylabel('Number of Customers', fontsize=14)
plt.xticks(rotation=0, fontsize=12)
plt.legend(title='Most Consumed Product', fontsize=10)
plt.tight_layout()
plt.show()

# 計算各職業的人數
profession_counts = df['Visit Frequency'].value_counts()
# 顯示人數分佈
print(profession_counts)
# 繪製柱狀圖
plt.figure(figsize=(10, 6))
profession_counts.plot(kind='bar', color='limegreen')
# 設定標題與座標軸標籤
plt.title('各職業人數分佈', fontsize=14)
plt.xlabel('Profession', fontsize=12)
plt.ylabel('人數', fontsize=12)
plt.xticks(rotation=45, fontsize=10, ha='right')
plt.tight_layout()
plt.show()



df['Prefered Form of Consumption'].value_counts()
# 交叉表：年齡層與消費方式的分佈
age_consumption = pd.crosstab(df['Age'], df['Prefered Form of Consumption'])

# 查看交叉表數據
print(age_consumption)

# 繪製堆疊柱狀圖
age_consumption.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')

# 圖表設置
plt.title('Age Group and Consumption Preference Distribution', fontsize=14)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Number of Customers', fontsize=12)
plt.legend(title='Consumption Preference', fontsize=10)
plt.xticks(rotation=45, fontsize=10, ha='right')
plt.tight_layout()
plt.show()

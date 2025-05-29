import pandas as pd
import matplotlib.pyplot as plt
from statistics import mean, median, mode
df = pd.read_csv("Data_football.csv")
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print(df.isnull().sum())
print(df.info())
print(df.head(10))
print(df.describe())
goal_scorers = df[df['Goals'] > 10]
xg_by_country = df.groupby('Country')['xG'].mean()
players_by_club = df['Club'].value_counts()

# Стовпчаста діаграма: середній xG по країнах (топ 10)
xg_by_country.sort_values(ascending=False).head(10).plot(kind='bar', figsize=(10, 6))
plt.title('Середній xG по країнах')
plt.ylabel('xG')
plt.xlabel('Країна')
plt.show()

# Лінійна діаграма: загальна кількість голів за роками
goals_by_year = df.groupby('Year')['Goals'].sum()
goals_by_year.plot(kind='line', marker='o')
plt.title('Голи за роками')
plt.xlabel('Рік')
plt.ylabel('Кількість голів')
plt.grid()
plt.show()

# Кругова діаграма: розподіл гравців по країнах (топ 5)
df['Country'].value_counts().head(5).plot(kind='pie', autopct='%1.1f%%', figsize=(6, 6))
plt.title('Гравці по країнах')
plt.ylabel('')
plt.show()

print("Середній xG:", mean(df['xG']))
print("Медіана голів:", median(df['Goals']))
print("Мода матчів:", mode(df['Matches_Played']))
print("Максимум голів:", max(df["Goals"]))
print("Максимум голів:", min(df["Goals"]))
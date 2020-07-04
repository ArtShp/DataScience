import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df = pd.read_csv('../datasets/USA_cars_datasets.csv')

'''
price = df.groupby('brand')['price'].max().reset_index()
price = price.sort_values(by='price')
price = price.tail(7)

fig = px.pie(price, values='price', names='brand', template='seaborn')
fig.update_traces(rotation=90, pull=0.05, textinfo='percent+label')
fig.show()
'''

'''
perm = df.loc[:, ['year', 'model']]
perm['count'] = perm.groupby([perm.model, perm.year])['model'].transform('count')
perm = perm.drop_duplicates()
perm = perm.sort_values(by='year', ascending=False)
top_model = ['door', 'mpv', 'f-150', 'x3']

perm = perm.loc[perm['model'].isin(top_model)]
perm = perm[perm.year > 2016]
perm = perm.sort_values(by='year')

fig = px.bar(perm, x='model', y='count', animation_frame='year', animation_group='model', hover_name='model')
fig.show()
'''

plt.scatter(df.mileage, df.price, c=df.mileage, cmap=plt.cm.inferno)
plt.title('Зависимость цены от пробега')
plt.xlabel('Цена')
plt.ylabel('Пробег')
plt.show()

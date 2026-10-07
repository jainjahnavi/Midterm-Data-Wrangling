import pandas as pd
import seaborn as sns
import numpy as np

import matplotlib.pyplot as plt

#i have used onlyy 2 columns rows here, we can use the actual sales dataset here as well.
df=pd.DataFrame({'order_date':['2026-01-04','2026-01-05'],
                 'region':['North', 'south'],
                 'product':['pen','Notebook'],
                 'units':[10,np.nan],
                 'price':[20,60],
                 'rep':['Ravi','Sita']})
df['region'] = df['region'].str.strip().str.title()

df['units'] = df['units'].fillna(df['units'].median())

df['revenue'] = df['units'] * df['price']
df['order_date'] = pd.to_datetime(df['order_date'])
df['month'] = df['order_date'].dt.strftime('%B')

region_revenue = df.groupby('region')['revenue'].sum().reset_index().sort_values(by='revenue', ascending=False)
print(region_revenue)

pivot_df = df.pivot_table(index='region', columns='product', values='revenue', aggfunc='sum', fill_value=0)

sns.barplot(data=region_revenue, x='region', y='revenue')
plt.show()

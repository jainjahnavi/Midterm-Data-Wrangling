import matplotlib.pyplot as plt
import pandas as pd
region_units= pd.DataFrame({'region':['North','South','East'],
                            'units':[15,9,10]})


plt.bar(region_units['region'], region_units['units'], color='skyblue', edgecolor='navy')


plt.title('Units Sold by Region', fontsize=14 )
plt.xlabel('Region', fontsize=12)
plt.ylabel('Units', fontsize=12)
plt.show()
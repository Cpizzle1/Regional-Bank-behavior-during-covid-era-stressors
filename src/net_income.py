import pandas as pd
import numpy as np

 
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import convert_bank_data_to_float

tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv")

def divide_1000(lst):
    lst1 = []
    for i in lst:
        i = i/1000
        i = round(i, 1)
        lst1.append(i) 
    return lst1

def autolabel(rects):
    
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

net_income_dec2017 = tcbi.iloc[1120]
net_income_dec2018 = tcbi.iloc[1119]
net_income_sept2019 = tcbi.iloc[1117]
net_income_dec2019 = tcbi.iloc[1118]
net_income_sept2020 = tcbi.iloc[1116]


bank_dates = ['dec 2017', 'dec 2018', 'sept 2019','dec 2019', 'sept 2020' ]

net_income = [net_income_dec2017,net_income_dec2018, net_income_sept2019,net_income_dec2019,  net_income_sept2020 ]
# c2= map(lambda x:x/1000, net_income)


converted_net_income = (divide_1000(convert_bank_data_to_float(net_income)))

fig, ax= plt.subplots(1, figsize=(6,5),dpi = 200)
rects1= ax.bar(bank_dates, converted_net_income)
ax.set_title ('Net Income TTM')
ax.set_ylabel('Millions(USD)')

ax.ticklabel_format(axis = 'y', style = 'plain')

autolabel(rects1)
# autolabel(rects2)

fig.tight_layout()

# print (list(c2))
plt.show()
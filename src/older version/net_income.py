import pandas as pd
import numpy as np

 
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import * 








net_income_dec2017 = tcbi.iloc[1120]
net_income_dec2018 = tcbi.iloc[1119]
net_income_sept2019 = tcbi.iloc[1117]
net_income_dec2019 = tcbi.iloc[1118]
net_income_sept2020 = tcbi.iloc[1116]


bank_dates = ['dec 2017', 'dec 2018', 'sept 2019','dec 2019', 'sept 2020' ]

net_income = [net_income_dec2017,net_income_dec2018, net_income_sept2019,net_income_dec2019,  net_income_sept2020 ]




converted_net_income = (divide_1000(convert_bank_data_to_float(net_income)))


fig, ax= plt.subplots(1, figsize=(6,5),dpi = 200)
rects1= ax.bar(bank_dates, converted_net_income)
ax.set_title ('Net Income (YTD)', fontsize = 24)
ax.set_ylabel('Millions(USD)', fontsize = 14)

ax.ticklabel_format(axis = 'y', style = 'plain')

autolabel(rects1, ax)


fig.tight_layout()

plt.show()


if __name__ == "__main__":
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv")
    

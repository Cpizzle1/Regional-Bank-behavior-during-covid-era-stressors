import pandas as pd
import numpy as np

 
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *



def net_income_func(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):


    net_income_dec2017 = dataframe.iloc[1120]
    net_income_dec2018 = dataframe.iloc[1119]
    net_income_sept2019= dataframe.iloc[1117]
    net_income_dec2019 = dataframe.iloc[1118]
    net_income_sept2020 =dataframe.iloc[1116]
    current_q = (quarter +str(year))
    dec_year_before = ('dec'+ str(year-1))
    year_before_q = (quarter + str(year-1))
    dec_2year_before = ('dec'+ str(year-2))
    dec_3year_before = ('dec'+ str(year-3))
    bank_dates = [dec_3year_before ,  dec_2year_before,  year_before_q,dec_year_before, current_q ]

    net_income = [net_income_dec2017,net_income_dec2018, net_income_sept2019,net_income_dec2019,  net_income_sept2020 ]


    converted_net_income = (divide_1000(convert_bank_data_to_float(net_income)))


    fig, ax= plt.subplots(1, figsize=(6,5),dpi = 200)
    rects1= ax.bar(bank_dates, converted_net_income)
    ax.set_title (f'{Bank_name} Net Income (YTD)', fontsize = 24)
    ax.set_ylabel('Millions(USD)', fontsize = 14)

    ax.ticklabel_format(axis = 'y', style = 'plain')

    autolabel(rects1, ax)


    fig.tight_layout()

    plt.show()




if __name__ == "__main__":
    # tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv")
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv", index_col='ItemName' )
    print(net_income_func(tcbi, 'sept', 2020, 'TCBI'))
  
   


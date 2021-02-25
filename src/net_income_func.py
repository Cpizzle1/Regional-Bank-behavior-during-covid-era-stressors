import pandas as pd
import numpy as np

 
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *



def net_income_func(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):


    net_income_dec2017 = dataframe.loc['BHSR1312_3Y']
    net_income_dec2018 = dataframe.loc['BHSR1312_2Y']
    net_income_sept2019= dataframe.loc['BHSR1312_4Q']
    net_income_dec2019 = dataframe.loc['BHSR1312_1Y']
    net_income_sept2020 =dataframe.loc['BHSR1312']

    bank_dates = make_bank_dates(quarter, year)
    

    net_income = [net_income_dec2017,net_income_dec2018, net_income_sept2019,net_income_dec2019,  net_income_sept2020 ]


    converted_net_income = (divide_1000(convert_bank_data_to_floatv2(net_income)))


    fig, ax= plt.subplots(1, figsize=(6,4),dpi = 200)
    rects1= ax.bar(bank_dates, converted_net_income)
    ax.set_title (f'{Bank_name} Net Income (YTD)', fontsize = 20)
    ax.set_ylabel('Millions(USD)', fontsize = 12)

    ax.ticklabel_format(axis = 'y', style = 'plain')

    autolabel(rects1, ax)


    fig.tight_layout()
    fig.savefig("Citigroup_income.png", dpi=200)
    plt.show()




if __name__ == "__main__":
    
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv", index_col='ItemName' )
    jpm = pd.read_csv("~/data/JPM_sept2020.csv", index_col='ItemName')
    
    GS = pd.read_csv("~/data/Goldman_Sachs_sept2020.csv", index_col='ItemName')
    Cap_one = pd.read_csv("~/data/Capital_one_sept2020.csv", index_col='ItemName')
    citi_group = pd.read_csv("~/data/Citigroup_sept2020.csv", index_col='ItemName')
    # print(net_income_func(Cap_one, 'sept', 2020, 'Capitol One'))
    # print(net_income_func(jpm, 'sept', 2020, 'JPM'))
    # print(net_income_func(GS, 'sept', 2020, 'Goldman_sachs'))
    print(net_income_func(citi_group, 'sept', 2020, 'Citi-Group'))
  
   


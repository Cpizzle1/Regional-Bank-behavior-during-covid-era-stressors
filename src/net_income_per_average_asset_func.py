import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *


def net_income_per_average_asset(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):
        
        
    net_income_per_avg_asset_sept2020= dataframe.iloc[492]
    net_income_per_avg_asset_sept2019= dataframe.iloc[493]
    net_income_per_avg_asset_dec2019 = dataframe.iloc[494]
    net_income_per_avg_asset_dec2018 = dataframe.iloc[495]
    net_income_per_avg_asset_dec2017 = dataframe.iloc[496]

    pg_net_income_per_avg_asset_sept2020= dataframe.iloc[502]
    pg_net_income_per_avg_asset_sept2019= dataframe.iloc[503]
    pg_net_income_per_avg_asset_dec2019 = dataframe.iloc[504]
    pg_net_income_per_avg_asset_dec2018 = dataframe.iloc[505]
    pg_net_income_per_avg_asset_dec2017 = dataframe.iloc[506]

    current_q = (quarter +str(year))
    dec_year_before = ('dec'+ str(year-1))
    year_before_q = (quarter + str(year-1))
    dec_2year_before = ('dec'+ str(year-2))
    dec_3year_before = ('dec'+ str(year-3))
    
    bank_dates = [dec_3year_before ,  dec_2year_before,  year_before_q,dec_year_before, current_q ]


        # bank_dates = ['dec 2017', 'dec 2018', 'sept 2019','dec 2019', 'sept 2020' ]


    tcbi_income_per_asset_lst =[net_income_per_avg_asset_dec2017,net_income_per_avg_asset_dec2018,net_income_per_avg_asset_sept2019,net_income_per_avg_asset_dec2019, net_income_per_avg_asset_sept2020]   
    converted_tcbi_income_per_asset_lst= (convert_bank_data_to_float(tcbi_income_per_asset_lst))
    pg_income_per_asset_lst = [pg_net_income_per_avg_asset_dec2017,pg_net_income_per_avg_asset_dec2018, pg_net_income_per_avg_asset_sept2019,pg_net_income_per_avg_asset_dec2019, pg_net_income_per_avg_asset_sept2020]
    converted_pg_income_per_asset_lst= (convert_bank_data_to_float(pg_income_per_asset_lst))

    x = np.arange(len(bank_dates)) 
    width = 0.35  

    fig, ax = plt.subplots(figsize = (12, 8))
    tcbi_income_per_asset_ax = ax.bar(x - width/2, converted_tcbi_income_per_asset_lst, width, label=f'{Bank_name}')
    pg_income_per_asset_ax = ax.bar(x + width/2, converted_pg_income_per_asset_lst, width, label='Peer Group n=130')

# Net interest income on a taxable equivalent basis divided by average assets.
    ax.set_ylabel('Ratio', fontsize =12)
    ax.set_title('NET OPERATING INCOME / AVERAGE ASSETS (YTD)', Fontsize = 24)
    ax.set_xticks(x)
    ax.set_xticklabels(bank_dates)
    ax.legend()
    autolabel(tcbi_income_per_asset_ax,ax)
    autolabel(pg_income_per_asset_ax, ax)
    
    plt.show()






if __name__ == "__main__":
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv")
    print(net_income_per_average_asset(tcbi, quarter = 'sept', year = 2020, Bank_name = 'Bank'))

    




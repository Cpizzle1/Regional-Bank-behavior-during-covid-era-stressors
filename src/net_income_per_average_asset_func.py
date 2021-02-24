import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *


def net_income_per_average_asset(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):
        
     # Net interest income on a taxable equivalent basis divided by average assets.   
    net_income_per_avg_asset_sept2020= dataframe.loc['BHSR023']
    net_income_per_avg_asset_sept2019= dataframe.loc['BHSR023_4Q']
    net_income_per_avg_asset_dec2019 = dataframe.loc['BHSR023_1Y']
    net_income_per_avg_asset_dec2018 = dataframe.loc['BHSR023_2Y']
    net_income_per_avg_asset_dec2017 = dataframe.loc['BHSR023_3Y']

    pg_net_income_per_avg_asset_sept2020= dataframe.loc['PHSR023']
    pg_net_income_per_avg_asset_sept2019= dataframe.loc['PHSR023_4Q']
    pg_net_income_per_avg_asset_dec2019 = dataframe.loc['PHSR023_1Y']
    pg_net_income_per_avg_asset_dec2018 = dataframe.loc['PHSR023_2Y']
    pg_net_income_per_avg_asset_dec2017 = dataframe.loc['PHSR023_3Y']

    bank_dates = make_bank_dates(quarter, year)
    



    tcbi_income_per_asset_lst =[net_income_per_avg_asset_dec2017,net_income_per_avg_asset_dec2018,net_income_per_avg_asset_sept2019,net_income_per_avg_asset_dec2019, net_income_per_avg_asset_sept2020]   
    converted_tcbi_income_per_asset_lst= (convert_bank_data_to_floatv2(tcbi_income_per_asset_lst))
    pg_income_per_asset_lst = [pg_net_income_per_avg_asset_dec2017,pg_net_income_per_avg_asset_dec2018, pg_net_income_per_avg_asset_sept2019,pg_net_income_per_avg_asset_dec2019, pg_net_income_per_avg_asset_sept2020]
    converted_pg_income_per_asset_lst= (convert_bank_data_to_floatv2(pg_income_per_asset_lst))

    x = np.arange(len(bank_dates)) 
    width = 0.35  

    fig, ax = plt.subplots(figsize = (12, 8))
    tcbi_income_per_asset_ax = ax.bar(x - width/2, converted_tcbi_income_per_asset_lst, width, label=f'{Bank_name}')
    pg_income_per_asset_ax = ax.bar(x + width/2, converted_pg_income_per_asset_lst, width, label='Peer Group n=130')


    ax.set_ylabel('Ratio', fontsize =12)
    ax.set_title('NET OPERATING INCOME / AVERAGE ASSETS (YTD)', Fontsize = 24)
    ax.set_xticks(x)
    ax.set_xticklabels(bank_dates)
    ax.legend()
    autolabel(tcbi_income_per_asset_ax,ax)
    autolabel(pg_income_per_asset_ax, ax)
    
    plt.show()






if __name__ == "__main__":
    
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv", index_col='ItemName' )
    jpm = pd.read_csv("~/data/JPM_sept2020.csv", index_col='ItemName')
    print(net_income_per_average_asset(jpm, quarter = 'sept', year = 2020, Bank_name = 'JPM'))
    # print(net_income_per_average_asset(tcbi, quarter = 'sept', year = 2020, Bank_name = 'Bank'))

    




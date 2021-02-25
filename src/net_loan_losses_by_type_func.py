import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib.ticker as mtick
from bank_data_gather import *


def net_loan_losses_by_type(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):
    
    #Net Commerical & Industrial Loan Losses
    net_losses_type_CI_sept2020 = dataframe.loc['BHSR247']
    net_losses_type_CI_sept2019 = dataframe.loc['BHSR247_4Q']
    net_losses_type_CI_dec2019 = dataframe.loc['BHSR247_1Y']
    net_losses_type_CI_dec2018 = dataframe.loc['BHSR247_2Y']
    net_losses_type_CI_dec2017 = dataframe.loc['BHSR247_3Y']
    
   


    

#Peer group CI losses:
    pg_net_losses_type_CI_sept2020 = dataframe.loc['PHSR247']
    pg_net_losses_type_CI_sept2019 = dataframe.loc['PHSR247_4Q']
    pg_net_losses_type_CI_dec2019 = dataframe.loc['PHSR247_1Y']
    pg_net_losses_type_CI_dec2018 = dataframe.loc['PHSR247_2Y']
    pg_net_losses_type_CI_dec2017 = dataframe.loc['PHSR247_3Y']

    bank_dates = make_bank_dates(quarter, year)

    

    total_percent_lst = [net_losses_type_CI_dec2017,net_losses_type_CI_dec2018,net_losses_type_CI_sept2019,net_losses_type_CI_dec2019,net_losses_type_CI_sept2020]


    pg_total_asset_catagory_by_percent_sept2020 =[pg_net_losses_type_CI_dec2017,pg_net_losses_type_CI_dec2018, pg_net_losses_type_CI_sept2019,pg_net_losses_type_CI_dec2019,  pg_net_losses_type_CI_sept2020 ]

    total_list = (convert_bank_data_to_floatv2(total_percent_lst))
    converted_pg_total_asset_catagory_by_percent_sept2020 = (convert_bank_data_to_floatv2(pg_total_asset_catagory_by_percent_sept2020))


    

   

    x = np.arange(len(bank_dates))  
    width = 0.35  

    fig, ax = plt.subplots(figsize = (12, 8))
    rects1 = ax.bar(x - width/2, total_list, width, label=f'{Bank_name}')
    rects2 = ax.bar(x + width/2, converted_pg_total_asset_catagory_by_percent_sept2020, width, label='Peer Group n =130')


    ax.set_ylabel('Percent of Total CI Loans')
    ax.set_title(f' Net Losses of Commercial & Industrial Loans ({Bank_name}) ', fontsize = 24)
    ax.set_xticks(x)
    ax.set_xticklabels(bank_dates)

    ax.legend(fontsize= 14)

    ax.yaxis.set_major_formatter(mtick.PercentFormatter())

    autolabel(rects1,ax)
    autolabel(rects2, ax)
    fig.savefig("net_CI_loan_lo.png", dpi=200)

    plt.show()
    





if __name__ == "__main__":
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv", index_col='ItemName')
    

    jpm = pd.read_csv("~/data/JPM_sept2020.csv", index_col='ItemName')
    print(net_loan_losses_by_type(tcbi, quarter ='sept', Bank_name = 'TCBI'))
    # print(net_loan_losses_by_type(jpm, Bank_name ='JPM'))

    

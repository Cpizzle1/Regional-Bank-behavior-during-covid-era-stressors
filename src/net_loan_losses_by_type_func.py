import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *


def net_loan_losses_by_type(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):
    
    net_losses_type_CI_sept2020 = dataframe.iloc[4668]
    net_losses_type_CI_sept2019 = dataframe.iloc[4669]
    net_losses_type_CI_dec2019 = dataframe.iloc[4670]
    net_losses_type_CI_dec2018 = dataframe.iloc[4671]
    net_losses_type_CI_dec2017 = dataframe.iloc[4672]
    
    #UNDER CONSTRUCdataframe


    

#Peer group CI losses:
    pg_net_losses_type_CI_sept2020 = dataframe.iloc[4678]
    pg_net_losses_type_CI_sept2019 = dataframe.iloc[4679]
    pg_net_losses_type_CI_dec2019 = dataframe.iloc[4680]
    pg_net_losses_type_CI_dec2018 = dataframe.iloc[4681]
    pg_net_losses_type_CI_dec2017 = dataframe.iloc[4682]

    bank_dates = make_bank_dates(quarter, year)

    

    total_percent_lst = [net_losses_type_CI_dec2017,net_losses_type_CI_dec2018,net_losses_type_CI_sept2019,net_losses_type_CI_dec2019,net_losses_type_CI_sept2020]


    pg_total_asset_catagory_by_percent_sept2020 =[pg_net_losses_type_CI_dec2017,pg_net_losses_type_CI_dec2018, pg_net_losses_type_CI_sept2019,pg_net_losses_type_CI_dec2019,  pg_net_losses_type_CI_sept2020 ]

    total_list = (convert_bank_data_to_float(total_percent_lst))
    converted_pg_total_asset_catagory_by_percent_sept2020 = (convert_bank_data_to_float(pg_total_asset_catagory_by_percent_sept2020))


    

    converted_pg_total_asset_catagory_by_percent_sept2020

    x = np.arange(len(bank_dates))  
    width = 0.35  

    fig, ax = plt.subplots(figsize = (12, 8))
    rects1 = ax.bar(x - width/2, total_list, width, label=f'{Bank_name}')
    rects2 = ax.bar(x + width/2, converted_pg_total_asset_catagory_by_percent_sept2020, width, label='Peer Group')


    ax.set_ylabel('Percent of Total CI Loans')
    ax.set_title(' Net  Losses of Commercial & Industrial Loans ', fontsize = 24)
    ax.set_xticks(x)
    ax.set_xticklabels(bank_dates)

    ax.legend(fontsize= 14)

    autolabel(rects1,ax)
    autolabel(rects2, ax)
    # fig.savefig("net_CI_loan_lo.png", dpi=200)

    plt.show()
    





if __name__ == "__main__":
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv")
    print(net_loan_losses_by_type(tcbi, quarter ='sept', Bank_name = 'TCBI'))
    

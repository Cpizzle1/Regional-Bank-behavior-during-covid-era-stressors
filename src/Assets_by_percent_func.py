import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *

tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv")
def assets_by_percent(dataframe, Bank_name = 'Bank'):
    percent_asset_real_estate_loan_sept2020 = dataframe.iloc[2516]
    percent_asset_commercial_industrial_loan_sept2020 = dataframe.iloc[2531]
    percent_asset_loan_to_individuals_sept2020 = dataframe.iloc[2546]
    percent_asset_other_loan_sept2020 = dataframe.iloc[2576]
    percent_asset_bank_balances_sept2020 = dataframe.iloc[2501]
    percent_asset_other_assets_sept2020 = dataframe.iloc[2591]
    percent_asset_debt_securities_greater_than_year_sept2020 = dataframe.iloc[2801]

#Peer group assets
    peer_real_estate_total_asset_sept2020 = dataframe.iloc[2526]
    peer_comm_and_indust_total_asset_sept2020 =dataframe.iloc[2541]
    peer_individual_total_asset_sept2020 =dataframe.iloc[2556]
    peer_other_total_asset_sept2020 =dataframe.iloc[2586]
    peer_bank_balances_asset_sept2020 =dataframe.iloc[2511]
    peer_debt_securities_less_year_set_sept2020 =dataframe.iloc[2811]
    peer_all_other_assets_sept2020 =dataframe.iloc[2601]

    total_percent_lst = [percent_asset_real_estate_loan_sept2020,percent_asset_commercial_industrial_loan_sept2020,percent_asset_loan_to_individuals_sept2020,percent_asset_other_loan_sept2020,percent_asset_bank_balances_sept2020,percent_asset_debt_securities_greater_than_year_sept2020,percent_asset_other_assets_sept2020]


    pg_total_asset_catagory_by_percent_sept2020 = [peer_real_estate_total_asset_sept2020,peer_comm_and_indust_total_asset_sept2020,peer_individual_total_asset_sept2020, peer_other_total_asset_sept2020,peer_bank_balances_asset_sept2020,peer_debt_securities_less_year_set_sept2020,peer_all_other_assets_sept2020]

    total_list = (convert_bank_data_to_float(total_percent_lst))
    converted_pg_total_asset_catagory_by_percent_sept2020 = (convert_bank_data_to_float(pg_total_asset_catagory_by_percent_sept2020))


    total_percent_catagories=['Real Estate', 'Comm&Industrial', 'Individ', 'Other', 'Bank balances', 'Securities>1year','All Other']

    total_list

    converted_pg_total_asset_catagory_by_percent_sept2020

    x = np.arange(len(total_percent_catagories))  
    width = 0.35  

    fig, ax = plt.subplots(figsize = (12, 8))
    rects1 = ax.bar(x - width/2, total_list, width, label=f'{Bank_name}')
    rects2 = ax.bar(x + width/2, converted_pg_total_asset_catagory_by_percent_sept2020, width, label='Peer Group')


    ax.set_ylabel('Percent Asset')
    ax.set_title('Assets by Percentage Current Qtr', fontsize = 24)
    ax.set_xticks(x)
    ax.set_xticklabels(total_percent_catagories)

    ax.legend()

    autolabel(rects1,ax)
    autolabel(rects2, ax)

    plt.show()

print(assets_by_percent(tcbi, 'TCBI'))



if __name__ == "__main__":
    pass

#     def net_income_func(dataframe, Bank_name = 'Bank'):
#         percent_asset_real_estate_loan_sept2020 = tcbi.iloc[2516]
#         percent_asset_commercial_industrial_loan_sept2020 = tcbi.iloc[2531]
#         percent_asset_loan_to_individuals_sept2020 = tcbi.iloc[2546]
#         percent_asset_other_loan_sept2020 = tcbi.iloc[2576]
#         percent_asset_bank_balances_sept2020 = tcbi.iloc[2501]
#         percent_asset_other_assets_sept2020 = tcbi.iloc[2591]
#         percent_asset_debt_securities_greater_than_year_sept2020 = tcbi.iloc[2801]

# #Peer group assets
#         peer_real_estate_total_asset_sept2020 = tcbi.iloc[2526]
#         peer_comm_and_indust_total_asset_sept2020 =tcbi.iloc[2541]
#         peer_individual_total_asset_sept2020 =tcbi.iloc[2556]
#         peer_other_total_asset_sept2020 =tcbi.iloc[2586]
#         peer_bank_balances_asset_sept2020 =tcbi.iloc[2511]
#         peer_debt_securities_less_year_set_sept2020 =tcbi.iloc[2811]
#         peer_all_other_assets_sept2020 =tcbi.iloc[2601]

#         total_percent_lst = [percent_asset_real_estate_loan_sept2020,percent_asset_commercial_industrial_loan_sept2020,percent_asset_loan_to_individuals_sept2020,percent_asset_other_loan_sept2020,percent_asset_bank_balances_sept2020,percent_asset_debt_securities_greater_than_year_sept2020,percent_asset_other_assets_sept2020]


#         pg_total_asset_catagory_by_percent_sept2020 = [peer_real_estate_total_asset_sept2020,peer_comm_and_indust_total_asset_sept2020,peer_individual_total_asset_sept2020, peer_other_total_asset_sept2020,peer_bank_balances_asset_sept2020,peer_debt_securities_less_year_set_sept2020,peer_all_other_assets_sept2020]

#         total_list = (convert_bank_data_to_float(total_percent_lst))
#         converted_pg_total_asset_catagory_by_percent_sept2020 = (convert_bank_data_to_float(pg_total_asset_catagory_by_percent_sept2020))


#         total_percent_catagories=['Real Estate', 'Comm&Industrial', 'Individ', 'Other', 'Bank balances', 'Securities>1year','All Other']

#         total_list

#         converted_pg_total_asset_catagory_by_percent_sept2020

#         x = np.arange(len(total_percent_catagories))  
#         width = 0.35  

#         fig, ax = plt.subplots(figsize = (12, 8))
#         rects1 = ax.bar(x - width/2, total_list, width, label=f'{Bank_name}')
#         rects2 = ax.bar(x + width/2, converted_pg_total_asset_catagory_by_percent_sept2020, width, label='Peer Group')


#         ax.set_ylabel('Percent Asset')
#         ax.set_title('Assets by Percentage Current Qtr', fontsize = 24)
#         ax.set_xticks(x)
#         ax.set_xticklabels(total_percent_catagories)

#         ax.legend()

#         autolabel(rects1,ax)
#         autolabel(rects2, ax)

#         plt.show()

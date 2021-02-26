import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *


def assets_by_percent(dataframe, Bank_name = 'Bank'):
    """ takes in a pandas dataframe and returns a graph of major loan percentages in 
    Real Estate, Comm&Industrial , Individ, Other, Bank balances, Securities>1year, All Other
    and saves PNG file as TCBI_PG_assets_by_percent.png

    Args:
        dataframe ([pandas dataframe]): [CSV file of BHCPR but needs to be read in with index_col='ItemName' argument]
        Bank_name([String]): Defaults to 'Bank': name of Bank for title and graph purposes
    """
    #bank assets
    percent_asset_real_estate_loan_sept2020 = dataframe.loc['BHSR112']
    percent_asset_commercial_industrial_loan_sept2020 = dataframe.loc['BHSR113']
    percent_asset_loan_to_individuals_sept2020 = dataframe.loc['BHSR114']
    percent_asset_other_loan_sept2020 = dataframe.loc['BHSR136']
    percent_asset_bank_balances_sept2020 = dataframe.loc['BHSR061']
    percent_asset_other_assets_sept2020 = dataframe.loc['BHSR139']
    percent_asset_debt_securities_greater_than_year_sept2020 = dataframe.loc['BHSR252']

    #Peer group assets
    peer_real_estate_total_asset_sept2020 = dataframe.loc['PHSR112']
    peer_comm_and_indust_total_asset_sept2020 =dataframe.loc['PHSR113']
    peer_individual_total_asset_sept2020 =dataframe.loc['PHSR114']
    peer_other_total_asset_sept2020 =dataframe.loc['PHSR136']
    peer_bank_balances_asset_sept2020 =dataframe.loc['PHSR061']
    peer_debt_securities_less_year_set_sept2020 =dataframe.loc['PHSR252']
    peer_all_other_assets_sept2020 =dataframe.loc['PHSR139']

    total_percent_lst = [percent_asset_real_estate_loan_sept2020,percent_asset_commercial_industrial_loan_sept2020,percent_asset_loan_to_individuals_sept2020,percent_asset_other_loan_sept2020,percent_asset_bank_balances_sept2020,percent_asset_debt_securities_greater_than_year_sept2020,percent_asset_other_assets_sept2020]
    pg_total_asset_catagory_by_percent_sept2020 = [peer_real_estate_total_asset_sept2020,peer_comm_and_indust_total_asset_sept2020,peer_individual_total_asset_sept2020, peer_other_total_asset_sept2020,peer_bank_balances_asset_sept2020,peer_debt_securities_less_year_set_sept2020,peer_all_other_assets_sept2020]

    total_list = (convert_bank_data_to_floatv2(total_percent_lst))
    converted_pg_total_asset_catagory_by_percent_sept2020 = (convert_bank_data_to_floatv2(pg_total_asset_catagory_by_percent_sept2020))


    total_percent_catagories=['Real Estate', 'Comm&Industrial', 'Individ', 'Other', 'Bank balances', 'Securities>1year','All Other']

    x = np.arange(len(total_percent_catagories))  
    width = 0.35  

    fig, ax = plt.subplots(figsize = (12, 8))
    rects1 = ax.bar(x - width/2, total_list, width, label=f'{Bank_name}')
    rects2 = ax.bar(x + width/2, converted_pg_total_asset_catagory_by_percent_sept2020, width, label='Peer Group n=130')


    ax.set_ylabel('Percent Asset')
    ax.set_title('Assets by Percentage Current Qtr', fontsize = 24)
    ax.set_xticks(x)
    ax.set_xticklabels(total_percent_catagories)

    ax.legend()

    autolabel(rects1,ax)
    autolabel(rects2, ax)
    fig.savefig("TCBI_PG_assets_by_percent.png", dpi=200)
    plt.show()





if __name__ == "__main__":
   

    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv", index_col='ItemName' )
    jpm = pd.read_csv("~/data/JPM_sept2020.csv", index_col='ItemName')
    print(assets_by_percent(tcbi, 'TCBI'))
    # print(assets_by_percent(jpm, 'JPM'))
    




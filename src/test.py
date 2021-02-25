import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *
import matplotlib.ticker as mtick


def CI_loans_30_late(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):
        
     #Bank C&I loans past due   
    CI_30_89_days_past_due_sept2020=dataframe.loc['BHSR629']
    CI_30_89_days_past_due_sept2019=dataframe.loc['BHSR629_4Q']
    CI_30_89_days_past_due_dec2019= dataframe.loc['BHSR629_1Y']
    CI_30_89_days_past_due_dec2018= dataframe.loc['BHSR629_2Y']
    CI_30_89_days_past_due_dec2017= dataframe.loc['BHSR629_3Y']
    #Peer Group C&I loans past due 
    PG_CI_30_89_days_past_due_sept2020=dataframe.loc['PHSR629']
    PG_CI_30_89_days_past_due_sept2019=dataframe.loc['PHSR629_4Q']
    PG_CI_30_89_days_past_due_dec2019= dataframe.loc['PHSR629_1Y']
    PG_CI_30_89_days_past_due_dec2018= dataframe.loc['PHSR629_2Y']
    PG_CI_30_89_days_past_due_dec2017= dataframe.loc['PHSR629_3Y']

    bank_dates = make_bank_dates(quarter, year)

    

    tcbi_ci_loans_30_89_past_due =[CI_30_89_days_past_due_dec2017,CI_30_89_days_past_due_dec2018,CI_30_89_days_past_due_sept2019,CI_30_89_days_past_due_dec2019, CI_30_89_days_past_due_sept2020]   
    converted_tcbi_ci_loans_30_89_past_due= (convert_bank_data_to_floatv2(tcbi_ci_loans_30_89_past_due ))
    pg_ci_loans_30_89_past_due = [PG_CI_30_89_days_past_due_dec2017,PG_CI_30_89_days_past_due_dec2018, PG_CI_30_89_days_past_due_sept2019,PG_CI_30_89_days_past_due_dec2019, PG_CI_30_89_days_past_due_sept2020]
    converted_pg_ci_loans_30_89_past_due= (convert_bank_data_to_floatv2(pg_ci_loans_30_89_past_due))

    x = np.arange(len(bank_dates)) 
    width = 0.35 

    fig, ax = plt.subplots(figsize = (12, 8))
    tcbi_CI_30_90days_pastdue_ax = ax.bar(x - width/2, converted_tcbi_ci_loans_30_89_past_due, width, label=f'{Bank_name}')
    pg_CI_30_90days_pastdue_ax = ax.bar(x + width/2, converted_pg_ci_loans_30_89_past_due, width, label='Peer Group n=130')


    ax.set_ylabel('Percentage', fontsize = 14)
    ax.set_title('Commercial & Industrial Loans 30-89 days late', Fontsize = 24)
    ax.set_xticks(x)
    ax.set_xticklabels(bank_dates)
    ax.legend()

    autolabel(tcbi_CI_30_90days_pastdue_ax, ax)
    autolabel(pg_CI_30_90days_pastdue_ax, ax)

    # plt.savefig('CI_loans_30_89_late.png')
    plt.show()

def assets_by_percent(dataframe, Bank_name = 'Bank'):
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
    # graph_ = ()
    # ax.yaxis.set_major_formatter(f'{graph_h}%')

    ax.yaxis.set_major_formatter(mtick.PercentFormatter())

    ax.legend()

    autolabel(rects1,ax)
    autolabel(rects2, ax)
    fig.savefig("TCBI_PG_assets_by_percent.png", dpi=200)
    plt.show()

if __name__ == "__main__":
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv", index_col='ItemName' )
    jpm = pd.read_csv("~/data/JPM_sept2020.csv", index_col='ItemName')
    # print(CI_loans_30_late(jpm, quarter = 'sept', year = 2020, Bank_name = 'JPM'))
    # print(CI_loans_30_late(tcbi, quarter = 'sept', year = 2020, Bank_name = 'TCBI'))
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv", index_col='ItemName' )
    jpm = pd.read_csv("~/data/JPM_sept2020.csv", index_col='ItemName')
    print(assets_by_percent(tcbi, 'TCBI'))
    # print(assets_by_percent(jpm, 'JPM'))












   

   
    




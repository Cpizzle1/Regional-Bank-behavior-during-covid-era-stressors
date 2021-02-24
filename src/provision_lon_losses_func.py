import pandas as pd
import numpy as np

 
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *



def prov_net_loan_losses(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):

    provison_loan_losses_q2020 = dataframe.loc['BHCK4230']
    provison_loan_losses_q2019 = dataframe.loc['BHCK4230_4Q']
    provison_loan_losses_dec2019 = dataframe.loc['BHCK4230_1Y']
    provison_loan_losses_dec2018 = dataframe.loc['BHCK4230_2Y']
    provison_loan_losses_dec2017 = dataframe.loc['BHCK4230_3Y']

    net_loan_losses_sept2020 = dataframe.loc['BHSR853']
    net_loan_losses_sept2019 = dataframe.loc['BHSR853_4Q']
    net_loan_losses_dec2019 = dataframe.loc['BHSR853_1Y']
    net_loan_losses_dec2018 = dataframe.loc['BHSR853_2Y']
    net_loan_losses_dec2017 = dataframe.loc['BHSR853_3Y']


    
   

    bank_dates = make_bank_dates(quarter, year)

    
    provision_loan_losses = [provison_loan_losses_dec2017, provison_loan_losses_dec2018,provison_loan_losses_q2019,provison_loan_losses_dec2019, provison_loan_losses_q2020 ]
    provision_loan_loss_lst = (divide_1000(convert_bank_data_to_floatv2(provision_loan_losses)))

    net_loan_losses = [net_loan_losses_dec2017, net_loan_losses_dec2018, net_loan_losses_sept2019, net_loan_losses_dec2019, net_loan_losses_sept2020]
    net_loan_losses_converted = (divide_1000(convert_bank_data_to_floatv2(net_loan_losses)))

    


    x = np.arange(len(bank_dates))  
    width = 0.35  
    

    fig, ax = plt.subplots(figsize = (12, 8))
    # ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
    

    provision_loan_loss_ax = ax.bar(x - width/2, provision_loan_loss_lst, width,color = 'k',alpha= 0.85, label='Provision for loan losses')
    net_loan_losses_ax = ax.bar(x + width/2, net_loan_losses_converted, width,color = 'r',alpha = 0.7,  label='Net Loan losses')
    
    
    ax.set_ylabel('Millions (USD)', fontsize = 14)
    ax.set_title(f'Loan Losses & Provision for Loan Losses ({Bank_name})', Fontsize = 24)
    ax.set_xticks(x)
    ax.set_xticklabels(bank_dates)
    ax.legend(fontsize= 14)

    

    autolabel(provision_loan_loss_ax, ax)
    autolabel(net_loan_losses_ax, ax)
    

    
    fig.savefig("citigroup_provisions&_losses.png", dpi=200)
    plt.show()

if __name__ == "__main__":
    


    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv", index_col='ItemName' )
    jpm = pd.read_csv("~/data/JPM_sept2020.csv", index_col='ItemName')
    GS = pd.read_csv("~/data/Goldman_Sachs_sept2020.csv", index_col='ItemName')
    Cap_one = pd.read_csv("~/data/Capital_one_sept2020.csv", index_col='ItemName')
    citi_group = pd.read_csv("~/data/Citigroup_sept2020.csv", index_col='ItemName')
    # print(prov_net_loan_losses(tcbi, 'TCBI'))
    print(prov_net_loan_losses(citi_group, Bank_name ='Citigroup'))
    
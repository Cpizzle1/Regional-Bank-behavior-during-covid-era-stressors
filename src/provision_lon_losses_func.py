import pandas as pd
import numpy as np

 
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *



def net_loan_losses(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):

    provison_loan_losses_q2020 = dataframe.iloc[1006]
    provison_loan_losses_q2019 = dataframe.iloc[1007]
    provison_loan_losses_dec2019 = dataframe.iloc[1008]
    provison_loan_losses_dec2018 = dataframe.iloc[1009]
    provison_loan_losses_dec2017 = dataframe.iloc[1010]

    net_loan_losses_sept2020 = dataframe.iloc[5308]
    net_loan_losses_sept2019 = dataframe.iloc[5309]
    net_loan_losses_dec2019 = dataframe.iloc[5310]
    net_loan_losses_dec2018 = dataframe.iloc[5311]
    net_loan_losses_dec2017 = dataframe.iloc[5312]


    
   

    bank_dates = make_bank_dates(quarter, year)

    
    provision_loan_losses = [provison_loan_losses_dec2017, provison_loan_losses_dec2018,provison_loan_losses_q2019,provison_loan_losses_dec2019, provison_loan_losses_q2020 ]
    provision_loan_loss_lst = (divide_1000(convert_bank_data_to_float(provision_loan_losses)))

    net_loan_losses = [net_loan_losses_dec2017, net_loan_losses_dec2018, net_loan_losses_sept2019, net_loan_losses_dec2019, net_loan_losses_sept2020]
    net_loan_losses_converted = (divide_1000(convert_bank_data_to_float(net_loan_losses)))

    


    x = np.arange(len(bank_dates))  
    width = 0.35  
    

    fig, ax = plt.subplots(figsize = (12, 8))
    # ax.grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
    

    provision_loan_loss_ax = ax.bar(x - width/2, provision_loan_loss_lst, width,color = 'k',alpha= 0.85, label='Provision for loan losses')
    net_loan_losses_ax = ax.bar(x + width/2, net_loan_losses_converted, width,color = 'r',alpha = 0.7,  label='Net Loan losses')
    
    
    ax.set_ylabel('Millions (USD)', fontsize = 14)
    ax.set_title('Loan Losses & Provision for Loan Losses', Fontsize = 24)
    ax.set_xticks(x)
    ax.set_xticklabels(bank_dates)
    ax.legend(fontsize= 14)

    

    autolabel(provision_loan_loss_ax, ax)
    autolabel(net_loan_losses_ax, ax)
    

   
    plt.show()

if __name__ == "__main__":
    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv")
    
    print(net_loan_losses(tcbi, quarter = 'sept', year = 2020, Bank_name = 'TCBI'))
    
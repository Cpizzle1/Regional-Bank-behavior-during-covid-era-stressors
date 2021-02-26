import pandas as pd
import numpy as np

 
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *



def net_loan_losses(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):
    """Makes a graph of net loan losses of a Bank from BHCPR CSV file

     Args:
        dataframe ([pandas dataframe]): CSV file of BHCPR
        quarter (str, optional): [start month of quarter of interset]. Defaults to 'sept'.
        year (int, optional): [Year of CSV BHCPR]. Defaults to 2020.
        Bank_name (str, optional): [Name of Bank in BHCPR file for labeling purposes]. Defaults to 'Bank'.
    """

    net_loan_losses_sept2020 = dataframe.loc['BHSR853']
    net_loan_losses_sept2019 = dataframe.loc['BHSR853_4Q']
    net_loan_losses_dec2019 = dataframe.loc['BHSR853_1Y']
    net_loan_losses_dec2018 = dataframe.loc['BHSR853_2Y']
    net_loan_losses_dec2017 = dataframe.loc['BHSR853_3Y']

    bank_dates = make_bank_dates(quarter, year)

    net_loan_losses = [net_loan_losses_dec2017, net_loan_losses_dec2018, net_loan_losses_sept2019, net_loan_losses_dec2019, net_loan_losses_sept2020]

    converted_net_income = (divide_1000(convert_bank_data_to_floatv2(net_loan_losses)))


    fig, ax= plt.subplots(1, figsize=(5,5),dpi = 200)
    rects1= ax.bar(bank_dates, converted_net_income, color='r', alpha = 0.7)
    ax.set_title (f'{Bank_name} Net Loan Losses (YTD)', fontsize = 20)
    ax.set_ylabel('Millions(USD)', fontsize = 14)

    ax.ticklabel_format(axis = 'y', style = 'plain')

    autolabel(rects1, ax)


    fig.tight_layout()

    plt.show()



if __name__ == "__main__":
    


    tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv", index_col='ItemName' )
    jpm = pd.read_csv("~/data/JPM_sept2020.csv", index_col='ItemName')
    print(net_loan_losses(tcbi, 'TCBI'))
    # print(net_loan_losses(jpm, Bank_name ='JPM'))
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import *

tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv")
def CI_loans_30_late(dataframe, quarter = 'sept', year = 2020, Bank_name = 'Bank'):
        
        
    CI_30_89_days_past_due_sept2020=tcbi.iloc[5896]
    CI_30_89_days_past_due_sept2019=tcbi.iloc[5897]
    CI_30_89_days_past_due_dec2019= tcbi.iloc[5898]
    CI_30_89_days_past_due_dec2018= tcbi.iloc[5899]
    CI_30_89_days_past_due_dec2017= tcbi.iloc[5900]

    PG_CI_30_89_days_past_due_sept2020= tcbi.iloc[5906]
    PG_CI_30_89_days_past_due_sept2019= tcbi.iloc[5907]
    PG_CI_30_89_days_past_due_dec2019= tcbi.iloc[5908]
    PG_CI_30_89_days_past_due_dec2018= tcbi.iloc[5909]
    PG_CI_30_89_days_past_due_dec2017= tcbi.iloc[5910]

    current_q = (quarter +str(year))
    dec_year_before = ('dec'+ str(year-1))
    year_before_q = (quarter + str(year-1))
    dec_2year_before = ('dec'+ str(year-2))
    dec_3year_before = ('dec'+ str(year-3))
    bank_dates = [dec_3year_before ,  dec_2year_before,  year_before_q,dec_year_before, current_q ]

    tcbi_ci_loans_30_89_past_due =[CI_30_89_days_past_due_dec2017,CI_30_89_days_past_due_dec2018,CI_30_89_days_past_due_sept2019,CI_30_89_days_past_due_dec2019, CI_30_89_days_past_due_sept2020]   
    converted_tcbi_ci_loans_30_89_past_due= (convert_bank_data_to_float(tcbi_ci_loans_30_89_past_due ))
    pg_ci_loans_30_89_past_due = [PG_CI_30_89_days_past_due_dec2017,PG_CI_30_89_days_past_due_dec2018, PG_CI_30_89_days_past_due_sept2019,PG_CI_30_89_days_past_due_dec2019, PG_CI_30_89_days_past_due_sept2020]
    converted_pg_ci_loans_30_89_past_due= (convert_bank_data_to_float(pg_ci_loans_30_89_past_due))

    x = np.arange(len(bank_dates))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots(figsize = (12, 8))
    tcbi_CI_30_90days_pastdue_ax = ax.bar(x - width/2, converted_tcbi_ci_loans_30_89_past_due, width, label=f'{Bank_name}')
    pg_CI_30_90days_pastdue_ax = ax.bar(x + width/2, converted_pg_ci_loans_30_89_past_due, width, label='Peer Group')


    ax.set_ylabel('Percentage', fontsize = 14)
    ax.set_title('Commercial & Industrial Loans 30-89 days late', Fontsize = 24)
    ax.set_xticks(x)
    ax.set_xticklabels(bank_dates)
    ax.legend()

    autolabel(tcbi_CI_30_90days_pastdue_ax, ax)
    autolabel(pg_CI_30_90days_pastdue_ax, ax)

    # plt.savefig('CI_loans_30_89_late.png')
    plt.show()
print(CI_loans_30_late(tcbi, quarter = 'sept', year = 2020, Bank_name = 'Bank'))
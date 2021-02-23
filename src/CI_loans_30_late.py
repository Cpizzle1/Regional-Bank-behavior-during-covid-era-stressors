import pandas as pd
import numpy as np

 
import matplotlib.pyplot as plt
import scipy.stats as stats
from bank_data_gather import convert_bank_data_to_float


tcbi = pd.read_csv("~/data/BHCPR_2706735_20200930.csv")

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


bank_dates = ['dec 2017', 'dec 2018', 'sept 2019','dec 2019', 'sept 2020' ]

tcbi_ci_loans_30_89_past_due =[CI_30_89_days_past_due_dec2017,CI_30_89_days_past_due_dec2018,CI_30_89_days_past_due_sept2019,CI_30_89_days_past_due_dec2019, CI_30_89_days_past_due_sept2020]   
converted_tcbi_ci_loans_30_89_past_due= (convert_bank_data_to_float(tcbi_ci_loans_30_89_past_due ))
pg_ci_loans_30_89_past_due = [PG_CI_30_89_days_past_due_dec2017,PG_CI_30_89_days_past_due_dec2018, PG_CI_30_89_days_past_due_sept2019,PG_CI_30_89_days_past_due_dec2019, PG_CI_30_89_days_past_due_sept2020]
converted_pg_ci_loans_30_89_past_due= (convert_bank_data_to_float(pg_ci_loans_30_89_past_due))

x = np.arange(len(bank_dates))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize = (12, 8))
tcbi_CI_30_90days_pastdue_ax = ax.bar(x - width/2, converted_tcbi_ci_loans_30_89_past_due, width, label='TCBI')
pg_CI_30_90days_pastdue_ax = ax.bar(x + width/2, converted_pg_ci_loans_30_89_past_due, width, label='Peer Group')


ax.set_ylabel('Percentage', fontsize = 14)
ax.set_title('Commercial & Industrial Loans 30-89 days late', Fontsize = 24)
ax.set_xticks(x)
ax.set_xticklabels(bank_dates)
ax.legend()
# Net interest income on a taxable equivalent basis divided by average assets.


def autolabel(rects):
   
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(tcbi_CI_30_90days_pastdue_ax)
autolabel(pg_CI_30_90days_pastdue_ax)

# plt.savefig('CI_loans_30_89_late.png')
plt.show()
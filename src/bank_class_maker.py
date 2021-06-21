import re   
import pandas as pd         
import matplotlib.ticker as mtick
from bank_data_gather import *  
import matplotlib.pyplot as plt
import numpy as np


# from bank_variables import url_banks
# from bank_helpers import bank

class bank:
    def __init__(self, dataframe, ticker):
        self.dataframe = dataframe
        self.ticker = ticker
    def __str__(self):
        return(self.ticker)
    def __repr__(self):
        return(self.ticker)
    
    def assets(self):
        percent_asset_real_estate_loan_sept2020 = self.dataframe.loc['BHSR112']
        percent_asset_commercial_industrial_loan_sept2020 = self.dataframe.loc['BHSR113']
        percent_asset_loan_to_individuals_sept2020 = self.dataframe.loc['BHSR114']
        percent_asset_other_loan_sept2020 = self.dataframe.loc['BHSR136']
        percent_asset_bank_balances_sept2020 = self.dataframe.loc['BHSR061']
        percent_asset_other_assets_sept2020 = self.dataframe.loc['BHSR139']
        percent_asset_debt_securities_greater_than_year_sept2020 = self.dataframe.loc['BHSR252']
        
        peer_real_estate_total_asset_sept2020 = self.dataframe.loc['PHSR112']
        peer_comm_and_indust_total_asset_sept2020 =self.dataframe.loc['PHSR113']
        peer_individual_total_asset_sept2020 =self.dataframe.loc['PHSR114']
        peer_other_total_asset_sept2020 =self.dataframe.loc['PHSR136']
        peer_bank_balances_asset_sept2020 =self.dataframe.loc['PHSR061']
        peer_debt_securities_less_year_set_sept2020 =self.dataframe.loc['PHSR252']
        peer_all_other_assets_sept2020 =self.dataframe.loc['PHSR139']
        
        total_percent_lst = [percent_asset_real_estate_loan_sept2020,percent_asset_commercial_industrial_loan_sept2020,percent_asset_loan_to_individuals_sept2020,percent_asset_other_loan_sept2020,percent_asset_bank_balances_sept2020,percent_asset_debt_securities_greater_than_year_sept2020,percent_asset_other_assets_sept2020]
        pg_total_asset_catagory_by_percent_sept2020 = [peer_real_estate_total_asset_sept2020,peer_comm_and_indust_total_asset_sept2020,peer_individual_total_asset_sept2020, peer_other_total_asset_sept2020,peer_bank_balances_asset_sept2020,peer_debt_securities_less_year_set_sept2020,peer_all_other_assets_sept2020]

        total_list = (convert_bank_data_to_floatv2(total_percent_lst))
        converted_pg_total_asset_catagory_by_percent_sept2020 = (convert_bank_data_to_floatv2(pg_total_asset_catagory_by_percent_sept2020))


        total_percent_catagories=['Real Estate', 'Comm&Industrial', 'Individ', 'Other', 'Bank balances', 'Securities>1year','All Other']

        x = np.arange(len(total_percent_catagories))  
        width = 0.35  

        fig, ax = plt.subplots(figsize = (12, 8))
        rects1 = ax.bar(x - width/2, total_list, width, label=f'{self.ticker}')
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

    def net_income_func(self, quarter = 'sept', year = 2020, Bank_name = 'Bank'):

        """
        Returns a graph of the net income of BCHPR bank file with bank dates pass into argument

        Args:
        dataframe ([pandas dataframe]): [CSV file of BHCPR but needs to be read in with index_col='ItemName' argument]
        quarter (str, optional): [Month of quarter to measure ]. Defaults to 'sept'
        year (int, optional): year of BHCPR report. Defaults to 'sept'
        Bank_name (str, optional): [name of Bank to fill in graph and label title ]. Defaults to 'Bank'.

        """
        net_income_dec2017 = self.dataframe.loc['BHSR1312_3Y']
        net_income_dec2018 = self.dataframe.loc['BHSR1312_2Y']
        net_income_sept2019= self.dataframe.loc['BHSR1312_4Q']
        net_income_dec2019 = self.dataframe.loc['BHSR1312_1Y']
        net_income_sept2020 =self.dataframe.loc['BHSR1312']

        bank_dates = make_bank_dates(quarter, year)


        net_income = [net_income_dec2017,net_income_dec2018, net_income_sept2019,net_income_dec2019,  net_income_sept2020 ]


        converted_net_income = (divide_1000(convert_bank_data_to_floatv2(net_income)))


        fig, ax= plt.subplots(1, figsize=(6,4),dpi = 200)
        rects1= ax.bar(bank_dates, converted_net_income)
        ax.set_title (f'{Bank_name} Net Income (YTD)', fontsize = 20)
        ax.set_ylabel('Millions(USD)', fontsize = 12)

        ax.ticklabel_format(axis = 'y', style = 'plain')

        autolabel(rects1, ax)


        fig.tight_layout()
        # fig.savefig("Citigroup_income.png", dpi=200)
        plt.show()
    
    def net_income_per_average_asset(self, quarter = 'sept', year = 2020, Bank_name = 'Bank'):

        """
        Returns graph of net income per average asset, with bank dates specified

        Args:
        dataframe ([pandas dataframe]): [CSV file of BHCPR but needs to be read in with index_col='ItemName' argument]
        quarter (str, optional): [Month of quarter to measure ]. Defaults to 'sept'
        year (int, optional): year of BHCPR report. Defaults to 'sept'self.
        Bank_name (str, optional): [name of Bank to fill in graph and label title ]. Defaults to 'Bank'.
        """

        # Net interest income on a taxable equivalent basis divided by average assets.   
        net_income_per_avg_asset_sept2020= self.dataframe.loc['BHSR023']
        net_income_per_avg_asset_sept2019= self.dataframe.loc['BHSR023_4Q']
        net_income_per_avg_asset_dec2019 = self.dataframe.loc['BHSR023_1Y']
        net_income_per_avg_asset_dec2018 = self.dataframe.loc['BHSR023_2Y']
        net_income_per_avg_asset_dec2017 = self.dataframe.loc['BHSR023_3Y']

        pg_net_income_per_avg_asset_sept2020= self.dataframe.loc['PHSR023']
        pg_net_income_per_avg_asset_sept2019= self.dataframe.loc['PHSR023_4Q']
        pg_net_income_per_avg_asset_dec2019 = self.dataframe.loc['PHSR023_1Y']
        pg_net_income_per_avg_asset_dec2018 = self.dataframe.loc['PHSR023_2Y']
        pg_net_income_per_avg_asset_dec2017 = self.dataframe.loc['PHSR023_3Y']

        bank_dates = make_bank_dates(quarter, year)
        



        tcbi_income_per_asset_lst =[net_income_per_avg_asset_dec2017,net_income_per_avg_asset_dec2018,net_income_per_avg_asset_sept2019,net_income_per_avg_asset_dec2019, net_income_per_avg_asset_sept2020]   
        converted_tcbi_income_per_asset_lst= (convert_bank_data_to_floatv2(tcbi_income_per_asset_lst))
        pg_income_per_asset_lst = [pg_net_income_per_avg_asset_dec2017,pg_net_income_per_avg_asset_dec2018, pg_net_income_per_avg_asset_sept2019,pg_net_income_per_avg_asset_dec2019, pg_net_income_per_avg_asset_sept2020]
        converted_pg_income_per_asset_lst= (convert_bank_data_to_floatv2(pg_income_per_asset_lst))

        x = np.arange(len(bank_dates)) 
        width = 0.35  

        fig, ax = plt.subplots(figsize = (12, 8))
        tcbi_income_per_asset_ax = ax.bar(x - width/2, converted_tcbi_income_per_asset_lst, width, label=f'{Bank_name}')
        pg_income_per_asset_ax = ax.bar(x + width/2, converted_pg_income_per_asset_lst, width, label='Peer Group n=130')


        ax.set_ylabel('Ratio', fontsize =12)
        ax.set_title('NET OPERATING INCOME / AVERAGE ASSETS (YTD)', Fontsize = 24)
        ax.set_xticks(x)
        ax.set_xticklabels(bank_dates)
        ax.legend()
        autolabel(tcbi_income_per_asset_ax,ax)
        autolabel(pg_income_per_asset_ax, ax)
        
        plt.show()
    
    def net_loan_losses_by_type(self, quarter = 'sept', year = 2020, Bank_name = 'Bank'):
        """Makes a graph of net loan losses of Commerical and Industrial loans

        Args:
            dataframe ([pandas dataframe]): CSV file of BHCPR
            quarter (str, optional): [start month of quarter of interset]. Defaults to 'sept'.
            year (int, optional): [Year of CSV BHCPR]. Defaults to 2020.
            Bank_name (str, optional): [Name of Bank in BHCPR file for labeling purposes]. Defaults to 'Bank'.
        """
        
        #Net Commerical & Industrial Loan Losses
        net_losses_type_CI_sept2020 = self.dataframe.loc['BHSR247']
        net_losses_type_CI_sept2019 = self.dataframe.loc['BHSR247_4Q']
        net_losses_type_CI_dec2019 = self.dataframe.loc['BHSR247_1Y']
        net_losses_type_CI_dec2018 = self.dataframe.loc['BHSR247_2Y']
        net_losses_type_CI_dec2017 = self.dataframe.loc['BHSR247_3Y']
        
        #Peer group CI losses:
        pg_net_losses_type_CI_sept2020 = self.dataframe.loc['PHSR247']
        pg_net_losses_type_CI_sept2019 = self.dataframe.loc['PHSR247_4Q']
        pg_net_losses_type_CI_dec2019 = self.dataframe.loc['PHSR247_1Y']
        pg_net_losses_type_CI_dec2018 = self.dataframe.loc['PHSR247_2Y']
        pg_net_losses_type_CI_dec2017 = self.dataframe.loc['PHSR247_3Y']

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
    def net_loan_losses(self, quarter = 'sept', year = 2020, Bank_name = 'Bank'):
        """Makes a graph of net loan losses of a Bank from BHCPR CSV file

        Args:
            dataframe ([pandas dataframe]): CSV file of BHCPR
            quarter (str, optional): [start month of quarter of interset]. Defaults to 'sept'.
            year (int, optional): [Year of CSV BHCPR]. Defaults to 2020.
            Bank_name (str, optional): [Name of Bank in BHCPR file for labeling purposes]. Defaults to 'Bank'.
        """

        net_loan_losses_sept2020 = self.dataframe.loc['BHSR853']
        net_loan_losses_sept2019 = self.dataframe.loc['BHSR853_4Q']
        net_loan_losses_dec2019 = self.dataframe.loc['BHSR853_1Y']
        net_loan_losses_dec2018 = self.dataframe.loc['BHSR853_2Y']
        net_loan_losses_dec2017 = self.dataframe.loc['BHSR853_3Y']

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
    
    def prov_net_loan_losses(self, quarter = 'sept', year = 2020, Bank_name = 'Bank'):
        """ Makes a graph of provision of loan losses and net loan losses of a Bank from BHCPR CSV file

        Args:
            dataframe ([pandas dataframe]): CSV file of BHCPR
            quarter (str, optional): [start month of quarter of interset]. Defaults to 'sept'.
            year (int, optional): [Year of CSV BHCPR]. Defaults to 2020.
            Bank_name (str, optional): [Name of Bank in BHCPR file for labeling purposes]. self.Defaults to 'Bank'.
        """
        
        
        provison_loan_losses_q2020 = self.dataframe.loc['BHCK4230']
        provison_loan_losses_q2019 = self.dataframe.loc['BHCK4230_4Q']
        provison_loan_losses_dec2019 = self.dataframe.loc['BHCK4230_1Y']
        provison_loan_losses_dec2018 = self.dataframe.loc['BHCK4230_2Y']
        provison_loan_losses_dec2017 = self.dataframe.loc['BHCK4230_3Y']
        
        '''net loan loss values for Bank_name'''
        net_loan_losses_sept2020 = self.dataframe.loc['BHSR853']
        net_loan_losses_sept2019 = self.dataframe.loc['BHSR853_4Q']
        net_loan_losses_dec2019 = self.dataframe.loc['BHSR853_1Y']
        net_loan_losses_dec2018 = self.dataframe.loc['BHSR853_2Y']
        net_loan_losses_dec2017 = self.dataframe.loc['BHSR853_3Y']

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
        

        
        # fig.savefig("JPM_provisions&_losses.png", dpi=200)
        plt.show()


url_banks = {

    'JPM':"https://www.ffiec.gov/npw/Institution/Profile/1039502?dt=20190519"
    , 'BAC':"https://www.ffiec.gov/npw/Institution/Profile/1073757?dt=20141231"
    , "C":"https://www.ffiec.gov/npw/Institution/Profile/1951350?dt=20170701"
    ,"WFC":"https://www.ffiec.gov/npw/Institution/Profile/1120754?dt=20200331"
    , 'GS': "https://www.ffiec.gov/npw/Institution/Profile/2380443?dt=20150101"

} 


def file_path_maker():

    download_dir = "/Users/cp/Documents/dsi/practice"
    bank_csv_file_path = []
    bank_csv_file_path_dct = {}
    for k, v in url_banks.items():
        pattern = "https://www.ffiec.gov/npw/Institution/Profile/(.*?)\?dt="
        substring = re.search(pattern, v).group(1) 
        # print (substring)
        final_name = f'/BHCPR_{substring}_20201231.csv'
        # print(final_name)
        file_path = download_dir+final_name
        # print(file_path)
        bank_csv_file_path.append(file_path)
        bank_csv_file_path_dct[k] = file_path
    # print(bank_csv_file_path)
    # print(bank_csv_file_path_dct)
    return bank_csv_file_path_dct



bank_dct = (file_path_maker())

# objs = [bank() for i in range(len(bank_dct))]
# for obj in objs:
#     obj[k]

# objs[0].do_sth()
holder = {}
lst1 = []
for k, v in bank_dct.items():
    # holder = {k: MyClass(name=name) for name in instanceNames}
    df = pd.read_csv(v,index_col='ItemName')
    bank1 = bank(df, k)
    lst1.append(bank1)
print(lst1)

JPM, BAC, C, WFC, GS =lst1 
BAC.prov_net_loan_losses()
    
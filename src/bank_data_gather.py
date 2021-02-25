import pandas as pd
import numpy as np
import matplotlib as plt
import scipy.stats as stats
import matplotlib.pyplot as plt

def make_bank_dates(quarter, year):

    current_q = (quarter +str(year))
    dec_year_before = ('dec'+ str(year-1))
    year_before_q = (quarter + str(year-1))
    dec_2year_before = ('dec'+ str(year-2))
    dec_3year_before = ('dec'+ str(year-3))
    bank_dates = [dec_3year_before ,  dec_2year_before,  year_before_q,dec_year_before, current_q ]
    return bank_dates



def divide_1000(lst):
    lst1 = []
    for i in lst:
        i = i/1000
        i = round(i, 1)
        lst1.append(i) 
    return lst1



def convert_bank_data_to_float(data_lst):
    
    lst = []
    for i in data_lst:
        i = float(i[2])
        lst.append(i)
    return lst
def convert_bank_data_to_floatv2(data_lst):
    
    lst = []
    for i in data_lst:
        i = float(i[1])
        lst.append(i)
    return lst

def autolabel(rects, ax):
   
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

if __name__ == "__main__":
    pass









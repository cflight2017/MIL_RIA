#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:53:40 2020

@author: christienwright
"""





#%% Who is currently the most undervalued player in the NBA?  Limit text to 500 words.

import pandas as pd
import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

data = pd.read_csv('~/Injury Analytics/player_info.csv')


#%%
#All players as of 2020 prior to NBA draft 
data_filter = data[(data['From'] >= 2000) & (data['To'] == 2020)]



salary_data = pd.DataFrame()
parent_link = 'https://www.basketball-reference.com'
salary_ = '#all_all_salaries'

driver = webdriver.Safari()

contract = pd.DataFrame()

for i in range(len(data_filter)):
    try:
        link = parent_link + str(data_filter.player_link.iloc[i]) + salary_
        print(data_filter.player_link.iloc[i])
        driver.implicitly_wait(30)
        driver.get(link)
        
        #After opening the url above, Selenium clicks the specific agency link
        python_button = driver.find_element_by_id('div_contract')
        
        python_button.click() #click the table with salaries
        
        soup_level1=BeautifulSoup(driver.page_source, 'lxml')
        
        #Beautiful Soup grabs the HTML table on the page
        table = soup_level1.find_all('table')
        
        df = pd.read_html(str(table),header=0)
        
        salary = list(filter(lambda x: 'Team' in x, df))
        
        
        salary_df = pd.DataFrame(salary[0])
        current_contract = pd.DataFrame(salary[1])
        current_contract['player_link'] = data_filter.player_link.iloc[i]
        contract = contract.append(current_contract)
        salary_df['player_link'] = data_filter.player_link.iloc[i]
        salary_data = salary_data.append(salary_df)
    
        time.sleep(1)
    except:
        continue
    


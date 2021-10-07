import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import os
import datetime 
cu_date = datetime.datetime.now()
pr_d = datetime.timedelta(days = 90)
last_90 = cu_date - pr_d
data = pd.read_excel("List of Stocks case study (1).xlsx")
os.mkdir("every_company_outputfile")
for i in range(len(data['SYMBOL    '])):
    z = data['SYMBOL    '][i]
    stock_data = yf.download(z, start = last_90,end =cu_date )
    stock_data['Close'].to_csv("every_company_outputfile/{}.csv".format(z))
#### Importing Libraries and Modules
import pandas as pd
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import numpy as np

#### Getting data from Yahoo Finance
amd = pd.read_csv('AMD.csv', header=0, index_col='Date', parse_dates=True)
nvda = pdr.get_data_yahoo('NVDA', start=datetime.datetime(2004,1,1), end=datetime.datetime(2019,12,31))
qcom = pdr.get_data_yahoo('QCOM', start=datetime.datetime(2004,1,1), end=datetime.datetime(2019,12,31))
intc = pdr.get_data_yahoo('INTC', start=datetime.datetime(2004,1,1), end=datetime.datetime(2019,12,31))
ibm  = pdr.get_data_yahoo('IBM', start=datetime.datetime(2004,1,1), end=datetime.datetime(2019,12,31))

#### Graph 1: Adjusted Closing values v/s time
plt.plot(ibm.index, ibm['Adj Close'])
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.grid(True)
plt.xticks(rotation=45)
plt.title("IBM [January 2004 to December 2019]")
plt.xlabel("Year")
plt.ylabel("Adjusted Close")
plt.show()

#### Adjusted Closing Values v/s Time (for other considered companies)
f, ax = plt.subplots(2, 2, figsize=(10,10), sharex=True)
f.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
f.gca().xaxis.set_major_locator(mdates.YearLocator())

ax[0,0].plot(nvda.index, nvda['Adj Close'], color='r')
ax[0,0].grid(True)
ax[0,0].tick_params(labelrotation=45)
ax[0,0].set_title('NVIDIA');

ax[0,1].plot(intc.index, intc['Adj Close'], color='g')
ax[0,1].grid(True)
ax[0,1].tick_params(labelrotation=45)
ax[0,1].set_title('INTEL');

ax[1,0].plot(qcom.index, qcom['Adj Close'], color='b')
ax[1,0].grid(True)
ax[1,0].tick_params(labelrotation=45)
ax[1,0].set_title('QUALCOMM');

ax[1,1].plot(amd.index, amd['Adj Close'], color='y')
ax[1,1].grid(True)
ax[1,1].tick_params(labelrotation=45)
ax[1,1].set_title('AMD');
plt.show()

#### Resampling (Up-Sampling)
ibm_18 = ibm.loc[pd.Timestamp('2019-01-01'):pd.Timestamp('2019-12-31')]
plt.plot(ibm_18.index, ibm_18['Adj Close'])
plt.grid(True)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)
plt.title("Up-Sampling (IBM)")
plt.xlabel("Year-Month")
plt.ylabel("Adjusted Close")
plt.show()

#### Resampling (Quarterly)
nvda_18 = nvda.loc[pd.Timestamp('2018-11-01'):pd.Timestamp('2019-12-31')]
monthly_nvda_18 = nvda_18.resample('4M').mean()
plt.plot(monthly_nvda_18.index, monthly_nvda_18['Adj Close'])
plt.grid(True)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45)
plt.title("Resampling (Quarterly) for Nvidia")
plt.xlabel("Year-Month")
plt.ylabel("Adjusted Close")
plt.show()

#### Analysing Difference between Levels (Resampling Weekly)
nvda['diff'] = nvda['Open'] - nvda['Close']
nvda_diff = nvda.resample('W').mean()
intc['diff'] = intc['Open'] - intc['Close']
intc_diff = intc.resample('W').mean()
qcom['diff'] = qcom['Open'] - qcom['Close']
qcom_diff = qcom.resample('W').mean()
amd['diff'] = amd['Open'] - amd['Close']
amd_diff = amd.resample('W').mean()

f, ax = plt.subplots(2, 2, figsize=(10,10), sharex=True, sharey=True)

ax[0,0].scatter(nvda_diff.loc['2019-01-01':'2019-12-31'].index, nvda_diff.loc['2019-01-01':'2019-12-31']['diff'], color='r')
ax[0,0].grid(True)
ax[0,0].tick_params(labelrotation=45)
ax[0,0].set_title('NVIDIA');

ax[0,1].scatter(intc_diff.loc['2019-01-01':'2019-12-31'].index, intc_diff.loc['2019-01-01':'2019-12-31']['diff'], color='g')
ax[0,1].grid(True)
ax[0,1].tick_params(labelrotation=45)
ax[0,1].set_title('INTEL');

ax[1,0].scatter(qcom_diff.loc['2019-01-01':'2019-12-31'].index, qcom_diff.loc['2019-01-01':'2019-12-31']['diff'], color='b')
ax[1,0].grid(True)
ax[1,0].tick_params(labelrotation=45)
ax[1,0].set_title('QUALCOMM');

ax[1,1].scatter(amd_diff.loc['2019-01-01':'2019-12-31'].index, amd_diff.loc['2019-01-01':'2019-12-31']['diff'], color='y')
ax[1,1].grid(True)
ax[1,1].tick_params(labelrotation=45)
ax[1,1].set_title('AMD');
plt.show()

#### Moving Windows (Daily Percentages)
daily_close_ibm = ibm[['Adj Close']]
daily_pct_change_ibm = daily_close_ibm.pct_change()
daily_pct_change_ibm.fillna(0, inplace=True)
daily_pct_change_ibm.hist(bins=50)
plt.title("Adjusted Close Analysis for IBM")
plt.show()

#### Windows Windows Comparison
daily_close_nvda = nvda[['Adj Close']]
daily_pct_change_nvda = daily_close_nvda.pct_change()
daily_pct_change_nvda.fillna(0, inplace=True)
daily_close_intc = intc[['Adj Close']]
daily_pct_change_intc = daily_close_intc.pct_change()
daily_pct_change_intc.fillna(0, inplace=True)
daily_close_qcom = qcom[['Adj Close']]
daily_pct_change_qcom = daily_close_qcom.pct_change()
daily_pct_change_qcom.fillna(0, inplace=True)
daily_close_amd = amd[['Adj Close']]
daily_pct_change_amd = daily_close_amd.pct_change()
daily_pct_change_amd.fillna(0, inplace=True)
sns.set()
f, axes = plt.subplots(2, 2, figsize=(12, 7))
sns.distplot(daily_pct_change_nvda['Adj Close'], color="b", ax=axes[0, 0], axlabel='NVIDIA');
sns.distplot(daily_pct_change_intc['Adj Close'], color="r", ax=axes[0, 1], axlabel='INTEL');
sns.distplot(daily_pct_change_qcom['Adj Close'], color="g", ax=axes[1, 0], axlabel='QUALCOMM');
sns.distplot(daily_pct_change_amd['Adj Close'], color="m", ax=axes[1, 1], axlabel='AMD');
plt.show()

#### Volatility of Stocks
min_periods = 75
vol = daily_pct_change_ibm.rolling(min_periods).std() * np.sqrt(min_periods)
vol.fillna(0,inplace=True)
vol.plot(figsize=(10, 8))
plt.title("Volatility for IBM")
plt.show()

#### Rolling Average (Trends)
ibm_adj_close_px = ibm['Adj Close']
ibm['42'] = ibm_adj_close_px.rolling(window=40).mean()
ibm['252'] = ibm_adj_close_px.rolling(window=252).mean()
ibm[['Adj Close', '42', '252']].plot(title="IBM")
plt.show() 

#### End of code
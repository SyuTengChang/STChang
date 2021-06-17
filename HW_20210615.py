#%%
import time
import numpy as np
import pandas as pd

df = pd.read_csv('D:\Data_Analysis\A咖訓練營\homework.csv')  # df.to_csv(index = False)
#df
#%%
# --------------- 2021/6/15 HW_Q1__Syu Teng Chang的解法 ----------------------
#numpy
start = time.process_time()
#start = time.time()

df1 = np.array(df,dtype = 'float')

npmedian = np.median(df1, axis = 0)
npmean = np.mean(df1, axis = 0)
npmax = np.max(df1, axis = 0)
npmin = np.min(df1, axis = 0)


end = time.process_time()
#end = time.time()
print(f"numpy 運算共花了 {(end - start):.4f} 秒")

#pandas
start1 = time.process_time()
#start1 = time.time()

dfmedian = df.median(axis = 0)
dfmean = df.mean(axis = 0)
dfmax = df.max(axis = 0)
dfmin = df.min(axis = 0)

end1 = time.process_time()
#end1 = time.time()
print(f"pandas 運算共花了 {(end1 - start1):.4f} 秒")

#%%
#----------------------------- 2021/6/15 HW_Q2__Syu Teng Chang的解法 --------------------

dfstd = df.std(axis = 0)

Deviation = df - dfmean  #離差

df_DelOutlier = df1[ Deviation.abs() <= 3*dfstd ] #取不超過3個標準差之data












#!/usr/bin/env python
# coding=utf-8
# Created by denghui on 2018/4/12.
#1. 请百度numpy中的loadtxt函数，将所有的数据读入一个二维numpy数组。请注意其中的头部（需要跳过）。
#2. 这个是苹果 公司的股票数据 ， 请分析出在这一段时间的股票平均价格 。
#3. 出在这一段时间内的苹果 公司股票变化图（曲线图）。其中要包括：开盘价，收盘价的曲线变化
#4. 统计有多少天的数据在平均价格以上，多少天在平均价格以上。
#5. 按每周（自然周），计算每周的股票平均价格 。

import numpy as np
from datetime import datetime,time
import os
import matplotlib.pyplot as plt
import matplotlib.dates

def get_weekNo(strdate:str):
    date=datetime.strptime(strdate.strip('b').strip('\''),'%Y/%m/%d') #去掉字符串里的无效字符，把字符串转换成日期
    yearNo,weekNo,dayNo=datetime.isocalendar(date)
    return '%4s%02d'%(yearNo,weekNo)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y%m%d'))
ax.xaxis.set_major_locator(matplotlib.dates.DayLocator(interval=1))

filename=os.getcwd()+'/apple.csv'
apple_datatype=np.dtype({'names':['date','open','high','low','close','vol'],
                         'formats':['S15','f','f','f','f','i']})
apple_data=np.loadtxt(filename,skiprows=1,delimiter=',',dtype=apple_datatype)
apple_datatype_do=np.dtype({'names':['avg_day','year','week','avg_week','yearweek'],'formats':['f','S4','S2','f','S6']})
apple_data_do=np.empty(apple_data.shape,dtype=apple_datatype_do)
apple_data_do[:]['yearweek']=[get_weekNo(str(strdate)) for strdate  in apple_data[:]['date']]
apple_data_do[:]['avg_day']=(apple_data[:]['open']+apple_data[:]['close'])/2.
apple_data_do[:]['year']=[yearweek[:4] for yearweek in apple_data_do[:]['yearweek']]
apple_data_do[:]['week']=[yearweek[4:] for yearweek in apple_data_do[:]['yearweek']]
yearweek=np.unique(apple_data_do[:]['yearweek'])
avg_week=np.zeros(yearweek.shape,dtype='f')
t=np.empty(yearweek.shape,dtype=str)
for i,y in enumerate(yearweek):
    idx=np.where(apple_data_do[:]['yearweek']==y)
    avg_week[i]=np.mean(apple_data_do[idx]['avg_day'])
    #t[i]=datetime.datetime.strptime('2016/1/1', '%Y/%m/%d')
#xs=[datetime.datetime.strptime(t, '%Y%m%d') for t in yearweek]

ax.axes.set_xticks(yearweek)
ax.axes.set_xticklabels(yearweek,rotation=40)
plt.plot(yearweek,avg_week,'--*')
plt.show()



pass
#apple_data_do[:]['year']=[get_weekNo(str(strdate)) for strdate  in apple_data[:]['date']]

#apple_data_do[:]['week']=[get_weekNo(str(strdate))[0] for strdate  in apple_data[:]['date']]

#apple_date=np.loadtxt(filename,skiprows=1,delimiter=',',dtype=np.str,usecols=0)
#apple_price=np.loadtxt(filename,skiprows=1,delimiter=',',dtype=np.float,usecols=range(1,5))
#apple_vol=np.loadtxt(filename,skiprows=1,delimiter=',',dtype=np.int,usecols=5)
#apple_weekday=np.array(list(map(get_weekday,apple_date)))
#apple_week=[get_weekNo(strdate) for strdate  in apple_date]




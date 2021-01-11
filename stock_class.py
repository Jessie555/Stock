########################################
#             Stock Class              #
#--------------------------------------#
#         Jessie Fehrenbach            #
########################################
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as datetime
import pandas_datareader.data as web
import os
import math


class stock:

    def __init__(self, name, start, end):
        self.name = name #string
        self.start = start
        self.end = end # datetime funtion
        
    
    def history_data(self):
        hist = web.DataReader(self.name,'yahoo',self.start, self.end)
        return hist
        
        
    def returnP(self):
        stonk = self.history_data()
        close = stonk['Close']
        returnlist = []
        for i in range(len(close)):
            if i != 0:
                returnVal = (close[i]/close[i-1])-1
                returnlist.append(returnVal)
            else:
                returnlist.append(0)
        stonk['Return'] = returnlist  #hopefully places a new collumn for the return rate
        return stonk
    
    def standard_deviation(self):
        stonk = self.returnP()
        array = []
        mean = sum(stonk['Return'])/stonk.count()['Return']
        for i in range(stonk.count()['Return']):
            array.append((stonk['Return'][i] - mean)**2)
        std = math.sqrt(sum(array)/len(array))
        return std
    
    def cum_return(self):
        stonk = self.returnP()
        stonk['Cumreturn'] = (stonk['Return']+1).cumprod()
        return stonk
    
    def yfticker(self): #should not be called by user
        stonk = yf.Ticker(self.name)
        info = stonk.info
        return info
    
    def PEG(self):
        info = self.yfticker()
        PEG = info['pegRatio']
        return PEG
    
    def FPE(self):
        info = self.yfticker()
        FPE = info['forwardPE']
        return FPE
    
    def price_book(self):
        info = self.yfticker()
        priceToBook = info['priceToBook']
        return priceToBook
    

stonk = stock('CHOLF', datetime.datetime(2016,12,31),datetime.datetime.now())
print(stonk.history_data())



        

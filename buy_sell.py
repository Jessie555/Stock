########################################
#             buy sell                 #
#--------------------------------------#
#         Jessie Fehrenbach            #
########################################
#This class will be responsible for buying 1 stock
#and pushing it to a csv file
#Does not make the descision, only does it

#from stock_class import stock
import stock_class as st
import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
import datetime
import time
class descision(st):

    def __init__(self, name, money): 
        self.name = name           
        self.money = money
    
    def buy(self):
        stock = st.stock(self.name ,datetime.datetime(2016,12,31),datetime.datetime.now()) 
        hist = stock.history_data()

        

file = open('growers.txt','r')
names = []
money = 1000
for i in file:
    names.append(str(i))
y = descision(names[0], money)
y.buy()
start = datetime.datetime(2016, 12, 31)
end = datetime.datetime.now()
#stock = st.stock('CHOLF',start, end)


#print(y.buy())
#start = datetime.datetime(2020,1,7)
#current = datetime.datetime.now()
#x = stock('TSLA',start, end)




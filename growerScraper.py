########################################
#             scraping                 #
#--------------------------------------#
#         Jessie Fehrenbach            #
########################################

import pandas as pd
file = open('growers.txt', 'w')
url = 'https://finance.yahoo.com/gainers'

dfs = pd.read_html(url)

print(dfs[0]['Symbol'])
for i in dfs[0]['Symbol']:
    file.write(i)
    file.write('\n')
file.close()

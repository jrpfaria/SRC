# pip install pygeoip
# pip install fastparquet 
# pip install dnspython
import pandas as pd
import numpy as np
import ipaddress
import dns.resolver
import dns.reversename
import pygeoip
import matplotlib.pyplot as plt 

datafile='dataset8/data8_mod2.parquet'
data=pd.read_parquet(datafile)
testfile='dataset8/test8_mod2.parquet'
test=pd.read_parquet(testfile)
serversfile='dataset8/servers8.parquet'
servers=pd.read_parquet(serversfile)

test.groupby(['timestamp'])[['down_bytes', 'up_bytes']].sum().plot()
plt.savefig('playing.png')
plt.close()

a = test.loc[(test['src_ip']=='192.168.108.97')].loc[(test['up_bytes']>=2*(10^8))]['timestamp'].diff().fillna(0).sort_index()
for x in a.keys():
    print(x, a[x])
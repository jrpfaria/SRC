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

# datafile='dataset8/data8_mod2.parquet'
# data=pd.read_parquet(datafile)
# testfile='dataset8/test8_mod2.parquet'
# test=pd.read_parquet(testfile)
serversfile='dataset8/servers8.parquet'
servers=pd.read_parquet(serversfile)

fig, ax = plt.subplots()
#a0=servers.groupby(['src_ip'])['timestamp'].diff().fillna(0).mean()
servers['diff_timestamp']=servers.groupby(['src_ip'])['timestamp'].diff().fillna(0)
servers.groupby(['src_ip'])['diff_timestamp'].max().sort_values(ascending=False).plot(kind='barh', figsize=(10,25))
#a0.sort_values().plot(kind='barh', figsize=(10,25))
plt.tight_layout()
plt.savefig('playing.png')
plt.close()

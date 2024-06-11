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

test['diff_timestamp']=test.groupby(['src_ip'])['timestamp'].diff()
print(test.groupby(['src_ip'])['diff_timestamp'].mean().sort_values(ascending=False))

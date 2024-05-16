import pandas as pd
import numpy as np
df = pd.read_csv('customer_rec.csv')
df1 = pd.read_csv('customer_info.csv')
df.head()
df.isnull().sum()
df.drop(columns=['Reference','Purchase order no.','Text','Terms of Payment'])
df.dropna()
df1.head()
df1.isnull().sum()
df1.drop(columns=['Street','Postal Code','City','Currency','Telephone 1','Payment Term (Sales Org)','Created on'])
customer_df= pd.merge(df,df1, on='Customer_ID')
customer_df.head()
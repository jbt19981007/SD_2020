#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_excel('/Users/Toby/Documents/Soverign_Debt/EM777_Group Project1_Data_20200101-20210331_tidydata.xlsx')
df1 = pd.read_excel('/Users/Toby/Documents/Soverign_Debt/country_list_two_words_aug8.xlsx',sheet_name="alt_names2")

# df1 = df[df['Full Text'].str.contains("US",na=False,case=True)]
# def increment():
# 	n = 0
# 	print(n)

# 	while True:
# 	    n += 1
# 	    print(n)
# print(df1.columns)

lst = []
country_list = df1['country'].tolist()
def count_country(thislist):
	for i in thislist:
		count=sum(df['Full Text'].str.contains(i,na=False,case=False))
		# print(i,count)
		lst.append([i,count])

count_country(country_list)
print(lst)
cols=['country','count']
df2 = pd.DataFrame(lst, columns=cols)
df2.to_excel('/Users/Toby/Documents/Soverign_Debt/country_adj_count_aug8.xlsx')
# df1.to_excel('/Users/Toby/Downloads/US_count_aug8.xlsx')
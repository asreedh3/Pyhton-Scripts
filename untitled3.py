#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 13:23:35 2020

@author: asreedhar
"""
import pandas as pd
list1 =['cat', 'dog', 'bus']
list2 =['cat', 'bus', 'truck']
list3= [x for x in list2 if x not in list1]
list4=[x for x in list2 if x in list1]

#creating a dictionary from a dataframe
dfdictionary ={'dominant':df_dominant,'underrepresented': df_underrepresented}

print(dfdictionary['dominant'].head())

#accessing a given dictionary from a data frame
df_from_dictionary=dfdictionary['dominant']

dictionary={1234:df_dominant,5678:df_underrepresented}
df_dominant.head()

print(dictionary[1234].head())

#removing a given element from a list
list2.remove('cat')

list5=['cat','dog', 'tiger', 'bus', 'truck', 'bus', 'cat']
#removing the duplicate elements present in the list
list5=list(set(list5))

#pre and post index of a column in a dataframe

df_new=pd.DataFrame(list5)
list6=[]

#for getting the index use item and for the actual item use frame
for item,frame in df_new[0].iteritems():
    if (frame=='tiger'):
        if (item==0): # zero preindex check
            preindex=0
        else:
            preindex=item-1

        list6.append(item)



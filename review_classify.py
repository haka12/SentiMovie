#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pickle
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)  
pd.set_option('display.max_colwidth', -1)
#from dataformatting import index
count=1
from chatpreprocessing import file_name


def reviewclassify(parsed_sent,index):
    with open("trainedmodel",'rb') as f:
        tf,svc=pickle.load(f)
        
# =============================================================================
#         data=pd.read_csv('/home/baka/SentiMovie/LionKing.csv')z
#         df=data['review']
# =============================================================================
        
        data=pd.read_csv('/home/baka/SentiMovie/'+file_name(parsed_sent))
        review=data.iat[int(index),11]
        review=review.replace("A review by",'|')
        review=review+'|'
        count=0
        br_pos=[]
        rev=[]
        for r in review:
            count+=1
            if r=='|':
                br_pos.append(count)
            #print(br_pos)
            #print(review[br_pos[0]:br_pos[1]])
        ran=len(br_pos)
        try:
            for i in range(0,ran):
                revi=review[br_pos[i]:br_pos[i+1]]
                rev.append(revi)
        except IndexError:
            pass
        df=pd.DataFrame(rev)
        if count%2==0:
            daf=df.iloc[:,0]
            print(daf[0:])
            tr=tf.transform(daf)
        else:
            dafe=df.iloc[:,0]
            print(dafe[0:])
            tr=tf.transform(dafe)
        count+=1  
        for senti in (svc.predict(tr)):
            if senti==1:
                print("positive")
            else:
                print("negative")
        #return review
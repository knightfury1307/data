import pandas as pd
import numpy as np

df  = pd.read_csv('tweets.csv')

#print(df['Tweet'])
def checkWord(text):
    count =0
    myList = ['fuck', 'shit','ten' , 'toxic' , 'to','stupid','yelling' ,'Mfs' ,'kill' ,'armed' , 'penalty' ,'drop','dead' , 'deleted' , 'bitch' ,'fight' , 'dumb' ,'danger' ]
    for x in myList :
        if x in text :
            count = count +1
    myList2 = ['happy', 'love','adorable' ,'awesome','nice' ]
    for x in myList2 :
        if x in text :
            count = count -1   
    checkCount(count)
    return count
            
    

def checkCount(count):
    if count<0 :
        count = 0
    elif count >5 :
        count =5      
    #print(count)    
            

df['Profanity'] = df.apply(lambda row : checkWord(row['Tweet']) ,axis=1 )                        

df.to_csv('modi.csv')
    







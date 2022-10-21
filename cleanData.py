#cleanData.py


import numpy as np
import pandas as pd
import os

def read_data(dirname):
    #new data frame 
    stats = pd.DataFrame(columns = ['Player', 'Pos', 'PassingYds', 'PassingTD', 
        'PassingAtt', 'Cmp', 'RushingAtt', 'RushingYds', 'RushingTD', 'Rec', 'Tgt',
        'ReceivingYds', 'ReceivingTD', 'HalfPPRFantasyPoints'])
    
    #reads in every file in the folder
    for f in os.listdir(dirname):
        df = pd.read_csv(os.path.join(dirname, f))
        #concats to main df
        stats = pd.concat([stats, df], ignore_index=True)
    
    return stats

def get_positions(df):

    return {'qb': , 'rb': , 'wr': , 'te': }
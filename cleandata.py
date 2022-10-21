#cleandata.py


import numpy as np
import pandas as pd
import os


def read_data(dirname):
    """
    Takes in a filepath and returns a dataframe containing
    all the dataframes combined.
    """
    #new data frame keeping relevant stats
    stats = pd.DataFrame(columns = ['Player', 'Pos', 'PassingYds', 'PassingTD', 
        'PassingAtt', 'Cmp', 'RushingAtt', 'RushingYds', 'RushingTD', 'Rec', 'Tgt',
        'ReceivingYds', 'ReceivingTD', 'HalfPPRFantasyPoints'])
    
    #reads in every file for every year in the data folder
    for folder in os.listdir(dirname)
        for f in os.listdir(os.path.join(dirname, folder)):
            df = pd.read_csv(os.path.join(dirname, folder, f))
            #concats to main df
            stats = pd.concat([stats, df], ignore_index=True)
    
    return stats


def get_positions(df):
    """
    Takes in a combined dataframe and returns a cleaned
    dataframe for each position.
    """
    qb_predictors = ["PassingYds", "PassingTD", "PassingAtt", "Cmp", "RushingAtt", "RushingYds", "RushingTD"]
    rb_predictors = ["RushingAtt", "RushingYds", "RushingTD", "Rec", "Tgt", "ReceivingYds", "ReceivingTD"]
    wr_predictors = ["Rec", "Tgt", "ReceivingYds", "ReceivingTD"]
    te_predictors = ["Rec", "Tgt", "ReceivingYds", "ReceivingTD"]
    qb = df[df['Pos'] == 'QB']
    rb = df[df['Pos'] == 'RB']
    wr = df[df['Pos'] == 'WR']
    te = df[df['Pos'] == 'TE']

    return {'qb': qb, 'rb': rb, 'wr': wr, 'te': te}

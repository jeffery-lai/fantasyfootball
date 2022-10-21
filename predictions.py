#predictions.py


import numpy as np
import pandas as pd
import os
import seaborn as sns
from sklearn.linear_model import LinearRegression
from cleandata import *


def train_model(df, pos):
    """
    Takes in a cleaned dataframe containing players and
    an argument with specified position and returns
    predictions for players in HalfPPR points.
    """
    #Determines predictors depending on position
    if pos.lower() == 'qb':
        predictors = ["PassingYds", "PassingTD", "PassingAtt", "Cmp", "RushingAtt", "RushingYds", "RushingTD"]
    elif pos.lower() == 'rb':
        predictors = ["RushingAtt", "RushingYds", "RushingTD", "Rec", "Tgt", "ReceivingYds", "ReceivingTD"]
    elif (pos.lower() == 'wr') | (pos.lower() == 'te'):
        #predicting WR and TE positions with similar features as they have similar roles for scoring in fantasy
        predictors = ["Rec", "Tgt", "ReceivingYds", "ReceivingTD"]
    else:
        raise ValueError("Invalid Position.")
    
    #target for preditions
    target = "HalfPPRFantasyPoints"
    #run linear regression from sklearn
    reg = LinearRegression()
    reg.fit(df[predictors], df[target])
    return reg


def predictions(df, pos, reg):
    #Determines predictors depending on position
    if pos.lower() == 'qb':
        predictors = ["PassingYds", "PassingTD", "PassingAtt", "Cmp", "RushingAtt", "RushingYds", "RushingTD"]
    elif pos.lower() == 'rb':
        predictors = ["RushingAtt", "RushingYds", "RushingTD", "Rec", "Tgt", "ReceivingYds", "ReceivingTD"]
    elif (pos.lower() == 'wr') | (pos.lower() == 'te'):
        #predicting WR and TE positions with similar features as they have similar roles for scoring in fantasy
        predictors = ["Rec", "Tgt", "ReceivingYds", "ReceivingTD"]
    else:
        raise ValueError("Invalid Position.")
    
    df_predictions = df.copy()
    #add predictions in column
    predictions = reg.predict(df_predictions[predictors])
    df_predictions["PredictedPoints"] = predictions
    df_predictions = df_predictions[["Player", "PredictedPoints"]]
    df_predictions = df_predictions.groupby("Player").mean().sort_values("PredictedPoints", ascending = False)
    df_predictions["PredictedPoints"] = np.round(df_predictions["PredictedPoints"], 2)
    return df_predictions

#fantasyfootball.py


import numpy as np
import pandas as pd
import os
from cleandata import *
from predictions import *


def main():
    #separate all players into respective positions
    train = read_data(os.path.join('data', 'train'))
    all_pos = get_positions(train)
    qb = all_pos['qb']
    rb = all_pos['rb']
    wr = all_pos['wr']
    te = all_pos['te']
    #train all models for all positions
    qb_reg = train_model(qb, 'qb')
    rb_reg = train_model(rb, 'rb')
    wr_reg = train_model(wr, 'wr')
    te_reg = train_model(te, 'te')
    #gets current year's data for each player to predict next year's performances
    test_data = read_data(os.path.join('data', 'test'))
    qb_test = get_positions(test_data)['qb']
    rb_test = get_positions(test_data)['rb']
    wr_test = get_positions(test_data)['wr']
    te_test = get_positions(test_data)['te']
    #stores predictions as csv files in predictions folder
    os.makedirs('predictions', exist_ok=True)  
    predictions(qb_test, 'qb', qb_reg).to_csv('predictions/qb.csv')  
    predictions(rb_test, 'rb', rb_reg).to_csv('predictions/rb.csv')  
    predictions(wr_test, 'wr', wr_reg).to_csv('predictions/wr.csv')  
    predictions(te_test, 'te', te_reg).to_csv('predictions/te.csv')

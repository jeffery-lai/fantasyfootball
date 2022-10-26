# fantasyfootball

Generates Half PPR projections for the 2022-23 season of fantasy 
football using data from the previous year. Uses machine learning 
to train on over 20 years of data provided by fantasydatapros with
scikit learn LinearRegression. Uses different predictor features 
for the four main positions (qb, rb, wr, te) and the average stats 
of players who played last season to predict their performances for 
this year.
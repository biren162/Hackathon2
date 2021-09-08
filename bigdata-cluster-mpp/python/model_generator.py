import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_log_error, r2_score
# import time
from utils import process_data, save_model
# from utils import predict_and_build_result

df = pd.read_csv("data/train.csv")
# test_df = pd.read_csv("data/test.csv")

# define a XGB Regressor
xgb = XGBRegressor(max_depth=3, n_estimators=300, subsample=0.8)
    
# function to train the model   
def train_model():
    preprocessed_df = process_data(df)
    X_features = np.array(preprocessed_df)
    labels = df['SalePrice'].astype(float)
    xgb.fit(X_features, labels)
    pred_train = xgb.predict(X_features)
    rmsle = np.sqrt(mean_squared_log_error(labels, pred_train))
    r2 = r2_score(labels, pred_train)
    print('rmsle: ',rmsle)
    print('r2: ',r2)
    save_model(xgb)

train_model()
# time.sleep(10)
# result = predict_and_build_result(test_df)
# print(result)



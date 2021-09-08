import pandas as pd
import numpy as np
from statistics import mean, mode, median
from sklearn.preprocessing import OrdinalEncoder
import pickle

df = pd.read_csv("data/train.csv")

# function to preprocess the data
def process_data(data):
    null_substitute = {
    'MSSubClass' : mode(df.MSSubClass), 'MSZoning' : mode(df.MSZoning), 'LotFrontage' : median(df.LotFrontage),
    'LotArea' : median(df.LotArea),'Street' : mode(df.Street), 'Alley' : -1, 'LotShape' : mode(df.LotShape),
    'LandContour' : mode(df.LandContour), 'Utilities' : mode(df.Utilities), 'LotConfig' : mode(df.LotConfig),
    'LandSlope' : mode(df.LandSlope), 'Neighborhood' : mode(df.Neighborhood), 'Condition1' : mode(df.Condition1),
    'Condition2' : mode(df.Condition2), 'BldgType' : mode(df.BldgType), 'HouseStyle' : mode(df.HouseStyle),
    'OverallQual' : mode(df.OverallQual), 'OverallCond' : mode(df.OverallCond), 'YearBuilt' : 0,
    'YearRemodAdd' : 0, 'RoofStyle' : mode(df.RoofStyle), 'RoofMatl' : mode(df.RoofMatl),
    'Exterior1st' : mode(df.Exterior1st), 'Exterior2nd' : mode(df.Exterior2nd), 'MasVnrType' : mode(df.MasVnrType),
    'MasVnrArea' : median(df.MasVnrArea), 'ExterQual' : mode(df.ExterQual), 'ExterCond' : mode(df.ExterCond),
    'Foundation' : mode(df.Foundation), 'BsmtQual' : -1, 'BsmtCond' : -1, 'BsmtExposure' : -1,
    'BsmtFinType1' : -1, 'BsmtFinSF1' : median(df.BsmtFinSF1), 'BsmtFinType2' : -1, 'BsmtFinSF2' : median(df.BsmtFinSF2),
    'BsmtUnfSF' : median(df.BsmtUnfSF), 'TotalBsmtSF' : median(df.TotalBsmtSF), 'Heating' : mode(df.Heating),
    'HeatingQC' : mode(df.HeatingQC), 'CentralAir' : mode(df.CentralAir), 'Electrical' : mode(df.Electrical),
    '1stFlrSF' : median(df['1stFlrSF']), '2ndFlrSF' : median(df['2ndFlrSF']), 'LowQualFinSF' : median(df.LowQualFinSF),
    'GrLivArea' : median(df.GrLivArea), 'BsmtFullBath' : 0, 'BsmtHalfBath' : 0, 'FullBath' : 0, 'HalfBath' : 0,
    'BedroomAbvGr' : 0, 'KitchenAbvGr' : 0, 'KitchenQual' : mode(df.KitchenQual), 'TotRmsAbvGrd' : 0,
    'Functional' : mode(df.Functional), 'Fireplaces' : 0, 'FireplaceQu' : -1, 'GarageType' : -1, 'GarageYrBlt' : 0,
    'GarageFinish' : -1, 'GarageCars' : 0, 'GarageArea' : median(df.GarageArea), 'GarageQual' : -1,
    'GarageCond' : -1, 'PavedDrive' : mode(df.PavedDrive), 'WoodDeckSF' : median(df.WoodDeckSF),
    'OpenPorchSF' : median(df.OpenPorchSF), 'EnclosedPorch' : median(df.EnclosedPorch),
    '3SsnPorch' : median(df['3SsnPorch']), 'ScreenPorch' : median(df.ScreenPorch),
    'PoolArea' : median(df.PoolArea), 'PoolQC' : -1, 'Fence' : -1, 'MiscFeature' : -1, 'MiscVal' : median(df.MiscVal),
    'MoSold' : 0, 'YrSold' : 0, 'SaleType' : mode(df.SaleType), 'SaleCondition' : mode(df.SaleCondition)
    }
    
    continuous_features = [
    'LotArea', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 
    'LowQualFinSF', 'GrLivArea', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', '3SsnPorch', 
    'ScreenPorch', 'MiscVal'
    ]
    
    discrete_features = [
    'YearBuilt', 'YearRemodAdd', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 
    'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces', 'GarageCars', 'GarageYrBlt', 'MoSold', 'YrSold'
    ]
    
    nominal_categorical_features = [
    'Alley', 'GarageType', 'MiscFeature', 'MSZoning', 'MSSubClass', 'Street', 'LandContour', 'LotConfig', 
    'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl',
    'Exterior1st', 'Exterior2nd', 'MasVnrType', 'Foundation', 'Heating', 'CentralAir', 'SaleType', 'SaleCondition'    
    ]
    
    ordinal_categorical_features = [
    'BsmtQual', 'BsmtCond', 'BsmtExposure', 'GarageFinish', 'GarageQual', 'GarageCond', 'BsmtFinType1', 'BsmtFinType2', 
    'FireplaceQu', 'LotShape', 'Utilities', 'LandSlope', 'OverallQual', 'OverallCond', 'ExterQual', 'ExterCond',
    'HeatingQC', 'Electrical', 'KitchenQual', 'Functional', 'PavedDrive', 'PoolQC', 'Fence'
    ]
    
    features_to_drop = [
    'WoodDeckSF', 'OpenPorchSF', 'MasVnrArea', 'BsmtFinSF1', 'BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 
    'LowQualFinSF', 'MSZoning', 'GarageCars', 'GarageArea', 'FullBath', 'YearBuilt', 'TotRmsAbvGrd',
    ]
    
    for i in data:
        if data[i].isnull().any():
            if(null_substitute[i] == 0):
                data[i] = data[i].fillna(0).astype(int)
            elif(null_substitute[i] == -1):
                data[i] = data[i].fillna('NA') 
            else:
                data[i] = data[i].fillna(null_substitute[i])
    
    df_continuous = data[continuous_features]
    df_discrete = data[discrete_features]
    
    encoder_nominal = OrdinalEncoder()
    df_nominal = data[nominal_categorical_features]
    df_nominal = pd.DataFrame(encoder_nominal.fit_transform(df_nominal))
    df_nominal.columns = nominal_categorical_features
    
    encoder = OrdinalEncoder()
    df_ordinal = data[ordinal_categorical_features]
    df_ordinal = pd.DataFrame(encoder.fit_transform(df_ordinal))
    df_ordinal.columns = ordinal_categorical_features
    
    df_concat = pd.concat([ 
    df_continuous, 
    df_discrete,
    df_ordinal, 
    df_nominal
    ], axis=1).astype(float)
    
    df_concat = df_concat.drop(features_to_drop, axis=1)
    
    return df_concat

# function to save the model
def save_model(model):
    pickle.dump(model, open("model/model.pkl", "wb"))

# function to load the model
def load_model():
    model = pickle.load(open("model/model.pkl", "rb"))
    return model

# function to predict
def predict_and_build_result(test_df):
    model = load_model()
    preprocessed_test = process_data(test_df)
    prediction = model.predict(np.array(preprocessed_test))
    df_pred_test = pd.DataFrame(prediction)
    df_pred_test.columns = ['SalePrice']
    result = pd.concat([test_df['Id'], df_pred_test.astype(float)], axis=1)
    # print(result)
    return result


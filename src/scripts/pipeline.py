import pandas as pd
from src.config.constants import CATEGORICAL_VARS

def transform_pipeline(data_json: dict) -> pd.DataFrame:
    data = json_to_dataframe(data_json)
    data = format_types(data)
    data = one_hot_encoding(data)
    return data

def json_to_dataframe(data_json: dict) -> pd.DataFrame:
    data = pd.DataFrame.from_dict([data_json])
    return data

def format_types(data: pd.DataFrame) -> pd.DataFrame:
    for col in data.columns:
        data[col] = data[col].astype("float64")   
    return data

def one_hot_encoding(X_train: pd.DataFrame) -> pd.DataFrame:
    X_train_ohe = pd.get_dummies(X_train, columns=CATEGORICAL_VARS, prefix=CATEGORICAL_VARS, drop_first=True)
    cols_ohe = X_train_ohe.select_dtypes(include=["bool"]).columns
    X_train_ohe[cols_ohe] = X_train_ohe[cols_ohe].astype("category")
    return X_train_ohe

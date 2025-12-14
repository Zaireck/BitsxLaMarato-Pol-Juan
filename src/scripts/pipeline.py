import pandas as pd

import sys
sys.path.insert(0, '../')
from config.constants import CATEGORICAL_VARS

def transform_pipeline(data_json: dict) -> pd.DataFrame:
    data = json_to_dataframe(data_json)
    data = format_types(data)
    data = one_hot_encoding(data)

    orden = ['recep_est_porcent',
                'tamano_tumoral',
                'tipo_histologico_2',
                'tipo_histologico_3',
                'tipo_histologico_4',
                'tipo_histologico_5',
                'tipo_histologico_6',
                'tipo_histologico_7',
                'tipo_histologico_8',
                'tipo_histologico_9',
                'tipo_histologico_10',
                'tipo_histologico_11',
                'tipo_histologico_12',
                'tipo_histologico_88',
                'Grado_2',
                'ecotv_infiltobj_2',
                'ecotv_infiltobj_3',
                'ecotv_infiltobj_4',
                'ecotv_infiltobj_5',
                'ecotv_infiltsub_2',
                'ecotv_infiltsub_3',
                'ecotv_infiltsub_4',
                'estadiaje_pre_i_2',
                'estadiaje_pre_i_3',
                'estadiaje_pre_i_4',
                'grupo_riesgo_1',
                'grupo_riesgo_2',
                'grupo_riesgo_3',
                'asa_1',
                'asa_2',
                'asa_3',
                'asa_4',
                'asa_5',
                'asa_6',
                'afectacion_linf_1',
                'afectacion_linf_2',
                'AP_ganPelv_1',
                'AP_ganPelv_2',
                'AP_ganPelv_3',
                'AP_ganPelv_4',
                'AP_glanPaor_1',
                'AP_glanPaor_2',
                'AP_glanPaor_3',
                'AP_glanPaor_4',
                'beta_cateninap_1',
                'beta_cateninap_2',
                'estadificacion__1',
                'estadificacion__2',
                'estadificacion__3',
                'estadificacion__4',
                'estadificacion__5',
                'estadificacion__6',
                'estadificacion__7',
                'estadificacion__8',
                'estadificacion__9',
                'FIGO2023_1',
                'FIGO2023_2',
                'FIGO2023_3',
                'FIGO2023_4',
                'FIGO2023_5',
                'FIGO2023_6',
                'FIGO2023_7',
                'FIGO2023_8',
                'FIGO2023_9',
                'FIGO2023_10',
                'FIGO2023_11',
                'FIGO2023_12',
                'FIGO2023_13',
                'FIGO2023_14',
                'grupo_de_riesgo_definitivo_1',
                'grupo_de_riesgo_definitivo_2',
                'grupo_de_riesgo_definitivo_3',
                'grupo_de_riesgo_definitivo_4',
                'grupo_de_riesgo_definitivo_5',
                'rdt_1',
                'rdt_2',
                'rdt_3',
                'rdt_4',
                'recep_est_porcent_medido_1.0',
                'tamano_tumoral_medido_1.0']
    
    data = data[orden]
    return data

def json_to_dataframe(data_json: dict) -> pd.DataFrame:
    data = pd.DataFrame.from_dict([data_json])
    return data

def format_types(data: pd.DataFrame) -> pd.DataFrame:
    data["afectacion_linf"] = data["afectacion_linf"].astype("float64")
    data["asa"] = data["asa"].astype("float64")
    data[CATEGORICAL_VARS] = data[CATEGORICAL_VARS].astype("category")
    data["tamano_tumoral_medido_1.0"] = data["tamano_tumoral_medido_1.0"].astype("category")
    data["recep_est_porcent_medido_1.0"] = data["recep_est_porcent_medido_1.0"].astype("category")

    data["recep_est_porcent"] = data["recep_est_porcent"].astype("float64")
    data["tamano_tumoral"] = data["tamano_tumoral"].astype("float64")

    data["tipo_histologico"] = data["tipo_histologico"].cat.set_categories([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 88])
    data["Grado"] = data["Grado"].cat.set_categories([1, 2])
    data["ecotv_infiltobj"] = data["ecotv_infiltobj"].cat.set_categories([1, 2, 3, 4, 5])
    data["ecotv_infiltsub"] = data["ecotv_infiltsub"].cat.set_categories([1, 2, 3, 4])
    data["estadiaje_pre_i"] = data["estadiaje_pre_i"].cat.set_categories([1, 2, 3, 4])    
    data["estadificacion_"] = data["estadificacion_"].cat.set_categories([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])    
    data["FIGO2023"] = data["FIGO2023"].cat.set_categories([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    data["grupo_riesgo"] = data["grupo_riesgo"].cat.set_categories([0, 1, 2, 3])
    data["grupo_de_riesgo_definitivo"] = data["grupo_de_riesgo_definitivo"].cat.set_categories([0, 1, 2, 3, 4, 5])
    data["asa"] = data["asa"].cat.set_categories([0, 1, 2, 3, 4, 5, 6])
    data["afectacion_linf"] = data["afectacion_linf"].cat.set_categories([0, 1, 2])
    data["AP_ganPelv"] = data["AP_ganPelv"].cat.set_categories([0, 1, 2, 3, 4])
    data["AP_glanPaor"] = data["AP_glanPaor"].cat.set_categories([0, 1, 2, 3, 4])
    data["beta_cateninap"] = data["beta_cateninap"].cat.set_categories([0, 1, 2])
    data["rdt"] = data["rdt"].cat.set_categories([0, 1, 2, 3, 4])

    print(data)

    return data



def one_hot_encoding(X_train: pd.DataFrame) -> pd.DataFrame:
    X_train_ohe = pd.get_dummies(X_train, columns=CATEGORICAL_VARS, prefix=CATEGORICAL_VARS, drop_first=True)
    cols_ohe = X_train_ohe.select_dtypes(include=["bool"]).columns
    X_train_ohe[cols_ohe] = X_train_ohe[cols_ohe].astype("category")

    print(X_train_ohe.columns)
    return X_train_ohe
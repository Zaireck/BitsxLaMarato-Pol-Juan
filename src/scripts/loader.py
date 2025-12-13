import joblib
from pathlib import Path
from sklearn.svm import SVC
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def guardar_modelo(modelo: SVC, nombre_modelo: str):
    """
    Funcion para guardar un modelo entrenado en disco.

    Args:
        modelo: Modelo entrenado a guardar.
        nombre_modelo (str): Nombre con el que se guardara el modelo.
    """
    ml_models_dir = Path(__file__).parent.parent / "ml_models"
    joblib.dump(modelo, ml_models_dir / f"{nombre_modelo}.joblib")

def cargar_modelo(nombre_modelo: str) -> SVC:
    """
    Funcion para cargar un modelo entrenado desde disco.

    Args:
        nombre_modelo (str): Nombre del modelo a cargar.

    Returns:
        Modelo cargado desde disco.
    """
    ml_models_dir = Path(__file__).parent.parent / "ml_models"
    return joblib.load(ml_models_dir / f"{nombre_modelo}.joblib")

def guardar_PCA(pca: PCA, nombre_pca: str):
    """
    Funcion para guardar un modelo PCA entrenado en disco.

    Args:
        pca: Modelo PCA entrenado a guardar.
        nombre_pca (str): Nombre con el que se guardara el modelo PCA.
    """
    ml_models_dir = Path(__file__).parent.parent / "ml_models"
    joblib.dump(pca, ml_models_dir / f"{nombre_pca}_PCA.joblib")

def cargar_PCA(nombre_pca: str) -> PCA:
    """
    Funcion para cargar un modelo PCA entrenado desde disco.

    Args:
        nombre_pca (str): Nombre del modelo PCA a cargar.

    Returns:
        Modelo PCA cargado desde disco.
    """
    ml_models_dir = Path(__file__).parent.parent / "ml_models"
    return joblib.load(ml_models_dir / f"{nombre_pca}_PCA.joblib")

def guardar_scaler(scaler: StandardScaler | MinMaxScaler, nombre_scaler: str):
    """
    Funcion para guardar un scaler entrenado en disco.

    Args:
        scaler: Scaler entrenado a guardar.
        nombre_scaler (str): Nombre con el que se guardara el scaler.
    """
    ml_models_dir = Path(__file__).parent.parent / "ml_models"
    joblib.dump(scaler, ml_models_dir / f"{nombre_scaler}_scaler.joblib")

def cargar_scaler(nombre_scaler: str) -> StandardScaler | MinMaxScaler:
    """
    Funcion para cargar un scaler entrenado desde disco.

    Args:
        nombre_scaler (str): Nombre del scaler a cargar.

    Returns:
        Scaler cargado desde disco.
    """
    ml_models_dir = Path(__file__).parent.parent / "ml_models"
    return joblib.load(ml_models_dir / f"{nombre_scaler}_scaler.joblib")
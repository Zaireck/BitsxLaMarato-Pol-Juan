import joblib
from pathlib import Path

def guardar_modelo(modelo, nombre_modelo: str):
    """
    Funcion para guardar un modelo entrenado en disco.

    Args:
        modelo: Modelo entrenado a guardar.
        nombre_modelo (str): Nombre con el que se guardara el modelo.
    """
    ml_models_dir = Path(__file__).parent.parent / "ml_models"
    joblib.dump(modelo, ml_models_dir / f"{nombre_modelo}.joblib")

def cargar_modelo(nombre_modelo: str):
    """
    Funcion para cargar un modelo entrenado desde disco.

    Args:
        nombre_modelo (str): Nombre del modelo a cargar.

    Returns:
        Modelo cargado desde disco.
    """
    ml_models_dir = Path(__file__).parent.parent / "ml_models"
    return joblib.load(ml_models_dir / f"{nombre_modelo}.joblib")
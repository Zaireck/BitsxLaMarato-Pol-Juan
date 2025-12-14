from flask import Flask, request, abort, render_template

app = Flask(__name__)

import sys
sys.path.insert(0, '../')
from scripts.loader import cargar_recursos
from scripts.pipeline import transform_pipeline


ALLOWED = {
    "tipo_histologico": {1,2,3,4,5,6,7,8,9,10,11,12,88},
    "Grado": {1,2},
    "ecotv_infiltobj": {1,2,3,4,5},
    "ecotv_infiltsub": {1,2,3,4},
    "estadiaje_pre_i": {1,2,3,4},
    "estadificacion_": {0,1,2,3,4,5,6,7,8,9},
    "FIGO2023": {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14},
    "grupo_riesgo": {0,1,2,3},
    "grupo_de_riesgo_definitivo": {0,1,2,3,4,5},
    "asa": {0,1,2,3,4,5,6},
    "afectacion_linf": {0,1,2},
    "AP_ganPelv": {0,1,2,3,4},
    "AP_glanPaor": {0,1,2,3,4},
    "beta_cateninap": {0,1,2},
    "Tributaria_a_Radioterapia": {0,1,2},
    "rdt": {0,1,2,3},
    "recep_est_porcent_medido": {0,1},
    "tamano_tumoral_medido": {0,1}
}

def get_int(name):
    try:
        return int(request.form[name])
    except (KeyError, ValueError):
        abort(400, f"Campo inválido o ausente: {name}")

def get_float(name):
    try:
        return float(request.form[name])
    except (KeyError, ValueError):
        abort(400, f"Campo inválido o ausente: {name}")

def validate_choice(name):
    value = get_float(name)
    if value not in ALLOWED[name]:
        abort(400, f"Valor no permitido para {name}: {value}")
    return value

@app.route("/", methods=["GET", "POST"])
def manejar_solicitud():

    if request.method == "POST":
        datos = {}

        # Numéricos
        datos["recep_est_porcent_medido_1.0"] = bool(validate_choice("recep_est_porcent_medido"))
        if datos["recep_est_porcent_medido_1.0"]:
            datos["recep_est_porcent"] = get_int("recep_est_porcent")
            if not (0 <= datos["recep_est_porcent"] <= 100):
                abort(400, "recep_est_porcent fuera de rango (0–100 %)")
        else:
            datos["recep_est_porcent"] = 0


        datos["tamano_tumoral_medido_1.0"] = bool(validate_choice("tamano_tumoral_medido"))
        if datos["tamano_tumoral_medido_1.0"]:
            datos["tamano_tumoral"] = get_float("tamano_tumoral")
            if not (0 <= datos["tamano_tumoral"] <= 20):
                abort(400, "tamano_tumoral fuera de rango (0–20 cm)")
        else:
            datos["tamano_tumoral"] = 0

        # --- Categóricos ---
        for field in [
            "tipo_histologico",
            "Grado",
            "ecotv_infiltobj",
            "ecotv_infiltsub",
            "estadiaje_pre_i",
            "estadificacion_",
            "FIGO2023",
            "grupo_riesgo",
            "grupo_de_riesgo_definitivo",
            "asa",
            "afectacion_linf",
            "AP_ganPelv",
            "AP_glanPaor",
            "beta_cateninap",
            "rdt"
        ]:
            datos[field] = validate_choice(field)

        tar = validate_choice("Tributaria_a_Radioterapia")
        if ((tar == 1) & (datos["rdt"] == 3)) | (tar == 2):
            datos["rdt"] = 4
        elif tar == 0:
            datos["rdt"] = 3

        modelo, scaler, pca = cargar_recursos("modelo_svm_recidiva", "scaler_std_recidiva", "pca_recidiva")

        df = transform_pipeline(datos)
        df_std = scaler.transform(df)
        df_pca = pca.transform(df_std)
        y_pred = modelo.predict(df_pca[:, :3])

        print(f"Resultado: {y_pred}")
               

        return render_template("form.html", datos=datos, enviado=True)

    return render_template("form.html", enviado=False)

if __name__ == '__main__':
    app.run(debug=True)
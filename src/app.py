from flask import Flask, request, render_template

app = Flask(__name__)

def procesar_datos(nombre, edad):
    if edad >= 18:
        estado = "mayor de edad"
    else:
        estado = "menor de edad"
    return f"Hola, {nombre}. Tienes {edad} años y eres {estado}."

@app.route("/", methods=["GET", "POST"])
def manejar_solicitud():

    if request.method == "POST":
        datos = request.form.to_dict()
        return render_template("form.html", datos=datos, enviado=True)

    return render_template("form.html", enviado=False)

if __name__ == '__main__':
    app.run(debug=True)
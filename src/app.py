from flask import Flask, request, jsonify

app = Flask(__name__)

def procesar_datos(nombre, edad):
    if edad >= 18:
        estado = "mayor de edad"
    else:
        estado = "menor de edad"
    return f"Hola, {nombre}. Tienes {edad} años y eres {estado}."

@app.route('/make_prediction', methods=['POST'])
def manejar_solicitud():
    # 2. Verifica que la solicitud sea POST y contenga datos JSON
    if request.method == 'POST':
        data = request.get_json()
        
        #TODO: Revisar esta logica
        if not data or 'nombre' not in data or 'edad' not in data:
            return jsonify({
                "error": "Datos incompletos", 
                "mensaje": "Se requieren 'nombre' y 'edad' en el cuerpo JSON."
            }), 400
        
        #TODO: Ajustar a nuestros parametros
        nombre = data.get('nombre')
        edad = data.get('edad')
        
        try:
            resultado_funcion = procesar_datos(nombre, int(edad))
            
            return jsonify({
                "status": "success",
                "datos_recibidos": {"nombre": nombre, "edad": edad},
                "resultado": resultado_funcion
            }), 200
            
        #TODO: Revisar esta logica    
        except ValueError:
            return jsonify({
                "error": "Tipo de dato incorrecto",
                "mensaje": "'edad' debe ser un número entero."
            }), 400
        except Exception as e:
            return jsonify({"error": "Error interno del servidor", "detalle": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
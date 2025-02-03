from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    datos = request.get_json()
    num1 = float(datos['num1'])
    num2 = float(datos['num2'])
    operacion = datos['operacion']

    if operacion == 'suma':
        resultado = num1 + num2
    elif operacion == 'resta':
        resultado = num1 - num2
    elif operacion == 'multiplicacion':
        resultado = num1 * num2
    elif operacion == 'division':
        resultado = num1 / num2  # No hay validación de división por cero aún

    return jsonify({'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)

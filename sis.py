from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def diagnostico():
    resultado = None

    if request.method == 'POST':
        fiebre = 'fiebre' in request.form
        tos = 'tos' in request.form
        garganta = 'garganta' in request.form
        cabeza = 'cabeza' in request.form
        congestion = 'congestion' in request.form

        if fiebre and tos and garganta:
            resultado = "Puede tener gripe."
        elif fiebre and cabeza and not tos:
            resultado = "Puede tener fiebre viral."
        elif congestion and garganta:
            resultado = "Puede tener resfriado común."
        else:
            resultado = "No se puede determinar con certeza. Consulte a un médico."

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)

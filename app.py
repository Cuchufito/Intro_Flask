from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return "hola mundo desde el backend"
#endpoint o ruta 
@app.route('/contacto')
def contacto():
    return "<h3>Introduciendo HTML desde el servidor</h3>"

@app.route('/contacto2')
def contacto2():
    return render_template('contacto.html')

@app.route('/guardarMascota', methods=['POST'])
def guardarMascota():
    print(request.form)
    nombreMascota = request.form.get('txtNombreMascota')
    return f"Ya llegó tu mascota <strong>{nombreMascota}</strong> al servidor"

if __name__ =='__main__':
    app.run(debug=True)
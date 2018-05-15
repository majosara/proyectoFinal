from flask import Flask, session

app = Flask(__name__)

@app.route('/', methods = ["POST"])

def index():
	usuario = request.form['usuario']
	contrasena = request.form['contrasena']
	session['usuario'] = usuario
	session['contrasena'] = contrasena
	return 'Hola' + usuario + 'su contrasena es ' + contrasena

if __name__== '__main__':
	app.run(debug=True)
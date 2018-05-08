from flask import Flask
app = Flask(__name__)
app.route('/')
def index():
    return "<h1> Era gol de Yepes </h1>"

@app.route('/<user>')
def welcomeUser(user):
    return "<h1> Bienvenido {} </h1>".format(user)

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True, use_reloader=False)

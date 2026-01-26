<<<<<<< HEAD
from flask import Flask
=======
from flask import Flask, render_template, request
>>>>>>> 8aff953 (macros)

app = Flask(__name__)

@app.route("/")
def index():
<<<<<<< HEAD
    return "Hello, World! "


@app.route("/hola")
def hola():
    return "Hola mundo!"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}"

@app.route('/numero/<int:n>')
def numero(n):
    return f"<h1>El número es: {n}</h1>"

@app.route('/user/<int:id>/<string:username>')
def username(id, username):
    return f"<h1>Hola, {username}! Tu ID es: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def username(n1,n2):
    return f"<h1>La Suma es: {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:parm>")
def func(param="juan"):
    return f"<h1>Hola, {param}!</h1>"
=======
    titulo = "Flask IDGS801"
    lista = ["Juan", "Mario", "Pedro", "Dario"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/operasBas", methods=["GET", "POST"])
def operas1():
    n1 = 0
    n2 = 0
    res = 0

    if request.method == "POST":
        n1 = request.form.get("n1", 0)
        n2 = request.form.get("n2", 0)

        try:
            res = float(n1) + float(n2)
        except:
            res = 0

    return render_template("operasBas.html", n1=n1, n2=n2, res=res)

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/usuarios")
def usuarios():
    return render_template("usuarios.html")

@app.route("/hola")
def hola():
    return "¡Hola, Mundo!"

@app.route("/user/<string:user>")
def user(user):
    return f"¡Hello, {user}!"

@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El número es: {n}</h1>"

@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>Hola {username}, tu ID es: {id}</h1>"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>¡Hola, {param}!</h1>"
>>>>>>> 8aff953 (macros)

@app.route("/operas")
def operas():
    return '''
        <form>
<<<<<<< HEAD
        <label for="name">Name:</label>
        <input type="text" id="name name="name" requiered>
        </br>
        <label for="name">apaterno:</label>
        <inout type="text" id="name" name="name"  requiered
        </form>
            '''


if __name__=="__main__":
    app.run()
=======
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <br>
            <label for="apaterno">Apaterno:</label>
            <input type="text" id="apaterno" name="apaterno" required>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 8aff953 (macros)

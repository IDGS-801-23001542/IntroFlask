from flask import Flask, render_template, request, flash
from flask_wtf.csrf import CSRFProtect

import forms

app = Flask(__name__)
app.secret_key = 'clave secreta'

csrf = CSRFProtect()


#  CINEPOLIS - CONSTANTES

PRECIO_BOLETO = 12.00
MAX_BOLETOS_POR_PERSONA = 7


def calcular_descuento_por_boletos(cantidad_boletos: int) -> float:

   # Devuelve el descuento base según cantidad de boletos.
   
    if cantidad_boletos >= 6:
        return 0.15
    elif 3 <= cantidad_boletos <= 5:
        return 0.10
    else:
        return 0.00


def calcular_total(nombre: str, compradores: int, boletos: int, tiene_cineco: bool) -> dict:
    # Validaciones
    if compradores <= 0:
        return {"error": "La cantidad de compradores debe ser mayor que 0."}

    if boletos <= 0:
        return {"error": "La cantidad de boletos debe ser mayor que 0."}

    # Regla: máximo 7 boletos por persona
    max_boletos_permitidos = compradores * MAX_BOLETOS_POR_PERSONA
    if boletos > max_boletos_permitidos:
        return {
            "error": f"No puedes comprar más de {MAX_BOLETOS_POR_PERSONA} boletos por persona. "
                     f"Con {compradores} comprador(es), máximo permitido: {max_boletos_permitidos}."
        }

    subtotal = boletos * PRECIO_BOLETO

    desc_base_pct = calcular_descuento_por_boletos(boletos)
    descuento_base = subtotal * desc_base_pct
    total_despues_desc_base = subtotal - descuento_base

    desc_cineco_pct = 0.10 if tiene_cineco else 0.0
    descuento_cineco = total_despues_desc_base * desc_cineco_pct

    total_final = total_despues_desc_base - descuento_cineco

    return {
        "nombre": nombre,
        "compradores": compradores,
        "boletos": boletos,
        "tiene_cineco": tiene_cineco,
        "precio_boleto": PRECIO_BOLETO,
        "max_boletos_permitidos": max_boletos_permitidos,
        "subtotal": subtotal,
        "desc_base_pct": desc_base_pct,
        "descuento_base": descuento_base,
        "desc_cineco_pct": desc_cineco_pct,
        "descuento_cineco": descuento_cineco,
        "total_final": total_final,
    }



@app.route("/")
def index():
    titulo = "Flask IDGS801"
    lista = ["Juan", "Mario", "Pedro", "Dario"]
    return render_template("index.html", titulo=titulo, lista=lista)


@app.route("/operasBas", methods=["GET", "POST"])
def operasBas():
    n1 = 0
    n2 = 0
    res = 0
    if request.method == 'POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        res = float(n1) + float(n2)
    return render_template("operasBas.html", n1=n1, n2=n2, res=res)


@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    tem = float(n1) + float(n2)
    return f"La suma es: {tem}"


@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")


@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
    mat = 0
    nom = ''
    apa = ''
    ama = ''
    email = ''
    usuarios_class = forms.UserForm(request.form)
    if request.method == 'POST' and usuarios_class.validate():
        mat = usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.apaterno.data
        ama = usuarios_class.amaterno.data
        email = usuarios_class.correo.data
        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template(
        "usuarios.html",
        form=usuarios_class,
        mat=mat, nom=nom, apa=apa, ama=ama, email=email
    )


@app.route("/hola")
def hola():
    return "Hola, Mundo!"


@app.route("/user/<string:user>")
def user(user):
    return f"Hello, {user}!"


@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El número es {n}</h1>"


@app.route("/user/<string:id>/<string:username>")
def username(id, username):
    return f"<h1>¡Hola, {username}! Tu ID es {id}"


@app.route("/operas")
def operas():
    return '''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="apaterno">apaterno:</label>
        <input type="text" id="apaterno" name="apaterno" required>
        </form>
    '''



#  CINEPOLIS 

@app.route("/cinepolis", methods=["GET"])
def cinepolis_form():
    return render_template("cinepolis/formulario.html", title="Cinépolis")


@app.route("/cinepolis/procesar", methods=["POST"])
def cinepolis_procesar():
    nombre = request.form.get("nombre", "").strip()

    try:
        compradores = int(request.form.get("compradores", "0"))
        boletos = int(request.form.get("boletos", "0"))
    except ValueError:
        return render_template(
            "cinepolis/resultado.html",
            title="Resultado Cinépolis",
            error="Compradores y boletos deben ser números enteros."
        )

    cineco = request.form.get("cineco", "no").lower() == "si"

    data = calcular_total(nombre, compradores, boletos, cineco)

    if "error" in data:
        return render_template(
            "cinepolis/resultado.html",
            title="Resultado Cinépolis",
            error=data["error"]
        )

    return render_template(
        "cinepolis/resultado.html",
        title="Resultado Cinépolis",
        data=data
    )


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)

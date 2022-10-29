from flask import Flask, render_template, request, redirect, url_for
import db
from models import Tarea

app = Flask(__name__)


@app.route("/")
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    categorias = db.session.query(Tarea.categoria.distinct().label("categoria")).all()
    tareas_listadas = []  # Group_by me devuelve como si solo pidiera el primero
    for categoria in categorias:
        categoria = categoria.categoria
        lista_aux = []
        for tarea in todas_las_tareas:
            if tarea.categoria == categoria:
                lista_aux.append(tarea)

        else:
            tareas_listadas.append(lista_aux)
    return render_template("index.html", lista_de_tareas=tareas_listadas)


@app.route("/crear-tarea", methods=["post"])
def crear():
    tarea = Tarea(contenido=request.form["contenido_tarea"], hecha=False, fecha=request.form["fecha_tarea"], categoria=request.form["categoria_tarea"])
    db.session.add(tarea)
    db.session.commit()
    db.session.close()
    return redirect(url_for("home"))


@app.route("/eliminar-tarea/<id>")
def eliminar(id):
    elim = db.session.query(Tarea).filter_by(id=id).delete()
    db.session.commit()  # Ejecutamos los cambios
    db.session.close()
    return redirect(url_for("home"))


@app.route("/tarea-hecha/<id>")
def hecha(id):
    echa = db.session.query(Tarea).filter_by(id=id).first()
    echa.hecha = not echa.hecha
    db.session.commit()  # Ejecutamos los cambios
    db.session.close()
    return redirect(url_for("home"))


@app.route("/editar-tarea/<id>")
def editar(id):
    modificado = db.session.query(Tarea).filter_by(id=id).first()
    return render_template("editar.html", editado=modificado)


@app.route("/guardar-edicion/<id>", methods=["post"])
def guardar(id):
    update = db.session.query(Tarea).filter_by(id=id).first()
    update.contenido = request.form["contenido_tarea"]
    update.categoria = request.form["categoria_tarea"]
    update.fecha = request.form["fecha_tarea"]
    db.session.commit()  # Ejecutamos los cambios
    db.session.close()
    return redirect(url_for("home"))


if __name__ == "__main__":

    db.Base.metadata.create_all(db.engine)
    app.run(debug=True)

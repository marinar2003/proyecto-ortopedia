from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def inicio():
    return render_template("index.html", titulo="Aved Medical - Sistema de Gestión")

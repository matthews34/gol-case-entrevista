from flask import Blueprint, render_template, request

from case_gol.auth import login_required
from case_gol.services.stats import generate_graph


bp = Blueprint("stats", __name__)


@bp.route("/", methods=("GET", "POST"))
@login_required
def index():
    if request.method == "POST":
        return render_template("stats/results.html", graph=generate_graph(request.form))

    return render_template("stats/index.html")

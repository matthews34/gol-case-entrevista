import base64
from io import BytesIO
from matplotlib import pyplot as plt

from case_gol.database import get_db


def _plot_graph(periods, rpks):
    fig, ax = plt.subplots()
    ax.set(
        title="RPK por período",
        xlabel="Período",
        ylabel="RPK",
        adjustable="datalim",
    )
    ax.set_xticklabels(periods, rotation=45)
    plt.ticklabel_format(style="plain", axis="y")
    ax.plot(periods, rpks)
    ax.grid()

    fig.tight_layout()

    buffer = BytesIO()
    fig.savefig(buffer)

    buffer.seek(0)
    return base64.b64encode(buffer.read()).decode()


def generate_graph(form: dict[str, str]) -> str:
    market = form["market"]

    start_year_month = f"{int(form['start_year']):04d}-{int(form['start_month']):02d}"
    end_year_month = f"{int(form['end_year']):04d}-{int(form['end_month']):02d}"

    result = (
        get_db()
        .execute(
            """SELECT ano_mes, sum(rpk) FROM stats
        WHERE mercado = :market
        AND ano_mes >= :start_year_month
        AND ano_mes <= :end_year_month
        GROUP BY mercado, ano_mes
        ORDER BY ano_mes""",
            {
                "market": market,
                "start_year_month": start_year_month,
                "end_year_month": end_year_month,
            },
        )
        .fetchall()
    )

    return _plot_graph(*zip(*result))

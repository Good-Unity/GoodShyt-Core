from __future__ import annotations

import typer
from .metrics import compute_gmi

app = typer.Typer(help="GoodShyt Core CLI")


@app.command()
def score(ecti: float, csm: float, stl_penalty: float, kaq: float) -> None:
    typer.echo(compute_gmi(ecti, csm, stl_penalty, kaq))


if __name__ == "__main__":
    app()

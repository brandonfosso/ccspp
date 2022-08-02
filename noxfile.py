from pathlib import Path

import nox

nox.options.sessions = ("check",)

root_dir = Path(__file__).absolute().parent
py_files = sorted(f.name for f in root_dir.iterdir() if f.suffix == ".py")


@nox.session(reuse_venv=True)
def check(session):
    args = session.posargs or py_files
    session.install(
        "flake8",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
    )
    session.run("flake8", *args)
    session.install("mypy")
    session.run("mypy", *args)


@nox.session(reuse_venv=True)
def lint(session):
    args = session.posargs or py_files
    session.install("autoflake")
    session.run("autoflake", "--in-place", *args)
    session.install("black")
    session.run("black", *args)
    check(session)

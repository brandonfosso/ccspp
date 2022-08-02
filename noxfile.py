from pathlib import Path

import nox

nox.options.sessions = ("lint",)

root_dir = Path(__file__).absolute().parent
py_files = sorted(f.name for f in root_dir.iterdir() if f.suffix == ".py")


@nox.session
def black(session):
    args = session.posargs or py_files
    session.install("black")
    session.run("black", *args)


@nox.session
def lint(session):
    args = session.posargs or py_files
    session.install(
        "flake8",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session
def mypy(session):
    args = session.posargs or py_files
    session.install("mypy")
    session.run("mypy", *args)

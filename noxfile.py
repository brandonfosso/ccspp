from pathlib import Path

import nox

nox.options.sessions = ("check",)

root_dir = Path(__file__).absolute().parent
py_files = sorted(f.name for f in root_dir.iterdir() if f.suffix == ".py")


# Tools
@nox.session
def autoflake(session):
    args = session.posargs or py_files
    session.install("autoflake")
    session.run("autoflake", "--in-place", *args)


@nox.session
def black(session):
    args = session.posargs or py_files
    session.install("black")
    session.run("black", *args)


@nox.session
def flake8(session):
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


@nox.session
def check(session):
    flake8(session)
    mypy(session)

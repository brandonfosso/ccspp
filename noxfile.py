from pathlib import Path

import nox

nox.options.sessions = ("lint",)

root_dir = Path(__file__).absolute().parent
py_files = sorted(f.name for f in root_dir.iterdir() if f.suffix == ".py")


@nox.session
def format(session):
    session.install("black")
    session.run("black", *py_files)


@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", *py_files)

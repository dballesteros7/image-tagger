VIRTUALENV="virtualenv"
virtualenv_dir="venv"

setup: venv deps

venv:
	test -d venv || ($(VIRTUALENV) $(virtualenv_dir) || true)

deps:
	pip install -r requirements_dev.txt

keys:
	./src/application/generate_keys.py


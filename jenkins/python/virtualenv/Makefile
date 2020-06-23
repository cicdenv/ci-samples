SHELL=/bin/bash

venv=.venv

.venv:
	if [ ! -d "$(venv)" ]; then python -m venv $(venv); fi
	source $(venv)/bin/activate;     \
	pip install --upgrade pip;       \
	pip install -r requirements.txt  \
	pip install -r requirements-dev.txt  \

test: .venv
	source $(venv)/bin/activate; pytest

# Makefile for Python project

.PHONY: help install test check format clean

VENV=venv
PYTHON=$(VENV)/bin/python
PIP=$(VENV)/bin/pip
POETRY=$(VENV)/bin/poetry
PYTEST=$(VENV)/bin/poetry run pytest
ISORT=$(VENV)/bin/poetry run isort
MYPY=$(VENV)/bin/poetry run mypy
RUFF=$(VENV)/bin/poetry run ruff
XENON=$(VENV)/bin/poetry run xenon

# Default Python binary, can be overridden: e.g., make install PYTHON_BIN=python3.11
PYTHON_BIN ?= python3

help:
	@echo "Available commands:"
	@echo "  make install [PYTHON_BIN=python3.11]  Set up virtualenv with optional Python version"
	@echo "  make test        					   Run tests with pytest"
	@echo "  make check      					   Run checks with isort and ruff"
	@echo "  make format    					   Format code with isort and ruff"
	@echo "  make clean    						   Remove temporary files and __pycache__"

install:
	test -d $(VENV) || $(PYTHON_BIN) -m venv $(VENV)
	$(PIP) install --upgrade pip
	$(PIP) install poetry
	$(POETRY) install

test:
	$(PYTEST)

check:
	$(ISORT) . --check
	$(RUFF) check
	$(RUFF) format --check
	$(MYPY) .
	$(XENON) -i venv,node_modules --max-absolute A --max-modules A --max-average A .

format:
	$(ISORT) .
	$(RUFF) format

doc:
	${PYTHON} -m pydoc -n localhost assertme

clean:
	find . -type d -name '__pycache__' -exec rm -r {} +
	find . -type f -name '*.pyc' -delete
	rm -rf $(VENV)

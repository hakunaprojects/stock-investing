#.DEFAULT_GOAL := start
SHELL=/bin/bash
NOW = $(shell date +"%Y%m%d%H%M%S")
UID = $(shell id -u)
PWD = $(shell pwd)
PYTHON=$(shell which python3)

.PHONY: help
help: ## prints all targets available and their description
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: start
start: ## how to start develop
	@echo "************  How start develop ************"
	@echo "1. For create virtual environment:"
	@echo "python3 -m venv venv"
	@echo ""
	@echo "2. To start virtual dev environment:"
	@echo "source venv/bin/activate"
	@echo ""
	@echo "3. Install all dependencies:"
	@echo "make all-dependencies"
	@echo ""
	@echo "4. To exit of dev environment:"
	@echo "deactivate"
	@echo ""

.PHONY: upgrade-pip
upgrade-pip: ## upgrade pip
	python -m pip install --upgrade pip

.PHONY: dev-dependencies
dev-dependencies:  pyproject.toml ## install development dependencies
	(. venv/bin/activate; \
	pip install -U pip poetry; \
	poetry install)

.PHONY: app-dependencies
app-dependencies: pyproject.toml ## install application dependencies
	(. venv/bin/activate; \
	pip install -U pip poetry; \
	poetry install --no-dev)

.PHONY: all-dependencies
all-dependencies: app-dependencies dev-dependencies ## install all dependencies

.PHONY: lint
lint: ## check source code for style errors
	flake8 . && black . --check

.PHONY: format
format: ## automatic source code formatter following a strict set of standards
	isort . --sp .isort.cfg && black .

.PHONY: venv
venv:  ## creates a virtualenv if does not exist and activates it
	@if [[ "${PYTHON_VERSION}" != "${PY_VER}" ]]; then \
       echo "You need Python ${PY_VER}. Detected ${PYTHON_VERSION}"; exit 1; \
    fi
		test -d venv || ${PYTHON} -m venv venv # setup a python3 virtualenv

.PHONY: install
install: venv all-dependencies ## Create venv and install all depencencies

.PHONY: install-hooks
install-hooks: ## installs git hooks in your local machine
	cp .pre-commit .git/hooks/pre-commit

.PHONY: flake-report
flake-report: ## flake8 Dashboards
	@echo "Generating flake8 report, please wait..."
	- flake8 --format=dashboard --outputdir=flake-report --title="Callid Project"
	open flake-report/index.html

.PHONY: unit-tests
unit-tests: ## Run all unit tests
	@echo "************ Unit Tests ************"
	coverage run -m unittest discover -s tests/unit
	coverage report

.PHONY: integration-tests
integration-tests: ## Search and execute all integration tests
	@echo "************ Integration Tests ************"
	coverage run -m unittest discover -s tests/integration
	coverage report

.PHONY: tests
tests: unit-tests integration-tests ## Run unit and integration tests

.PHONY: coverage-report
coverage-report: ## coverage report of all tests
	coverage run -m unittest discover
	coverage html
	open htmlcov/index.html

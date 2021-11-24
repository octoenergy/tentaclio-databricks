
# Help
.PHONY: help

help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Local installation
.PHONY: init clean lock update install

install: ## Initalise the virtual env installing deps
	pipenv install --dev
	pipenv run pip install -e .

clean: ## Remove all the unwanted clutter
	find src -type d -name __pycache__ | xargs rm -rf
	find src -type d -name '*.egg-info' | xargs rm -rf
	pipenv clean

lock: ## Lock dependencies
	pipenv lock

update: ## Update dependencies (whole tree)
	pipenv update --dev

sync: ## Install dependencies as per the lock file
	pipenv sync --dev
	pipenv run pip install -e .

# Linting and formatting
.PHONY: lint test format

lint: ## Lint files with flake and mypy
	pipenv run flake8 src tests
	pipenv run mypy src tests
	pipenv run black --check src tests
	pipenv run isort --check-only src tests


format: ## Run black and isort
	pipenv run black src tests
	pipenv run isort src tests

# Testing

.PHONY: test
test: ## Run unit tests
	pipenv run pytest tests

# Release
package:
	# create a source distribution
	pipenv run python setup.py sdist
	# create a wheel
	pipenv run python setup.py bdist_wheel

release: package
	pipenv run twine upload dist/*
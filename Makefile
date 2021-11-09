
# Help
.PHONY: help

help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

# Local installation
.PHONY: init clean lock update install

install: ## Initalise the virtual env installing deps
	pipenv install --dev

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

# Linting and formatting
.PHONY: lint test format

lint: ## Lint files with flake and mypy
	pipenv run flake8 src
	pipenv run flake8 tests
	pipenv run mypy src
	pipenv run mypy tests
	pipenv run black --check src
	pipenv run black --check tests
	pipenv run isort --check-only src
	pipenv run isort --check-only tests


format: ## Run black and isort
	pipenv run black src
	pipenv run black tests
	pipenv run isort src
	pipenv run isort tests

# Testing

.PHONY: test
test: ## Run unit tests
	pipenv run pytest tests

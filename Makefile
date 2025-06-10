install:
	@echo "Installing for dev environment"
	@.venv/bin/python -m pip install -e '.[dev]'

ipython:
	@.venv/bin/ipython
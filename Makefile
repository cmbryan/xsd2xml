all: build test integration_test

build:
	poetry build

test:
	python -m pytest


integration_test:
	rm -rf .testenv
	python -m venv .testenv
	. .testenv/bin/activate \
	&& python -m pip install /workspaces/xsd2xml/dist/xsd2xml-*-py3-none-any.whl \
	&& python -m xsd2xml

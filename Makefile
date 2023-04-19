all: test package package_test

test:
	python -m pytest

package:
	poetry build

package_test:
	rm -rf .testenv
	python -m venv .testenv
	. .testenv/bin/activate \
	&& python -m pip install /workspaces/xsd2xml/dist/xsd2xml-*-py3-none-any.whl \
	&& python -m xsd2xml --xsd tests/test_data/example_schema.xsd

clean:
	rm -rf dist

install:
	@python setup.py install

pack:
	@rm -fr dist/*
	@python setup.py sdist

build:
	@rm -fr build/*
	@python setup.py build

publish: pack build
	@twine upload dist/*

.PHONY: install pack build publish

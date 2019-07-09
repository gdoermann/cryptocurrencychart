clean:
	find . -name *.pyc -delete

compile: clean
	python -m compileall .

install_deps: clean
	pip install -r requirements.txt

test_format: install_deps
	flake8 .

test: test_format
	python setup.py test

build: test
	python setup.py sdist bdist_wheel

test_release: build
	twine upload -s -i gdoermann@gmail.com --repository-url https://test.pypi.org/legacy/ dist/*

upload_release:
	twine upload -s -i gdoermann@gmail.com --repository-url https://upload.pypi.org/legacy/ dist/*

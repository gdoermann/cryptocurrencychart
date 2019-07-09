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

release: test
	python setup.py sdist upload



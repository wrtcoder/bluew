test:
	nosetests tests --tc-file=tests/.testconfig.yaml --tc-format=yaml --with-id -v --with-coverage --cover-package=bluew
lint:
	flake8 --ignore=F401 bluew
	pylint --rcfile=.pylintrc --notes=FIXME bluew
	mypy --no-warn-no-return --ignore-missing-imports .
publish:
	python3 setup.py sdist bdist_wheel
	twine upload dist/*
	rm -rf build dist .egg bluew.egg-info
docs:
	cd docs && make html

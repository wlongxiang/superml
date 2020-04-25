.PHONY: docs
setup:
	rm -rf build
	rm -rf dist
	python setup.py bdist_wheel
install:
	pip uninstall superml -y
	pip install --find-links=dist  --no-cache-dir superml
publish:
	make setup
	git tag $(version)
	git push origin $(version)
	twine upload dist/*
docs:
	rm -rf docs/_build && sphinx-apidoc -o docs initpkg && cd docs && make html
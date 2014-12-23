all:
	@echo "make clean"

clean:
	rm -rf build dist *.egg-info */__pycache__ */*.pyc

pypireg:
	python setup.py register
	python setup.py sdist upload

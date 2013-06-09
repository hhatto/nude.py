all:
	@echo "make clean"

clean:
	rm -rf build dist *.egg-info */__pycache__
	rm */*.pyc

pypireg:
	${PYTHON} setup.py register
	${PYTHON} setup.py sdist upload

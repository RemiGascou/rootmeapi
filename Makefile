.PHONY : all clean build upload

BASEDIR=./rootmeapi

all : clean

clean :
	@rm -rf `find ./ -type d -name "*__pycache__"`

build :
	python3 setup.py sdist bdist_wheel

upload :
	python3 setup.py sdist upload

.PHONY : all clean build upload

BASEDIR=./rootmeapi

all : clean

clean :
	@/usr/bin/rm -rf `/usr/bin/find ./ -type d -name "*__pycache__"`

build :
	/usr/bin/python3 setup.py sdist bdist_wheel

upload :
	/usr/bin/python3 setup.py sdist upload

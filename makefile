all: check

default: check

clean:
	rm ./*.pyc

hashmap.pyc: hashmap.py
	python -m compileall hashmap.py

test: hashmap.pyc test.py
	python test.py

check: test

dist:
	dir=`basename $$PWD`; cd ..; tar cvf $$dir.tar ./$$dir; gzip $$dir.tar

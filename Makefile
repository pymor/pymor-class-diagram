.PHONY: clean

class_diagram.svg: class_diagram.dot
	dot -Tsvg $< -o$@

class_diagram.dot: classes.txt
	python -c 'from helpers import create_dot; create_dot()'

classes.txt:
	grep -rPh 'class [A-Za-z_]+\(' pymor/src/pymor > classes.txt
	sed -i 's/class //' classes.txt
	sed -i 's/\s//g' classes.txt
	sed -i 's/://' classes.txt

clean:
	rm -f classes.txt class_diagram.dot class_diagram.svg

def create_dot():
    with open('classes.txt', 'r') as fin, open('class_diagram.dot', 'w') as fout:
        fout.write('digraph G {\n')
        fout.write('  rankdir = LR;\n')
        for line in fin:
            line = line.strip('\n')
            if '(' in line:
                class_name, other = line.split('(')
                super_classes = other[:-1].split(',')
                for i, super_class in enumerate(super_classes):
                    super_class_clean = super_class.split('=')[-1]
                    fout.write(f'  "{super_class_clean}" -> "{class_name}"')
                    if i > 0:
                        fout.write('[style=dashed]')
                    fout.write(';\n')
            else:
                fout.write(f'  "{line}";\n')
        fout.write('}\n')

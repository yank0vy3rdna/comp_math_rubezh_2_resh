from methods.methods_chooser import methods


def main():
    with open('input.txt') as f:
        lines = f.readlines()
        num = int(lines[0])
        key = list(methods.keys())[num]
        method = methods[key]
        method(lines)


if __name__ == '__main__':
    main()

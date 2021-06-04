def polyLagrange(xes, yes, argument):
    L = 0
    for i in range(len(xes)):
        l = 1
        string = f'l({i}) = '
        for j in range(len(xes)):
            if i != j:
                l *= (argument - xes[j]) / (xes[i] - xes[j])
                string += f'({argument} - {xes[j]}) / ({xes[i]} - {xes[j]}) * '
        string += f'= {l}'
        print(string)
        L += l * yes[i]

    return L


def f(lines):
    xes = [float(i) for i in lines[1].split()]
    yes = [float(i) for i in lines[2].split()]
    val = float(lines[3])
    print('Вики: https://en.wikipedia.org/wiki/Lagrange_polynomial')
    print()
    print(f'L({val}) = sum(l(i)*y_i) = {polyLagrange(xes, yes, val)}')

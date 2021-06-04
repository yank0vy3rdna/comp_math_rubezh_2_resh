def polyNewton(xes, yes, k):
    answer = 0
    string = f'f(x_0, ... x_{k}) = '
    for i in range(k + 1):
        string += f'{yes[i]} / ('
        pr = 1
        for j in range(k + 1):
            if j != i:
                pr *= xes[i] - xes[j]
                string += f'({xes[i]} - {xes[j]})'
        string += ') + '
        answer += yes[i] / pr
    string += f' = {answer}'
    print(string)
    return answer


def fNewton(xes, yes, argument):
    answer = polyNewton(xes, yes, 0)
    for i in range(1, len(xes)):
        pr = 1
        for j in range(i):
            pr *= argument - xes[j]
        answer += polyNewton(xes, yes, i) * pr
    return answer


def f(lines):
    xes = [float(i) for i in lines[1].split()]
    yes = [float(i) for i in lines[2].split()]
    val = float(lines[3])
    print()
    print(f'N({val}) = {fNewton(xes, yes, val)}')

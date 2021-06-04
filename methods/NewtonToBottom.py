import math


def dyes(yes, k, por):
    if por == 0:
        return yes[k]
    else:
        return dyes(yes, k, por - 1) - dyes(yes, k - 1, por - 1)


def fNewton(xes, yes, argument):
    print()
    just_i = len(xes) - 1
    answer = 0
    q = (argument - xes[just_i]) / (xes[1] - xes[0])
    print(f'q=(x - x_{just_i})/h=', q)
    pr = 1
    string_pr = ''
    string = f'P({argument})='
    for i in range(len(xes)):
        d = dyes(yes, just_i, i)
        print(f'd^{i}y_{just_i}={d}')
        answer += d * pr / math.factorial(i)
        string += f'+{string_pr}*{d}/{i}!'
        pr *= q + i
        string_pr += f'({round(q,5)}+{round(i,5)})'
    print(string)
    return answer


def f(lines):
    yes = [float(i) for i in lines[1].split()]
    x = float(lines[2])
    h = float(lines[3])
    xes = [x + h * i for i in range(len(yes))]
    val = float(lines[4])
    print(f'P({val}) = {fNewton(xes, yes, val)}')

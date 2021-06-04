from methods import Lagrange, Newton, NewtonToBottom, NewtonToTop

methods = {
    'Lagrange': Lagrange.f,
    'Newton': Newton.f,
    'Newton from Top to Bottom': NewtonToBottom.f,
    'Newton to Top from Bottom': NewtonToTop.f
}

import time

from decorators import benchmark
from math_commons import h, v, createPrecomputationArray, getBinaryArray, getEmptyArray


@benchmark
def precompute(G, l, S, a, b):
    t0 = time.perf_counter()
    hc = h(l, a)
    vc = v(a, b)
    array = createPrecomputationArray(G, a, b, l)

    for row in range(1, 2 ** hc):
        binaryArray = getBinaryArray(row)
        l = h(l, a) - len(binaryArray)
        binary = getEmptyArray(hc)
        binary[l:] = binaryArray

        array = performSquaring(G, a, hc, array, row, binary)
        array = performMultiplying(vc, b, row, array)

    t1 = time.perf_counter()
    return array


def performSquaring(G, a, hc, array, row, binary):
    for iterator in range(hc):
        exponent = pow(2, iterator * a)
        r = G * exponent
        array[0][row] += r * binary[-(iterator + 1)]
    return array


def performMultiplying(vc, b, row, array):
    for iterator in range(1, vc):
        array[iterator][row] = array[0][row] * (pow(2, iterator * b))
    return array

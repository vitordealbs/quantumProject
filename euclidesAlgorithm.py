from idna import ulabel


def extend_euclidian(a,b):
    r = a
    rl = b
    u = 1
    v = 0
    u1 = 0
    v1 = 1
    auxr = 0
    auxu = 0
    auxv = 0
    q = 0

    while(rl != 0):
        q = r//rl
        auxr = r
        auxu = u
        auxv = v
        r = rl
        u = u1
        v = v1
        rl = auxr - q *rl
        u1 = auxu - q *u
        v1 = auxv - q *v
    return [r, u, v]


print(extend_euclidian(340,29))
import random

def miller_rabin(n: int, rounds: int = 40) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    # Escreve n-1 como 2^s * d
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(rounds):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)  # a^d mod n — built-in, eficiente para n grande

        if x == 1 or x == n - 1:
            continue  # passou essa rodada

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # composto com certeza

    return True  # provavelmente primo


# Teste
print(miller_rabin(2**127 - 1))          # True  — primo de Mersenne
print(miller_rabin(2**1024 + 643))       # depende — número enorme
print(miller_rabin(561))                 # False — número de Carmichael (engana Fermat, não engana Miller-Rabin)
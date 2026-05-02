"""
Biel Piqué
"""

import doctest

class Aleat:
    """
    Implementación del algoritmo LGC como un iterador.

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    16
    29
    18
    15
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    18
    15
    20
    1
    """

    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        """Inicialización con argumentos forzosamente por clave."""
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __iter__(self):
        """Retorna el iterador."""
        return self

    def __next__(self):
        """Genera el siguiente número aleatorio."""
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, x0, /):
        """Reinicia la semilla. Argumento forzosamente posicional."""
        self.x = x0


def aleat(*, m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora del algoritmo LGC.

    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    34
    24
    38
    44
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    44
    10
    32
    14
    """
    x = x0
    while True:
        x = (a * x + c) % m
        recibido = yield x
        if recibido is not None:
            x = recibido

if __name__ == "__main__":
    doctest.testmod(verbose=True)
matrika = [
    [1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [5, 2, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 4, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

from typing import Dict, Tuple

RedkaMatrika = Tuple[int, Dict[Tuple[int, int], int], int, int]


redka_matrika: RedkaMatrika = (
    1,
    {(0, 2): 4, (1, 0): 5, (1, 1): 2, (2, 4): 3, (4, 2): 4},
    6,
    9,
)

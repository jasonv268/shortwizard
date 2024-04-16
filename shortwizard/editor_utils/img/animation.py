from math import sin
import math


class Animation:
    def __init__(self, position_func=None, size_func=None) -> None:
        self.position_func = position_func
        self.size_func = size_func


battement = Animation(size_func=lambda t: (1 + sin(10 * t) * 0.2),
                      position_func=lambda x, y, t: (x, y + sin(10 * t) * (-50)))

slide = Animation(position_func=lambda x, y, t: (x-100 + t*50, y)
                  if x - t*50 < x+50 else (x+50, y))

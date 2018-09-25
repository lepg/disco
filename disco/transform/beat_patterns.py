from typing import List


class Pattern:

    def __init__(self, positions: List[float], color: str):
        self.positions, self.color = positions, color

    def __iter__(self):
        return iter(self.positions)

    def __eq__(self, other):
        return type(self) is type(other) and self.positions == other.positions and self.color == other.color

    @classmethod
    def rhythm(cls, *signatures, color=None):
        offsets, offset, x = [], 0, None

        for notes, rate in signatures:
            for x in range(notes):
                offsets.append(offset + x / rate * 4)

            offset += (x + 1) / rate * 4

        assert all(0 <= x < 4 for x in offsets)
        return cls(offsets, color)


BEAT_PATTERNS = [
    Pattern.rhythm((4, 4), color='blue'),
    Pattern.rhythm((2, 2), color='red'),
    Pattern.rhythm((8, 8), color='green'),
    Pattern.rhythm((16, 16), color='brown'),
    Pattern.rhythm((1, 4), color='yellow'),
    Pattern.rhythm((8, 16), (2, 4), color='orange'),
    Pattern([0, 0.5, 2, 2.5], 'purple')
]

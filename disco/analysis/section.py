import random
from typing import List

from disco.transform.transition import Transition
from disco.analysis.measure import Measure


class Section(object):
    CONST_RANDOM = random.Random('test')

    def __init__(self, measures: List[Measure], pattern_base, sr):
        self.measures, self.sr = measures, sr
        self.pattern = self.CONST_RANDOM.choice(pattern_base)

    def transitions(self):
        for measure in self.measures:
            for subbeat in self.pattern:
                yield Transition(measure.beat(subbeat), self.pattern.color, self.sr)

    def __repr__(self):
        return f'Section({len(self.measures)} measures at {self.pattern})'

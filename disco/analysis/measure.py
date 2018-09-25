import librosa


class Measure(object):

    def __init__(self, start: int, end: int, beats_per_measure: int, sr: int):
        self.start, self.end, self.beats_per_measure, self.sr = start, end, beats_per_measure, sr
        self.beat_length = len(self) / beats_per_measure

    def __len__(self):
        return self.end - self.start

    def __repr__(self):
        return f'Measure({self.start} -> {self.end}, {len(self)} frames, {self.power} power)'

    def beat(self, position):
        assert 0 <= position < 4
        return int(self.start + position * self.beat_length)

    @property
    def time(self):
        return librosa.frames_to_time(self.start, self.sr)
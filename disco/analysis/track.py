import librosa

from disco.analysis.section import Section
from disco.analysis.measure import Measure
from disco.utils import cache
from disco.utils.collection_utils import chunks


class Track(object):

    def __init__(self, file_path, duration=None):
        self.file_path = file_path

        self.y, self.sr = cache.load(file_path, 'y', lambda: librosa.load(file_path, offset=0, duration=duration))
        self.o_env = cache.load(file_path, 'o_env', lambda: librosa.onset.onset_strength(self.y, sr=self.sr))
        self.tempo, self.beat_track = cache.load(file_path, 'beat_track', lambda: librosa.beat.beat_track(self.y, self.sr, onset_envelope=self.o_env))

    def measures(self, beats_per_measure=4):
        for beats in chunks(self.beat_track, beats_per_measure, overlap=1):
            o_env_slice = self.o_env[beats[0]:beats[-1]]
            yield Measure(beats[0], beats[-1], beats_per_measure, self.sr)

    def sections(self, pattern_base):
        measures = list(self.measures())
        for measures in chunks(measures, 4):
            yield Section(measures, pattern_base, self.sr)

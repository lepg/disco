import librosa


class Transition(object):

    def __init__(self, frame: int, color: str, sr: int, text: str=None):
        self.frame, self.color, self.text, self.sr = frame, color, text, sr

    def serialize(self):
        return {
            'frame': self.frame,
            'time': self.time,
            'color': self.color,
            'text': self.text
        }

    @property
    def time(self):
        return librosa.frames_to_time(self.frame, self.sr)

    def __repr__(self):
        return f'Transition({self.time} {self.color}'

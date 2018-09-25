from disco.analysis.track import Track
from disco.transform.beat_patterns import BEAT_PATTERNS, Pattern

from disco.utils.collection_utils import flatten
from disco.visualize.visualize import visualize

beat_pattern_iterator = iter(BEAT_PATTERNS)

if __name__ == '__main__':
    f = '/Users/ytanay/Music/Hadag Nahash/Lazuz/02 Lazuz.mp3'

    track = Track(f)
    measures = list(track.measures())
    SR = track.sr
    a, b, c = list(flatten(track.sections(BEAT_PATTERNS))), list(flatten(track.sections(BEAT_PATTERNS))), list(
        flatten(track.sections([Pattern.rhythm((4, 4), color='white')])))

    visualize(f, a, b, c)

import librosa

from disco.visualize.visualize import visualize


def onset_times(input_file, duration: float=None):
    y, sr = librosa.load(input_file, offset=30, duration=duration)
    # o_env = librosa.onset.onset_strength(y, sr=sr)
    # onset_frames = librosa.onset.onset_detect(y=y, sr=sr, onset_envelope=o_env)
    return librosa.frames_to_time(onset_frames, sr=sr)


f = librosa.util.example_audio_file()
times = onset_times(f)
print(times)

visualize(f, times, offset=30)

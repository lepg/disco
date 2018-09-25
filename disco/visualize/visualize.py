import json
import os
import tempfile
import webbrowser
from typing import List


CURRENT_PATH = os.path.dirname(__file__)

with open(os.path.join(CURRENT_PATH, 'visualization_template.html')) as f:
    TEMPLATE = f.read()


def visualize(audio_path: str, *channels: List, offset: float=0, power=None):
    """
    Opens a browser window with a visualization of any number of time-channels
    """

    rendered = TEMPLATE\
        .replace('{{AUDIO_FILE}}', audio_path)\
        .replace('{{OFFSET}}', str(offset))\
        .replace('{{CHANNEL_DATA}}', json.dumps([[x.serialize() for x in channel] for channel in channels], indent=4))

    with tempfile.NamedTemporaryFile('w', suffix='.html', delete=False) as f:
        f.write(rendered)
        f.flush()
        webbrowser.open(f.name)

import os

import mido
import pytest

from beatboxer.midi_processing.midi_to_text import midi_to_text
from beatboxer.midi_processing.text_to_midi import text_to_midi


@pytest.fixture
def sample_midi(tmp_path):
    """
    Fixture to create a sample MIDI file for testing.
    """
    midi_file = tmp_path / "sample_input.mid"
    midi = mido.MidiFile()
    track = mido.MidiTrack()
    midi.tracks.append(track)
    track.append(mido.Message("note_on", note=60, velocity=64, time=0))
    track.append(mido.Message("note_off", note=60, velocity=64, time=200))
    midi.save(midi_file)
    return midi_file


@pytest.fixture
def sample_text(tmp_path):
    """
    Fixture to create a sample text representation of MIDI messages for testing.
    """
    text_file = tmp_path / "sample_text_input.txt"
    text_representation = "note_on channel=0 note=60 velocity=64 time=0\nnote_off channel=0 note=60 velocity=64 time=200"
    with open(text_file, "w") as f:
        f.write(text_representation)
    return text_file

import os

import pytest

from beatboxer.midi_processing.midi_to_text import midi_to_text


def test_midi_to_text(sample_midi, tmp_path):
    """
    Test the conversion of a MIDI file to its text representation.
    """
    output_txt = tmp_path / "test_output.txt"
    text_representation = midi_to_text(sample_midi)
    with open(output_txt, "w") as f:
        f.write(text_representation)

    assert "note_on" in text_representation
    assert "note_off" in text_representation

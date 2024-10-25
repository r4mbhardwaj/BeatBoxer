import os

import mido
import pytest

from beatboxer.midi_processing.text_to_midi import text_to_midi


def test_text_to_midi_conversion(sample_text, tmp_path):
    """
    Test converting a text representation back into a MIDI file.
    """
    output_midi_file = tmp_path / "test_output_midi.mid"
    text_to_midi(sample_text, output_midi_file)

    assert os.path.exists(output_midi_file)
    # Verify the output MIDI file
    midi = mido.MidiFile(output_midi_file)
    track = midi.tracks[0]
    assert len(track) == 3  # Adjust to account for MetaMessage 'end_of_track'
    assert track[0].type == "note_on"
    assert track[1].type == "note_off"
    assert track[2].type == "end_of_track"

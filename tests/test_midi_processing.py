# beatboxer/tests/test_midi_processing.py
import os

import mido
import pytest

from beatboxer.midi_processing.midi_to_text import midi_to_text
from beatboxer.midi_processing.text_to_midi import text_to_midi


def test_midi_to_text(tmp_path):
    # Setup: Create a simple MIDI file
    midi_file = tmp_path / "test_input.mid"
    output_txt = tmp_path / "test_output.txt"
    output_midi = tmp_path / "test_output.mid"

    # Test: Write a dummy MIDI file and use midi_to_text
    midi = mido.MidiFile()
    track = mido.MidiTrack()
    midi.tracks.append(track)
    track.append(mido.Message("note_on", note=60, velocity=64, time=0))
    track.append(mido.Message("note_off", note=60, velocity=64, time=200))
    midi.save(midi_file)

    # Use the midi_to_text function
    text_representation = midi_to_text(midi_file)
    with open(output_txt, "w") as f:
        f.write(text_representation)

    assert "note_on" in text_representation
    assert "note_off" in text_representation

    # Test: Convert text back to MIDI
    text_to_midi(output_txt, output_midi)
    assert os.path.exists(output_midi)


def test_text_to_midi_conversion(tmp_path):
    # Test: Create a dummy text representation and convert it back to MIDI
    text_file = tmp_path / "test_text_input.txt"
    output_midi_file = tmp_path / "test_output_midi.mid"
    text_representation = "note_on channel=0 note=60 velocity=64 time=0\nnote_off channel=0 note=60 velocity=64 time=200"

    with open(text_file, "w") as f:
        f.write(text_representation)

    # Test: Convert text to MIDI
    text_to_midi(text_file, output_midi_file)

    assert os.path.exists(output_midi_file)
    # Verify the output MIDI file
    midi = mido.MidiFile(output_midi_file)
    track = midi.tracks[0]
    assert len(track) == 3  # Adjust to account for MetaMessage 'end_of_track'
    assert track[0].type == "note_on"
    assert track[1].type == "note_off"
    assert track[2].type == "end_of_track"

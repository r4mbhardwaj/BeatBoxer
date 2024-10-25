import mido


def midi_to_text(midi_file):
    """
    Convert a MIDI file to its text representation.

    Parameters:
    midi_file (str): Path to the input MIDI file.

    Returns:
    str: Text representation of the MIDI file.
    """
    midi = mido.MidiFile(midi_file)
    text_representation = []

    for track in midi.tracks:
        for msg in track:
            text_representation.append(str(msg))

    return "\n".join(text_representation)

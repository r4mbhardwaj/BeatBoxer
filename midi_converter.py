import os

from beatboxer.midi_processing.midi_to_text import midi_to_text
from beatboxer.midi_processing.text_to_midi import text_to_midi


def main():
    # Convert MIDI to text
    midi_file = "data/raw/input.mid"  # Adjust path to point to your MIDI file
    text_file = "data/processed/output.txt"
    output_midi_file = "data/processed/output.mid"

    try:
        # MIDI to Text Conversion
        print("Converting MIDI to text...")
        text_rep = midi_to_text(midi_file)
        with open(text_file, "w") as f:
            f.write(text_rep)
        print(f"MIDI successfully converted to text and saved as {text_file}")

        # Text to MIDI Conversion
        print("Converting text back to MIDI...")
        text_to_midi(text_file, output_midi_file)
        print(
            f"Text successfully converted back to MIDI and saved as {output_midi_file}"
        )
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

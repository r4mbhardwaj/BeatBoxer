import mido
from mido import Message, MetaMessage, MidiFile, MidiTrack, UnknownMetaMessage


def text_to_midi(text_file, output_midi_file):
    """
    Convert a text representation of a MIDI file back into a MIDI file.

    Parameters:
    text_file (str): Path to the input text file.
    output_midi_file (str): Path to save the output MIDI file.
    """
    with open(text_file, "r") as f:
        lines = f.readlines()

    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    for line in lines:
        if line.strip():  # Only process non-empty lines
            msg_str = line.strip()
            if msg_str.startswith("MetaMessage") or msg_str.startswith(
                "UnknownMetaMessage"
            ):
                try:
                    parts = msg_str.split("(", 1)[1].strip(") ").split(", ")
                    msg_type = parts[0].split("=")[1].strip("'")
                    params = {
                        param.split("=")[0]: param.split("=")[1].strip()
                        for param in parts[1:]
                        if "=" in param
                    }

                    if "name" in params:
                        params["name"] = params["name"].strip("'")

                    if msg_str.startswith("UnknownMetaMessage"):
                        data_str = params.get("data", "()")[1:-1]
                        data = (
                            tuple(int(x) for x in data_str.split(",") if x)
                            if data_str
                            else ()
                        )
                        msg = UnknownMetaMessage(
                            type_byte=int(parts[0].split("=")[1]),
                            data=data,
                            time=int(params["time"]),
                        )
                    else:
                        msg = MetaMessage(msg_type, **params)
                except (IndexError, ValueError) as e:
                    print(f"Error parsing message: {msg_str} ({e})")
                    continue
            else:
                msg_parts = msg_str.split()
                msg_type = msg_parts[0]
                msg_params = {}
                for part in msg_parts[1:]:
                    if "=" in part:
                        key, value = part.split("=")
                        msg_params[key] = int(value) if value.isdigit() else value
                msg = Message(msg_type, **msg_params)

            track.append(msg)

    midi.save(output_midi_file)

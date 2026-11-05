from dataclasses import dataclass


@dataclass
class MusicalNote:
    pitch: str
    start_beat: float
    duration: float
    voice: str = "melody"
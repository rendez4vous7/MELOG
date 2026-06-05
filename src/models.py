from dataclasses import dataclass

@dataclass
class MelogNode:
    string: int
    fret: int
    time: int

    role: str = ""
    stem: str = "up"

    is_tied: bool = False
    is_slur: bool = False
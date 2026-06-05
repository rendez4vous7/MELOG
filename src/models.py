from dataclasses import dataclass, field

@dataclass
class MelogNode:
    string: int
    fret: int
    time: int

    id: int | None = None

    role: str = ""
    stem: str = "up"

    is_tied: bool = False
    is_slur: bool = False

@dataclass
class MelogCell:
    time: int
    nodes: list = field(default_factory=list)
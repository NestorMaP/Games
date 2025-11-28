from dataclasses import dataclass
from typing import List

from PlayerEnum import Player

@dataclass
class Node:
    board:List[List[str]]
    turn: Player
    childrens: List["Node"]
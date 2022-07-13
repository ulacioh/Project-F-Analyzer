from dataclasses import dataclass
from typing import List, Union


X = int
Y = int
Width = int
Height = int
Position = List[Union[X, Y]]
Dimentions = List[Union[Width, Height]]


@dataclass(frozen=True)
class Element:
    position: Position
    dimentions: Dimentions

from dataclasses import dataclass
from typing import Final, Sequence

from .types import Element


class Driver(Element):
    # Position on the session. Not on the screen! lol
    position_: Final[Element] = Element(position=[0, 0], dimentions=[32, 35])
    name: Final[Element] = Element(position=[76, 0], dimentions=[54, 35])
    sectors: Final[Element] = Element(position=[76, 0], dimentions=[54, 35])

@dataclass(frozen=True)
class GraphicsBase():
    driver: Driver
    gp_title: Final[Element] = Element(position=[230, 50], dimentions=[1140, 64])
    session: Final[Element] = Element(position=[1382, 45], dimentions=[220, 70])
    driver_offset: Final[Sequence[int]] = (36, 36, 35)


QualyGraphics = GraphicsBase(
    Driver(position=[270, 0], dimentions=[101, 35])
)

RaceGraphics = GraphicsBase(
    Driver(position=[195, 0], dimentions=[101, 35])
)

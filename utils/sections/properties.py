# sections/models.py
from dataclasses import dataclass

from utils.units.structural_units import *

@dataclass
class SteelSectionProps:
    pass

@dataclass
class CnpGrp():
    t : float # mm
    A : float # cm2
    w : float # kg/m
    Ix: float # cm4
    Iy: float # cm4
    Zx: float # cm3
    Zy: float # cm3
    rx: float # cm
    ry: float # cm
    Cy: float # cm
    Xo: float # cm
    J: float # cm4
    Cw: float # cm6

@dataclass(frozen=True)
class SteelSection:
    name: str
    props: SteelSectionProps
    standard: str       # AISC, JIS, EN, SNI
    source: str         # e.g., "AISC 15th"

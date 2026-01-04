from dataclasses import dataclass
from .base import Material
from ..units.structural_units import *

@dataclass(frozen=True)
class Steel(Material):
    Fy: float        # yield strength
    Fu: float        # ultimate strength
    E: float         # Young's modulus
    nu: float        # Poisson's ratio
    density: float

ASTM_A992 = Steel(
    name="ASTM A992/A992M",
    source="ASTM A992/A992M",
    Fy=345 * MPa,
    Fu=450 * MPa,
    E=200_000 * MPa,
    nu=0.29,
    density=7850 * kg/m**3,
)

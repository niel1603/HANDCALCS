import csv
from utils.sections.properties import SteelSection, SteelSectionProps
from utils.units.structural_units import *

def load_steel_csv(path, standard):
    table = {}

    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for r in reader:
            name = r["name"].strip()

            props = SteelSectionProps(
                A  = float(r["A_cm2"])  * 100 * mm**2,
                Ix = float(r["Ix_cm4"]) * 1e4 * mm**4,
                Iy = float(r["Iy_cm4"]) * 1e4 * mm**4,
                Zx = float(r["Zx_cm3"]) * 1e3 * mm**3,
                Zy = float(r["Zy_cm3"]) * 1e3 * mm**3,
                rx = float(r["rx_cm"]) * 10 * mm,
                ry = float(r["ry_cm"]) * 10 * mm,
            )

            table[name] = SteelSection(
                name=name,
                props=props,
                standard=standard,
                source=str(path),
            )

    return table


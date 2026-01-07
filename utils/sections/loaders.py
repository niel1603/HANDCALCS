import csv
from utils.sections.properties import (
    SteelSection, SteelSectionProps, 
    CnpGrp)
from utils.units.structural_units import *

def load_cnp_grp(path, standard):
    table = {}

    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        for r in reader:
            name = r["name"].strip()
            
            props = CnpGrp(
                t  = float(r["t_mm"]) * mm,
                A  = float(r["A_cm2"]) * cm**2,
                w  = float(r["w_kg/m"]) * kg/m,
                Ix = float(r["Ix_cm4"]) * cm**4,
                Iy = float(r["Iy_cm4"]) * cm**4,
                Zx = float(r["Zx_cm3"]) * cm**3,
                Zy = float(r["Zy_cm3"]) * cm**3,
                rx = float(r["rx_cm"]) * cm,
                ry = float(r["ry_cm"]) * cm,
                Cy = float(r["Cy_cm"]) * cm,
                Xo = float(r["Xo_cm"]) * cm,
                J  = float(r["J_cm4"]) * cm**4,
                Cw = float(r["Cw_cm6"]) * cm**6,
            )

            table[name] = SteelSection(
                name=name,
                props=props,
                standard=standard,
                source=str(path),
            )

    return table


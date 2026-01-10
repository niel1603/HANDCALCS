from handcalcs_adapter.section import section
sec = section("C150x50x20x3.2")

## 2. Selec purlin
section_name = (sec.name)
w_self = (sec.w) # self weight
I_x = (sec.Ix) # strong-axis moment of inertia
I_y = (sec.Iy) # weak-axis moment of inertia
Z_x = (sec.Zx) # strong-axis modulus of section
Z_y = (sec.Zy) # weak-axis modulus of section
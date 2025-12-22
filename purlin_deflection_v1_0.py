import math

# ============================================================
# INPUTS (EDIT THESE)
# ============================================================

# Span
L = 6.0                 # span [m]

# Load combination (given)
D = 0.6                 # dead load [kN/m]
LL = 1.2                # live load [kN/m]
w_total = D + LL        # total service load [kN/m]

# Material
E = 200_000             # Young's modulus [MPa = N/mm²]

# Section properties (example values - REPLACE with real C-purlin)
Ix = 7.16e6              # strong-axis inertia [mm^4]
Iy = 0.84e6              # weak-axis inertia [mm^4]

# Geometry
theta_deg = 10.0        # purlin roll angle from strong axis [deg]

# ============================================================
# CONVERSIONS
# ============================================================

L_mm = L * 1000                          # m → mm
w = w_total                              # kN/m
w_Nmm = w * 1e3 / 1e3                    # kN/m → N/mm

theta = math.radians(theta_deg)

# ============================================================
# LOAD RESOLUTION
# ============================================================

w_strong = w_Nmm * math.cos(theta)
w_weak   = w_Nmm * math.sin(theta)

# ============================================================
# DEFLECTION CALCULATIONS (SIMPLY SUPPORTED, UDL)
# ============================================================

deflection_strong = (5 * w_strong * L_mm**4) / (384 * E * Ix)
deflection_weak   = (5 * w_weak   * L_mm**4) / (384 * E * Iy)

# Resultant deflection
deflection_total = math.sqrt(
    deflection_strong**2 + deflection_weak**2
)

# ============================================================
# OUTPUT
# ============================================================

print("PURLIN DEFLECTION CHECK (1.0D + 1.0LL)")
print("-------------------------------------")
print(f"Span                 : {L:.2f} m")
print(f"Total load           : {w_total:.2f} kN/m")
print(f"Purlin roll angle    : {theta_deg:.1f} deg")
print()
print("Deflection results:")
print(f"  Strong-axis defl.  : {deflection_strong:.2f} mm")
print(f"  Weak-axis defl.    : {deflection_weak:.2f} mm")
print(f"  Resultant defl.    : {deflection_total:.2f} mm")
print()
print(f"Deflection ratio L/δ : {L_mm / deflection_total:.0f}")

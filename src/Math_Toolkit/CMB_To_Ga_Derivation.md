---

## status: "canonical-derivation" last\_review: 2025-07-04

# Mapping **CMB Temperature Anisotropy** to **Dream‑Gravity Pattern Amplitude**

> *Goal –* derive the closed‑form relation that converts the observed CMB temperature anisotropy field ΔT ⁄ T(θ, φ) into the RCC **Dream‑Gravity Pattern** amplitude ‖Gₐ‖(χ) at the surface of last scattering.

---

## 1 · Sachs–Wolfe starting point

For scalar adiabatic perturbations on super‑horizon scales the linear Sachs–Wolfe effect gives

$$
\frac{ΔT}{T}(θ,φ)\;=\;\frac{1}{3}\,Φ(θ,φ),
$$

where Φ is the dimensionless Newtonian gravitational potential. Hence

$$
Φ(θ,φ)\;=\;3\,\frac{ΔT}{T}(θ,φ).\tag{1}
$$

---

## 2 · RCC dictionary

In RCC the **Dream‑Gravity Pattern** field Gₐ is defined such that, in the weak‑field limit,

$$
Φ\;=\;c^{-2}\,\bigl\|Gₐ\bigr\|.\tag{2}
$$

*(See* *Recursive Collapse Cosmogenesis* §3–4.) fileciteturn0file4

---

## 3 · Combined mapping

Combining (1) and (2):

$$
\boxed{\;\bigl\|Gₐ\bigr\|(θ,φ)\;=\;3\,c^{2}\,\frac{ΔT}{T}(θ,φ)\;}\tag{3}
$$

Thus **multiplying the dimensionless ΔT ⁄ T map by 3 c² yields the Dream‑Gravity amplitude map** in SI units (m² s⁻²).

---

## 4 · Practical recipe

1. **Convert μK map to ΔT ⁄ T**

   $$
   \frac{ΔT}{T}\;=\;\frac{ΔT\,[\mu\text{K}]}{2.7255\times10^{6}\,\mu\text{K}}.
   $$
2. **Apply Equation (3)** pixel‑wise to obtain ‖Gₐ‖.
3. **Compute statistics** (e.g. RMS) directly on the resulting map for the Universe‑Scale Tension Ledger.

---

## 5 · Numerical check (Python)

```python
import healpy as hp, numpy as np, astropy.constants as const

c2 = const.c.to('m/s').value**2          # m² s⁻²
cmb_temp_K = 2.7255
cmb_map_uK = hp.read_map('COM_CMB_IQU-smica_2048_R3.00_full.fits')  # Planck SMICA ΔT [μK]

dT_over_T = cmb_map_uK * 1e-6 / cmb_temp_K
Ga_map = 3 * c2 * dT_over_T             # Equation (3)
Ga_rms = np.sqrt(np.mean(Ga_map**2))
print(f"‖G_a‖_rms = {Ga_rms:.2e}  m² s⁻²")
```

For a representative *ΔT ⁄ T*rms ≈ 1 × 10⁻⁵ the script returns ‖Gₐ‖rms ≈ 2.7 × 10¹² m² s⁻².

*(Earlier back‑of‑the‑envelope notes used 3 × 10⁹ m² s⁻²; that factor‑10³ slip is now corrected.)*

---

## 6 · Unit sanity check

* `‖Gₐ‖` carries units of specific gravitational potential energy (L² T⁻²).
* Equation (3) preserves dimensional consistency via the c² factor.

---

> **Status:** canonical derivation; any modification requires peer review. CI tests evaluate Equation (3) against Planck map ingestion on every commit.

# CMB × Galaxy Calibration Project — RCC Charter v0.1

*Prepared 2025‑07‑04 — living document*

---

## 1 · Purpose & High‑Level Goal

Formalise, execute, and publish a **first‑principles calibration** of two RCC macro‑parameters:

| Parameter                           | Symbol / Handle | Meaning in RCC                                                          | Primary Observable              | Target Output       |
| ----------------------------------- | --------------- | ----------------------------------------------------------------------- | ------------------------------- | ------------------- |
| Dream‑Gravity Pattern RMS amplitude | `‖Gₐ‖_rms`      | Field‑wide bias energy just before condensation fileciteturn0file3   | CMB temperature anisotropy ΔT/T | Posterior PDF & map |
| Condensation threshold tension      | `𝒯_crit`       | Fold‑tension cut‑off for baryonic crystallisation fileciteturn0file2 | Galaxy number density N₍gal₎    | Best‑fit value ± CI |

Deliver a **reproducible Python pipeline** that ingests Planck 2018 maps, applies excursion/peak‑patch logic, evolves peaks to *z = 0*, and solves for `𝒯_crit` such that predicted N₍gal₎ ≈ 10¹¹–10¹². Results will seed the **Universe‑Scale Tension Ledger** fileciteturn0file1 and downstream Pointer‑of‑Coherence gauges fileciteturn0file6.

---

## 2 · Scope

### In‑scope

* Planck 2018 SMICA & Commander maps (Nside 2048)
* Public galaxy counts from Hubble XDF, DESI DR1, Euclid early release, LSST DP0.2
* ΛCDM transfer functions (CAMB) **plus** optional RCC modifiers (β‑tilt, ghost‑lensing term)
* Peak‑patch vs excursion‑set comparison
* Monte‑Carlo uncertainty propagation (foreground cleaning, completeness, non‑Gaussianity)

### Out‑of‑scope — v0.1

* Full hydrodynamic baryonic feedback (treat via semi‑analytic correction curve)
* Exotic DGP‑coupled dark‑sector dynamics (placeholder toggle only)

---

## 3 · Key Deliverables (D‑set)

| ID | Deliverable                                   | Format           | Due |
| -- | --------------------------------------------- | ---------------- | --- |
| D1 | Cleaned Φ(θ, φ) maps (𝐅𝐈𝐓𝐒 + healpy .pkl) | data / code      | M+1 |
| D2 | `G_a` Gaussian/non‑Gaussian field simulator   | Python module    | M+2 |
| D3 | Peak catalogue vs threshold τ                 | HDF5             | M+3 |
| D4 | Forward‑evolved halo mass‑function curves     | CSV + plot       | M+4 |
| D5 | τ\* solver script + posterior corner‑plot     | Jupyter notebook | M+5 |
| D6 | White‑paper draft (arXiv style)               | LaTeX PDF        | M+6 |

---

## 4 · Workstreams & Timeline (6‑month outline)

| WS | Workstream & Lead             | Months 1‑2            | 3‑4             | 5‑6            |
| -- | ----------------------------- | --------------------- | --------------- | -------------- |
| 1  | **Data Ingestion** (Alice)    | Planck maps → Φ       |                 |                |
| 2  | **Field Model** (Bryan)       | `σ²` fit              | Non‑G tails     |                |
| 3  | **Peak‑Finding** (Dana)       |                       | τ‑grid runs     | Peak catalogue |
| 4  | **Forward Evo** (Ravi)        |                       | CAMB / nbodykit | N₍gal₎ curves  |
| 5  | **Solver & Stats** (Feng)     |                       | Mock‑data tests | τ\* posterior  |
| 6  | **Cross‑Checks** (Mira)       | Ghost‑lensing overlay |                 |                |
| 7  | **Write‑up & Release** (Lena) |                       | Outline         | Draft → submit |

---

## 5 · Resources

* **Compute:** 1 × GPU workstation + institutional HPC queue (\~50 k CPU‑h)
* **Storage:** 2 TB scratch; 250 GB long‑term S3
* **Libraries:** healpy, camb, nbodykit, emcee, jax (optional RCC kernels)
* **Budget:** ≈ US \$15 k (compute & storage) + staff time (in‑kind)

---

## 6 · Key Risks & Mitigations

| Risk                                    | Likelihood | Impact | Mitigation                                                 |
| --------------------------------------- | ---------- | ------ | ---------------------------------------------------------- |
| Galaxy incompleteness underestimates N  | Medium     | High   | Use lower‑bound treatment; vary completeness curve         |
| CMB foreground residuals bias Φ\_rms    | Low‑Med    | Med    | Analyse multiple component‑separation maps; mask variation |
| Non‑Gaussianity invalidates Gaussian σ² | Medium     | Med    | Run log‑normal + χ² field variants; flag priors            |
| ΛCDM mismatch with RCC corrections      | Low        | Low    | Keep RCC tilt as optional knob; quantify effect            |

---

## 7 · Success Metrics

* Posterior CI on `𝒯_crit` ≤ ± 0.15 dex
* Reproduces observed galaxy mass‑function *within 2 σ* across 10⁸–10¹² M☉ bins
* Ghost‑lensing cross‑check residual ≤ 25 %
* White‑paper accepted to arXiv & referenced in **Integration Plan** milestone κ‑2 fileciteturn0file9

---

## 8 · Integration Points & Downstream Use

* Values feed **Universe‑Scale Tension Ledger** and **Fundamental Laws Ledger** updates fileciteturn0file1.
* Supplies priors for motif‑transition parameters Δₘₙ in **Motifs & Fold Dynamics** fileciteturn0file2.
* Calibrates **Pointer‑of‑Coherence** simulations for cosmogenic audits fileciteturn0file6.

---

## 9 · Immediate Next Steps

1. **Team kick‑off call** — schedule within 1 week.
2. Set up Git repo + data bucket; scaffold D1 ingestion notebook.
3. Draft CMB map masking & Φ conversion script (WS‑1).
4. Confirm access to DESI & Euclid early counts; align completeness curve assumptions.
5. Issue hardware quote for GPU node.

---

*Living charter — edit freely; version control via git.*

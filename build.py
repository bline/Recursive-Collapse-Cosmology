#!/usr/bin/env python3
"""
build.py — concatenate bundles, copy single docs, rewrite links, emit PDF
"""

import re
import subprocess
from pathlib import Path

# ------------------------------------------------------------------ Config ---
BUNDLES = {
    # output name            ordered list of source files
    "03_Motifs_and_Fold_Dynamics.md": sorted(Path("src/mechanics/motifs").glob("0*.md")),
    "04_Five_Primary_Axes.md":        sorted(Path("src/practice/five_primary_axes").glob("0*.md")),
    "05_UMH.md":                      sorted(Path("src/practice/umh").glob("0*.md")),
    "06_RCC_Codex.md":                sorted(Path("src/rcc_codex").glob("0*.md")),
}

COPY_FILES = {
    "src/cosmology/recursive_collapse_cosmogenesis.md": "00_Recursive_Cosmogenesis.md",
    "src/laws/fundamental_laws_of_fold_dynamics.md":    "01_Fundamental_Laws_Ledger.md",
    "src/cosmology/fractal_field_ontology.md":          "02_Fractal_Field_Ontology.md",
    "src/mechanics/pointer_of_coherence.md":            "07_Pointer_of_Coherence.md",
    "src/ethics/sef.md":                                "08_Symmetry_Ethics_Framework.md",
    "src/integration/coherence_map.md":                 "09_Coherence_Map.md",
    "src/integration/integration_plan.md":              "10_Integration_Plan.md",
}

FINAL_DOCS = [
    "00_Recursive_Cosmogenesis.md",
    "01_Fundamental_Laws_Ledger.md",
    "02_Fractal_Field_Ontology.md",
    "03_Motifs_and_Fold_Dynamics.md",
    "04_Five_Primary_Axes.md",
    "05_UMH.md",
    "06_RCC_Codex.md",
    "07_Pointer_of_Coherence.md",
    "08_Symmetry_Ethics_Framework.md",
    "09_Coherence_Map.md",
    "10_Integration_Plan.md",
]

LINK_MAP = [
    ("../practice/five_primary_axes/", "04_Five_Primary_Axes.md"),
    ("../practice/umh/",               "05_UMH.md"),
    ("../rcc_codex/",                  "06_RCC_Codex.md"),
    ("../mechanics/motifs/",           "03_Motifs_and_Fold_Dynamics.md"),  # specific first
    ("../mechanics/",                  "07_Pointer_of_Coherence.md"),      # fallback
    ("../ethics/",                     "08_Symmetry_Ethics_Framework.md"),
    ("../integration/",                "09_Coherence_Map.md"),
]

# -------------------------------------------------------------- Helpers ------
def slugify(text: str) -> str:
    """Convert header to GitHub/Pandoc anchor slug."""
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

def rewrite_links(text: str) -> str:
    pattern = re.compile(r"\[([^\]]+)]\(([^)]+)\)")
    def _repl(match):
        label, rel = match.groups()
        for old, new in LINK_MAP:          # keep declared order
            if rel.startswith(old):
                slug = slugify(Path(rel).stem)
                return f"[{label}]({new}#{slug})"
        return match.group(0)
    return pattern.sub(_repl, text)

# ------------------------------------------------------------ Build steps ---
print("▶ Copying single-file docs …")
for src, dst in COPY_FILES.items():
    Path(dst).write_text(Path(src).read_text())

print("▶ Building bundled docs …")
for out, sources in BUNDLES.items():
    combined = [Path(f).read_text().strip() for f in sources]
    Path(out).write_text("\n\n".join(combined))

print("▶ Rewriting cross-links …")
for md in FINAL_DOCS:
    path = Path(md)
    path.write_text(rewrite_links(path.read_text()))

print("▶ Generating PDF …")
subprocess.run(
    ["pandoc", *FINAL_DOCS, "--toc", "--pdf-engine=xelatex", "--verbose", "--number-sections", "-o", "RCC_Documentation.pdf"],
    check=True
)

print("✅ Done.")

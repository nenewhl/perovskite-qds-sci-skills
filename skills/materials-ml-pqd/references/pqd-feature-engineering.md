# PQD Feature Engineering Guide

## Composition descriptors

For perovskite quantum dots, encode:

- A-site species: Cs, FA, MA, mixed A-site ratios.
- B-site species: Pb, Sn, Ge, Mn-doped, rare-earth-doped, alloyed species.
- Halide fractions: Cl, Br, I.
- Dopant identity and fraction.
- Stoichiometry deviation if known.

Recommended engineered descriptors:

- ionic radius descriptors for A, B, and X,
- Goldschmidt tolerance factor,
- octahedral factor,
- electronegativity statistics,
- halide radius mean and variance,
- estimated bandgap-related descriptors when justified,
- mixed-halide entropy or composition variance,
- dopant valence mismatch,
- dopant ionic-radius mismatch.

## Surface and ligand descriptors

PQD performance often depends strongly on surface chemistry. Preserve:

- ligand type: OA, OAm, DDAB, zwitterionic ligand, phospholipid, thiol, silane, polymer ligand, etc.
- ligand chain length,
- ligand functional group,
- ligand binding type when known,
- ligand ratio or concentration,
- purification cycles,
- post-treatment conditions.

Possible engineered descriptors:

- ligand chain carbon number,
- acid/base ligand indicator,
- ammonium/phosphonium/sulfonate/silane flags,
- ligand polarity class,
- hard/soft binding class,
- hydrophobicity proxy if justified.

## Synthesis descriptors

Record and encode:

- hot injection, room-temperature recrystallization, ligand-assisted reprecipitation, grinding, solvothermal, spin-coating, in situ growth,
- reaction temperature,
- reaction time,
- precursor concentration,
- solvent/antisolvent,
- injection temperature,
- purification protocol,
- inert atmosphere or air condition.

## Shell, matrix, and film descriptors

For stability and X-ray/scintillation-related PQD studies, encode:

- shell material: SiO2, ZnS, Al2O3, polymer, inorganic salt, ligand shell,
- matrix: PMMA, PS, PDMS, PVDF, glass, silica, MOF, polymer blend,
- shell strategy: in situ, physical mixing, sol-gel, ALD-like, ligand-assisted,
- film thickness,
- QD loading,
- layer number,
- substrate and encapsulation.

## Target variables for PQD ML

Common targets:

- PLQY,
- emission_peak_nm,
- FWHM_nm,
- lifetime_ns,
- stability_retention_percent,
- RL_intensity,
- light_yield,
- detection_limit,
- spatial_resolution,
- response_time,
- high_performance_label.

## Domain caution

Feature importance can be dominated by literature bias. For example, if most high-PLQY rows come from a few papers using a specific ligand, the model may learn source/lab bias rather than chemistry.

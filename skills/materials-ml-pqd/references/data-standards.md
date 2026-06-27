# Data Standards for PQD Materials ML

## Minimal table columns

Recommended columns:

```text
sample_id
source_id
A_site
B_site
X_site
composition
halide_Cl_fraction
halide_Br_fraction
halide_I_fraction
dopant
dopant_fraction
ligand_1
ligand_2
shell_material
matrix_material
synthesis_method
synthesis_temperature_C
reaction_time_min
solvent
antisolvent
purification_cycles
film_thickness_um
measurement_temperature_C
excitation_wavelength_nm
emission_peak_nm
FWHM_nm
PLQY
lifetime_ns
stability_retention_percent
target_metric
```

Not every dataset needs all columns. Missing columns should remain explicit rather than silently guessed.

## Required metadata for literature-extracted data

For each row, preserve:

- `source_id`: paper DOI or short ID,
- `figure_or_table`: where the value came from,
- `extraction_method`: manual, digitized, table, supplementary data,
- `unit_original`,
- `unit_converted`,
- `notes`.

## Unit conventions

Use consistent units:

- Temperature: °C or K, but do not mix silently.
- Time: min or h, converted into a consistent column.
- Thickness: µm or nm, converted consistently.
- PLQY: either 0–1 or percent; choose one and label it.
- Stability: retention percentage at a defined condition and duration.
- Emission peak: nm.
- FWHM: nm or meV, not mixed without conversion.

## Missing data

Accepted encodings:

- blank cells,
- `NaN`,
- `None`.

Do not encode missing values as 0 unless 0 is physically meaningful.

## Avoid target leakage

Do not use features that are directly calculated from the target unless explicitly modeling a downstream derived property.

Examples:

- Do not use color class to predict emission peak if color class was assigned from emission peak.
- Do not use post-aging PL intensity to predict stability retention.
- Do not use measured PLQY as a feature to predict high/low PLQY.

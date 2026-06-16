# PQD Figure Design

## Figure Contract

Before drawing, define:

- Core conclusion of the figure.
- Audience: thesis examiner or SCI reviewer.
- Data panels required to support the conclusion.
- Panel order: material/design -> characterization -> mechanism -> performance -> stability.
- Export format and target journal or thesis requirement.

## Visual Style

- White canvas, no decorative background.
- Arial, Helvetica, or compatible sans-serif.
- Panel letters in bold, consistent location.
- Thin axes and ticks; avoid heavy boxes unless matching journal style.
- Colorblind-aware palette. Good defaults: dark blue, teal, vermilion, purple, neutral gray. Use green carefully and avoid red/green-only comparisons.
- Use the same color for the same sample across all panels.
- Use vector export for plots and schematics. Use high-resolution raster only for microscopy/photos.

## Multi-Panel Archetypes

Mechanism-led PQD paper:

- a: Concept or synthesis/surface schematic.
- b: TEM/HRTEM and size distribution.
- c: XRD or composition/surface evidence.
- d: Absorption/PL/PLQY.
- e: TRPL or mechanism evidence.
- f: Device/function metric.
- g: Stability or benchmark.

Solar-cell paper:

- a: Device architecture and PQD film/process schematic.
- b: Structure/composition/film morphology.
- c: Energy levels or interface evidence.
- d: J-V curves with stabilized output.
- e: EQE plus integrated current.
- f: PCE statistics.
- g: Stability/hysteresis/benchmark.

LED/emission paper:

- a: Material/passivation concept.
- b: PL and PLQY/FWHM.
- c: Film/device structure.
- d: EL spectra and CIE.
- e: J-V-L curves.
- f: EQE/current density.
- g: Lifetime and benchmark.

X-ray detection paper:

- a: Scintillation/detector concept and setup.
- b: RL spectrum and optical image if relevant.
- c: Dose-rate response/linearity.
- d: Detection limit with noise criterion.
- e: Response/recovery.
- f: Imaging/spatial resolution.
- g: Radiation stability and benchmark.

## Thesis vs SCI

Thesis figures:

- Include complete controls, method diagrams, raw-to-processed examples, and supplementary distributions.
- Favor clarity and traceability over compression.

SCI top-journal figures:

- Each main figure must carry one claim.
- Move routine characterization to supplementary unless it is central.
- Use benchmarks only when comparable and current.
- Avoid overfilled panels; create clean insets only when necessary.

## QA Checklist

- All axes have units.
- Normalization is stated in labels or captions.
- Sample names are consistent.
- Panel letters and captions match.
- Microscopy scale bars are visible and correct.
- Legends do not cover data.
- Fonts remain readable at final print width.
- Colors are distinguishable in grayscale or colorblind preview.
- No unsupported mechanism arrows in schematics.

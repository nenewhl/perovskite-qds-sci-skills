# Workflow

## Intake

Before analysis or writing, identify:

- Material system or sample family, if provided.
- Measurement type and instrument output format.
- Raw file availability.
- Target output: exploratory analysis, report, manuscript figure, supplementary figure, or review comment.
- Missing metadata: units, acquisition settings, calibration, sample thickness, device area, integration time, excitation wavelength, dose/dose rate, scan rate, atmosphere, temperature, or number of replicates.

## Integrity rules

- Never overwrite raw data.
- Keep raw, processed, and exported files separate.
- Record all smoothing, normalization, baseline correction, interpolation, cropping, outlier exclusion, and fitting decisions.
- Do not infer physical quantities without required geometry, calibration, or units.
- Do not report performance improvements without a defined reference/control.

## Output contract

For complex tasks, provide:

1. Detected tracks.
2. Inputs used and missing metadata.
3. Processing or writing plan.
4. Result files or draft text, when created.
5. Quality-control checklist.
6. Limitations and next data needed.

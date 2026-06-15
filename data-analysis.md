# Data Analysis

## Supported data categories

- Steady-state photoluminescence and absorption spectra.
- Time-resolved photoluminescence or decay curves.
- Quantum yield, stability, and degradation time-series.
- Device J-V, EQE, luminance-voltage-current, responsivity, and response-speed datasets.
- Diffraction peak tables and microscopy-derived measurements.
- Imaging intensity matrices and resolution-related line profiles.

## General rules

- Preserve raw data and create a processing log.
- Normalize only when the claim is about shape, peak position, or relative comparison.
- Use absolute intensity only when calibration and acquisition settings are consistent.
- Baseline correction must be stated.
- Smoothing must not shift peak position or alter linewidth meaningfully.
- Fitting must include initial assumptions, bounds, fit residuals, and parameter uncertainty when possible.

## Common outputs

- Peak position, FWHM, integrated intensity, spectral overlap, lifetime components, average lifetime, stability retention, response linearity, sensitivity, detection limit, rise/fall time, and reproducibility statistics.

## Avoid

- Reporting more significant digits than justified.
- Treating normalized plots as proof of absolute intensity enhancement.
- Comparing device metrics measured under inconsistent conditions without caveats.

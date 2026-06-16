# PQD Data Analysis

## General Rules

- Keep raw, processed, and final-export datasets separate.
- Use explicit filenames: `sample_condition_date_instrument_raw.ext`, `..._processed.csv`, `..._fit.csv`, `..._figure.pdf`.
- Store processing parameters with the output: baseline method, smoothing window, normalization basis, fit model, bounds, excluded points, and software version.
- Use SI units unless field convention differs. Keep nm/eV conversion explicit: `E(eV)=1240/lambda(nm)`.

## Spectroscopy

UV-vis:

- Correct solvent or substrate baseline before comparison.
- Do not infer bandgap from absorption onset without describing method. Use Tauc only when the material and transition assumption are defensible.
- For QDs, report excitonic peak and changes in peak/FWHM rather than overinterpreting onset shifts.

PL/PLE/PLQY:

- Compare peak position, FWHM, integrated intensity, PLQY, and excitation wavelength.
- Normalize by area for shape comparison; use absolute intensity or PLQY for efficiency comparison.
- Watch reabsorption, concentration, inner-filter effects, and substrate scattering.

TRPL:

- Fit with the simplest model justified by residuals. Common forms: single, bi-, or tri-exponential; report amplitude-weighted and intensity-weighted lifetimes when relevant.
- Provide fit equation, instrument response handling, time window, chi-square/residual check, and uncertainty.
- Avoid claiming trap passivation from lifetime alone; connect with PLQY, XPS/FTIR, defect-sensitive measurements, or device performance.

## Structure and Microscopy

XRD:

- Mark expected perovskite phase peaks and possible impurity peaks.
- Use peak shift to support alloying/strain only with controls and composition evidence.
- Avoid Scherrer size claims when broadening may come from instrument, strain, or nanocrystal distribution unless corrected.

TEM/SEM/AFM:

- Report particle/grain size distributions from enough counts for the claim.
- Do not rely on one representative image for monodispersity or film coverage.
- For thesis figures, include distribution histograms; for journal figures, keep representative image plus concise distribution.

XPS/UPS:

- Calibrate binding energy and state charge correction.
- Assign Pb 4f, Cs 3d, Br/I/Cl core levels, ligand-related C/N/O/S/P signals, and dopant states cautiously.
- For valence/energy levels, report fitting/onset method and avoid overprecision.

## Device Data

J-V and EQE:

- Check active area, scan direction, scan rate, delay time, light intensity calibration, and hysteresis.
- Integrate EQE to cross-check Jsc. Explain discrepancies.
- Report champion and statistics; include box/violin plots when batches matter.

LED:

- Pair J-V-L with EQE/current density and EL spectra.
- Watch inflated EQE from area definition, outcoupling assumptions, pulsed operation, or unstable measurement.

X-ray:

- Use calibrated dose rate and background subtraction.
- For detection limit, state the signal-to-noise criterion and linear-fit range.
- Include response/recovery and repeatability if claiming detector reliability.

## Analysis Deliverables

For a data-analysis response, include:

- Processing steps and rationale.
- Tables of extracted metrics with units.
- Fit model and fit diagnostics.
- Reviewer-risk notes.
- Recommended figure panels for thesis and SCI manuscript.

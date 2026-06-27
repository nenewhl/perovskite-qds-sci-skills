# Materials ML PQD Example

This folder demonstrates how to use the `materials-ml-pqd` Skill and templates.

## Run the synthetic demo

From the repository root:

```bash
python templates/python/pqd_ml_pipeline.py \
  --data templates/data/pqd_ml_example.csv \
  --target PLQY \
  --group source_id \
  --exclude sample_id \
  --output outputs/pqd_ml_demo
```

## Replace with your own data

Prepare a CSV table where each row is a sample and each column is a descriptor or target value.

Recommended targets:

- `PLQY`
- `emission_peak_nm`
- `FWHM_nm`
- `lifetime_ns`
- `stability_retention_percent`
- `RL_intensity`
- `light_yield`
- `detection_limit`

For literature-curated datasets, keep `source_id` and use grouped validation to reduce paper-level leakage.

## Scientific caution

The bundled CSV is synthetic and intended only to test the code path. It must not be used as evidence for scientific conclusions.

---
name: pqd-skills
description: General research workflow for perovskite quantum-dot and nanocrystal studies. Use when Codex needs to analyze, clean, fit, visualize, interpret, organize, write, polish, or review academic work related to halide perovskite quantum dots, nanocrystals, optoelectronic materials, photophysics, light emission, photovoltaic devices, radiation-related optoelectronic applications, stability, synthesis, surface chemistry, and publication-ready scientific figures or manuscripts. Also trigger on Chinese requests such as 钙钛矿量子点, 量子点材料, 发光材料, 太阳能电池, 光电探测, 数据处理, SCI绘图, 学术写作, 文献综述.
---

# PQD Skills

Use this skill as a general router for perovskite quantum-dot and nanocrystal research workflows, including raw data processing, reproducible analysis, literature organization, scientific writing, publication-grade figure preparation, academic review, and revision planning.

Do not invent experimental results, statistics, journal policies, or citations. When information may have changed, especially journal scopes, author instructions, publication fees, reference styles, data-sharing policies, or figure-format requirements, verify against current official sources before final recommendations.

## Routing Protocol

1. Classify the request into one or more tracks:

   - `data`: raw spectra, curves, microscopy tables, device metrics, fitting, batch processing, reproducibility checks, or general research datasets.
   - `literature`: search strategies, reference selection, benchmark tables, novelty positioning, citation verification, or topic maps.
   - `manuscript`: titles, abstracts, introductions, results, discussions, conclusions, cover letters, Chinese-to-English drafting, or academic polishing.
   - `figures`: SCI-style figures, multi-panel plates, mechanism schematics, chart styling, and visual quality assurance.
   - `submission-review`: journal targeting, presubmission checks, reviewer simulation, response letters, and revision strategy.
   - `domain-standards`: perovskite/nanocrystal terminology, metric definitions, control experiments, device conventions, and reporting checklists.

2. Read `references/workflow.md` first for every task. It defines the intake, integrity rules, and output contract.

3.  Read `workflow.md` first for every task.

- `data-analysis.md`
- `literature.md`
- `manuscript.md`
- `figures.md`
- `submission-review.md`
- `domain-standards.md`

4. If the task spans multiple tracks, apply them in this order:

   data integrity → literature grounding → scientific argument → figure design → manuscript prose → submission/review strategy.

5. For plotting or file creation, use the user's real files when available. If no data are provided, build templates, analysis plans, or clearly labeled mock examples only when the user explicitly asks for examples.

## Default Standards

- Treat raw data as evidence, not decoration. Preserve raw files, record all cleaning and fitting decisions, and report exclusions.
- Separate comprehensive academic documentation from journal-style presentation. Long-form reports can be complete and process-oriented; top-journal figures should be selective, claim-driven, and defensible.
- Use field conventions: material composition first, surface/interface chemistry second, photophysical mechanism third, and device/application relevance last unless the work is device-led.
- Prefer publication-grade exports: vector PDF/SVG for plots and schematics; high-resolution TIFF/PNG only when required by a journal or when exporting raster imaging.
- Use restrained scientific styling: white background, Arial/Helvetica-like typography, thin axes, clear panel letters, colorblind-aware palettes, and no decorative gradients.
- Preserve chemical notation and dimensional correctness. Render chemical formulas, units, dose, fluence, irradiance, current density, luminance, external quantum efficiency, power conversion efficiency, and detector geometry consistently and explicitly.

## Output Contract

For substantial tasks, return:

1. `Detected task tracks`
2. `Assumptions or missing inputs`
3. `Actionable workflow or artifact`
4. `Quality-control checklist`
5. `Next files/data needed`, when relevant

For direct edits, drafts, figures, scripts, or review comments, produce the artifact and include a short verification summary.

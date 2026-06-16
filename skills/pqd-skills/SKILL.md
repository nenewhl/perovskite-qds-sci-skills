---
name: pqd-skills
description: Perovskite quantum-dot research workflow for PhD thesis data processing and top-tier SCI publication work. Use when Codex needs to analyze, clean, fit, visualize, interpret, search literature for, write, polish, submit, or review work on perovskite quantum dots/nanocrystals, including CsPbX3, FAPbX3, MAPbX3, lead-free/doped/alloyed PQDs, solar cells, LEDs/light emission, photophysics, X-ray scintillation/detection, stability, synthesis, surface chemistry, ligand exchange, and dissertation-ready or journal-ready figures/manuscripts. Also trigger on Chinese requests such as 钙钛矿量子点, 量子点太阳能电池, 发光, X射线探测, 博士论文数据处理, SCI绘图, 投稿, 审稿, 论文润色.
---

# PQD Skills

Use this skill as a router for the complete perovskite quantum-dot research cycle: raw data to thesis-quality analysis, literature grounding, manuscript writing/polishing, publication-grade figures, submission, peer review, and rebuttal.

Do not invent experimental results, statistics, journal policies, or citations. When information may have changed, especially journal scopes, author instructions, impact positioning, publication fees, reference styles, or data-sharing policies, verify against current official sources before final recommendations.

## Routing Protocol

1. Classify the request into one or more tracks:
   - `data` for raw spectra, curves, microscopy tables, device metrics, fitting, batch processing, thesis datasets, or reproducibility checks.
   - `literature` for search strategies, reference selection, benchmark tables, novelty positioning, citation verification, or topic maps.
   - `manuscript` for titles, abstracts, introductions, results, discussions, conclusions, cover letters, Chinese-to-English drafting, or polishing.
   - `figures` for SCI/top-journal figures, thesis figures, multi-panel plates, schematics, chart styling, and visual QA.
   - `submission-review` for journal targeting, presubmission checks, reviewer simulation, response letters, and revision strategy.
   - `domain-standards` for PQD-specific terminology, metrics, control experiments, device conventions, and reporting checklists.
2. Read `references/workflow.md` first for every task. It defines the intake, integrity rules, and output contract.
3. Read only the reference files required by the detected tracks:
   - `references/data-analysis.md`
   - `references/literature.md`
   - `references/manuscript.md`
   - `references/figures.md`
   - `references/submission-review.md`
   - `references/domain-standards.md`
4. If the task spans multiple tracks, apply them in this order: data integrity -> literature grounding -> scientific argument -> figure design -> manuscript prose -> submission/review strategy.
5. For plotting or file creation, use the user's real files when available. If no data are provided, build templates, analysis plans, or clearly labeled mock examples only when the user asks for examples.

## Default Standards

- Treat raw data as evidence, not decoration. Preserve raw files, record all cleaning and fitting decisions, and report exclusions.
- Separate thesis needs from journal needs. A thesis can be comprehensive; a top SCI figure must be selective, claim-driven, and defensible.
- Use PQD field conventions: phase/composition first, surface chemistry second, optoelectronic mechanism third, device relevance last unless the paper is device-led.
- Prefer publication-grade exports: vector PDF/SVG for plots and schematics; 600 dpi TIFF/PNG only when required by journal or raster imaging.
- Use restrained scientific styling: white background, Arial/Helvetica-like typography, thin axes, clear panel letters, colorblind-aware palettes, and no decorative gradients.

## Output Contract

For substantial tasks, return:

1. `Detected task tracks`
2. `Assumptions or missing inputs`
3. `Actionable workflow or artifact`
4. `Quality-control checklist`
5. `Next files/data needed`, when relevant

For direct edits, drafts, figures, or scripts, produce the artifact and include a short verification summary.

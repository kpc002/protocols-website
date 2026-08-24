---
title: "Mouse CD8 isolation and CD3 activation"
description: "Composite protocol for untouched mouse CD8 T-cell enrichment from spleen and lymph nodes, purity assessment, and antibody-mediated activation."
order: 10
author:
  - "Nicole Scharping"
  - "Kelsey Bennion"
  - "Maximilian Heeg"
date: last-modified
---

This composite combines three workflows for enriching untouched mouse CD8 T cells by biotin-antibody depletion and streptavidin magnetic separation, followed by CD3/CD28 activation. Source-specific differences are labeled throughout. Select one internally consistent set of volumes and activation conditions for an experiment.

## Source comparison

| Parameter | `Nicole_s protocols` | `Kelsey_s Protocols/Mouse` | `t_cells` |
|---|---|---|---|
| Plate coating | Anti-CD3, 5 µg/mL; 1 mL/well | Goat anti-hamster IgG, 1:30; 550 µL/well; also describes an anti-CD3-coated alternative | Goat anti-hamster IgG, 1:30; 550 µL/well |
| Coating time | Approximately 3 hours at 37°C | At least 2 hours at 37°C or overnight at 4°C | At least 2 hours at 37°C |
| Tissue homogenization | R10 through a filter | R10/RP5 through a 70 µm filter | PBS using frosted glass slides |
| ACK treatment | 1 mL for 3 minutes | 1 mL for 4 minutes | 1–2 mL for 5–6 minutes |
| Biotin-antibody stain volume | 3 mL per spleen plus lymph nodes | 500 µL; approximately 100 µL per 10^7 cells when scaling | 500 µL |
| Streptavidin beads | 100 µL in 500 µL MACS buffer | 50 µL in 500 µL MACS buffer | 50 µL in 500 µL MACS buffer |
| Column washes | Two × 3 mL | Three × 3 mL | Three × 3 mL |
| Activation density | Not explicitly stated | 1 × 10^6 cells/mL final | 1 × 10^6 cells/mL final |
| Activation antibodies | Plate-bound anti-CD3 plus soluble CD28 at 2 µg/mL | GAH plate: anti-CD3 and anti-CD28, each 1:1000 final; anti-CD3 plate: anti-CD28 at 1 µg/mL final | GAH plate: anti-CD3 and anti-CD28, each 1:1000 final |
| IL-2 | 50 U/mL | Not specified | Not specified |
| Activation time | 24 hours | 18–24 hours | Until further processing; duration not specified |

## Safety and sterility

- Follow institutional biological and chemical safety requirements.
- Use aseptic technique in a biological safety cabinet for all culture steps.
- Disinfect materials that contact cultures using an approved method.

These cautions are stated explicitly in `Nicole_s protocols` and should be applied to all variants.

## Materials

- Mouse spleen and lymph nodes
- Complete T-cell medium: R10 or TCM, according to the selected source workflow
- PBS
- ACK red-blood-cell lysis buffer
- MACS buffer
- Biotinylated lineage-depletion antibodies
- Streptavidin magnetic beads
- Appropriate MACS column and magnet
- Six-well tissue-culture plate
- Anti-CD3 antibody
- Anti-CD28 antibody
- Optional goat anti-hamster IgG coating antibody
- Optional recombinant IL-2
- Cell counter and viability reagent
- Optional flow-cytometry antibody for CD8 purity assessment

## 1. Prepare activation plates

Choose one coating strategy and prepare the plate before beginning the isolation.

### Direct anti-CD3 coating — `Nicole_s protocols`

1. Begin approximately 3 hours before plating cells.
2. Dilute anti-CD3 to 5 µg/mL in sterile PBS.
3. Add 1 mL per well of a six-well plate. The source uses three wells per spleen-plus-lymph-node isolation.
4. Tap the plate gently to cover the well surface.
5. Incubate at 37°C for approximately 3 hours.

### Goat anti-hamster IgG coating — `Kelsey_s Protocols/Mouse` and `t_cells`

1. Begin at least 2 hours before plating cells.
2. Dilute goat anti-hamster IgG 1:30 in sterile PBS.
3. Add 550 µL per well of a six-well plate.
4. Tap the plate gently to cover the well surface.
5. Incubate at 37°C for at least 2 hours.
6. `Kelsey_s Protocols/Mouse` also permits coating overnight at 4°C.

## 2. Harvest and homogenize tissues

1. Collect the spleen and desired lymph nodes into medium or buffer.
2. Mechanically dissociate the tissues to produce a single-cell suspension.
3. Centrifuge at 1,600 rpm for 4 minutes and remove the supernatant.

### Tissue-processing differences

- `Nicole_s protocols`: Homogenize spleen and lymph nodes in R10 using a filter in a dish. Rinse the apparatus with additional R10 and collect the wash.
- `Kelsey_s Protocols/Mouse`: Collect spleen plus inguinal, brachial, and axillary lymph nodes in R10; avoid mesenteric lymph nodes when possible. Pass cells through a 70 µm filter, place the filter over a 50 mL conical tube, and wash the dish twice with 1 mL RP5.
- `t_cells`: Homogenize tissues in PBS using frosted glass slides and transfer the suspension to a 15 mL tube.

## 3. Lyse red blood cells

Choose the timing used by the source workflow:

- `Nicole_s protocols`: Resuspend in 1 mL ACK, incubate for 3 minutes at room temperature, dilute with 3 mL R10, and centrifuge at 1,600 rpm for 4 minutes.
- `Kelsey_s Protocols/Mouse`: Resuspend in 1 mL ACK, incubate for 4 minutes, add 40 mL MACS buffer, and centrifuge at 1,600 rpm for 4 minutes.
- `t_cells`: Resuspend in 1–2 mL ACK, incubate for 5–6 minutes at room temperature, neutralize with 3–4 mL MACS buffer, and centrifuge at 1,600 rpm for 4 minutes.

Remove the supernatant completely before beginning negative-selection staining.

## 4. Prepare the biotinylated depletion cocktail

The depletion cocktails overlap but are not identical.

| Target | Cell population depleted | `Nicole_s protocols` | `Kelsey_s Protocols/Mouse` | `t_cells` |
|---|---|---:|---:|---:|
| NK1.1 | NK cells | 1:200 | 3 µL | 3 µL |
| MHC class II | Antigen-presenting cells | 1:200 | 3 µL | 3 µL |
| CD4 | CD4 T cells | 1:200 | 3 µL | 3 µL |
| B220 | B cells | 1:200 | 3 µL | 3 µL |
| CD19 | B cells | 1:200 | Not included | Not included |
| CD11b | Monocytes/myeloid cells | 1:200 | Not included | Not included |
| Ter119 | Erythroid cells | Not included | 3 µL | 3 µL |
| GR-1/Ly6G or Ly6C | Granulocytes/neutrophils | 1:200 | 3 µL | 3 µL |
| MACS buffer | Diluent | 3 mL total per spleen plus lymph nodes | 600 µL cocktail; use 500 µL to stain | 600 µL cocktail; use 500 µL to stain |

Use clone identities and depletion markers validated for the mouse strain and experimental goal. Do not assume that GR-1/Ly6G and Ly6C are interchangeable without confirming the antibody clone.

## 5. Stain cells for negative selection

1. Resuspend the cell pellet in the selected biotin-antibody cocktail.
2. Incubate for 15 minutes at 4°C, protected from light.
3. Wash with MACS buffer.
4. Centrifuge at 1,600 rpm for 4 minutes and remove the supernatant.

### Staining-volume differences

- `Nicole_s protocols`: Use 3 mL biotin-antibody stain per spleen-plus-lymph-node sample and wash with 10 mL MACS buffer.
- `Kelsey_s Protocols/Mouse`: Use 500 µL cocktail, scaling at approximately 100 µL per 10^7 cells when needed. Fill the tube with approximately 10–14 mL MACS buffer for the wash. The source also expresses the centrifugation condition as approximately 400 × g for 4 minutes.
- `t_cells`: Use 500 µL cocktail, fill the tube with MACS buffer for the wash, and centrifuge at 1,600 rpm for 4 minutes.

## 6. Label depleted populations with streptavidin beads

1. Resuspend the washed cells in 500 µL MACS buffer.
2. Add streptavidin magnetic beads:
   - 100 µL: `Nicole_s protocols`
   - 50 µL: `Kelsey_s Protocols/Mouse` and `t_cells`
3. Incubate for 15 minutes at 4°C, protected from light.
4. Wash with MACS buffer.
5. Centrifuge at 1,600 rpm for 4 minutes and remove the supernatant.
6. Resuspend cells for column loading:
   - 1 mL MACS buffer: `Nicole_s protocols`
   - 500 µL MACS buffer: `Kelsey_s Protocols/Mouse` and `t_cells`

## 7. Perform magnetic negative selection

1. Attach the appropriate MACS column to the magnet.
2. Equilibrate the column with 3 mL MACS buffer and discard this initial flow-through.
3. Apply the cell suspension to the column.
4. **Collect the unlabeled flow-through.** This fraction contains the enriched, untouched CD8 T cells.
5. Wash the column with 3 mL MACS buffer, combining each wash with the collected flow-through:
   - Two washes: `Nicole_s protocols`
   - Three washes: `Kelsey_s Protocols/Mouse` and `t_cells`
6. Do not allow the column to dry during separation (`Kelsey_s Protocols/Mouse`).
7. Centrifuge the collected flow-through at 1,600 rpm for 4 minutes and remove the supernatant.

## 8. Count cells and assess purity

1. Resuspend enriched cells in culture medium and count them.
2. Assess viability when required.
3. Check CD8 enrichment by flow cytometry when possible.

### Source-specific resuspension and purity checks

- `Nicole_s protocols`: Resuspend in 6 mL R10 and count with an automated cell counter.
- `Kelsey_s Protocols/Mouse`: Resuspend initially in approximately 500 µL R10, count, and assess viability with Trypan Blue or another method. Stain a pre- and post-isolation aliquot with FITC-CD8β at 1:100, wash once with FACS buffer, and acquire by flow cytometry. The source notes that 90–95% purity may be assumed only when a rapid workflow is necessary.
- `t_cells`: Resuspend in 500 µL TCM, count, and adjust to 2 × 10^6 cells/mL.

## 9. Plate and activate enriched CD8 T cells

Use the activation method that matches the plate-coating strategy from step 1.

### Direct anti-CD3-coated plate — `Nicole_s protocols`

1. Remove the anti-CD3/PBS coating solution and leave the wells free of residual liquid.
2. Supplement the enriched cells with anti-CD28 at 2 µg/mL and IL-2 at 50 U/mL; the source describes IL-2 as a 1:2,000 dilution.
3. Plate 2 mL cell suspension per well. The source distributes 6 mL across three wells.
4. Handle and resuspend the cells gently.
5. Incubate at 37°C for 24 hours.

### Goat anti-hamster IgG-coated plate — `Kelsey_s Protocols/Mouse`

1. Remove the coating solution.
2. Wash each well twice with 1 mL R10 and aspirate thoroughly.
3. Prepare anti-CD3 and anti-CD28, each at 1:500 in R10.
4. Add 1 mL cell suspension at 2 × 10^6 cells/mL to each well.
5. Add 1 mL anti-CD3/CD28 mixture to each well.
6. The resulting total volume is 2 mL, final density is 1 × 10^6 cells/mL, and each antibody is at a final 1:1,000 dilution.
7. Incubate at 37°C with 5% CO2 for 18–24 hours.

`Kelsey_s Protocols/Mouse` also describes an anti-CD3-coated plate alternative: add anti-CD28 at 1:250 in the 1 mL antibody solution so that the final well concentration is 1 µg/mL after mixing with 1 mL cells.

### Goat anti-hamster IgG-coated plate — `t_cells`

1. Wash each coated well twice with 1 mL TCM.
2. Plate 2 × 10^6 cells in 1 mL TCM per well.
3. Dilute anti-CD3 and anti-CD28, each at 1:500 in TCM.
4. Add 1 mL antibody mixture to each well and mix gently.
5. The resulting total volume is 2 mL, final density is 1 × 10^6 cells/mL, and each antibody is at a final 1:1,000 dilution.
6. Incubate at 37°C until the planned downstream processing time. The source does not specify an exact duration.

## 10. Record the selected conditions

Document the following for reproducibility:

- Mouse strain, tissue sources, and lymph-node groups
- Cell count before and after selection
- Depletion-antibody clones and amounts
- Streptavidin-bead volume and column type
- Number of column washes
- Post-isolation purity and viability
- Plate-coating method
- Anti-CD3 and anti-CD28 clones, stock concentrations, and final concentrations
- Cell density, culture volume, IL-2 condition, and activation duration

## Source protocols

| Protocol subfolder | Source protocol |
|---|---|
| `Nicole_s protocols` | [CD8 isolation and activation protocol](<../Nicole_s_protocols/CD8 isolation and activation protocol.md>) |
| `Kelsey_s Protocols/Mouse` | [CD8 isolation and activation](../t_cells/CD8%20activation%20protocol.md) |
| `t_cells` | [CD8 selection and activation](../t_cells/cd8_selection.md) |

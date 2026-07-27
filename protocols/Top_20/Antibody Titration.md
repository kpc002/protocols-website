---
title: "Antibody Titration"
description: "Composite flow-cytometry protocol for surface and intracellular antibody titration, with source-attributed workflows and compensation guidance."
order: 10
author:
  - "Giovanni Galleti"
  - "Kelsey Bennion"
date: last-modified
---

This composite combines a general tube-based antibody titration protocol from `Giovanni_s Protocols/FACS` with a 96-well plate workflow from `Kelsey_s Protocols/Mouse`. Differences are labeled throughout. Select one internally consistent set of conditions for each experiment rather than mixing source-specific volumes or buffers without validation.

## Source comparison

| Parameter | `Giovanni_s Protocols/FACS` | `Kelsey_s Protocols/Mouse` |
|---|---|---|
| Format | Eight flow-cytometry tubes | 96-well plate |
| Example cell input | Up to 10 × 10^6 cells per test | Approximately 2 × 10^6 cells per well |
| Viability dye | Live/Dead Blue | APC-Cy7 live/dead dye at 1:500 |
| Fc block and viability stain | 50 µL Fc block plus 50 µL dye mix | 50 µL Fc block plus 50 µL dye mix |
| Surface titration | Two-fold serial transfer across tubes | Antibodies diluted per well |
| Example intracellular series | General two-fold series | 1:50, 1:100, 1:200, 1:400, and 1:800 |
| Surface incubation | 20 minutes at 4°C | 20 minutes at 4°C |
| Intracellular incubation | 20 minutes unless kit conditions differ | 30 minutes at 4°C |
| Fixation options | BioLegend fix buffer or preferred fix/perm system | Foxp3 eBioscience or BD Cytofix/Cytoperm system |
| Brilliant dye buffer | 5 µL Super Bright Complete Staining Buffer per test | Not specified |
| Compensation | Detailed bead and viability-dye controls | Use established QC voltages; controls not detailed |

## Before starting

1. Review the antibody datasheet for recommended buffer, staining temperature, and incubation time. Some internalizing or recycling receptors may require staining at 37°C (`Giovanni_s Protocols/FACS`).
2. Mix antibodies thoroughly and briefly spin them down to reduce aggregates. An antibody master mix may instead be prepared and spun before staining (`Giovanni_s Protocols/FACS`).
3. Select cells containing a clearly identifiable positive and negative population.
4. Choose a dilution range broad enough to bracket the expected optimum.
5. Include an unstained sample and the required single-color compensation controls.
6. For tandem dyes, use the same antibody conjugate in the compensation control (`Giovanni_s Protocols/FACS`).

## Materials

- Cells containing positive and negative populations for the target antigen
- Antibody to be titrated
- Optional co-staining antibodies
- Calcium- and magnesium-free PBS
- FACS buffer: PBS with 2% FBS
- Fc block
- Compatible viability dye
- Fixation and permeabilization reagents appropriate for the target
- 96-well plate or flow-cytometry tubes
- Compensation beads appropriate for the antibody fluorophores and viability dye
- Optional Super Bright Complete Staining Buffer

### Additional materials — `Giovanni_s Protocols/FACS`

- Live/Dead Blue reconstituted with 50 µL DMSO
- ArC Amine Reactive Compensation Bead Kit
- UltraComp eBeads
- Super Bright Complete Staining Buffer, 5 µL per test

### Additional materials — `Kelsey_s Protocols/Mouse`

- Foxp3 eBioscience fixation/permeabilization kit for transcription factors or other intranuclear targets
- BD Cytofix/Cytoperm kit for cytokines or other cytoplasmic targets

## 1. Prepare cells

1. Count the cells and divide equal numbers among the titration conditions.
2. Wash once with PBS.
3. If cells are suspended in complete RPMI, wash thoroughly with PBS to remove FBS or BSA before using an amine-reactive viability dye (`Giovanni_s Protocols/FACS`).

### Cell-input options

- `Giovanni_s Protocols/FACS`: The viability-dye example is calculated for 10 × 10^6 cells per sample and uses eight tubes.
- `Kelsey_s Protocols/Mouse`: Combine suitable positive and negative cells when needed. The source example uses approximately 60 × 10^6 total cells and plates 2 × 10^6 cells per well.

## 2. Viability stain and Fc block

1. Prepare the selected viability dye according to its product instructions.
2. Resuspend each sample in 50 µL Fc block.
3. Add 50 µL viability-dye mix.
4. Incubate for 15 minutes at room temperature in the dark.
5. Wash and remove the supernatant.

### Viability-dye options

- `Giovanni_s Protocols/FACS`: Prepare Live/Dead Blue mix for four samples by combining 19.5 µL water with 0.5 µL dye, then adding 380 µL PBS. Wash afterward with 2 mL FACS buffer and centrifuge at 1,600 rpm for 4 minutes.
- `Kelsey_s Protocols/Mouse`: Use APC-Cy7 live/dead dye at 1:500. Wash once with 100 µL FACS buffer.

## 3. Design the dilution series

Prepare antibody solutions at 2× the desired final concentration when equal volumes of antibody solution and cell suspension will be combined.

### Example plate series — `Kelsey_s Protocols/Mouse`

| Well | Final antibody dilution |
|---|---:|
| 1 | 1:50 |
| 2 | 1:100 |
| 3 | 1:200 |
| 4 | 1:400 |
| 5 | 1:800 |
| Control | Unstained |

The source begins the serial dilution at 1:25 so that adding it to an equal volume of cell suspension produces a 1:50 final dilution.

### Eight-tube series — `Giovanni_s Protocols/FACS`

1. Resuspend cells in 50 µL FACS buffer per tube.
2. Add 50 µL FACS buffer to every tube except tube 1. Add 5 µL Super Bright Complete Staining Buffer per test when appropriate.
3. Prepare at least 115 µL of a 2× antibody mix in the same staining buffer.
4. Add 50 µL antibody mix to tubes 1 and 2.
5. Mix tube 2 and transfer 50 µL from tube 2 to tube 3.
6. Continue mixing and transferring 50 µL through tube 7.
7. Remove and discard 50 µL from tube 7. Tube 8 remains the unstained control.

## 4. Surface-antibody titration

1. Add the selected antibody dilution to each sample.
2. Add optional surface co-staining antibodies at their established titers.
3. Incubate for 20 minutes at 4°C in the dark unless the antibody datasheet requires another condition.
4. Wash and remove the supernatant.

### Tube workflow — `Giovanni_s Protocols/FACS`

1. Add 50 µL cell suspension to each tube containing the prepared dilution.
2. After staining, wash with 2 mL FACS buffer.
3. Centrifuge at 1,600 rpm for 4 minutes.
4. If the target antibody requires 20 minutes at 37°C, perform its titration under that condition before adding the remaining surface co-stain.

### Plate workflow — `Kelsey_s Protocols/Mouse`

1. Resuspend cells in 50 µL surface-staining solution per well.
2. The source uses established CD45.2-BV510 and CD45.2-BV786 co-stains at 1:100.
3. After staining, wash twice with 100 µL FACS buffer.

Proceed to acquisition if fixation is unnecessary. For intracellular targets, continue with the appropriate branch below.

## 5. Intracellular or intranuclear titration

Prepare intracellular antibody dilutions in the permeabilization buffer specified by the selected kit. Do not use Super Bright Complete Staining Buffer for intracellular antibodies (`Giovanni_s Protocols/FACS`).

### Foxp3/transcription-factor workflow — `Kelsey_s Protocols/Mouse`

1. Prepare fixation buffer by combining one part fixation/permeabilization concentrate with three parts diluent. The source example uses 1 mL concentrate plus 3 mL diluent.
2. Prepare 1× permeabilization buffer by combining one part 10× stock with nine parts water.
3. Resuspend cells in 100 µL fixation buffer.
4. Incubate for 20 minutes at 4°C in the dark.
5. During fixation, add 100 µL permeabilization buffer to the first serial-dilution well and 50 µL to each successive well.
6. Add the antibody to the first well at 1:25, mix, and transfer 50 µL sequentially to generate 2× solutions for final dilutions of 1:50 through 1:800.
7. Leave the final control well without antibody.
8. Wash cells once with 100 µL permeabilization buffer, not FACS buffer.
9. Resuspend cells in the corresponding intracellular-antibody dilution.
10. Incubate for 30 minutes at 4°C in the dark.
11. Wash once with permeabilization buffer and once with FACS buffer.

### Cytofix/Cytoperm workflow — `Kelsey_s Protocols/Mouse`

1. After the surface-staining wash, add 100 µL Cytofix per well.
2. Incubate for 20 minutes at 4°C in the dark.
3. Prepare 1× permeabilization buffer by combining one part 10× stock with nine parts water.
4. Generate the 2× two-fold antibody dilution series in Cytoperm permeabilization buffer as described above.
5. Wash cells once with 100 µL permeabilization buffer.
6. Resuspend cells in the corresponding intracellular-antibody dilution.
7. Incubate for 30 minutes at 4°C in the dark.
8. Wash once with permeabilization buffer and once with FACS buffer.

### General fixation option — `Giovanni_s Protocols/FACS`

1. Add 150 µL BioLegend fix buffer and incubate for 10 minutes, or use the preferred fixation/permeabilization conditions for the application.
2. Wash with 2 mL FACS buffer and centrifuge at 1,600 rpm for 4 minutes.
3. For an intracellular or intranuclear titration, repeat the serial-dilution approach using Perm/Wash buffer instead of FACS buffer.
4. Add any intracellular co-staining antibodies after fixation and permeabilization.

## 6. Compensation controls — `Giovanni_s Protocols/FACS`

1. Vortex compensation beads thoroughly.
2. For each antibody fluorophore, combine one drop UltraComp eBeads with antibody at the selected titer. Use at least 0.5 µL antibody when the selected volume is lower.
3. Prepare an unstained control with one drop UltraComp eBeads.
4. For Live/Dead Blue, prepare a positive control with two drops ArC Amine Reactive beads plus 2 µL dye.
5. Prepare the Live/Dead Blue negative control with two drops ArC Amine Negative beads and no dye.
6. Incubate controls for at least 20 minutes in the dark.
7. Wash antibody-stained beads with 2 mL FACS buffer and centrifuge at 1,600 rpm for 4 minutes. Do not wash the positive or negative Live/Dead Blue controls in this source workflow.
8. When matching fixed samples, fix antibody compensation beads with 150 µL of 1% formaldehyde or PFA in HBSS for 15 minutes in a chemical hood. Do not fix the Live/Dead Blue controls in this source workflow.
9. Wash fixed beads with 2 mL FACS buffer and centrifuge at 1,600 rpm for 5 minutes.
10. Resuspend controls in 200 µL FACS buffer and keep at 4°C until acquisition.

For spectral cytometry, include an unstained-cell control to model cellular autofluorescence. Single-stained cells are optional but recommended. Beads are preferred when they represent the fluorophore appropriately.

## 7. Acquire and select the titer

1. Resuspend samples in FACS buffer and keep them at 4°C until acquisition.
   - `Giovanni_s Protocols/FACS`: 200 µL per tube.
   - `Kelsey_s Protocols/Mouse`: Samples are ready after the final permeabilization-buffer and FACS-buffer washes.
2. Acquire every titration sample with identical instrument settings.
3. Use established QC voltages when applicable (`Kelsey_s Protocols/Mouse`).
4. Gate the same positive and negative populations in every sample.
5. Compare signal separation, background, percentage positive, and staining pattern across the series.
6. Select the lowest antibody concentration that provides maximal or near-maximal separation without unacceptable background or nonspecific staining.
7. Record the antibody clone, fluorophore, lot, cell type, staining buffer, time, temperature, and selected dilution.

## Source protocols

| Protocol subfolder | Source protocol |
|---|---|
| `Giovanni_s Protocols/FACS` | [FC1.antibody_titration](<../Giovanni_s_Protocols/FACS/FC1.antibody_titration.md>) |
| `Kelsey_s Protocols/Mouse` | [Antibody titration](<../Kelsey_s_Protocols/Mouse/Antibody titration.md>) |

---
title: "Ex vivo peptide stim"
description: "Composite protocol for ex vivo gp33 peptide restimulation of lymphocytes before intracellular cytokine staining, with source-attributed experimental options."
order: 10
author:
  - "Giovanni Galleti"
  - "Nicole Scharping"
  - "Maximilian Heeg"
  - "Kelsey Bennion"
date: last-modified
---

This composite protocol combines four workflows for ex vivo gp33 peptide restimulation followed by flow-cytometric analysis of cytokine production. Where the sources differ, the relevant protocol subfolder is named explicitly. Choose one validated set of conditions and apply it consistently across the experiment.

## Source-specific conditions

The peptide concentrations below are reported as written in the source protocols. They are not assumed to be equivalent.

| Parameter | `Giovanni_s Protocols/cellular` | `Nicole_s protocols` | `t_cells` | `Kelsey_s Protocols/Mouse` |
|---|---|---|---|---|
| Peptide | gp33, KAVYNFATC | GP33 aliquot | gp33 | gp33–41 |
| Final peptide condition | 1 µM | 1:500 source-stock dilution | 10 nM from 1 mM stock | 0.4 µg/mL |
| Culture volume | 200 µL/well | 200 µL/well | 200 µL/well | 200 µL/well |
| Transport inhibitor | Protein Transport Inhibitor Cocktail, 1:500 | Protein Transport Inhibitor, 1:500 | Protein Transport Inhibitor Cocktail, 1:500 | GolgiPlug, 1:500 |
| Incubation | 4 hours at 37°C | 4 hours at 37°C | 4 hours at 37°C | 4–6 hours at 37°C |
| APC support | 30 µL naïve splenocytes per well | APCs must be present | 50 µL congenically distinct splenocytes for TRM | Native spleen/APC-containing sample |
| Negative control | No cognate peptide/plain medium | Not specified in stimulation section | Not specified | No peptide plus GolgiPlug |
| Positive control | Cell Stimulation Cocktail, 1:500 | Not specified | Not specified | Not specified |

## Materials

- Freshly isolated lymphocytes or tissue-derived cell suspension
- Complete T-cell medium
- gp33 peptide or the experiment-specific cognate peptide
- Protein transport inhibitor compatible with the cytokines being measured
- Optional naïve splenocytes to provide antigen-presenting cells
- 96-well U-bottom or round-bottom plate for stimulation
- 96-well V-bottom or round-bottom plate for staining
- PBS and FACS buffer
- Fc-receptor blocking reagent
- Surface-staining antibody panel
- Intracellular cytokine antibodies
- Appropriate fixation and permeabilization reagents
- Single-color compensation controls

## 1. Prepare cells

1. Harvest the required tissues and prepare single-cell suspensions.
2. Count cells when the experimental design requires normalization.
3. Plate cells in a 96-well U-bottom or round-bottom plate.
4. Ensure that antigen-presenting cells are present. Purified T cells alone cannot efficiently use peptide presented through this workflow (`Nicole_s protocols`).

### Source-attributed plating options

- `Giovanni_s Protocols/cellular`: Count freshly isolated tumor-infiltrating lymphocytes and splenocytes. If cells are not counted, plate approximately one-third to one-quarter of the TIL or draining-lymph-node preparation, or 10 µL of spleen suspension prepared in 1 mL.
- `Giovanni_s Protocols/cellular`: To support TIL stimulation, resuspend a naïve spleen in 5 mL medium and add 30 µL per well. Use naïve splenocytes with the same congenic marker as the recipient mice.
- `t_cells`: Resuspend T cells in 100 µL T-cell medium. For TRM samples, add 50 µL congenically distinct splenocytes as an APC spike-in; for splenocyte-only samples, add 50 µL medium instead.
- `Kelsey_s Protocols/Mouse`: For spleen samples, plate 5% of the spleen preparation—250 µL from a spleen resuspended in 5 mL. Use a consistent volume across samples and retain cell counts for normalization.
- `Nicole_s protocols`: Plate cells in a 96-well round-bottom plate and centrifuge at 2,000 rpm for 1 minute before adding stimulation medium.
- `Kelsey_s Protocols/Mouse`: Centrifuge the plated samples at 1,500 rpm for 3 minutes before replacing the medium.

## 2. Prepare controls

1. Include a stimulated condition containing cognate peptide and protein transport inhibitor.
2. Include an unstimulated negative control containing protein transport inhibitor but no peptide.
3. Keep the cell input and total culture volume consistent between stimulated and unstimulated conditions.
4. Add a positive stimulation control when needed.

### Source-attributed control options

- `Giovanni_s Protocols/cellular`: Use cells treated identically without cognate peptide as the cytokine-negative control. Plain medium is also described as a negative control. Use Cell Stimulation Cocktail at 1:500 as a positive control.
- `Kelsey_s Protocols/Mouse`: Prepare either an unstimulated sample for every mouse or one pooled unstimulated control per tissue. The unstimulated medium contains GolgiPlug but no gp33.

## 3. Prepare stimulation medium

Prepare enough medium for all wells plus pipetting excess. The final culture volume is 200 µL per well in all four source protocols.

Choose one of the following source-specific formulations:

### Option A — `Giovanni_s Protocols/cellular`

- Standard T-cell medium
- gp33 peptide at 1 µM final concentration
- Protein Transport Inhibitor Cocktail at 1:500 final dilution

### Option B — `Nicole_s protocols`

- T-cell medium
- GP33 source aliquot at 1:500
- Protein Transport Inhibitor containing brefeldin A and monensin at 1:500

The GP33 stock concentration is not stated in this source; do not interpret 1:500 as a molar concentration without checking the aliquot record.

### Option C — `t_cells`

For each well:

1. Begin with 100 µL cells in T-cell medium.
2. Add either 50 µL APC splenocytes for TRM samples or 50 µL additional medium for splenocyte samples.
3. Add 50 µL stimulation mix.

An example stimulation mix contains:

- 500 µL T-cell medium
- 4 µL Protein Transport Inhibitor Cocktail, producing a final 1:500 dilution after addition to the well
- 2 µL gp33 that has first been diluted 1:100, producing a final gp33 dilution of 1:100,000 from a 1 mM stock, or 10 nM

### Option D — `Kelsey_s Protocols/Mouse`

1. Calculate the required medium as 200 µL multiplied by the number of samples, including unstimulated controls.
2. Add 500× GolgiPlug at 1:500.
3. Divide the medium into stimulated and unstimulated portions.
4. Prepare a 1:10 intermediate dilution of the 4 mg/mL gp33 stock to obtain 0.4 mg/mL.
5. Add 1 µL of the 0.4 mg/mL intermediate dilution per 1 mL stimulated medium to obtain 0.4 µg/mL final peptide.
6. Do not add peptide to the unstimulated portion.

## 4. Stimulate cells

1. Remove the existing medium after the applicable centrifugation step.
2. Add 200 µL of the selected stimulation medium to each stimulated well.
3. Add 200 µL matched inhibitor-containing medium without peptide to each negative-control well.
4. Resuspend cells thoroughly.
5. Incubate at 37°C:
   - 4 hours: `Giovanni_s Protocols/cellular`, `Nicole_s protocols`, and `t_cells`
   - 4–6 hours: `Kelsey_s Protocols/Mouse`

### CD107a timing — `t_cells`

When measuring CD107a, add the CD107a antibody and gp33 peptide at the beginning of stimulation. Incubate for 30–60 minutes before adding Protein Transport Inhibitor Cocktail for the remainder of the stimulation period.

## 5. Wash and surface stain

1. Transfer cells to a V-bottom plate if needed (`Giovanni_s Protocols/cellular`).
2. Wash cells twice before staining (`Giovanni_s Protocols/cellular`).
3. Block Fc receptors.
4. Stain viability and surface markers using the validated panel.
5. Wash the cells before fixation and permeabilization.

### Detailed surface-staining option — `Nicole_s protocols`

1. Add 20–50 µL Fc block to cells in medium and incubate on ice for at least 10 minutes.
2. Prepare the surface-antibody cocktail in FACS buffer at 100 µL per well.
3. Centrifuge at 2,000 rpm for 1 minute and remove supernatant.
4. Add 100 µL staining cocktail and resuspend.
5. Incubate on ice in the dark for 15 minutes.
6. Add 180 µL FACS buffer and centrifuge to wash.

## 6. Fix, permeabilize, and stain cytokines

Use a fixation/permeabilization system validated for cytoplasmic cytokines.

### Detailed intracellular-staining option — `Nicole_s protocols`

1. After surface staining, centrifuge cells at 2,000 rpm for 1 minute.
2. Resuspend in 100 µL 4% PFA in PBS and incubate for 20 minutes at room temperature in the dark. This preliminary fixation is used in this source to help preserve selected surface antigens and fluorescent reporters.
3. Add 180 µL FACS buffer, centrifuge, and remove supernatant.
4. Resuspend in 100 µL BD Cytofix/Cytoperm.
5. Incubate for 20 minutes at room temperature.
6. Add 180 µL 1× BD Perm/Wash buffer, centrifuge, and remove supernatant.
7. Prepare intracellular cytokine antibodies in 1× Perm/Wash buffer at 100 µL per well.
8. Resuspend cells in 100 µL intracellular staining solution.
9. Incubate for 30 minutes at room temperature in the dark.
10. Wash with 180 µL Perm/Wash buffer and centrifuge.
11. Resuspend in 100 µL FACS buffer for acquisition.

`Giovanni_s Protocols/cellular` specifies surface staining followed by intracellular staining for effector molecules and cytokines but does not prescribe a particular fixation/permeabilization kit in the source protocol.

## 7. Acquire and analyze

1. Prepare single-color compensation controls for every fluorophore.
2. Acquire stimulated and unstimulated samples using identical cytometer settings.
3. Gate matched populations consistently across all conditions.
4. Use the no-peptide control to establish cytokine-positive gates.
5. Report both the frequency of cytokine-positive cells and fluorescence intensity when appropriate.

`Nicole_s protocols` notes that stimulated cytokine responses and inhibitor choice should be optimized empirically for each cytokine. TNFα, IL-2, IL-17, and IFNγ commonly produce clearer positive populations, whereas IL-4, IL-5, IL-10, and IL-13 may appear primarily as fluorescence-intensity shifts.

## Source protocols

| Protocol subfolder | Source protocol |
|---|---|
| `Giovanni_s Protocols/cellular` | [CB8.Ex vivo restim](<../Giovanni_s_Protocols/cellular/CB8.Ex vivo restim.md>) |
| `Nicole_s protocols` | [012725 NES - Flow cytometry staining](<../Nicole_s_protocols/012725 NES - Flow cytometry staining.md>) |
| `t_cells` | [Ex vivo stimulation](../t_cells/Ex_vivo_Stimulation/ex_vivo_stimulation.md) |
| `Kelsey_s Protocols/Mouse` | [ICS_GP33 peptide restim](../t_cells/Ex_vivo_Stimulation/ICS_GP33%20peptide%20restim.md) |

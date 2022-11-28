---
order: 5
title: "RNA Isolation from tissues"
author: Maximilian Heeg
date: last-modified
description: 
  Isolate RNA from tissues for qPCR
image: rna.svg
---

# RNA Isolation from Tissues

## Tissue collection

-   Label eppies, chill in dry ice
-   Harvest tissues and put directly on dry ice (intestines: push feces out first)
-   Freeze \@ -80°C until ready to use

## Homogenize: (done in TC hood)

-   Chill Trizol on ice
-   Clean 1ml glass dounce with PBS, bleach, EtOH, PBS, Trizol after each sample
-   Homogenize samples from least to highest LCMV, keep order across time points
-   Freeze \@ -80°C until ready to use

## RNA extraction: (done in fume hood)

-   Thaw Trizol sample at RT
-   Add 200μl chloroform
-   Vortex vigorously for approx 15s
-   Incubate 2-3 min at RT
-   Centrifuge 15 min at 12000g, 4°C
-   Carefully transfer aqueous phase to a fresh tube \~500ul (work on ice from this point)
-   Add 500μl isopropanol (flick, do not pipette)
-   Centrifuge 20 min at 12,000g, 4°C, remove supernatant with pipette tip
-   Wash with 1ml cold 75% EtOH (make fresh using DNAse/RNAse-free water), vortex to loose pellet
-   Centrifuge 15 min at 7,400g, 4°C
-   Pipette of as much EtOH as possible. Use 10ul micropipettor for small volume
-   Dry 10-15 min
-   Resuspend RNA pellet in 50μl (or more) nuclease-free water until no more pellet visible

## Remove DNA contamination

-   add 5μl TruboDNAse 10x Buffer and 1μl TurboDNAse, mix gently
-   Incubate at 37°C for 20-30 min
-   Add resuspended Inactivation Reagent (5µl to 50 µl mix), and mix well
-   Incubate 5 min at RT, mixing occasionally
-   Centrifuge at 10000 x g for 1.5 min and transfer the RNA to a fresh tube
-   Nanodrop (260/280 \~2, 260/230 \>2)
-   Freeze \@ -80°C until ready to use

## cDNA synthesis

-   Dilute RNA into 96-well plate to the same concentration across all samples (5μg)

-   Follow [SuperScript IV protocol](/protocols/mol_bio/cDNA.html#cdna-preparation-using-superscript-iv) including RNA H

    ::: callout-tip
    Instead of incubate the combined reaction mixture at 50--55°C for 10 minutes, incubate it for 60min
    :::

-   Freeze \@ -20°C until ready to use

## qPCR

-   HPRT SYBR and LCMV GP primers, stock 100μM
-   Dilute primers:
    -   2.5μl F, 2.5μl R, 195 μl water
-   qPCR rxn:
    -   Primers: 1μl
    -   SYBR 2x: 5μl
    -   cDNA: 4μl

## Analysis

-   Get Ct values for all samples, both genes
-   Calculate dCt = HPRT-LCMV
-   Expression = 2^dCT^

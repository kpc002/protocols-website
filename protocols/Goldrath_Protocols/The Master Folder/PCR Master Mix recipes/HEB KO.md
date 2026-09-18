---
title: "HEB KO"
description: "PCR master mix recipe converted from the HEB KO sheet."
author: "Goldrath Lab"
date: last-modified
---

# HEB KO

This page reproduces the **PCR master mix recipes** workbook sheet. Formula cells are shown as entered in the workbook.

[Download the original workbook](../PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

| Row | A | B | C | D | E | F | G | H | I | J | K | L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Heb KO |  |  |  |  |  |  | Folder | PCR name | PCR cycle | Primer Squence | Band Size |
| 2 |  | x1 | 20 |  |  |  |  | Louise | HEB+/- | 1. Incubate at 94°C for 3:00 | HEB wt- TCT GAC TTG CTG TTC TAG ACT | WT- 200bp |
| 3 | 5x buffer | 5 | =B3*C2 |  |  |  |  |  |  | 2. Incubate at 94°C for 0:30 | HEB ko- TGG ATT CAT CGA CTG TGG | KO- 800bp |
| 4 | MgCl2 | 3 | =B4*C2 |  |  |  |  |  |  | 3. Incubate at 55°C for 0:30 | HEB com- GAA GGA GAG GCG GAT GGC TAA |  |
| 5 | DNTP | 0.5 | =B5*C2 |  |  |  |  |  |  | 4. Incubate at 72°C for 1:00 |  |  |
| 6 | P1 | 0.5 | =B6*C2 |  |  |  |  |  |  | 5. Cycle to step 2, 34 times |  |  |
| 7 | P2 | 0.5 | =B7*C2 |  |  |  |  |  |  | 6. Incubate at 72°C for 5:00 |  |  |
| 8 | P3 | 0.5 | =B8*C2 |  |  |  |  |  |  |  |  |  |
| 9 | Taq | 0.5 | =B9*C2 |  |  |  |  |  |  |  |  |  |
| 10 | H20 | 13.5 | =B10*C2 |  |  |  |  |  |  |  |  |  |
| 11 | DNA | 1 | =B11*C2 |  |  |  |  |  |  |  |  |  |
| 12 | Total | =SUM(B3:B11) | =B12*C2 |  |  |  |  |  |  |  |  |  |

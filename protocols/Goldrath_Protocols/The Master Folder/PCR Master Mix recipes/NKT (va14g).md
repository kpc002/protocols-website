---
title: "NKT (va14g)"
description: "PCR master mix recipe converted from the NKT (va14g) sheet."
author: "Goldrath Lab"
date: last-modified
---

# NKT (va14g)

This page reproduces the **PCR master mix recipes** workbook sheet. Formula cells are shown as entered in the workbook.

[Download the original workbook](../PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

| Row | A | B | C | D | E | F | G | H | I | J | K | L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | NKT |  |  |  |  |  |  | Folder | PCR name | PCR cycle | Primer Squence | Band Size |
| 2 |  | x1 | 20 |  |  |  |  | Louise | NKT | 1. Incubate at 94°C for 5:00 | Va14 geno F (iNKT)- CTAAGCACAGCACGCTGCACA | 135bp |
| 3 | 5x buffer | 5 | =B3*C2 |  |  |  |  |  |  | 2. Incubate at 94°C for 0:30 | Va14 geno R (iNKT)- CAGGTATGACAATCAGCTGAGTCC |  |
| 4 | MgCl2 | 3 | =B4*C2 |  |  |  |  |  |  | 3. Incubate at 56°C for 0:30 |  |  |
| 5 | DNTP | 0.5 | =B5*C2 |  |  |  |  |  |  | 4. Incubate at 72°C for 0:30 |  |  |
| 6 | P1 | 0.5 | =B6*C2 |  |  |  |  |  |  | 5. Cycle to step 2, 34 times |  |  |
| 7 | P2 | 0.5 | =B7*C2 |  |  |  |  |  |  | 6. Incubate at 72°C for 10:00 |  |  |
| 8 | Taq | 0.5 | =B8*C2 |  |  |  |  |  |  |  |  |  |
| 9 | H20 | 13.5 | =B9*C2 |  |  |  |  |  |  |  |  |  |
| 10 | DNA | 1 | =B10*C2 |  |  |  |  |  |  |  |  |  |
| 11 | Total | =SUM(B3:B10) | =B11*C2 |  |  |  |  |  |  |  |  |  |

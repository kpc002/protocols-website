---
title: "OT-I"
description: "PCR master mix recipe converted from the OT-I sheet."
author: "Goldrath Lab"
date: last-modified
---

# OT-I

This page reproduces the **PCR master mix recipes** workbook sheet. Formula cells are shown as entered in the workbook.

[Download the original workbook](../PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

| Row | A | B | C | D | E | F | G | H | I | J | K | L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OT-1 |  |  |  |  |  |  | Folder | PCR name | PCR cycle | Primer Squence | Band Size |
| 2 |  | x1 | 20 |  |  |  |  | Kyla | OT-1 | 1. Incubate at 95°C for 3:00 | Vb5 F- AAGGTGGAGAGAGACAAAGGA |  |
| 3 | 5x buffer | 5 | =B3*C2 |  |  |  |  |  |  | 2. Incubate at 94°C for 1:00 | Vb5 R- CCAGTGCATGCATACCTCAG |  |
| 4 | MgCl2 | 2.5 | =B4*C2 |  |  |  |  |  |  | 3. Incubate at 55°C for 1:00 |  |  |
| 5 | DNTP | 0.5 | =B5*C2 |  |  |  |  |  |  | 4. Incubate at 72°C for 1:00 |  |  |
| 6 | P1 | 1.25 | =B6*C2 |  |  |  |  |  |  | 5. Cycle to step 2, 34 times |  |  |
| 7 | P2 | 1.25 | =B7*C2 |  |  |  |  |  |  | 6. Incubate at 72°C for 3:00 |  |  |
| 8 | Taq | 0.25 | =B8*C2 |  |  |  |  |  |  |  |  |  |
| 9 | H20 | 13.25 | =B9*C2 |  |  |  |  |  |  |  |  |  |
| 10 | DNA | 1 | =B10*C2 |  |  |  |  |  |  |  |  |  |
| 11 | Total | =SUM(B3:B10) | =SUM(C3:C10) |  |  |  |  |  |  |  |  |  |

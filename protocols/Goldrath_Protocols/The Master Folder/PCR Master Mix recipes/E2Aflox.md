---
title: "E2Aflox"
description: "PCR master mix recipe converted from the E2Aflox sheet."
author: "Goldrath Lab"
date: last-modified
---

# E2Aflox

This page reproduces the **PCR master mix recipes** workbook sheet. Formula cells are shown as entered in the workbook.

[Download the original workbook](../PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

| Row | A | B | C | D | E | F | G | H | I | J | K |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | E2A flox |  |  |  |  |  | Folder | PCR name | PCR cycle | Primer Squence | Band Size |
| 2 |  | x1 | 20 |  |  |  | Louise | E2Aflox | 1. Incubate at 94°C for 3:00 | E2Aflox F1- GCCACCAGCACATCGTGCCTA | WT band- 850bp |
| 3 | 10x buffer | 2.5 | =B3*C2 |  |  |  |  |  | 2. Incubate at 94°C for 0:30 | E2Aflox R3- CCACATAAGAGGGCATGGAAG | flox band- 1kb |
| 4 | B-ine | 2.5 | =B4*C2 |  |  |  |  |  | 3. Incubate at 65°C for 0:30 | YZ150- ACATGGCTGAATATCGACGGT |  |
| 5 | MgCl2 | 3 | =B5*C2 |  |  |  |  |  | 4. Incubate at 72°C for 1:00 |  |  |
| 6 | DNTP | 0.5 | =B6*C2 |  |  |  |  |  | 5. Cycle to step 2, 39 times |  |  |
| 7 | P1 | 1.5 | =B7*C2 |  |  |  |  |  | 6. Incubate at 72°C for 5:00 |  |  |
| 8 | P2 | 1.5 | =B8*C2 |  |  |  |  |  |  |  |  |
| 9 | P3 | 1.5 | =B9*C2 |  |  |  |  |  |  |  |  |
| 10 | Taq | 0.5 | =B10*C2 |  |  |  |  |  |  |  |  |
| 11 | H20 | 10.5 | =B11*C2 |  |  |  |  |  |  |  |  |
| 12 | DNA | 1 | =B12*C2 |  |  |  |  |  |  |  |  |
| 13 | Total | =SUM(B3:B12) | =B13*C2 |  |  |  |  |  |  |  |  |

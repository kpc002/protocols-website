---
title: "HEBflox"
description: "PCR master mix recipe converted from the HEBflox sheet."
author: "Goldrath Lab"
date: last-modified
---

# HEBflox

This page reproduces the **PCR master mix recipes** workbook sheet. Formula cells are shown as entered in the workbook.

[Download the original workbook](../PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

| Row | A | B | C | D | E | F | G | H | I | J | K | L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Heb flox |  |  |  |  |  |  | Folder | PCR name | PCR cycle | Primer Squence | Band Size |
| 2 |  | x1 | 20 |  |  |  |  | Louise | HEBflox | 1. Incubate at 94°C for 3:00 | HEBflox F- CTG GGA CAG AAG TTC AGC ACT TAG TAC | Deleted-0.5kb |
| 3 | 10x buffer | 2.5 | =B3*C2 |  |  |  |  |  |  | 2. Incubate at 94°C for 0:30 | HEBflox R- CAT TCC TAT ACA TCA GCT TCT TGG ACG | Flox- 1.3kb |
| 4 | MgCl2 | 3 | =B4*C2 |  |  |  |  |  |  | 3. Incubate at 59.5°C for 0:30 |  | WT- 1.1kb |
| 5 | DNTP | 0.5 | =B5*C2 |  |  |  |  |  |  | 4. Incubate at 72°C for 1:30 |  |  |
| 6 | P1 | 1.5 | =B6*C2 |  |  |  |  |  |  | 5. Cycle to step 2, 37 times |  |  |
| 7 | P2 | 1.5 | =B7*C2 |  |  |  |  |  |  | 6. Incubate at 72°C for 10:00 |  |  |
| 8 | Taq | 0.5 | =B8*C2 |  |  |  |  |  |  |  |  |  |
| 9 | H20 | 14.5 | =B9*C2 |  |  |  |  |  |  |  |  |  |
| 10 | DNA | 1 | =B10*C2 |  |  |  |  |  |  |  |  |  |
| 11 | Total | =SUM(B3:B10) | =B11*C2 |  |  |  |  |  |  |  |  |  |

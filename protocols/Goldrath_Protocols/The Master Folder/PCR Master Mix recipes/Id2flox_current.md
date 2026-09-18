---
title: "Id2flox_current"
description: "PCR master mix recipe converted from the Id2flox_current sheet."
author: "Goldrath Lab"
date: last-modified
---

# Id2flox_current

This page reproduces the **PCR master mix recipes** workbook sheet. Formula cells are shown as entered in the workbook.

[Download the original workbook](../PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

| Row | A | B | C | D | E | F | G | H | I | J |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Id2 f/f  |  |  |  |  | Folder | PCR name | PCR cycle | Primer Squence | Band Size |
| 2 |  | x1 | 35 |  |  | Kyla | ID2flox_op | 1. Incubate at 94°C for 3:00 |  |  |
| 3 | 5x buffer | 5 | =B3*C2 |  |  |  |  | 2. Incubate at 94°C for 0:40 |  |  |
| 4 | MgCl2 | 2 | =B4*C2 |  |  |  |  | 3. Incubate at 60°C for 0:40 |  |  |
| 5 | DNTP | 0.5 | =B5*C2 |  |  |  |  | 4. Incubate at 72°C for 0:50 |  |  |
| 6 | P1 | 0.5 | =B6*C2 |  |  |  |  | 5. Cycle to step 2, 37 times |  |  |
| 7 | P2 | 0.5 | =B7*C2 |  |  |  |  | 6. Incubate at 72°C for 5:00 |  |  |
| 8 | Taq | 0.2 | =B8*C2 |  |  |  |  |  |  |  |
| 9 | H20 | 15.3 | =B9*C2 |  |  |  |  |  |  |  |
| 10 | DNA | 1 | =B10*C2 |  |  |  |  |  |  |  |
| 11 | Total | =SUM(B3:B10) | =SUM(C3:C10) |  |  |  |  |  |  |  |

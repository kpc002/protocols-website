---
title: "Cre Reporter"
description: "PCR master mix recipe converted from the Cre Reporter sheet."
author: "Goldrath Lab"
date: last-modified
---

# Cre Reporter

This page reproduces the **PCR master mix recipes** workbook sheet. Formula cells are shown as entered in the workbook.

[Download the original workbook](../PCR%20master%20mix%20recipes.xlsx){.btn .btn-primary download="PCR master mix recipes.xlsx"}

| Row | A | B | C | D | E | F | G | H | I | J | K | L |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | cre reporter |  |  |  |  |  |  | Folder | PCR name | PCR cycle | Primer Squence | Band Size |
| 2 |  | x1 | 20 |  |  |  |  | Kyla | Cre rep | 1. Incubate at 94°C for 3:00 | oIMR9020- AAG GGA GCT GCA GTG GAG TA | Wild type- 297bp |
| 3 | 10x buffer | 2.5 | =B3*C2 |  |  |  |  |  |  | 2. Incubate at 94°C for 0:20 | oIMR9021- CCG AAA ATC TGT GGG AAG TC | Mutant- 199bp |
| 4 | B-ine | 3.45 | =B4*C2 |  |  |  |  |  |  | 3. Incubate at 62°C for 0:30 | oIMR9103- GGC ATT AAA GCA GCG TAT CC | Het- 297 and 199bp |
| 5 | DNTP | 0.5 | =B5*C2 |  |  |  |  |  |  | 4. Incubate at 72°C for 0:30 | oIMR9104- AAC CAG AAG TGG CAC CTG AC |  |
| 6 | P1 | 1.25 | =B6*C2 |  |  |  |  |  |  | 5. Cycle to step 2, 35 times |  |  |
| 7 | P2 | 1.25 | =B7*C2 |  |  |  |  |  |  | 6. Incubate at 72°C for 2:00 |  |  |
| 8 | P3 | 1.25 | =B8*C2 |  |  |  |  |  |  | 7.Incubate at 10°C forever |  |  |
| 9 | P4 | 1.25 | =B9*C2 |  |  |  |  |  |  |  |  |  |
| 10 | Taq | 0.5 | =B10*C2 |  |  |  |  |  |  |  |  |  |
| 11 | H20 | 11.05 | =B11*C2 |  |  |  |  |  |  |  |  |  |
| 12 | DNA | 2 | =B12*C2 |  |  |  |  |  |  |  |  |  |
| 13 | Total | =SUM(B3:B12) | =B13*C2 |  |  |  |  |  |  |  |  |  |

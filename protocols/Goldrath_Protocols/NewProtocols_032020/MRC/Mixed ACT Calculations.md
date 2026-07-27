---
title: "Mixed ACT Calculations"
description: 'Goldrath Lab protocol.'
order: 10
author: "Goldrath Lab"
date: last-modified
---

# Mixed ACT Calculations

## Sheet1

|CD8 T cell 1:1 mixing calculations|||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|||Equation|x + y = 2000000||||||||||||||
||||FractionAme+CD45.1*x = FractionAme+CD45.1.2y||||||||||||||
|Wash 2x with PBS|||||||||||||||||
|Resuspend in X volume - Usually 1ml of PBS 1X|||||||||||||||||
||||||||ATTEMPT 1|||||ATTEMPT 2|||||
|CD45.1 CELLS|shCD19||Cells to STAIN|100000|||MINI-MIX|||||MINI-MIX|(ul)||||
|Total Volume|1.6||Volume to Stain (ul) (FACSbuffer)|100||x|Total Cells from CD45.1|=500000-I9||||Total Cells from CD45.1|=I8/K18||||
|Dilution to count||(1/100)||||y|Total Cells from CD45.1.2|=(500000*B16)/B37||||Total Cells from CD45.1.2|=I9/K19||||
|Actual Count (cells/ml)|||Volume to Take for FIRST stain (ul)|=(E7/B11)*1000|||Total Cells|=SUM(I8+I9)||||Total Cells|=SUM(N8+N9)||||
|Corrected Count (cells/ml)|3400000||||||||||||||||
|Total Cells|=B11*B8||||||Volume from CD45.1 (ul)|=(I8/B11)*1000||||Volume from CD45.1 (ul)|=(N8/B11)*1000||||
||||||||Volume from CD45.1.2 (ul)|=(I9/B25)*1000||||Volume from CD45.1.2 (ul)|=(N9/B25)*1000||||
||||||||Volume total (ul)|=SUM(I12:I13)||||Volume total|=SUM(N12:N13)||||
|Proportion of Ametrine + Cells in CD45.1/CD8a/Va2+ gate|0.543||||||||||||||||
|Concentration of Ametrine+ cells (cells/ml)|=B11*B16||||||RESULTS|Observed Ratio|Expected|Correction||RESULTS|Observed Ratio|Expected|Correction||
|Total Ametrine+ cells|=B17*B8||||||CD45.1|0.45|0.5|=I18/J18||CD45.1|0.49|0.5|=N18/O18|OK|
||||||||CD45.1.2|0.55|0.5|=I19/J19||CD45.1.2|0.51|0.5|=N19/O19|OK|
|CD45.1.2 CELLS|shSrebf2||Cells to STAIN|100000|||||||||||||
|Total Volume|1.6||Volume to Stain (ul) (FACSbuffer)|100|||FINAL MIX|For 1 mouse|For n mice|||FINAL MIX|For 1 mouse|For n mice|||
|Dilution to count||(1/100)|||||Total Cells from CD45.1|=2*I8|=$I$37*I23|||Total Cells from CD45.1|=4*N8|=$I$37*N23|||
|Actual Count (cells/ml)|||Volume to Take for FIRST stain (ul)|=(E21/B25)*1000|||Total Cells from CD45.1.2|=2*I9|=$I$37*I24|||Total Cells from CD45.1.2|=4*N9|=$I$37*N24|||
|Concentration hemocytometer (cells/ml)|4100000||||||||||||||||
|Total Cells|=B25*B22||||||Volume from CD45.1|=(I23/B11)*1000|=(J23/B11)*1000|||Volume from CD45.1|=(N23/B11)*1000|=(O23/B11)*1000|||
||||||||Volume from CD45.1.2|=(I24/B25)*1000|=(J24/B25)*1000|||Volume from CD45.1.2|=(N24/B25)*1000|=(O24/B25)*1000|||
||||||||Volume total (ul)|=SUM(I26:I27)|=SUM(J26:J27)|||Volume total (ul)|=SUM(N26:N27)|=SUM(O26:O27)|||
|Proportion of Ametrine + Cells in CD45.1.2/CD8a/Va2+ gate|0.22||||||||||||||||
|Concentration of Ametrine+ cells (cells/ml)|=B25*B30||||||Final Volume (ul)||=I37*200|||Final Volume (ul)||=I37*200|||
|Total Ametrine+ cells|=B31*B22||||||Add Volume (ul)||=J31-J29|||Add Volume (ul)||=O31-O29|||
||||STAINING||||||||||||||
||||CD8a||||||||||||||
||||CD45.1||||Total Cells|=SUM(I23+I24)|=SUM(J23:J24)|||Total Cells|=SUM(N23+N24)|=SUM(O23:O24)|||
||||CD45.2||||||||||||||
|Fraction1 + Fraction2|=B16+B30||Va2||||mice number|9|||||||||
||||AmCyan (Ametrine aka BV510)||||||||||||||
||||||||(its 4* because we need 2M total)||||||||||

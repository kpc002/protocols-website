---
order: 11
title: "Hic1 Flox/Cre PCR Protocol"
author: Maximilian Heeg
date: last-modified
description: 
  Genotyping PCRs for my Hic1 mouse strains
filters:
   - lightbox
lightbox: auto
---

## PCR Protocol

1.  Thaw DNA in water bath or incubator
2.  Centrifuge and vortex X, MgCl2, and 5X GO buffer
3.  Gently flick primers and controls
    1.  Hic1 primers: 84, 85, 86 (Max's primer box)
        -  Hic1 + control: cKO
        -  Hic1 - control: CT2 and H2O
    2.  UBC Cre primers: 80, 81, 82, 83 (Max's primer box)
        -  Cre + control: CT2
        -  Cre - control: cKO and H2O
    3.  Zeb2 primers: Zeb1, Zeb2, Zeb3 (Shannon's box); working on finding primer stock
        -  Zeb2 + control: Zeb2 +
        -  Zeb2 - control: Zeb2 - and H2O
    4. Hic1 Cre primers: 133, 134, 135 (Max’s primer box)
        - Hic1 Cre +: CT2
        - Hic1 Cre -: cKO and H2O
    5. tdTomato primers: 136, 137, 138, 139 (Max’s primer box)
        - tdTomato +: R26
        - tdTomato -: CT2 and H2O
    
:::callout-note
Making Primers: Dilute primers 1:10 in ddH~2~O (100μL final volume)
:::

4.  Make master mix; [PCR calculator](https://docs.google.com/spreadsheets/u/1/d/1KQnku03JQWAxwmSI1ExukldTsRrIlwtF--9MxJH9g_M/edit)
    1.  Hic1 fl & Hic1 Cre use ER Cre sheet
    2.  UBC Cre and tdTomato use LSL Cas 9 sheet
    3.  Zeb2 use Zeb2 flox
5.  Label and add 1uL of controls/ DNA to PCR tubes
6.  Add Taq polymerase (must be kept on ice!)
7.  Vortex and centrifuge master mix
8.  Add 24μL of master mix to PCR tubes
9.  Centrifuge PCR strips
10. Place in PCR machine
    1.  Hic1 fl / Hic1 Cre / UBC Cre / tdTomato: ER Cre setting (machine A, B, D) or new TD protocol
    2.  Zeb2: Zeb2 setting (machine C) 

## Gel Electrophoresis

1.  Make agarose gel (more % agarose for small fragments)
    -  Hic1 gel (small): 1.5% (1.5g) agarose and 100mL **TBE**
    -  Zeb2 & Hic1 Cre/tdTomato/UBC Cre (small): 2.5% (2.5g) agarose and 100mL TAE
    -  Add 4μL EtBr for small gel; \> 20 samples
    -  Add 8μL EtBr for large gel; \< 20 samples
    -  For large gel double grams of agarose and volume of buffer
2.  Microwave gel bottle for 1.5 - 2 minutes until agarose has dissolved; add EtBr (mix well) and let cool for 15 minutes
3.  Load gel mold & combs
4.  Pour liquid into gel mold; pop/move bubbles to the bottom with pipet tip; let cool for 10 - 15 minutes
5.  Remove combs & place gel into easycast
6.  Fill easycast with 1x TAE OR 1x TBE (for Hic1) to cover gel
7.  Load 10μL gene ladder in the first lane; 20μL of sample in other lanes
8.  Run gel \@ 90-120V
    1.  UBC Cre & Zeb2 & Hic1 Cre: 40 minutes
    2.  Hic1 fl: 80 minutes
9.  UV Image

## Results

### Hic1 fl Expected Bands:
- WT: 650bp
- Flox: 700bp
- Deletion: 320bp
- Example in @fig-hic1-fl

### UBC Cre Expected Bands:
- Cre +: band @ 100bp
- Cre -: no band @ 100bp
- Example in @fig-cre

### Zeb2 Expected Bands:
- Zeb2 fl/+: 1 band @ 500bp; other @ 700bp
- Zeb2 fl/fl: band @ 700bp
- Zeb2 WT: band @ 500bp

### Hic1 Cre Expected Bands:
- Hic1 Cre -/+: 1 band @ 450bp; other @ 500bp
- Hic1 Cre -/-: 1 band @ 500bp
- Hic1 Cre WT: 1 band @ 450bp

### tdTomato Expected Bands:
- tdTomato mutant: 1 band @ 200bp
- tdTomato heterozygous: 1 band @ 200bp; other @ 297bp
- tdTomato WT: 1 band @ 297bp

::: {#fig-examples layout-ncol=2}

![Hic1 floxed: 1st lane: Hic1 WT (650bp); 2nd lane: Hic1 floxed (700bp)](Hic1_floxed.jpg){#fig-hic1-fl}

![CRE: 1st lane: Cre positive sample; 2nd lane: Cre negative sample; 3rd lane: positive control; 4th lane: H20 control](Cre.jpg){#fig-cre}

Examples of PCR results
:::





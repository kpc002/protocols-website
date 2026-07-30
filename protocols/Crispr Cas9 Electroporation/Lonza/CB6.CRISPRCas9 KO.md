---
title: CB6.CRISPRCas9 KO
description: Workflow for generating CRISPR-Cas9 knockout cells.
order: 10
author: Giovanni Galleti
date: last-modified
image: oligo.svg
---

**CRISPR/Cas9 knock out in primary T cells and *in vivo* transfer**

> **Materials**

  - Lonza 4D-NucleofectorTM System **(near Xenium)**

  - P3 primary cell 4D Nucleofector electroporation kit (Lonza, Cat\# V4XP-3032 for electroporation wells, Cat\# V4SP-4032 for cuvettes) **(under Nicole’s bench at RT)**

  - P3 buffer: make fresh on the day, mix 3.6 μl reagent 1 with 16.4 μl diluent per reaction (Lonza Nucleofector kit) *\*Though Lonza tech support said it’s good for a month in 4’C. **(inside Nicole*****’s bucket at 4ºC*)***

  - Recombinant Cas9 protein, 40uM, @ -80ºC **(middle shelf, rightmost rack, Cas9 Box, 10 µL aliquots)**

  - 20bp gRNAs+80mer scaffold with chemical modification

  - R10 (RPMI + 10% FCS, glutamine, antibiotics, 50 nM BME, NEAA, HEPES)

**Enrich CD8+ T cells** – naïve or activated

  - **If naïve, do CD8 enrichment prior to protocol**

  - **If activated, activate 24hr prior to this protocol.**

**CRISPR/Cas9 electroporation**

1.  To make a Cas9/RNA complex, mix guides plus tracr RNA as below in PCR tubes:
    
    1.  gRNA thy1 guide only control
    
    2.  gRNA thy1 guide plus guide of 1<sup>st</sup> target
    
    3.  gRNA thy1 guide plus guide of 2<sup>nd</sup> target
    
    4.  etc.

<!-- end list -->

  - want to do 3:1 molar ratio of guide RNA to Cas9 enzyme.

  - Thy1 AC guide at 100uM concentration.

  - Experimental guides are at 100uM concentration.

  - Set up as follows:
    
      - Control
        
          - **3uL thy1 AC crRNA guide from IDT (Box ‘Nicole’ at -20ºC)**
        
          - 3uL tracr RNA (Alt-R® CRISPR-Cas9 tracrRNA, ATTO™ 550) **(Box ‘Nicole’ at -20ºC)**
    
      - Experimental (x number of groups needed)
        
          - **1.5uL thy1 AC crRNA guide from IDT**
        
        <!-- end list -->
        
          - **1.5uL guide of experimental guide (Alt-R CRISPR-Cas9 crRNA from IDT)**
        
          - 3uL tracr RNA (Alt-R® CRISPR-Cas9 tracrRNA, ATTO™ 550)

<!-- end list -->

1.  Incubate in PCR machine at 95’C for 5 minutes, then immediately remove at put at RT in the dark for 1 hour for annealing.

2.  Add 1.9uL 40uM Cas9 enzyme to each tube (-80’, middle shelf, middle rack). DO NOT MIX. Gently flick the tube to mix sgRNAs with Cas9 and spin down briefly to collect drops from the sides of the tube. Incubate for 20 minutes at room temperature for complex formation.

3.  Turn on Lonza 4D-NucleofectorTM System: select wells, pulse code (see below) and solution (P3 primary).

4.  Make a P3 buffer mix below per reaction and keep at room temperature.
    
      - 1x buffer recipe, make enough for each rxn:
        
          - <span class="underline">Supplement 1</span>: 3.6uL
        
          - <span class="underline">P3</span>: 16.4uL

5.  Take 10mL of R10 plus 50U/ml hIL2 (a 1:2000 dilution), and put into a waterbath to warm to 37deg.

6.  **Count cells, then spin down cells in large volume (use 50 mL conical) of STERILE, RT PBS to remove potential RNase contamination from FCS containing media before electroporation (IMPORTANT).** Can do 2-10x10^6 cells per reaction.

7.  Immediately after complex formation, transfer cells into Eppendorf tubes in 1 ml of PBS, and spin down on a tabletop centrifuge at 5000 RPM for 5min **<span class="underline">room temperature</span>**). **It is important to prepare everything before resuspending the cells in P3 buffer to minimize the time that cells are exposed to the buffer.**

8.  Take supernatant from the cell pellet using pipets (make sure to take off all remaining liquid from cell pellet to not dilute out the small reaction volume of 25 μl). Resuspend <span class="underline">cell pellet in 20μl P3 buffer</span> per reaction

9.  Transfer 5 μl of CRISPR/Cas9 RNP into the 20 μl P3 buffer with cells and mix gently.

10. Transfer the 25 μl cell/RNP mix to the bottom hole of a well of the Lonza nucleofector strip. **Be careful to not create any bubbles.** **(keep time of cells in P3 buffer as short as possible as it is cytotoxic to the cells).**

11. Electroporate cells by putting the nucleofector strip into the Lonza nucleofector and as depicted, start the program
    
      - Naïve CD8 T cells: use DN100 program in P3 buffer
    
      - Activated CD8 T cells: use DS137 program in P3 buffer

12. After electroporation (a few seconds) add 130 μl of 37°C pre-warmed R10 media into the well containing electroporated cells and rest cells for 10 minutes in the incubator (5% CO2, 37°C).

13. In the meantime, prepare a 6-MW plates with R10 and IL-2 at 15 U/mL

14. Dilute 1:3.33 the leftover R10 + IL-2 (50 U/mL) from step 6: 600 µL of R10+IL-2 with 1400 µL of R10 plain (final 15 U/mL)

15. After the 10-minute incubation is done split the cells over the original number of cells they were into (e.g., if three wells were originally pooled to do CRISPR on, then split them back into the original 3 wells)

16. Incubate for overnight/24 hrs

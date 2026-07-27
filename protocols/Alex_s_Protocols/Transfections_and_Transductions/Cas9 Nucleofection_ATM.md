---
title: "Cas9 Nucleofection_ATM"
description: "Protocol for assembling Cas9 ribonucleoprotein complexes and nucleofecting enriched or activated CD8 T cells."
order: 10
author: "Alex Monell"
date: last-modified
image: dna.svg
---

[View the original PDF](Cas9%20Nucleofection_ATM.pdf){.btn .btn-outline-primary}

# Cas9 Nucleofection

Introduction

Get started by giving your protocol a name and editing this introduction.

Materials

**›** Materials

**›** Lonza 4D-NucleofectorTM System

**›** P3 primary cell 4D Nucleofector electroporation kit (Lonza, Cat\# V4XP-3032 for electroporation wells, Cat\#

V4SP-4032 for cuvettes)

**›** P3 buffer: make fresh on the day, mix 3.6 μl reagent 1 with 16.4 μl diluent per reaction (Lonza Nucleofector

kit) \[*Though Lonza tech support said it’s good for a month in 4 °C.*\]

**›** Recombinant Cas9 protein, 40 μM, –80 °C \[Ordered Cas9-NLS purified protein (2.5 mg) from University of

California Berkeley Macrolab\]

**›** 20 bp gRNAs – 80-mer scaffold with chemical modification

**›** R10 (RPMI + 10% FCS, glutamine, antibiotics, 50 mM BME, NEAA, HEPES)

Procedure

CD8 Enrichment

1\. If naïve, do CD8 enrichment prior to protocol.

2\. If activated, activate 24 hr prior to this protocol.

Reconstitute Tracr

3\. To reconstitute tracrRNA - if 20 nmol + 200 μl buffer

\- new CRISPR tracr resuspend in 200ul of Duplex buffer

4\. Resuspending crRNA - Check the resuspension calculator on IDT. I did 100 ul to get to 100 uM

CRISPR/Cas9 electroporation

5\. **To make a Cas9/RNA complex**, mix guides plus tracr RNA as below in PCR tubes:

a) gRNA thy1 guide only control

> Page 1 of 3

b) gRNA thy1 guide plus guide of 1st target

c) gRNA thy1 guide plus guide of 2nd target

d) etc.

\- We want to do 3:1 molar ratio of guide RNA to Cas9 enzyme.

\- Thy1 AC guide at 100 μM concentration.

\- Experimental guides are at 100 μM concentration.

\- tracrRNA at 100 μM concentration.

**- Set up as follows:**

**Control**

> \- 3 μl thy1 AC crRNA guide from IDT
> 
> \- 3 μl tracr RNA (Alt-R® CRISPR-Cas9 tracrRNA, ATTOTM 550)
> 
> \- We might need to add 1.5 μl buffer here too (idk ask Nicole)

**Experimental (× number of groups needed)**

> \- 1.5 μl thy1 AC crRNA guide from IDT
> 
> \- 3 μl guide of experimental guide (Alt-R CRISPR-Cas9 crRNA from IDT)
> 
> \- 3 μl tracr RNA (Alt-R CRISPR-Cas9 tracrRNA, ATTOTM 550)

6\. **Incubate** in thermocycler at 95 °C for 5 minutes, then immediately remove and put at RT in the dark for 1 hour for

annealing.

7\. **Add 2.38μl 40 μM Cas9 enzyme** to each tube (use –80). **DO NOT MIX.** Gently flick the tube to mix sgRNAs with

Cas9 and spin down briefly to collect drops from the sides of the tube. Incubate for 20 minutes at room temperature

for complex formation.

8\. **Make a P3 buffer mix** below per reaction and keep at room temperature.

**1× buffer recipe, make enough for each run:** \[Lonza (in fridge)\]

Supplement 1: 3.6 μl

P3: 16.4 μl

9\. Take 10 mL of R10 plus 50 U/mL hIL2 (a 1:2000 dilution), and put into a water bath to warm to 37 °C.

Pipette media into well and collect in tube, then spin.

10\. Count cells, then spin down cells in large volume of **STERILE, RT PBS** (4ml) to remove potential RNase

contamination from FCS-containing media before electroporation (**IMPORTANT**). Can do 2-10×10^6 cells per

reaction.

11\. Immediately after complex formation, transfer cells into Eppendorf tubes in **1 mL of PBS**, and spin down on a

tabletop centrifuge at 5000 RPM for 5 min at room temp. It is important to prepare everything before resuspending the cells in P3 buffer to minimize the time the cells are exposed to the buffer.

12\. Take supernatant from the cell pellet using pipets (make sure to take off all remaining liquid from cell pellet to not

dilute out the small reaction volume of 25 μl). Resuspend cell pellet in **20 μl P3 buffer per reaction**.

13\. Transfer **5 μl CRISPR/Cas9 RNP** into the **20 μl P3 buffer** with cells and mix gently.

> Page 2 of 3

14\. Transfer the **25 μl** cell/RNP mix into the bottom of a well of the Lonza nucleofector plate and mix gently. Be careful

to not create any bubbles. (Keep time of cells in P3 buffer as short as possible — it is cytotoxic to the cells.)

15\. Electroporate cells by putting the nucleofector strip into the Lonza nucleofector and as specified, start program:

**- Naïve CD8 T cells: use DN100 program in P3 buffer**

**- Activated CD8 T cells: use DS137 program in P3 buffer**

16\. After electroporation (a few seconds) add **130 μl of 37 °C pre-warmed R10 media** into the well containing

electroporated cells and rest cells for 10 minutes in the incubator (5% CO2, 37 °C).

17\. Resuspend the cells in the electroporation well using a pipette, and transfer the cell suspension into a fresh tube or

well. To recover any remaining cells, wash the electroporation well with an additional **150 μl R10 media** by pipetting, and transfer the media into the same collection tube. Add **700 μl pre-warmed R10** to make **1 mL total**.

18\. Count the cells with Trypan Blue. **20–50% of T cells will be lost during the electroporation step.**

19\. **For in vivo adoptive transfer**, resuspend in PBS at desired concentration and adoptively transfer into recipient

mice via intravenous injection. Keep some cells growing in culture for future flow and KO validation with flow or Sanger sequencing (if naïve, activate as well).

> Page 3 of 3

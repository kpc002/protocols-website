---
title: "CB1.Tissue processing for viral titers"
description: "Protocol for collecting and processing tissue samples for measurement of viral titers."
order: 10
author: "Nicole Sharping"
date: last-modified
---

**Tissue processing for viral titers**

Kennidy Takehara

Last updated 11/22/23

**Reagents:**

Homogenization beads: BioSpec \#11079125Z

Tubes for homogenization: Genesee scientific: \#21-354

Primer LCMV GP Rev: GCAACTGCTGTGTTCCCGAAA

Primer LCMV GP Fwd: CATTCACCTGGACTTTGTCAGACTC

**Collecting tissues:**

1.  Collect \<30mg of tissues (can use 30ul as reference) into shatterproof homogenizer tubes and immediately place on dry ice. Store in -80 until ready to use
    
    1.  Can also take remaining organ into eppies to keep in -80 as backup, suggest cutting small pieces before freezing.

**Processing tissues:**

Recommended: label 2 sets of eppie tubes per sample and pre-label RNEasy columns to limit protocol time. Want to work as quickly as possible.

1.  Keep tissues on dry ice (and then ice) while preparing for homogenization

2.  Add 600ul RLT buffer (from RNEasy kit) with one scoop of beads to homogenizer tube
    
    1.  Recommended for tissue: add 10ul BME for every 1mL RLT

3.  Take tubes to Zuniga lab and homogenize (need to be trained by Kennidy or Zuniga lab member)
    
    1.  For homogenizer: 30 seconds, check for chunks and do another 30 seconds if necessary

4.  Spin down entire tube full speed 4 degrees for 10 minutes.

5.  Pipette \~350ul of supernatant into new eppie tube & add one volume 70% ethanol.

6.  Continue with RNeasy kit – pick up with transfer to RNeasy spin column: <https://www.qiagen.com/us/resources/download.aspx?id=0e32fbb1-c307-4603-ac81-a5e98490ed23&lang=en>

7.  I usually elute in 30ul of H20

**Continue with cDNA synthesis**: <https://protocols.heeg.io/protocols/mol_bio/cDNA.html>

All reagents can be found in pink qPCR box or SSIV box

Briefly:

1)  Remove DNA contamination (scale up for 30ul)
    
    1.  Add 2.5ul of 10X TURBO DNase Buffer and 1.25µl TURBO DNase to 25 µl of RNA, and mix gently
        
        1.  May need to adjust these numbers based on how much volume you get from elution
    
    2.  Incubate at 37°C for 20-30 min
    
    3.  Add resuspended Inactivation Reagent (5µl to 28.75 µl mix), and mix well
    
    4.  Incubate 5 min at RT, mixing occasionally
    
    5.  
    6.  Centrifuge at 10000 x g for 1.5 min and transfer the RNA to a fresh tube
    
    7.  Recommended: nanodrop to get concentration and purity

2)  Anneal primer to template RNA

<!-- end list -->

  - Heat the RNA-primer mix at 65°C for 5 minutes, and then incubate on ice for at least 1 minute

| **Component**                                                                              | **Volume**  |
| ------------------------------------------------------------------------------------------ | ----------- |
| 50 μM Oligo d(T)20 primer, **50 μM random hexamers**, or 2 μM gene-specific reverse primer | 1 μL        |
| 10 mM dNTP mix (10 mM each)                                                                | 1 μL        |
| Template RNA (10 pg–5 μg total RNA or 10 pg–500 ng mRNA)                                   | up to 11 μL |
| DEPC-treated or nuclease-free water                                                        | to 13 μL    |

  - Use 50uM random hexamers to amplify all RNA, use oligo d(T) primers if want entire RNA fragment (ie for cloning gene)

**Prepare RT reaction mix**

  - Vortex and briefly centrifuge the 5× SSIV Buffer.

  - Combine the following components in a reaction tube.

| **Component**                                    | **Volume** |
| ------------------------------------------------ | ---------- |
| 5× SSIV Buffer                                   | 4 μL       |
| 100 mM DTT                                       | 1 μL       |
| RNaseOUT™ Recombinant RNase Inhibitor            | 1 μL       |
| SuperScript® IV Reverse Transcriptase (200 U/μL) | 1 μL       |

  - Add 7µl RT reaction mix to the annealed RNA (13 µl)

**Incubate reactions**

  - If using random hexamer, incubate the combined reaction mixture at 23°C for 10 minutes, and then proceed to next step.  
    If using oligo d(T)20 or gene-specific primer, directly proceed to next step.

  - Incubate the combined reaction mixture at 50–55°C for 10 minutes.

  - Inactivate the reaction by incubating it at 80°C for 10 minutes

**Remove RNA**

  - To remove RNA, add 1 μL E. coli RNase H, and incubate 37°C for 20 minutes.

For qPCR:

HPRT SYBR and LCMV GP primers, stock 100μM

  - Dilute primers: 2.5μl F, 2.5μl R, 195 μl water

I usually dilute cDNA with 20ul of water, for 40ul total of cDNA (enough to repeat if needed)

qPCR rxn:

  - Primers: 1μl

  - SYBR 2x: 5μl

  - cDNA: 4μl

Tips for qPCR:

1.  Group primers together, so at least 2 replicates per sample

2.  Make sure to mix with pipette all reagents

3.  Use same batch of SYBR – make sure have enough before starting

4.  I like to pipette all of my cDNA on one side of well (make sure some in every well) and then flip around and pipette master mix on other side

5.  Make sure to be VERY accurate with pipetting (I like to reverse pipette)

6.  Include cDNA positive control (so know qPCR works with housekeeping) and water control

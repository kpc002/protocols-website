---
title: "Human tumor sample collection, processing, and flow analysis"
description: "Human tumor sample collection, processing, and flow analysis"
order: 10
author: Kelsey Bennion
date: last-modified
image: blood_sample.svg
---

**<span class="underline">TUMOR TISSUE PROCESSING</span>**

Sample ID:\_\_\_\_\_\_\_\_ Patient ID:\_\_\_\_\_\_\_\_

Collection Date/Time:\_\_\_\_\_\_\_\_ Processing Date/Time:\_\_\_\_\_\_\_\_

Processing Scientist Initials:\_\_\_\_\_\_\_

**<span class="underline">SAMPLE PREPARATION</span>**

1.  Ideally at least one week prior to collection, identify samples and ensure sufficient amounts of antibody. Book flow time on cytometer for the day of processing

2.  Day before or day of tissue collection, prepare 50mL conical tube with 25mL RPMI/10%FBS/1% Pen-Strep. If multiple samples, prepare multiple tubes (for both collection, as well as processing and flow steps below)

3.  Record mass of tissue at time of collection, and record

<!-- end list -->

  - > POST-COLLECTION MASS OF TUBE (g): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

  - > MASS OF FLOW TISSUE (g):\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**<span class="underline">SAMPLE PROCESSING</span>**

1.  Prepare enzymatic processing tube: 50mL conical containing 4.7mL RPMI-1640 (no FBS/Pen-Strep, or L-Glut) + 200 µL Enzyme H + 100 µL Enzyme R + 25 µL Enzyme A (Tumor Dissociation Kit from Miltenyi).

2.  Remove tissue from 50mL collection conical tube and place into petri dish, and dissect into small pieces using scalpel or sterile scissors. Transfer sample into gentleMACS “C Tube” using the enzymatic solution, making sure to transfer all tissue.

3.  Tightly close tube, attach it upside down into one of the two sleeves on the gentleMACS dissociator (either sleeve may be used). Make sure tumor samples are near the rotor/stator and not adhered to the upper walls of the tube. Ensure tube is seated properly. You should hear and feel a “click” when the tube is properly attached.

4.  Run gentleMACS program “h\_tumor\_01”.

5.  Detach tube. Incubate for 30 minutes at 37ºC with continuous rotation. If tube rotator is not available, manually rotate/agitate tube every \~5 minutes.

6.  Attach tube to gentleMACS dissociator, run program “h\_tumor\_01” (second time doing this).

7.  Detach tube. Incubate for 30 minutes at 37ºC with continuous rotation. If tube rotator is not available, manually rotate/agitate tube every \~5 minutes.

8.  Attach tube to gentleMACS dissociator, run program “h\_tumor\_01” (third time doing this).

9.  Using sterile RPMI-1640, resuspend sample/wash out of C tube and cap, strain through a 70 µm filter and wash with \~20ml media.

10. Should have a (mostly) single cell suspension free of chunks of tissue. Centrifuge at 300*xg* for 5 minutes.

11. Resuspend sample in FACS buffer and aliquot sample to appropriate flow tubes for downstream staining. Proceed to flow staining as below.

> **<span class="underline">TUMOR IMMUNE CELL ANALYSIS</span>**
> 
> **Surface stain**

1.  Centrifuge samples for 5min at 300*xg*, and gently remove supernatant.

2.  Resuspend samples in surface antibody solutions.

3.  Incubate samples for 30min on ice in the dark.

4.  Wash samples with 250μl FACS buffer, spin down 5min at 300*xg*, and gently remove supernatant.

**Fixation, Permeabilization and Cytokine/TF staining**

5.  Resuspend cells with 100μL of eBioscience transcription factor fixation buffer per well, and incubate 30min. on ice in dark.

6.  Prepare solution of 1x PermWash by diluting 10x PermWash to 1x in sterile H<sub>2</sub>O. Add 100μl 1x PermWash to each sample, spin down 5min at 300*xg*, and gently remove supernatant.

7.  Wash cells with 100µl 1x PermWash, spin 5min. at 300*x*g, gently remove supernatant.

8.  Add intracellular staining solutions as follows, and incubate 60min at room temperature in the dark.

9.  While samples are incubating with intracellular stain, prepare individual compensation controls using eBioscience UltraComp eBeads with individual antibodies from lymphocyte panel, as well as unstained beads. Also prepare Sphero Rainbow beads (drop of positive and negative beads + 200μl FACS buffer). Rainbow beads are especially important to maintain consistency across donors and across collection timepoints.

10. Add 150µl 1x PermWash, spin down 5min at 300*xg*, gently remove supernatant.

11. Resuspend samples in 250μl FACS buffer, and transfer to flow tubes.

12. Flow samples

**<span class="underline">RUNNING AND ANALYSIS OF FLOW DATA</span>**

1.  For all populations (lymphocyte, Treg, and myeloid), gate on singlets (FSC-A x FSC-H), cellular events (FSC-A x SSC-A), live events (Ghost Dye780 x SSC-A), dump negative events (Mouse CD8-FITC x SSC-A), and CD45+ events (CD45-PE-Cy7 x SSC-A).

2.  After isolating CD45+ cells, go through and evaluate panels using individual analysis

> **<span class="underline">LYMPHOCYTE PANEL:</span>**
> 
> CD4+ and CD8+ T cells, CD19+ B cells, NK cells (CD3- CD56+), and NK-T cells (CD3+ CD56+). We will then evaluate markers of T cell memory (CD45RO and CD26), T cell activation/exhaustion (PD-1 and TIM-3), as well as a PD-1 responsive stem-like population of CD8+ T cells (HLA-DR+ CD38+ Ki67+).
> 
> **<span class="underline">Treg PANEL:</span>**
> 
> To evaluate regulatory T cell populations, samples will be stained with CD45, CD3, CD4, CD25, GITR, CD127, and Foxp3
> 
> **<span class="underline">MYELOID PANEL:</span>**
> 
> CD45, CD11b, CD11c, CD14, CD15, CD16, CD33, CD40, CD103, HLA-DR, and will also be evaluated for expression of PD-L1.

  - Monocytes (CD11b+ CD11c+ CD14+ CD16<sup>lo</sup> HLA-DR+)

  - Macrophages (CD11b+ CD11c+ CD33+ CD14- CD16+ M1 macrophages and CD11b+ CD11c+ CD33+ CD14+ CD16+ M2 macrophages),

  - Dendritic cells (CD11c+ CD14+ CD16- CD103+ HLA-DR+, with CD40 expression used to identify activated DCs),

  - Myeloid-derived suppressor cells (CD11b+ HLA-DR<sup>lo/neg</sup> CD33+ CD14+ CD15- monocyte MDSC and CD11bb+ HLA-DR<sup>lo/neg</sup> CD33+ CD14+ CD15+ granulocytic MDSC),

  - Neutrophils (SSC<sup>hi</sup> CD11b+ CD14<sup>lo/neg</sup> HLA-DR- CD14+ CD15+ CD16<sup>hi</sup> CD11+)

  - Eosinophils (SSC<sup>hi</sup> HLA-DR- CD15+ CD16-).

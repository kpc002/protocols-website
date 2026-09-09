---
title: FC1.antibody_titration
description: Protocol for titrating flow-cytometry antibodies to identify an optimal
  staining concentration.
order: 10
author: Giovanni Galleti
date: last-modified
image: oligo.svg
---

Date: 02/08/2023

**<span class="underline">Antibody titration</span>**

**NOTES:**

1.  > Before using the antibodies, mix well and spin down in order to avoid antibody aggregates. Alternatively, prepare the antibody mix and spin it before staining.

2.  > Have a look to antibody datasheets to know if the staining has to be performed at 37°C (especially for receptors undergoing cell internalization and recycling). Add co-staining with other markers if needed.

3.  > Since BV and BUV conjugates are very sensible to the buffer and since we are using them daily in our FACS panels, it is strongly suggested to titrate all the Abs in Super Bright Complete Staining Buffer (Thermo Fisher, catalog \#: SB-4401-42).

**MATERIALS:**

  - Live/Dead Blue (Thermo Fisher, -80°C, GG reagents box) → **Add 50 μL of DMSO to the vial of reactive dye.**

  - ArC™ Amine Reactive Compensation Bead Kit (Thermo Fisher, 4°C, my drawer) → comp beads for Live/Dead Blue

  - UltraComp eBeads™ Compensation Beads (Thermo Fisher, 4°C, my drawer)

  - FACS buffer (1X PBS-/- + 2% FBS)

  - Super Bright Complete Staining Buffer (Thermo Fisher, catalog \#: SB-4401-42) --\> 5 µL/test to be added directly to the antibody mix

  - Fix solution depending on the application

  - Antibody to be titrated

  - Cells

**PROTOCOL**

  - Wash the cells with 2 mL (20X staining volume) of 1X PBS-/- if cells are suspended in complete RPMI, in order to eliminate FBS or BSA that can bind Live/Dead Blue

  - Prepare Live/Dead Blue mix: for 4 samples (100 µL/test) 10M cells each (19.5 µL ddH2O in which you add 0.5 µL Live/Dead Blue; then add 380 µL PBS-/-)

  - Add 50 µL Live/Dead Blue mix to each sample tube. Add 50 µL of Fc Block (ready to use at 4ºC) to each sample tube. Incubate 15 min at RT in the dark.

  - Wash the cells with 2 mL FACS buffer and centrifuge 1600 rpm 4 min

  - Discard the supernatant

  - If antibody to titrate goes at 37ºC for 20 minutes than perform now the steps described below for titration and co-stain after.

  - Add surface co-staining at this step, if needed. Then wash and discard as above. <span class="underline">NB: if titrating an intracellular antibody proceed with fixation and permeabilization.</span>

  - Resuspend the cells into a FACS buffer volume equal to N° tubes (8) X 50 µL

  - Put 50 µL of FACS buffer (with 5 µL/test of Super Bright Complete Staining Buffer) in all tubes <span class="underline">but tube 1</span>

<!-- end list -->

  - Prepare 115 µL Antibody mix 2X (it will be in excess). The mix has to be prepared in FACS buffer with 5 µL/test of Super Bright Complete Staining Buffer

<!-- end list -->

  - Add 50 µL Antibody mix in the <span class="underline">first two tubes</span> and mix well. Then proceed with serial dilution as described: remove 50 µL of suspension from tube 2 and put it in tube 3, mix well; remove 50 µL from tube 3 and put it in tube 4, mix well, etc. <span class="underline">NB: remove 50 uL from tube 7 and toss it as tube 8 is the unstained control</span>

  - Put 50 µL cell suspension into each tube and incubate 20 min at 4ºC in the dark

  - Wash with 2 mL of FACS buffer and centrifuge 1600 rpm 4 min

  - Discard the supernatant

  - In order to fix cells, add 150 µL of fix buffer (BioLegend – brown bottle) and incubate for 10 minutes. Alternatively, you can fix and perm in the preferred conditions.

  - Wash cells with 2 mL FACS buffer and centrifuge 1600 rpm 4 min. Alternatively, follow the manufacturer protocol for fixation and permeabilization.

  - Discard the supernatant

  - Add intracellular co-staining at this step, if needed. Then wash and discard as above. Alternatively, proceed with intracellular/intranuclear antibody titration as described above (<span class="underline">use PermWash instead of FACS buffer and avoid use of SB buffer for intracellular antiobodies</span>).

  - Resuspend the cells with 200 µL of FACS buffer, keep samples at 4°C until ready for acquisition

**<span class="underline">Compensation</span>**

**NOTES:**

1.  > You can use cells or beads. Use beads preferentially and <span class="underline">vortex very well</span> them before using.

2.  > For Bigfoot it is mandatory to prepare the unstained control even with cells only to detect and spectral unmix the autofluorescent signal coming from cells. Optional but recommended are the single stained control with cells.

3.  > If the antibody is conjugated with tandem dyes, you must use the same antibody to prepare the comps.

**PROTOCOL**

  - > For each dye make one comp using 1 drop of UltraComp eBeads + Ab at the right titer (if the titer is lower than 0.5 µL use 0.5 µL).

  - > Make the unstained control comp with 1 drop of UltraComp eBeads.

  - > Make the positive control comp for Live/Dead Blue with 2 drops of ArC Amine Reactive beads + 2 µL Live/Dead Blue

  - > Make the negative control comp for Live/Dead Blue with 2 drops of ArC Amine Negative beads <span class="underline">(no Live/Dead Blue)</span>

  - > Incubate comps at least for 20 minutes in the dark. <span class="underline">NB: If in a hurry you can avoid doing the steps below. Usually bead comps are stable for up to a week.</span>

<!-- end list -->

  - Wash with 2 mL FACS buffer **<span class="underline">(DO NOT WASH positive neither negative control comp for Live/Dead Blue)</span> and centrifuge** 1600 rpm 4 min

  - Fix comps with 150 µL of fix solution (FA 1% in HBSS-/- or PFA 1% in HBSS-/-) and incubate for 15 minutes. <span class="underline">NB: work under the chemical hood.</span> **<span class="underline">DO NOT FIX positive neither negative control comp for Live/Dead Blue\!</span>**

  - Wash cells with 2 mL FACS buffer and centrifuge 1600 rpm 5 minutes. <span class="underline">NB: work under the chemical hood.</span>

  - Discard the supernatant.

  - Resuspend comps with 200 µL of FACS buffer, keep samples at 4°C until ready for acquisition.

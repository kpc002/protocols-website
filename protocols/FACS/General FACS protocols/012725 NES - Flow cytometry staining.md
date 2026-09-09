---
title: "012725 NES - Flow cytometry staining"
description: "Protocol for antibody staining and preparation of cells for flow cytometry analysis."
order: 10
author: "Nicole Sharping"
date: last-modified
---

**Flow cytometry staining techniques**

**Nicole Scharping February 2025**

Flow cytometry is an extremely useful technique that can provide you with a LOT of data at once, but it can be complicated. This is a straightforward set of protocols to stain and run samples fairly easily.

**Table 1**

<table>
<thead>
<tr class="header">
<th>Analyzer</th>
<th>Lasers</th>
<th>Colors available</th>
<th>Software</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BD Fortessa</td>
<td><p>Blue (488)<br />
<br />
Red (621)<br />
<br />
Violet (405)</p>
<p>Yellow-green (561)</p></td>
<td><p>FITC/488/NBD/BODIPY/GFP/YFP PerCP-Cy5.5<br />
APC/AxF647/660/MitoDR, APC-Cy7, AxF700</p>
<p>Pac Blue/BV421/V450, BV510/Ametrine, BV605, BV650, BV711, BV786</p>
<p>PE/RFP/Cherry, PE-594/MitoOr, PE-Cy7</p></td>
<td>FACSDiva</td>
</tr>
</tbody>
</table>

**Recipes for FAC buffer (for analysis)**

  - 500 mL 1X PBS

  - 2% (10 mL) FBS

  - 1:1000 Sodium azide

**Basic surface staining (includes Alternative Protocol: Fixation)**

1.  Aliquot your cells in a 96-well round or V bottom plate

2.  Add 20-50uL FC block into wells with cells in media, put on ice for minimum 10min (longer is ok)

3.  During the FC block, make up your staining cocktail in FACS Buffer (1XPBS + 2% FCS), make enough for 100uL per well.

4.  Spin the plate down at 2000rpm for 1 min

5.  Flick off the supernatant into the sink. Some like to use a vacuum and suck the individual supernatants off, I never found much utility in this.

6.  Aliquot 100uL into each well as appropriate (you can use a multichannel if there’s a lot of samples). Resuspend up and down with a multichannel pipet. DO NOT reuse tips for multiple rows

7.  Incubate on ice in the dark for 15 minutes.

8.  Add 180 uL of FACS buffer to each well and spin down (this is a wash step).

9.  Resuspend in 100 uL of FACS buffer and move to FACS tubes.

10. Make single color controls with beads (see protocol below)

11. Analyze on flow cytometer.

> **Alternate Protocol: Fixation**
> 
> If you cannot run the samples immediately (remember, they are still live cells), you can fix them. Paraformaldehyde (4% made up in PBS) is the most common fixation method for flow cytometry. It is fast and works very well, while still preserving cellular structure. Some antigens are lost with PFA fixation.

1.  After the wash step (step 8) spin, resuspend cells instead in 100 uL of 4% PFA in PBS. Incubate at room temperature in the dark for 20 minutes.

2.  Add 180 uL of FACS and spin down.

3.  Resuspend pellet in 100 uL of FACS buffer. Seal the plate with Parafilm around the outside, wrap in foil, and store at 4 deg for up to 7 days (could last longer)

4.  Make single color controls with beads (see protocol below)

**Cytoplasmic intracellular staining I (for cytoplasmic proteins)  
includes Alternate Protocol: Intracellular Cytokine Staining)**

For most intracellular (but non-nuclear) proteins, this protocol will suffice to stain fairly well. As always, though, this is heavily antibody dependent.

1.  Surface stain the cells as normal.

2.  After the wash step, spin down cells at 2000 rpm for 1 min.

3.  First, resuspend cells instead in 100 uL of 4% PFA in PBS. Incubate at room temperature in the dark for 20 minutes. (This step helps preserve certain surface stains like Tim3, as well as ametrine expression in transduced cells)

4.  Add 180 uL of FACS and spin down.

5.  Resuspend cells in 100 uL BD CytoFix/CytoPerm, kept at 4 deg in a brown bottle.

6.  Incubate at RT for 20 min.

7.  Add 180 uL of BD PermWash (10X solution kept at 4 deg in a clear bottle, dilute into ddH20).

8.  Spin down and flick off.

9.  During the spin, make up a staining solution as you would for surface staining (100 uL/well), but make it up in BD PermWash rather than FACS buffer.

10. Resuspend cells in 100uL of staining solution per well and incubate at RT in the dark for 30 minutes.

11. Wash with 180 uL of PermWash and spin down.

12. Resuspend in 100 uL FACS buffer and move to FACS tubes.

13. Run on analyzers or parafilm the plate, wrap in foil, and store at 4 deg for up to 7 days.

14. Make single color controls with beads (see protocol below)

**Alternate Protocol II: Intracellular cytokine staining**

This protocol is used to detect the frequency of cytokine producing cells in a mixed culture, as well as the amount of cytokine produced (by MFI). Cytokines are measured by first stimulating the cells in the presence of a protein transport inhibitor (usually brefeldin A or monensin, which collapse the Golgi or late ER, respectively), then doing cytoplasmic staining using anti-cytokine antibodies. For some cytokines, like TNFa, IL-2, IL-17, and IFN-g, these assays work beautifully. For other cytokines, such as IL-4, -5, -10, and -13, the effects are much less so, relying on shifts of MFI rather than a large shift of cytokine positive cells. Stimulation times, protein transport inhibitor choices, and stimulation type for each of these cytokine should be determined empirically.

1.  Harvest and stimulate your cells
    
    1.  Peptide mix
        
        1.  Plate cells in 96 well round bottom plate, spin down at 2000 RPM for 1 minute
        
        2.  Add 200uL T cell media per well with cells (there must be some APCs in the mix somewhere, purified T cells would not be able to use this method) in the presence 1:500 peptide (GP33 aliquots in Goldrath TC freezer) and 1:500 Protein Transport Inhibitor (mixture of brefeldin A and monensin)
        
        3.  Resuspend using multichannel
        
        4.  Stim for 4hr at 37deg (in incubator)

2.  Surface stain your cells according to Basic Protocol.

3.  Fix/perm the cells and stain your cytokine by the intracellular cytoplasmic protocol.

4.  Resuspend in FACS buffer and analyze, or store at 4 deg in the dark for up to 3 days.

5.  Make single color controls with beads (see protocol below)

**Nuclear intracellular staining**

This protocol allows for identification of cells based on their expression of transcription factors and other nuclear proteins. The staining reagents used to accomplish this, however, are very harsh, and can dramatically changing forward/side scatter profiles and potentially hiding some antigens. In addition, fluorescent proteins used in reporter constructs will leech out, deadening their signal. Including a 4% PFA fix before the nuclear fix helps decrease this effect.

1.  Stain cells as in Basic Surface staining protocol.

2.  After the wash step, spin down at 2000rpm for 1 minute.

3.  First, resuspend cells instead in 100 uL of 4% PFA in PBS. Incubate at room temperature in the dark for 20 minutes. (This step helps preserve certain surface stains like Tim3, as well as ametrine expression in transduced cells)

4.  Add 180 uL of FACS and spin down.

5.  During the spin, dilute 1 part eBioscience Fix/Perm Concentrate into 3 parts Fix/Perm Diluent. Make enough for 100 uL per well.

6.  Resuspend cells in 100uL of Fix/Perm and incubate 20 min at RT in the dark.

7.  During the incubation, make up your nuclear stain (in the Perm Buffer), enough for 100uL per well.

8.  After 20min, for the wash, add 180 uL of eBioscience 1x Perm buffer (diluted to 1x ddH2O) and spin down.

9.  Resuspend cells in 100 uL staining buffer and incubate for 30 m RT in the dark.

10. Add 180 uL of Perm buffer and spin down.

11. Resuspend in 100 uL FACS buffer and move to tubes.

12. Analyze immediately or parafilm seal, wrap in foil, and store for 3-5 d at 4 deg.

13. Make single color controls with beads (see protocol below)

**Single color controls**

For single color controls, I use OneComp eBeads™ Compensation Beads. The beads include positive and negative population for each sample, as only \~half of the beads bind antibody (therefore the other half is your negative control). This only works for using antibodies from mouse or rat sources (rabbit antibodies or dyes do not work here). For flow on the Fortessa X20, something like FITC vs A488 are interchangeable. On a spectral cytometer, this would not be the case.

1.  Vortex beads, then add one drop per tube. Make enough tubes for each fluorophore ‘color’ you have. If you have a reporter or dye than cannot be used as beads, still make a tube for these colors.

2.  Add 1uL of antibody for the appropriate single color per tube. For tubes representing reporter or dye, pick an antibody with a fluorophore that would be read out in the same channel and add to tube. Vortex to mix.

3.  Let single color control tubes sit in the dark at RT for at least 10min.

4.  After incubation, add 200uL FACS buffer per tube. THERE IS NO WASH STEP. Samples are now ready to run.

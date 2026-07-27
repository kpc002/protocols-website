---
order: 10
title: "Protocol for CRISPR amplicon sequencing 2025-11-06 (etr_PxVJqvYTzT) Custom_low_plex_LsgA_cloning_MRC"
author: Alex Monell
date: last-modified
image: dna.svg
description: "Protocol for cloning customizable low-plex CRISPR-Cas9 sgRNA screening libraries in the LsgA backbone for Illumina amplicon sequencing."
---

**Custom CRISPR Cas9 screens in the LsgA backbone**

**using Illumina-compatible libraries**

Miguel Reina-Campos – Goldrath Lab

07/13/2022

Objective: Clone \~150 sgRNAs covering 50 genes (\~3x sgRNAs/gene) in the LsgA vector for customizable screening pools in CD8 T cells

1)  **Order OligoPools**
    
    1.  Forward library: 5’ Phospho-CACCNNNNNNNNNNNNNNNNNNNN
    
    2.  Reverse library: 5’ Phospho-AAACNNNNNNNNNNNNNNNNNNNN

Annealed oligos will look like this:

5’ Phospho-CACCNNNNNNNNNNNNNNNNNNNN

NNNNNNNNNNNNNNNNNNNNCAAA-5’ Phospho

\*The 5’ Phosphate will allow ligation to occur using dephosphorylated BbsI-linearized LsgA vector.

Design your sgRNA sequences and upload to IDT to order <span class="underline">oPools Oligo Pools</span>

Order two different pools of single-stranded DNA oligos, Forward library and Reverse library.

*Price: 10 pmol/oligo, 120 sgRNA sequences.*

*Each sequence is 24 nts \* 120 = 2880 nts total, charged at oPools DNA Base 1 ($109 / pool) + $1.65 \* 120 = $109 per pool and $198 for 5’ phosphorylation for a total of $307 per pool.*

![](media/image1.png)

2)  **Vector Preparation: LsgA library vector**

<!-- end list -->

1)  Digest and dephosphorylate 20 ug of vector with BbsI for 1h at 37C. Set up the following reaction:

<span class="underline">100 ul reaction</span>

  - 10X rCutSmart Buffer 10 uL

  - LsgA vector (20 ug)

  - HF-BbsI (NEB) 3 uL

  - Alkaline Phosphatase Quick CIP (NEB) 5 uL

  - Water Fill to 100 uL

Run in a 0.8 % Agarose TAE Gel using wide combs

Purify linearized dephosphorylated oligo using QIAGEN Gel purification kit

Resuspend in \~40 ul of ddH2O

3)  **sgRNA oligo annealing**

IDT oligopools come as a dried DNA pellet with 10 pmols of each oligo.

Resuspension in 100 ul of ddH2O generates 1 uM stock for each oligo. For a 155 oligo-pool, this makes a \~150 uM ssDNA.

1)  Anneal sgRNA ssODN:

1 uL Forward library (Final concentration of each oligo \~100 nM)

1 uL Reverse library (Final concentration of each oligo \~100 nM)

1 uL 10X T4 Ligation Buffer (NEB)

7 uL ddH2O

2)  Put the phosphorylation/annealing reaction in a thermocycler using the following parameters:

> 37<sup>o</sup>C 30 min
> 
> 95<sup>o</sup>C 5 min
> 
> ramp down to 25<sup>o</sup>C at 6<sup>o</sup>C/min
> 
> keep at RT

4)  **Ligation**

1:1 ligation ratios

Vector is 7Kb while oligos are 24 nts, which makes the vector \~300x bigger than the insert.

Include a “No insert negative control”

25 ng of 7kb dsDNA vector in 10 ul reaction makes for a \~550 pM

1)  Dilute annealed library 1:200 (100 nM to 500 pM)

2)  Set up ligation reaction in a total volume of 10 ul

> Dephosphorylated BbsI-linearized LsgA vector backbone 25 ng (550 pM)
> 
> 1:200 Annealed sgRNA library 1 uL
> 
> 10X Ligase buffer 1 uL
> 
> ddH2O Fill to 10 uL

5)  **Test Transformation**

*A series of test transformations will be performed to verify correct inserts and successful ligations with low background. Two serial transformations will be performed, as a single transformation of the ligation product generates many mixed peaks during Sanger sequencing of colony PCR product.*

1)  *Primary transformation with high efficiency chemically competent cells (Stbl3 cells*).

<!-- end list -->

  - Add 0.5uL ligation to 20 uL Stellar cells, and gently tap to mix.

  - Incubate on ice for 30 minutes.

  - Heat-shock 45s @ 42oC.

  - Incubate on ice for 2 min.

  - Add 300 uL pre-warmed SOC and incubate for 1 hour at 37oC.

  - Plate 200 uL on pre-warmed plates (save the remaining recovery at RT or 4C).

  - Incubate O/N at 37oC.

  - \*Set up as many plates as needed - test transformation to obtain \~1k to 4k colonies per plate.

  - \*Limit culture time to \~16h to prevent colonies from overgrowing

**Got \~5k colonies per plate on the first try, with \~200 colonies in the vector-only plate (negative control). Vector only might self-religate in the absence of an insert (\~50 to 200 colonies is normal background).**

2)  *Plasmid prep: If your negative control shows \<5% background colonies, it is safe to proceed.*

3)  *Scrape plates with 1.5 mL of LB and purify plasmid and prepare midi-prep. **This is the plasmid library prep used for large-scale transformation, although it could be also used for the screen - subsequent steps are needed for verification of equal sgRNA representation.***

4)  *Secondary transformation with subcloning efficiency in Stbl3 cells.*

<!-- end list -->

  - Add 1ul of the prepared plasmid to 15-20uL of DH5a and gently tap to mix.

  - Incubate on ice for 2 minutes

  - Heat-shock 30s @ 42oC

  - Incubate on ice for 2 min

  - Add 980 uL SOC

  - Plate 1/50x (\~20uL) in 6 different plates for each sample.

  - Plate 6 plates per

  - Incubate O/N at 37oC

Pick as many colonies from each plate as needed. The rule of thumb is to pick one colony for every 5 sgRNAs (\~20%, ie 30 colonies for 155 sgRNas) – make minipreps and sequence using hU6. This QC makes sure the ration of the un-inserted religated vector is low, and that inserts are correctly cloned in the vector

  - Align the Sanger sequence output to the library vector map in your favorite cloning software (e.g. SnapGene) to ensure the sgRNAs were cloned properly

  - The 19 to 20bp corresponding to the unique protospacer sequence should not align it the vector. Search for this sequence in the list of sgRNAs in your oligo pool. If 70-90% of the sequences match to the correct library (you will likely see some oligo synthesis errors and sequencing errors), it is safe to proceed with the large-scale transformation.

*\***No sequences should perfectly align to the library vector at the protospacer region**. This would indicate that the parental vector was incompletely digested and the stuffer sequence is present in the library.*

*\*\***It is also extremely unlikely that any sgRNA appears multiple times in a random set of 10 colonies**. Repeated sequences are an indication that one species from the oligo pool is very overrepresented.*

6)  **Large Scale Transformation**

If the test transformation worked, use the plasmid library prep from step **5c**. to transform Stbl3 bacteria following this protocol:

1)  Pre-warm LB/carbenecillin plates 3-4 hours ahead of time.

2)  Thaw Stbl3 cells on ice

3)  Add 10 ng plasmid to 50 uL Stbl3 cells

4)  Heat shock at 42 C for 30 seconds

5)  Leave on ice for 2 minutes

6)  Add 950 uL of SOC media

7)  Incubate at 37 C for one hour

8)  Plate 10X LB Agar Carbenicillin plates

<!-- end list -->

7)  **Scrape Plates**

Add 15-25 mL LB for the initial scrape. Transfer to a clean collection tube. Add an additional 5-15 mL LB and transfer to collection tube. If you are scraping multiple plates, place your collection tube on ice. Once you are finished scraping, spin at 4,000 rpm for 20 min. The pellet should be tight. Pour off media and freeze pellet or proceed with plasmid preparation.

8)  **Plasmid Preparation**

Qiagen or Sigma midi, maxi, mega or giga plasmid prep kits. Make sure columns are dry prior to the final elution. Wet columns will give a low recovery.

> **9) Prepare Samples for Illumina Sequencing**

Illumina sequencing of the resulting plasmids is advised to ensure the resulting plasmid libraries from this protocol are correct, have a large fraction of sgRNAs that match perfectly to the expected library, and the relative fractions of each sgRNA are tightly distributed. You only need \~100 sequencing reads per sgRNA in the library to be able to validate the library (ex. 12K reads), so you can include your samples as a \<5% spike- in other sequencing runs.

To sequence your libraries, follow Step 3 of the sequencing sample prep protocol with the following modifications:

  - If you are spiking into a sequencing sample with high diversity, such as an RNA-seq experiment, you can omit the Set A/B strategy and just sequence with Set A primer pairs and sequencing primer

  - For the PCR, perform one 100uL PCR per library. If you have cloned multiple sublibraries, PCR each individually with a different sample index to allow you to detect any cross-contamination or sample mix-ups (although be careful to not introduce this during the PCR\!).

  - Substitute the genomic DNA input into the PCR with 100ng library plasmid.

  - Only perform 15 cycles of PCR.

<span class="underline">Amplicon sequence:</span>

TTCGA<span class="underline">TTTCTTGGCTTTATATATCT</span>TGTGGAAAGGACGAAANNNNNNNNNNNNNNNNNNNNGTTTTAGAGCTAGAAATAGC<span class="underline">AAGTTAAAATAAGGCTAGTC</span>CGTTATCAACTTGAAAAAGTGGCACCGAGTCGGTGCTTTTTTGAATTC 3’

1)  These primers are first used to amplify plasmid-coded amplicon from genomic DNA. IMPORTANT: These primers will amplify a 96 bp from the LsgA, and a 1962 bp from the LMG (containing the sgFdft1). Purify lower band by gel if necessary to clean.

<span class="underline">LsgA\_amplicon\_F: 5’TTTCTTGGCTTTATATATCT 3’</span>

<span class="underline">LsgA\_amplicon\_R: 5’GACTAGCCTTATTTTAACTT 3’</span>

![](media/image2.png)

**PCR**

Q5 2X

Vt=50

Touchdown PCR: 10 cycles starting at 61 C in -0.5 C delta

Everything else standard for Q5 protocol

Followed by 25 cycles at Ta 56

Extension times 7 sec

Purified with Qiaquick PCR purification kit

2)  PCR for amplification of the plasmid region with addition of Nextera Handles (P5, P7 tags)

Nextera-Handle-F (P5tag):

5 ‘ TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG<span class="underline">TTTCTTGGCTTTATATATCT</span> 3’

Nextera-Handle-R (P7tag):

5 ‘ GTCTCGTGGGCTCGGAGATGTGTATAAGAGACAG<span class="underline">GACTAGCCTTATTTTAACTT</span> 3’

This will amplify a 163 PCR product.

Use 2X Q5 high fidelity DNA polymerase protocol with 20 cycles.

Amplicon:

5’ to 3’

TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG<span class="underline">TTTCTTGGCTTTATATATCT</span>TGTGGAAAGGACGAAANNNNNNNNNNNNNNNNNNNNGTTTTAGAGCTAGAAATAGC<span class="underline">AAGTTAAAATAAGGCTAGTCCTGTCTCTTATACACATCT</span>CCGAGCCCACGAGAC

3)  Purify PCR product with AMPure XP beads 2X ratio and perform **Indexing PCR**:

<span class="underline">(</span><https://teichlab.github.io/scg_lib_structs/methods_html/Illumina.html><span class="underline">)</span>

Use Q5 2X polymerase

Vt=50 ul

16 cycles, TA = 58 C, extension 10 seconds

After PCR, AMPure XP purification with 2X beads ratio

**Indices were taken from illumina-adapter-sequences\_1000000002694-00.pdf**

<span class="underline">Sample 1 example</span>

F501 (i5-index-handle): AATGATACGGCGACCACCGAGATCTACAC**TAGATCGC**TCGTCGGCAGCGTC

R701 (i7-index-handle): CAAGCAGAAGACGGCATACGAGAT**TCGCCTTA**GTCTCGTGGGCTCGG

This will generate a 232 bp PCR amplicon (F501 R701 index example):

AATGATACGGCGACCACCGAGATCTACAC**TAGATCGC**TCGTCGGCAGCGTCAGATGTGTATAAGAGACAG’<span class="underline">TTTCTTGGCTTTATATATCT</span>TGTGGAAAGGACGAAANNNNNNNNNNNNNNNNNNNNGTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCCTGTCTCTTATACACATCTCCGAGCCCACGAGAC**TAAGGCGA**ATCTCGTATGCCGTCTTCTGCTTG

Green: i5, i7

**Black: index,**

blue: handle P5 and P7 Nextera,

yellow: internal primer used for genomic amplification,

purple: sgRNA sequence

‘: starts reading read 1.

**Sequencing math:**

  - 10K cell outputs should provide a 64X sgRNA coverage

  - Every cell should have only one copy of the sgRNA -\> 10K sgRNAs

  - 500 reads per sgRNA \* 10K sgRNAs = 5M reads per sample

  - Some samples have 100K, to 230K cells

  - 19 samples \* 5M = 95M 300 M minimum

  - For sequencing read length: the sgRNA sequence starts at 69 nts from the i5 index, and 106 nts from the beginning of the DNA fragment.

Miseq Reagent Kit v3 (https://www.illumina.com/systems/sequencing-platforms/miseq/specifications.html)

**<span class="underline">Experimental Setup LCMV infection Model</span>**

1.  > Enrich and in vitro activate P14 Cas9-eGFP donor cells (SOP)

2.  > Transduce (SOP)
    
    1.  > LsgA pool + LMG-Cd19 -\> Cd19-pool
    
    2.  > LsgA pool + LMG-Fdft1 -\> Fdft1KO-pool
    
    3.  > Expand 1:6 in IL-2/IL-7 for 24h
    
    4.  > Sort out Ametrine<sup>+</sup>/GFP<sup>high</sup> P14 cells:
        
        1.  > 500K per mouse. N=5 per group. Total 2.5 M per condition
        
        2.  > Sorted in cold MACS 10% FBS
        
        3.  > Keep 100K cell input for both samples (\~650X coverage)
    
    5.  > Transfer sorted P14 cells into B6 recipients and infect with LCMV (SOP)
    
    6.  > Bleed at day 7 pi to check proportions of TE and TMP for proper expansion
    
    7.  > Take Down at day 14 pi, and sort 10K Ame<sup>+</sup> GFP<sup>high</sup> P14 from
        
        1.  > Spleen P14 Cd19-pool X2
        
        2.  > Spleen P14 Fdft1KO-pool X2
        
        3.  > SI P14 Cd19-pool X2
        
        4.  > SI P14 Fdft1KO-pool X2
        
        5.  > Liver P14 IV- Cd19-pool X2
        
        6.  > Liver P14 IV- Fdft1KO-pool X2

**<span class="underline">Experimental Setup MC38-GP<sub>33-41</sub></span>**

500K Mc38-Gp33-41 implanted

Transferred 500K per mouse at day 10 post-implantation

Sorted cells at day 5 post-transfer

Example output of Fastq file

head -20 Input\_sgCd19pool\_1\_S27\_L001\_R1\_001.fastq

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC GACCTTCACGTGCCTCTCGA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (<span class="underline">sgCd19 sgRNA</span>)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC AGAGGTTCTGCTGGAACAAG GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (Cyb5b sgRNA)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC GACCTTCACGTGCCTCTCGA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (<span class="underline">sgCd19 sgRNA</span>)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC TGGACTACATCGATGAAGGA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (Soat1 sgRNA)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC TGGACTACATCGATGAAGGA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (Soat1 sgRNA)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC AGAGGGCATCCAGCTGACCG GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (Nr1h2 sgRNA)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC GACCTTCACGTGCCTCTCGA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (<span class="underline">sgCd19 sgRNA</span>)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC ACTGATCGTTAAGAAGTCCA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (Inpp5d sgRNA)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC CCTCCATGGAGAACACGCTG GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (Mvk sgRNA)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC GACCTTCACGTGCCTCTCGA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (<span class="underline">sgCd19 sgRNA</span>)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC TACTCCCTAAAGCAACCCGA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (Fntb sgRNA

head -20 Input\_sgCD19pool\_S15\_L001\_R1\_001.fastq

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC ATGCGCCTGGACAAGCCCAT GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (Coq2 sgRNA)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC GACCTTCACGTGCCTCTCGA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (<span class="underline">sgCd19 sgRNA</span>)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC GACCTTCACGTGCCTCTCGA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (<span class="underline">sgCd19 sgRNA</span>)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC GCACACTGCTTACCTCATCA GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (Uqcrc1 sgRNA)

NTTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACC GGATGTCGGGATGAGGAGAG GTTTTAGAGCTAGAAATAGCAAGTTAAAATAAGGCTAGTCC (Dhdds sgRNA)
